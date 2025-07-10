# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ACCEPT_COSUME_GIFT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ACCEPT_COSUME_GIFT(self.person)
        # params begin ( don't move this line )

        packet['giftId'] = self.person['giftId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ACCEPT_COSUME_GIFT")
        return res
