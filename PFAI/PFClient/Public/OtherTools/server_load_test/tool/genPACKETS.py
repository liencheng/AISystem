# -*- coding: utf-8 -*-
import sys
import os

# 功能：根据PacketID.cfg，更新PACKETS.py，如果有特写保留特写，如果有增加或删除，则相应增加或删除（删除的协议如果有特写，则改删除为注释）
# PACKETS.py 用于处理服务器消息接收

g_packet_ids = "PacketID.cfg"
g_packets_py = "..\\wmydjd\\tasks\\actions\\net_packets\\PACKETS.py"
g_packets_template = "PACKETS_template.txt"
"""
Server protocol prefix that is not used in this tool
"""
packet_prefix_server = ["OB_", "BO_", "GH_", "HG_", "GD_", "DG_", "GM_", "CB_", "BC_"]
packet_prefix_locust = ["CG_", "GC_", "XX_"]

if __name__ == '__main__':

    if not os.path.exists(g_packet_ids):
        sys.stderr.write("Error: PacketID.cfg not found\n")
        sys.exit(1)

    """
    如果没有文件，则用模板创建
    """
    if not os.path.exists(g_packets_py):
        if not os.path.exists(g_packets_template):
            sys.stderr.write("Error: PACKETS_template.txt not found\n")
            sys.exit(1)
        with open(g_packets_template, "r") as f:
            copy_str = f.readlines()
            with open(g_packets_py, "w") as tar:
                tar.writelines(copy_str)
                tar.close()
            f.close()

    """
    取出本次待处理协议名，忽略服务器间消息，也不处理客户端往服务器的消息（由action处理）
    """
    packet_class_names = []
    with open(g_packet_ids, 'r') as f:
        line = f.readline()
        while line:
            if line[0:3] in packet_prefix_locust:    #
                packet_class_names.append(line.split("=")[0])
            line = f.readline()
        f.close()

    g_source = None
    with open(g_packets_py, 'r', encoding='utf-8') as f:
        g_source = f.readlines()
        f.close()

    g_target = []

    for line in g_source:
        g_target.append(line)
        if line.startswith("class"):
            class_name = line.split(" ")[1]
            if class_name in packet_class_names:
                packet_class_names.remove(class_name)

    if len(packet_class_names) > 0:
        print(f"new packet count {len(packet_class_names)}")
        print(packet_class_names)
    else:
        print("no new packet")

    for class_name in packet_class_names:
        g_target.append("\n\nclass " + class_name + " (Packet):\n")
        # only GC_xx and XX_xx has handle function
        if class_name[0:3] == "GC_" or class_name[0:3] == "XX_":
            g_target.append("    def handle(self):\n")
            g_target.append("        # begin handle [" + class_name + "] message attrs, auto generate do not change\n")
            g_target.append("        # end handle [" + class_name + "] message attrs, auto generate do not change\n")
            g_target.append("        pass\n")
        else:
            g_target.append("\tpass\n")
    g_target.append("\n")

    with open(g_packets_py, 'w', encoding='utf-8') as f:
        f.writelines(g_target)
        f.close()

    print("finish generate/update PACKETS.py")
