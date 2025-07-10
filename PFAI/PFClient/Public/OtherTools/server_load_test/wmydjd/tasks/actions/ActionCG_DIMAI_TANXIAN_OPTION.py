# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DIMAI_TANXIAN_OPTION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DIMAI_TANXIAN_OPTION(self.person)
        # params begin ( don't move this line )

        packet['OpType'] = self.person['OpType']
        # packet['JingCuIndex'] = self.person['JingCuIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DIMAI_TANXIAN_OPTION")
        return res
