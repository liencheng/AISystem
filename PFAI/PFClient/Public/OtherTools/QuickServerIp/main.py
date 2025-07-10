#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import get_new_serverconfiglist as config

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def recombine():
    ip_short_names = {}
    server_ip_short_names = {}
    if config.do_update():
        with open("OnlineServerIp.txt") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                line_split = line.split()
                if len(line_split) < 2:
                    continue
                ip_short_names[line_split[0]] = line_split[1]

        server_ips = config.read_server_ip()
        for server_id, server_ip in server_ips.items():
            if server_ip in ip_short_names.keys():
                server_ip_short_names[server_id] = (server_ip,ip_short_names[server_ip])

        bigworld_origins = renew_server_mapping()

        with open("ServerIdIpShot.txt", "w") as f:
            f.write("worldId\tinner_ip\tshort_name\n")
            for server_id, server_strings in server_ip_short_names.items():
                f.write("%d\t%s\t%s" % (server_id, server_strings[0], server_strings[1]))
                if server_id in bigworld_origins.keys():
                    for origin_id in bigworld_origins[server_id]:
                        f.write("\t%d" % origin_id)
                f.write("\n")
        # print(u"更新ServerConfigList.txt ServerConfigList_Operation.txt 成功")
    else:
        print(u"更新ServerConfigList.txt ServerConfigList_Operation.txt 失败")
    return server_ip_short_names


def renew_server_mapping():
    bigworld_origins = {}
    with open("./tmp/ServerConfigList.txt", "r") as f:
        read_lines = f.readlines()
        for line in read_lines[3:]:
            if line.startswith("#"):
                continue
            line_splits = line.split()
            if line_splits[3] == '0' and line_splits[0] == line_splits[5]:
                if line_splits[4] == '-1':
                    continue
                if int(line_splits[4]) not in bigworld_origins.keys():
                    bigworld_origins[int(line_splits[4])] = set()
                bigworld_origins[int(line_splits[4])].add(int(line_splits[0]))
    print bigworld_origins
    return bigworld_origins

def read_server_ip_short_names():
    server_ip_short_names = {}
    with open("ServerIdIpShot.txt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line_split = line.split()
            if len(line_split) < 2:
                continue
            if not line_split[0].isdigit():
                continue
            server_ip_short_names[int(line_split[0])] = (line_split[1], line_split[2])
    return server_ip_short_names

def main(query_server_id, recombined=False):
    # Use a breakpoint in the code line below to debug your script.
    _server_ip_short_names = {}
    if recombined:
        _server_ip_short_names = recombine()
    else:
        _server_ip_short_names = read_server_ip_short_names()

    if query_server_id == -1:
        # print server_ips
        for server_id, server_ip in _server_ip_short_names.items():
            print(server_id, server_ip)
    else:
        if query_server_id in _server_ip_short_names.keys():
            print(query_server_id, _server_ip_short_names[query_server_id])
        else:
            print("server_id not found")


def print_info():
    print("usage: %s worldid=<server id> [recombined=<0,1>]")
    print("if recombined set to 1, will regenerate the ServerIpShortName.txt file")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server_id = -1
    recombined = False
    args = {"worldid": 10001, "recombined": 1}
    parse_ok = True
    for i in range(len(sys.argv)):
        line_split = sys.argv[i].split("=")
        if len(line_split) == 2:
            if line_split[0].lower() in args.keys() and line_split[1].isdigit():
                args[line_split[0]] = int(line_split[1])
            else:
                print "args error"
                parse_ok = False
                break

    main(args["worldid"], bool(args["recombined"]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
