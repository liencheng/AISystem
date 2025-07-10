# -*- coding: utf-8 -*-
import argparse
import sys
import os
from enum import Enum
import re
# 功能：根据PacketID.cfg，更新PACKETS.py，如果有特写保留特写，如果有增加或删除，则相应增加或删除（删除的协议如果有特写，则改删除为注释）
#
g_packet_define_file = "PBMessage.proto"

g_target_path = "../wmydjd/tasks/actions"

"""
Server protocol prefix that is not used in this tool
"""
packet_prefix = ["CG_", "XX_"]

g_message_infos = {}
g_message_attr_define_prefix = ["required", "optional", "repeated"]

g_action_files = []


def read_action_files():
    if not os.path.exists(g_target_path):
        sys.stderr.write("Error: target path not found\n")
        return False
    exists_action_files = os.listdir(g_target_path)
    for action_file in exists_action_files:
        if action_file.startswith("ActionCG"):
            g_action_files.append(action_file)
    return True


def read_message_infos():
    """读取message 中的定义"""
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
            if line_splits[0] == 'required':
                message_attrs.append([line_splits[2], True])
            else:
                message_attrs.append([line_splits[2], False])
    # 最后一个
    g_message_infos[message_name] = message_attrs
    return True


class ParamStage(Enum):
    BEFORE_PARAM = 1
    IN_PARAM = 2
    AFTER_PARAM = 3


if __name__ == '__main__':

    if not read_message_infos():
        err_str = "Error: " + g_packet_define_file + " not found\n"
        sys.stderr.write(err_str)
        sys.exit(1)

    """
    读取action files
    """
    if not read_action_files():
        err_str = "Error: " + g_target_path + " not found\n"
        sys.stderr.write(err_str)
        sys.exit(1)

    os.chdir(g_target_path)
    for action_file in g_action_files:
        packet_name = action_file[6:-3] #ActionCG_LOGIN.py
        if packet_name not in g_message_infos.keys():
            continue
        # replace
        old_lines = []
        old_lines_before_params = []
        old_lines_for_params = []
        old_lines_after_params = []
        new_lines = []

        with open(action_file, 'r') as f:
            old_lines = f.readlines()
            f.close()

        params_stages = ParamStage.BEFORE_PARAM

        for read_line in old_lines:
            if read_line.strip().startswith("# params begin"):
                params_stages = ParamStage.IN_PARAM
                old_lines_before_params.append(read_line)
                continue
            if read_line.strip().startswith("# params end"):
                params_stages = ParamStage.AFTER_PARAM
                old_lines_after_params.append(read_line)
                continue
            if params_stages == ParamStage.BEFORE_PARAM:
                old_lines_before_params.append(read_line)
            elif params_stages == ParamStage.IN_PARAM:
                old_lines_for_params.append(read_line)
            elif params_stages == ParamStage.AFTER_PARAM:
                old_lines_after_params.append(read_line)

        # get new attrs
        new_attrs = []
        for attr_name in g_message_infos[packet_name]:
            found = False
            for attr_line in old_lines_for_params:
                if attr_line.strip() == "\n":
                    continue
                if attr_line.find(attr_name[0]) != -1:
                    found = True
                    break
            if not found:
                new_attrs.append(attr_name)

        for old_line in old_lines_before_params:
            new_lines.append(old_line)
        for old_line in old_lines_for_params:
            new_lines.append(old_line)
        for new_attr in new_attrs:
            if new_attr[1]:
                new_line = "        packet['" + new_attr[0] + "'] = self.person['" + new_attr[0] + "']\n"
            else:
                new_line = "        # packet['" + new_attr[0] + "'] = self.person['" + new_attr[0] + "']\n"
            new_lines.append(new_line)
        for old_line in old_lines_after_params:
            new_lines.append(old_line)

        with open(action_file, 'w') as f:
            f.writelines(new_lines)
            f.close()

    # print(new_packet_files)

    # os.chdir(g_target_path)
    # for packet_name in new_packet_files:
    #     action_file = "Action"+packet_name+".py"
    #     with open(action_file, 'w', encoding='utf-8') as f:
    #         for line in action_template:
    #             new_line = line.replace("PACKETNAME", packet_name)
    #             f.write(new_line)
    #         f.close()

    print("ok")
