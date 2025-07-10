import binascii
import json
import loadlog
import os
import platform
import random
import socket
import struct
import time

import gevent

from tasks.actions import net_packets
from tasks.actions.net_packets import Defines
import zlib

unencrypted_packets = [Defines.ID_DEFINE('CG_LOGIN'), Defines.ID_DEFINE('GC_LOGIN_RET'),
                       Defines.ID_DEFINE('XX_REQUEST_HEARTBEAT'), Defines.ID_DEFINE('XX_RESPONSE_HEARTBEAT'),
                       Defines.ID_DEFINE('GC_SESSION')]


def is_encrypted_packet(packet_id):
    return packet_id not in unencrypted_packets



def send_packet(packet):
    """模拟客户端发送协议：
    协议格式: total_len(4bytes) + msg_id(2bytes) + seq(4bytes) + crc(4bytes) + packet_data(packet_len bytes)
    关于crc: 如果协议加密，则先加密再计算crc
    关于加密: 采用服务器发来的session来做xor加密，长度不变
    关于加密: 指定协议不加密，其它协议加密
    """
    logger = loadlog.getLogger('send_packet')
    packet_id = packet.get_id()
    packet_size = packet.get_data_size()

    if packet_id == net_packets.Defines.ID_DEFINE("CG_LOGIN"):
        packet.person['seq'] = 0
    else:
        packet.person['seq'] += 1

    if is_encrypted_packet(packet_id) and packet.person['session'] != b'':
        sending_stream = net_packets.Xor32.bxor_slow(packet.get_data_stream(),
                                                     packet_size,
                                                     packet.person['session'])
    else:
        sending_stream = packet.get_data_stream()

    # crc
    crc_client = zlib.crc32(sending_stream)
    packet_size = 4 + 2 + 4 + 4 + packet_size
    sending_stream = struct.pack("!IHII", packet_size, packet_id, packet.person['seq'], crc_client) + sending_stream

    if not packet.person.getloadflag():
        logger.debug('send packet : ' + packet.__class__.__name__)
        logger.debug('packet data : ' + packet.dump())
        #logger.debug('packet stream : ' + str(binascii.hexlify(sending_stream)))

    try:
        send_bytes = packet.person['socket'].send(sending_stream)
        if send_bytes == 0:
            loadlog.error("send_packet failed. Socket disconnected ")
            return False, 0, "send_packet failed. Socket disconnected "
    except Exception as e:
        return False, 0, "send_packet failed. Socket err %s" % e
    return True, 0, "send_packet %s successfully." % packet.__class__.__name__


def get_packet(person):
    """解析收取的packet
    服务器发包结构: total_len(4bytes) + msg_id(2bytes) + packet_data(packet_data_len bytes)
    关于解密: 指定消息包不加密
    关于解密: 客户端使用固定session_key做xor解密
    """

    logger = loadlog.getLogger('get_packet')
    decoder = person['decoder']
    try:
        buf_len = len(person['inputbuffer'])
        if buf_len < 6 or person['is_packect_truncated'] == True:
            if person['packet_rec_time'] == 1:
                person['packet_rec_time'] = 0
                return None

            recbuf = b''
            with gevent.Timeout(30, False) as timeout:
                recbuf = person['socket'].recv(655360)
            if len(recbuf) > 0:
                person['inputbuffer'] = person['inputbuffer'] + recbuf

            if person['packet_rec_time'] == 0 or person['packet_rec_time'] is None:
                person['packet_rec_time'] = 1

            if person['is_packect_truncated']:
                person['is_packect_truncated'] = False

        buf_len = len(person['inputbuffer'])
        if buf_len >= 6:
            packetsize, packet_id = struct.unpack("!IH", person['inputbuffer'][0:6])
            if buf_len < packetsize:
                person['is_packect_truncated'] = True
                return None
            if buf_len >= packetsize:
                try:
                    packetclass = net_packets.Defines.PACKET_DEFINE(packet_id)
                except KeyError as info:
                    logger.error('Error! Packet is not defined! Packet ID:' + str(packet_id))
                    logger.error('ErrorPacket stream:' + str(binascii.hexlify(person['inputbuffer'])))
                    person['inputbuffer'] = person['inputbuffer'][packetsize:]
                    return None

                if not person.getloadflag():
                    logger.debug('Receive packet: ' + packetclass)
                    #logger.debug('Receive packet stream : ' + str(binascii.hexlify(person['inputbuffer'])))

                packet = eval('net_packets.PACKETS.' + packetclass + "(person)")
                packet_body = person['inputbuffer'][6:packetsize]
                person['num_receive_packets'] = person['num_receive_packets'] + 1

                if is_encrypted_packet(packet_id):
                    packetbuf = net_packets.Xor32.bxor_slow(packet_body, len(packet_body), bytes(net_packets.Xor32.skey, 'utf-8')) # decrypt the packet body
                else:
                    packetbuf = packet_body
                try:
                    packet.fill_data_from_stream(packetbuf)
                except Exception as e:
                    errorstr = f"packet.filldatafromstream error : packet-name: {packetclass},- input: {str(binascii.hexlify(person['inputbuffer']))}"
                    logger.error(errorstr)

                if not person.getloadflag():
                    try:
                        logger.debug('packet data : ' + packet.dump())
                    except TypeError as info:
                        logger.error('Error! Packet dump error :' + str(info) + " " + packetclass + " " + str(binascii.hexlify(
                            person['inputbuffer'])))

                person['inputbuffer'] = person['inputbuffer'][packetsize:]

                return packet
            else:
                person['is_packect_truncated'] = True
                return None
        else:
            return None
    except Exception as e:
        logger.error(person['account'] + str(e))
        loadlog.error(person['account'] + str(e))
        raise e
    return None


