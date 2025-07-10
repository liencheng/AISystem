# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_LIFESKILL_MAKE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_LIFESKILL_MAKE(self.person)
        # params begin ( don't move this line )

        packet['productid'] = self.person['productid']
        packet['materialid'] = self.person['materialid']
        packet['count'] = self.person['count']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_LIFESKILL_MAKE")
        return res
