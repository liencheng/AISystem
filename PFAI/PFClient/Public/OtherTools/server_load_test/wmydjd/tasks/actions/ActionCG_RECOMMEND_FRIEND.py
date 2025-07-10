# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_RECOMMEND_FRIEND:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_RECOMMEND_FRIEND(self.person)
        # params begin ( don't move this line )

        packet['levelCondition'] = self.person['levelCondition']
        packet['addressCondition'] = self.person['addressCondition']
        packet['maleCondition'] = self.person['maleCondition']
        packet['femaleCondition'] = self.person['femaleCondition']
        packet['recommendway'] = self.person['recommendway']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_RECOMMEND_FRIEND")
        return res
