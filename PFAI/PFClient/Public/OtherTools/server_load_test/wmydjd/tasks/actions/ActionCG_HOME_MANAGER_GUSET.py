# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HOME_MANAGER_GUSET:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HOME_MANAGER_GUSET(self.person)
        # params begin ( don't move this line )

        packet['OperaType'] = self.person['OperaType']
        # packet['ParamGuid_0'] = self.person['ParamGuid_0']
        # packet['ParamGuid_1'] = self.person['ParamGuid_1']
        # packet['Param0'] = self.person['Param0']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HOME_MANAGER_GUSET")
        return res
