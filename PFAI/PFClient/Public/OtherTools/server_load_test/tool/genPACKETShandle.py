# -*- coding: utf-8 -*-
import argparse
import sys
import os
from enum import Enum
import re
# 功能：根据PacketID.cfg，更新PACKETS.py，如果有特写保留特写，如果有增加或删除，则相应增加或删除（删除的协议如果有特写，则改删除为注释）
#
g_packet_define_file = "PBMessage.proto"

g_target_file = "..\\wmydjd\\tasks\\actions\\net_packets\\PACKETS.py"

"""
Server protocol prefix that is used in this tool
"""
packet_used_prefix = ["GC_", "XX_"]

# unpdated protocol messages
g_message_infos = {}
g_message_attr_define_prefix = ["required", "optional", "repeated"]

# old protocol messages
g_packets_handles = {} # key=value pairs: packet_name=[attrs,]


def read_PACKETS_classes():
    """read the PBMessage classes, and attributes in handle function"""
    if not os.path.exists(g_target_file):
        sys.stderr.write("Error: target path not found\n")
        return False

    with open(g_target_file) as f:
        lines = f.readlines()
        f.close()

    # read all classes and attributes in handle function
    class_name = ""
    class_handle_attrs = []
    packets_lines = iter(lines)
    for line in packets_lines:
        if line.strip().startswith("#"):
            continue
        line_splits = line.strip().split()

        if len(line_splits) > 0 and line_splits[0] == "class":
            #print(line)
            exists_class = line.split()[1]

            if len(exists_class) > 0 and exists_class not in g_packets_handles:
                g_packets_handles[class_name] = class_handle_attrs
                class_name = exists_class
                class_handle_attrs = []
        if line.find("self[") > 0 : #  extract attribute name
            attr_name = re.findall(r"self\[\'(.*)\'\]", line)[-1]
            print("extract " + class_name + "." + attr_name)
            if attr_name not in class_handle_attrs:
                class_handle_attrs.append(attr_name)
    return True


def read_message_infos():
    """读取message 中的attributes定义"""
    if not os.path.exists(g_packet_define_file):
        str_err = "Error: " + g_packet_define_file + " not found\n"
        sys.stderr.write(str_err)
        return False
    with open(g_packet_define_file, 'r') as f:
        message_defines = f.readlines()
        f.close()
    message_defines_lines = iter(message_defines)
    message_name = ""
    message_attrs = []
    for one_line in message_defines_lines:
        line_splits = re.split(r"=|\s+|{", one_line.strip())
        if one_line.startswith("message"):
            if message_name != "" and len(message_attrs) > 0:
                g_message_infos[message_name] = message_attrs
                message_name = ""
                message_attrs = []
            if len(line_splits) >= 2:
                message_name = line_splits[1]
                #one_line = next(message_defines_lines)
                #line_splits = one_line.split()

                continue
        if not one_line.strip().startswith("//") and len(line_splits) >= 5 and line_splits[0] in g_message_attr_define_prefix:
            message_attrs.append(line_splits[2])
    # 最后一个
    g_message_infos[message_name] = message_attrs
    return True


class AttrStage(Enum):
    BEFORE_ATTR = 1
    IN_ATTR = 2
    AFTER_ATTR = 3


if __name__ == '__main__':

    # read message to g_message_infos map
    if not read_message_infos():
        err_str = "Error: " + g_packet_define_file + " not found\n"
        sys.stderr.write(err_str)
        sys.exit(1)

    # read PACKETS.py to g_packets_handles map
    if not read_PACKETS_classes():
        err_str = "Error: " + g_target_file + " not found\n"
        sys.stderr.write(err_str)
        sys.exit(1)

    # parse new attributes,解析出新增的
    for packet_name, attrs in g_packets_handles.items():
        if packet_name in g_message_infos.keys():
            msg_attrs = g_message_infos[packet_name]
            for attr_name in attrs:
                if attr_name in msg_attrs:
                    msg_attrs.remove(attr_name)
            if len(msg_attrs) == 0:
                g_message_infos.pop(packet_name)
    if len(g_message_infos) > 0:
        print(f"{len(g_message_infos)} message has new attributes")
        print(g_message_infos)
    else:
        print("no attributes updated")

    with open(g_target_file, "r") as f:
        old_lines = f.readlines()
        f.close()
    new_lines = []
    stages = AttrStage.BEFORE_ATTR
    cur_packet_name = ""
    for line in old_lines:
        if line.find("# end handle ") > -1:
            cur_packet_name = re.split("\[|\]", line)[1]
            if cur_packet_name in g_message_infos and len(g_message_infos[cur_packet_name]) > 0:
                for attr_name in g_message_infos[cur_packet_name]:
                    new_attr_line = "        self.person['" + attr_name + "'] = self['" + attr_name + "']\n"
                    new_lines.append(new_attr_line)
        new_lines.append(line)

    with open(g_target_file, "w") as f:
        f.writelines(new_lines)
        f.close()
    print("ok")
