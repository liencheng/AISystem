import os
import sys
import platform
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BIN_DIR)

sysstr = platform.system()


if(sysstr =="Windows"):
    CUR_DIR = os.path.join(ROOT_DIR, "wmydjd\\tasks\\actions\\net_packets")
else:
    CUR_DIR = os.path.join(ROOT_DIR, "wmydjd/tasks/actions/net_packets")

sys.path.insert(0, CUR_DIR)

Defines = __import__("Defines")
PACKETS = __import__("PACKETS")

__all__ = ["Defines", "PACKETS"]