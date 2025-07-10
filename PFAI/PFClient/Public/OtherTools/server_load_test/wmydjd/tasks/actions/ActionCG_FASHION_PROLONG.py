# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FASHION_PROLONG:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FASHION_PROLONG(self.person)
        # params begin ( don't move this line )

        packet['fashionType'] = self.person['fashionType']
        packet['fashionId'] = self.person['fashionId']
        packet['prolongTypoe'] = self.person['prolongTypoe']
        # packet['price'] = self.person['price']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FASHION_PROLONG")
        return res
