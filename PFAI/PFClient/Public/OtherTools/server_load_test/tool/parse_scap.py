import struct

from scapy.layers.inet import *
import scapy.all as scapy
import sys, os.path
import binascii
import argparse

scap_file = "change_scene.pcap"

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CUR_DIR)
ACTIONS = os.path.join(ROOT_DIR, "wmydjd\\tasks\\actions")
NET_PACKET_DIR = os.path.join(ROOT_DIR, "wmydjd\\tasks\\actions\\net_packets")
sys.path.insert(0, ACTIONS)
sys.path.insert(0, NET_PACKET_DIR)
net_packets = __import__("net_packets")
PACKETS = __import__("PACKETS")
Defines = __import__("Defines")
Functions = __import__("Functions")

input_dir = os.path.join(CUR_DIR,"pcaps")
output_dir = os.path.join(CUR_DIR,"outputs")

# 不需要参与测试的发送消息包
ignore_packet_names = ['CG_TGLOG_CLIENT_BEHAVIOR', 'CG_CACHELOG']
# 不需要一定有回包的发送消息包
ignore_receive_names = ['CG_MOVE','CG_CLEARN_USE_SKILL_CD','CG_CLIENT_BEHAVIOR']


SERVER_PORT = 3341

FILTER_PORTS = [3341,]


def is_filter_port(port):
    return port in FILTER_PORTS


def get_flow(sport, dport):
    """ 根据源端口和目的端口，判断是否是需要抓取的包"""
    if dport == SERVER_PORT:
        return 'CG'
    if sport == SERVER_PORT:
        return 'GC'
    return None


class ScapParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.packet_seqs = []
        self.send_stream = b''
        self.receive_stream = b''
        self.gc_group = []
        self.action_seqs = []  # [(ltime, packet_name, attr_key_vals), ..]
        pass

    def parse(self, person, debug_info=False):
        if self.read_scap_file():
            self.parse_packet_seqs(person, debug_info)
            return self.action_seqs
        return None
    def read_scap_file(self):
        scap_file_path = os.path.join(input_dir, self.file_name)
        packets = scapy.rdpcap(scap_file_path)
        for p in packets:
            if p.haslayer('TCP'):
                tcp_layer = p.getlayer('TCP')
                if is_filter_port(tcp_layer.sport) or is_filter_port(tcp_layer.dport):
                    pac_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(p.time)))
                    if p.len > 40:
                        one_tcp = [pac_time, p.time, get_flow(tcp_layer.sport, tcp_layer.dport), bytes_encode(tcp_layer.payload)]
                        self.packet_seqs.append(one_tcp)
        return len(self.packet_seqs) > 0
    def parse_packet_seqs(self, mock_person, debuginfo=False):
        for s_time, l_time, flow, b_data in self.packet_seqs:
            if flow == 'CG' and b_data and len(b_data) > 0:
                self.send_stream += b_data
                self.send_stream = self.parse_packet_from_CG(l_time, self.send_stream, mock_person, debuginfo)
                if debuginfo:
                    print(f"Send CG packet at {s_time}")
            elif flow == 'GC' and b_data and len(b_data) > 0:
                self.receive_stream += b_data
                self.receive_stream = self.parse_packet_from_GC(l_time, self.receive_stream, mock_person, debuginfo)
                if debuginfo:
                    print(f"Received GC packet at {s_time}")
    def parse_packet_from_CG(self, l_time, stream, person, debuginfo=False):
        buf_len = len(stream)
        while buf_len >= 6:
            packet_size, packet_id = struct.unpack("!IH", stream[0:6])
            if buf_len < packet_size:
                return stream
            else:
                packet_class = eval("net_packets.Defines.PACKET_DEFINE(packet_id)")
                # 协议必须正确
                if not packet_class:
                    raise Exception(
                        f"Error! Packet is not Defined! Packet Id: {packet_id}, stream: {str(binascii.hexlify(stream))}")
                packet = eval("net_packets.PACKETS." + packet_class + "(person)")
                packet_body = stream[14:packet_size]
                if Functions.is_encrypted_packet(packet_id) and person['session'] and person['session'] != b'':
                    packet_body = net_packets.Xor32.bxor_slow(packet_body, len(packet_body), person['session'])
                try:
                    packet.fill_data_from_stream(packet_body)
                    attributes = self.parse_attributes(packet_class, packet)  # attributes = []
                except Exception as e:
                    print(f"Failed to iterate packet {packet_class}")
                    attributes = []
                action_info = (l_time, packet_class, attributes)
                self.action_seqs.append(action_info)
                if debuginfo:
                    print(f"    {packet_class} [{packet_size}] attr:{attributes}")
            stream = stream[packet_size:]
            buf_len = len(stream)
        return stream

    def parse_packet_from_GC(self, l_time, stream, person, debuginfo=False):
        buf_len = len(stream)
        while buf_len >= 6:
            packet_size, packet_id = struct.unpack("!IH", stream[:6])
            if buf_len < packet_size:
                return stream
            else:
                packet_class = eval("net_packets.Defines.PACKET_DEFINE(packet_id)")
                # 协议必须正确
                if not packet_class:
                    raise Exception(f"Error! Packet is not Defined! Packet Id: {packet_id}, stream: {str(binascii.hexlify(stream))}")
                packet = eval("net_packets.PACKETS." + str(packet_class) + "(person)")
                packet_body = stream[6:packet_size]
                if Functions.is_encrypted_packet(packet_id):
                    packet_body = net_packets.Xor32.bxor_slow(packet_body, len(packet_body), bytes(net_packets.Xor32.skey, 'utf8'))
                # if packet_id in ignore_packets:
                #     stream = stream[packet_size:]
                #     return stream
                try:
                    packet.fill_data_from_stream(packet_body)
                    if packet_id == Defines.ID_DEFINE('GC_SESSION'):
                        person['session'] = bytes(str(packet['session']), 'utf8')
                        if debuginfo:
                            print(f"{person['session']}")
                    # fill file_lines using the packet data
                    attributes = self.parse_attributes(packet_class, packet)  # attributes = []
                except Exception as e:
                    print(f"Failed to iterate :{packet_id} packetclass:{packet_class}")
                    attributes = []
                action_info = (l_time, packet_class, attributes)
                self.action_seqs.append(action_info)
                if debuginfo:
                    print(f"    {packet_class} [{packet_size}] attr:{attributes}")
            stream = stream[packet_size:]
            buf_len = len(stream)
        return stream

    def parse_attributes(self, packet_class, packet):
        attributes = []
        for key in packet.obj.DESCRIPTOR.fields_by_name.keys():
            # if not packet[key]:
            #     continue
            # print(f"{packet_class}.{key}:{type(packet[key])}")
            if type(packet[key]) in (int, float, bool, list):
                attributes.append(f"\t\tself.person['{key}'] = {packet[key]}")
            elif isinstance(packet[key], str):
                try:
                    packet[key].encode('ascii')
                    attributes.append(f"\t\tself.person['{key}'] = '{packet[key]}'")
                except UnicodeEncodeError:
                    attributes.append(f"\t\tself.person['{key}'] = u'{packet[key]}'")
            else:
                attr_obj = self.decode_struct_attr(key, packet[key], attributes)
                attributes.append(f"\t\tself.person['{key}'] = {attr_obj}")
        return attributes

    @staticmethod
    def decode_struct_attr(attr_name, attr_value, attributes):
        type_str = str(type(attr_value))  # type __name__ 只显示最后的类名不满足需求
        type_name = type(attr_value).__name__
        if type_name == 'RepeatedScalarContainer':
            return attr_value
        elif len(type_str) > 20 and type_str[8:20] == "PBMessage_pb":
            attributes.append(f"\t\t{attr_name} = actions.net_packets.PBMessage_pb2.{type(attr_value).__name__}")
            for sub_key in attr_value.DESCRIPTOR.fields_by_name.keys():
                sub_value = eval("attr_value."+sub_key)
                if type(sub_value) in (int, float, bool):
                    attributes.append(f"\t\t{attr_name}.{sub_key} = {sub_value}")
                elif type(sub_value) in (str,):
                    attributes.append(f"\t\t{attr_name}.{sub_key} = '{sub_value}'")
                else:
                    attr_obj = ScapParser.decode_struct_attr(sub_key, sub_value, attributes)
                    attributes.append(f"\t\t{attr_name}.{sub_key} = {attr_obj}")

        return attr_name


class MockPerson:
    def __init__(self):
        self.__data = {}

    def setdata(self, name, value):
        self.__data[name] = value
        return self.getdata(name)

    def getdata(self, name):
        if name in self.__data.keys() and self.__data[name] != None:
            return self.__data[name]
        else:
            return None

    def __getitem__(self, name):
        return self.getdata(name)

    def __setitem__(self, name, value):
        return self.setdata(name, value)