def handle_packet(packet):
    # logger = logging.getLogger('Functions handlepacket')
    # logger.debug('Handle packet: ' + packet.__class__.__name__)
    if hasattr(packet, 'handle'):
        loadlog.debug('receive and handle packet: ' + packet.__class__.__name__)
        packet.handle()


def heartbeat(person):
    if person['heartbeat_time']:
        total_time = int((time.time() - person['heartbeat_time']) * 1000)
        if total_time > 6 * 1000:
            # send heartbeat
            packet = net_packets.PACKETS.XX_RESPONSE_HEARTBEAT(person)
            send_packet(packet)
            person['heartbeat_time'] = time.time()
    else:
        person['heartbeat_time'] = time.time()


def wait_for_packet(person, packetname, timeout=30, contiue=False):
    logger = loadlog.getLogger('packet')
    logger.debug('Wait for packet: ' + packetname)
    latesttime = time.time()
    decoder = person['decoder']

    while 1:
        packet = get_packet(person)
        if packet is None:
            # time.sleep(0.03)
            # heartbeat(person)
            total_time = int((time.time() - latesttime) * 1000)
            if total_time > timeout * 1000:
                break
            else:
                gevent.sleep(0)
                continue
        if packet.__class__.__name__ == packetname:
            total_time = int((time.time() - latesttime) * 1000)
            handle_packet(packet)
            return True, total_time, "Successfully get packet " + packetname
        else:
            handle_packet(packet)

    errstr = "Failed get packet"
    if person['account'] != '':
       errstr = f"account : {person['account']} {errstr} "

    if contiue:
        return True, total_time, errstr + "%s, but continue set" % packetname
    else:
        return False, total_time, errstr + packetname


def wait_for_packets(person, packetname, timeout=30):
    logger = loadlog.getLogger('wait_packet')
    for name in packetname:
        logger.debug('Wait for packets: ' + name)
    latesttime = time.time()
    gevent.sleep(0)
    while 1:
        packet = get_packet(person)
        if packet is None:
            total_time = int((time.time() - latesttime) * 1000) # this time used in locust report, milliseconds
            if total_time > timeout * 1000:
                break
            else:
                gevent.sleep(0)
                continue
        if packet.__class__.__name__ in packetname:
            total_time = int((time.time() - latesttime) * 1000)
            handle_packet(packet)
            return True, total_time, "Successfully get packet " + packet.__class__.__name__
        else:
            handle_packet(packet)
    errstr = "Failed get packet"
    if person['account'] != '':
       errstr = f"account : {person['account']} {errstr} "
    return False, total_time, errstr + packet.__class__.__name__


def wait_packet_with_heartbeat(person, packetname, timeout=30, contiue=False):
    logger = loadlog.getLogger('wait_packet')
    logger.debug('Wait for packet with heartbeat: ' + packetname)
    latesttime = time.time()
    while 1:
        try:
            packet = get_packet(person)
        except Exception as e:
            return False, total_time, "socket error " + str(e)
        else:
            heartbeat(person)
            if packet is None:
                # time.sleep(0.03)
                # heartbeat(person)
                total_time = int((time.time() - latesttime) * 1000)
                if total_time > timeout * 1000:
                    break
                else:
                    gevent.sleep(0)
                    heartbeat(person)
                    continue
            if packet.__class__.__name__ == packetname:
                total_time = int((time.time() - latesttime) * 1000)
                handle_packet(packet)
                return True, total_time, "Successfully get packet " + packetname
            else:
                handle_packet(packet)

    errstr = "Failed get packet"
    if person['account'] != '':
       errstr = f"account : {person['account']} {errstr} "

    if contiue:
        return True, total_time, errstr + packetname + ", but continue set"
    else:
        return False, total_time, errstr + packetname

