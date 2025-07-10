#!/bin/python
# -*- coding=utf-8 *-*
import numpy as np
import sys

direct_ch_set = {'-', '.', '_', '~'}

def url_encode(source_str):
    length = len(source_str)
    dest_str = ""
    for i in range(length):
        ch = source_str[i]
        if ch.isdigit() or ch.isalpha() or ch in direct_ch_set:
            dest_str += ch
        elif ch == ' ':
            dest_str += '+'
        else:
            # 其它字符编码为 % 加上字符的16进制表示，2位，不足补0
            encoded_ch = hex(ord(ch))
            dest_str += "%" + encoded_ch[2:]
    return dest_str


def url_decode(source_str):
    length = len(source_str)
    dest_str = ""
    parser = ''
    cur_index = -1
    for i in range(length):
        cur_index += 1
        if cur_index >= length:
            break
        ch = source_str[cur_index]
        if ch.isdigit() or ch.isalpha() or ch in direct_ch_set:
            dest_str += ch
        elif ch == '+':
            dest_str += ' '
        elif ch == '%':
            # 其它字符编码为 % 加上字符的16进制表示，2位，不足补0
            parser = ''
            if cur_index + 3 <= length:
                parser = source_str[cur_index+1:cur_index+3]
                #print source_str[cur_index:cur_index+5], chr(int(parser, 16))
                dest_str += chr(int(parser, 16))
                cur_index += 2
    return dest_str

usage = "Usage: urlcoder.py -e= [-d=]"

def main():
    if len(sys.argv) < 2:
        print usage
        return
    elif len(sys.argv[1]) < 3:
        print usage
        return
    encode = False
    decode = False
    encode_str = ""
    decode_str = ""
    if sys.argv[1][0:3] == "-e=":
        encode = True
        encode_str = sys.argv[1][3:]
        sys.stdout.write("encode: " + encode_str)
        sys.stdout.write("\r\nresult:\r\n")
    elif sys.argv[1][0:3] == "-d=":
        decode = True
        decode_str = sys.argv[1][3:]
        sys.stdout.write("decode:" + decode_str)
        sys.stdout.write("\r\nresult:\r\n")
    else:
        print usage
        return

    if encode:
        sys.stdout.write(url_encode(encode_str))
    if decode:
        sys.stdout.write(url_decode(decode_str))
    return



if __name__ == "__main__":
    main()

    # sour = "{\"account\":\"0_p_accoun100\", \"rolename\":\"月下丶\", \"sex\":1, \"profession\":3, \"bios\":1, \"channelId\":\"laohu\"}"
    # print sour
    # dest = url_encode(sour)
    # print dest
    # new_sour = url_decode(dest)
    # print new_sour