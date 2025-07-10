# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_AUCTION_SELL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_AUCTION_SELL(self.person)
        # params begin ( don't move this line )

        packet['sellguid'] = self.person['sellguid']
        packet['sellbase'] = self.person['sellbase']
        packet['sellone'] = self.person['sellone']
        packet['time'] = self.person['time']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_AUCTION_SELL")
        return res