class TaskWriter(object):
    output_task_headers = ["import gevent", "from tasks import actions", "from tasks.actions import accounts", "", ""]
    output_class_init = ["\tdef __init__(self, person):", "\t\tself.person = person", ""]
    output_run_def_prefix = ["\tdef run(self):"]
                            # "\t\tres = self.person.login(server_ip, server_port, account_startwith)",
                            # "\t\tif not res[0]:",
                            #"\t\t\treturn res",""]
    def __init__(self, action_list, output_class):
        self.action_list = action_list
        self.output_class = output_class
        self.last_action = None
        self.gc_action_list = []
        self.file_lines = []
        self.last_cg_action = None  # 用于处理sleep

    def filter_ignores(self, ignore_packet_list):
        self.action_list = [action for action in self.action_list if action[1] not in ignore_packet_list]
        pass

    def cutout_action_by_start_packet(self, start_packet):
        count = 0
        for action in self.action_list:
            count+=1
            if action[1] == start_packet:
                self.action_list = self.action_list[count-1:]
                break

    def write(self, action_count, start_packet=None):
        if start_packet:
            self.cutout_action_by_start_packet(start_packet)
        if not self.action_list:
            return
        write_line = 0
        for action in self.action_list:
            if write_line >= action_count:
                break
            if action[1][:2] == 'CG':
                if self.last_action and self.last_action[1][:2] == 'GC':
                    if len(self.gc_action_list) > 0:
                        if len(self.gc_action_list) == 1:
                            self.write_one_gc(self.gc_action_list[0])
                            write_line += 1
                        else:
                            self.write_gc_list()
                            write_line += 1
                self.write_one_cg(action)
                write_line += 1
            elif action[1][:2] =='GC':
                # GC需要累计
                self.gc_action_list.append(action)
            if action[1][:2] =='GC' or action[1][:2] == 'CG':
                # 忽略XX,只记录CG,GC
                self.last_action = action
                if action[1][:2] == 'CG':
                    self.last_cg_action = action
        # 忽略最后的GC组，不用等待
        outputfile = os.path.join(output_dir, self.output_class+'.py')
        with open(outputfile, 'w') as f:
            for line in TaskWriter.output_task_headers:
                f.write(line + "\n")
            f.write('class %s:\n' % self.output_class)
            for line in TaskWriter.output_class_init:
                f.write(line + "\n")
            for line in TaskWriter.output_run_def_prefix:
                f.write(line + "\n")
            for line in self.file_lines:
                f.write(line + "\n")
            f.write('\t\treturn res\n')
            f.close()
    def write_one_cg(self, action):
        # 判断是否需要加sleep
        if self.last_cg_action:
            sleep_time = int(action[0] - self.last_cg_action[0])
            if self.last_cg_action and sleep_time >= 1:
                if sleep_time > 2:
                    sleep_time = 2
                self.file_lines.append(f"\t\tgevent.sleep({sleep_time})")
        # 先attributs
        for attr_line in action[2]:
            self.file_lines.append(attr_line)
        self.file_lines.append(f"\t\tres = self.person.Action{action[1]}()")
        self.file_lines.append(f"\t\tif not res[0]:")
        self.file_lines.append(f"\t\t\treturn res")
        pass

    def write_one_gc(self, action):
        self.file_lines.append(
            f"\t\tres = actions.Functions.wait_packet_with_heartbeat(self.person,'{action[1]}')")
        write_res = True
        if self.last_cg_action and self.last_cg_action[1] in ignore_receive_names:
            write_res = False
        if write_res:
            self.file_lines.append(f"\t\tif not res[0]:")
            self.file_lines.append(f"\t\t\treturn res")
        self.gc_action_list = []
    def write_gc_list(self, use_timeout=False):
        line = "\t\tres = actions.Functions.wait_packets_with_heartbeat(self.person,["
        timeout = int(self.gc_action_list[-1][0] - self.gc_action_list[0][0])
        if timeout < 5:
            timeout = 5
        wroten_list = []
        for action in self.gc_action_list:
            if action[1] not in wroten_list:
                wroten_list.append(action[1])
        for gc_packet_name in wroten_list[:-1]:
            line += f"'{gc_packet_name}', "
        if use_timeout:
            line += f"'{wroten_list[-1]}'],{timeout})"
        else:
            line += f"'{wroten_list[-1]}'])"
        self.file_lines.append(line)
        write_res = True
        if self.last_cg_action and self.last_cg_action[1] in ignore_receive_names:
            write_res = False
        if write_res:
            self.file_lines.append(f"\t\tif not res[0]:")
            self.file_lines.append(f"\t\t\treturn res")
        self.gc_action_list = []


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'please enter two : pcap and out ...'
    parser.add_argument("-s", "--pcap=", help="pcap file name under ./pcaps",
                        dest="pcap",type=str, default="")
    parser.add_argument("-o", "--output=", help="output python file name, use pcap name if not set",
                        dest="out",type=str,default="")
    args = parser.parse_args()
    if args.pcap and args.pcap != "":
        scap_file = args.pcap

    print("pcap :", args.pcap)
    print("output :", args.out)

    mock_person = MockPerson()
    parser = ScapParser(scap_file)
    action_list = parser.parse(mock_person,True)
    if args.out and args.out != "":
        output_class_name = args.out
    else:
        output_class_name = scap_file.split('.')[0]
    writer = TaskWriter(action_list, output_class_name)
    writer.filter_ignores(ignore_packet_names)
    writer.write(300, 'CG_ENTER_SCENE_OK')  #

    with open("lastaction.log", "w") as log:
        for line in action_list:
            log.write(str(line)+"\n")
            # print(line)
        log.close()
