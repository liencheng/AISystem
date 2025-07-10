# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_PANDORA_TLOG:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_PANDORA_TLOG(self.person)
        # params begin ( don't move this line )

        packet['nFunctionType'] = self.person['nFunctionType']
        packet['nSubType'] = self.person['nSubType']
        packet['nTargetGuid'] = self.person['nTargetGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_PANDORA_TLOG")
        return res
