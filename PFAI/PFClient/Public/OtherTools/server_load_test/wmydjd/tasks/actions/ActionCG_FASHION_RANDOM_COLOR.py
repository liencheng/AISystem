# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FASHION_RANDOM_COLOR:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FASHION_RANDOM_COLOR(self.person)
        # params begin ( don't move this line )

        packet['SoltIndex'] = self.person['SoltIndex']
        # packet['FashionId'] = self.person['FashionId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FASHION_RANDOM_COLOR")
        return res