def wait_packets_with_heartbeat(person, packet_names, timeout=30):
    logger = loadlog.getLogger('wait_packet')
    for name in packet_names:
        logger.debug('Wait for packets with heartbeat: ' + name)
    latesttime = time.time()
    while 1:

        packet = get_packet(person)
        heartbeat(person)
        if packet is None:
            # time.sleep(0.03)
            # heartbeat(person)

            total_time = int((time.time() - latesttime) * 1000)
            if total_time > timeout * 1000:
                break
            else:
                gevent.sleep(0)
                heartbeat(person)
                continue
        if packet.__class__.__name__ in packet_names:
            total_time = int((time.time() - latesttime) * 1000)
            handle_packet(packet)
            return (True, total_time, "Successfully get packet " + packet.__class__.__name__)
        else:
            handle_packet(packet)
    errstr = "Failed get packet"
    if person['account'] != '':
       errstr = f"account : {person['account']} {errstr} "
    return (False, total_time, errstr + " ".join(packet_names))


TRIGGER_INDEX = False
TRIGGER_FILE = '../../locusttemptrigger.txt'

if os.path.exists(TRIGGER_FILE):
    os.remove(TRIGGER_FILE)


def get_account_startnumber(startnumber, endnumber):
    global TRIGGER_FILE
    try:
        output_file = open(TRIGGER_FILE, 'r')
        cur_number = int(output_file.readline())
        if cur_number >= endnumber:
            next_number = startnumber
        elif cur_number < startnumber:
            next_number = startnumber
        else:
            next_number = cur_number + 1
        output_file.close()
        output_file = open(TRIGGER_FILE, 'w')
        output_file.write(str(next_number))
        output_file.close()
        return next_number
    except IOError:
        output_file = open(TRIGGER_FILE, 'w')
        output_file.write(str(startnumber))
        output_file.close()
        return int(startnumber)


role_name_suffix = ['roleA', 'roleB', 'roleC', 'roleD']


def get_role_name_with_account(account_name, role_count=0):
    global role_name_suffix

    if role_count <= len(role_name_suffix):
        index = role_count
        role_name = account_name + role_name_suffix[index]
    else:
        role_name = account_name + str(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
    return role_name


def gen_sex():
    return random.randint(0, 1)


# professions
profession_list = [0, 1, 2, 3, 4, 5, 6, 8, 15]


def gen_profession():
    global profession_list
    return random.choice(profession_list)


default_visual = [0, 1, 2, 3, 4, 5]
default_body_visual = [0, 1, 2]

def gen_default_visual():
    global default_visual
    return random.choice(default_visual)

def gen_default_body_visual ():
    global default_body_visual
    return random.choice(default_body_visual)


def gen_nieren_info():
    nieren_list = []
    for i in range(45):
        nieren_list.append(1)
    return     nieren_list

def is_trigger_start():
    global TRIGGER_INDEX
    global TRIGGER_FILE
    if not TRIGGER_INDEX:
        if os.path.exists(TRIGGER_FILE):
            TRIGGER_INDEX = True
            return True
        else:
            return False
    else:
        return True


def http(person, packet_name, url, data, params=None, headers=None, method='POST'):
    logger = loadlog.getLogger('http')
    if not person.loadtestflag():
        logger.debug('get url : ' + person['requestUrl'] + url)
    start_time = time.time()
    res = person['client'].request(method, person['requestUrl'] + url, data=data, params=params, headers=headers)

    response_time = int((time.time() - start_time) * 1000)
    if res.status_code != 200:
        print("Error accounts : ", person['accounts'])
        print("Http status code : " + str(res.status_code))
        print(res)
        print(res.content)
        return False, response_time, "get response fail " + url
    else:
        # print "get response:" + res.content
        # print res.headers
        # print "get status_code:" + str(res.status_code)
        if not person.loadtestflag():
            logger.debug("get response:" + res.content)
        if net_packets.Handles.HandlesDic.has_key(packet_name):
            net_packets.Handles.HandlesDic[packet_name](person, json.loads(res.content))
        return True, response_time, "get response success" + url
