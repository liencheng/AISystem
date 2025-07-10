# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_PRESTIGESHOPBUYITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_PRESTIGESHOPBUYITEM(self.person)
        # params begin ( don't move this line )

        packet['prestigeshopId'] = self.person['prestigeshopId']
        packet['buycount'] = self.person['buycount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_PRESTIGESHOPBUYITEM")
        return res
