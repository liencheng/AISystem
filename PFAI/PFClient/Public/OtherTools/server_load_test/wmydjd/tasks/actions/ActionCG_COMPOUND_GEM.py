# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_COMPOUND_GEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_COMPOUND_GEM(self.person)
        # params begin ( don't move this line )

        packet['operateType'] = self.person['operateType']
        packet['gemId'] = self.person['gemId']
        # packet['gemCount'] = self.person['gemCount']
        # packet['bagConsumeIds'] = self.person['bagConsumeIds']
        # packet['bagConsumeNums'] = self.person['bagConsumeNums']
        # packet['shopConsumeIds'] = self.person['shopConsumeIds']
        # packet['shopConsumeNums'] = self.person['shopConsumeNums']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_COMPOUND_GEM")
        return res
