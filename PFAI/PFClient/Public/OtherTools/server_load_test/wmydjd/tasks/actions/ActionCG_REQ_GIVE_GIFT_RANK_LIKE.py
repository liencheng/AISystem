# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GIVE_GIFT_RANK_LIKE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GIVE_GIFT_RANK_LIKE(self.person)
        # params begin ( don't move this line )

        packet['targetGuid'] = self.person['targetGuid']
        packet['rankType'] = self.person['rankType']
        packet['rank'] = self.person['rank']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GIVE_GIFT_RANK_LIKE")
        return res
