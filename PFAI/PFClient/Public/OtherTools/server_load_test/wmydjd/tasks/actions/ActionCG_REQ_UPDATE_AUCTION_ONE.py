# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_UPDATE_AUCTION_ONE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_UPDATE_AUCTION_ONE(self.person)
        # params begin ( don't move this line )

        packet['type'] = self.person['type']
        packet['auctionGuid'] = self.person['auctionGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_UPDATE_AUCTION_ONE")
        return res
