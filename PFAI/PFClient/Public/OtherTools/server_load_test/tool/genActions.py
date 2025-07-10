# -*- coding: utf-8 -*-
import sys
import os

# 功能：根据PacketID.cfg，更新PACKETS.py，如果有特写保留特写，如果有增加或删除，则相应增加或删除（删除的协议如果有特写，则改删除为注释）
#
g_packet_ids = "PacketID.cfg"

g_target_path= "../wmydjd/tasks/actions"

"""
Server protocol prefix that is not used in this tool
"""
packet_prefix_server = ["OB_", "BO_", "GH_", "HG_", "GD_", "DG_", "GM_"]

action_template = []


def read_action_template():
    with open("action_template.txt") as f:
        global action_template
        action_template = f.readlines()
        f.close()
        return True
    return False


if __name__ == '__main__':

    if not os.path.exists(g_packet_ids):
        sys.stderr.write("Error: PacketID.cfg not found\n")
        sys.exit(1)

    """
    读取action模板
    """
    if not read_action_template():
        sys.stderr.write("Error: action_template.txt not found\n")
        sys.exit(1)

    """
    如果没找到action文件路径，返回
    """
    if not os.path.exists(g_target_path):
        sys.stderr.write("Error: target path not found\n")
        sys.exit(1)

    """
    路径下的所有文件
    """
    exists_action_files = os.listdir(g_target_path)

    """
    取出本次待处理协议名，检查是否需要新增
    """
    new_packet_files = []
    action_names_all = []
    with open(g_packet_ids, 'r') as f:
        line = f.readline()
        while line:
            if line[0:3] == "CG_" or line[0:3] == "XX_":
                packet_name = line.split("=")[0]
                action_file_name = "Action"+packet_name+".py"
                action_names_all.append("Action"+packet_name)
                if action_file_name not in exists_action_files:
                    new_packet_files.append(packet_name)
            line = f.readline()
        f.close()

    # print(new_packet_files)

    os.chdir(g_target_path)

    for packet_name in new_packet_files:

        action_file = "Action"+packet_name+".py"
        with open(action_file, 'w', encoding='utf-8') as f:
            for line in action_template:
                new_line = line.replace("PACKETNAME", packet_name)
                f.write(new_line)
            f.close()

    action_all_line = "__all__ = ['Functions','accounts','AConnectToServer','net_packets','" + "','".join(action_names_all[:-1]) + "','" + action_names_all[-1] + "']"
    action_init_template = ["import Functions", "import accounts", "import AConnectToServer", "import net_packets"]

    with open('__init__.py', 'w') as f:
        for line in action_init_template:
            f.write(line+'\n')
        for action in action_names_all:
            f.write('import '+action+'\n')
        f.write('\n')
        f.write(action_all_line+'\n')
        f.close()
