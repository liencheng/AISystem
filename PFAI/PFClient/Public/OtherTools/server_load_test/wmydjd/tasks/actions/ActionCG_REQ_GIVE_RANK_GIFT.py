# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GIVE_RANK_GIFT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GIVE_RANK_GIFT(self.person)
        # params begin ( don't move this line )

        packet['itemId'] = self.person['itemId']
        packet['itemGuid'] = self.person['itemGuid']
        packet['itemCount'] = self.person['itemCount']
        packet['targetGuid'] = self.person['targetGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GIVE_RANK_GIFT")
        return res
