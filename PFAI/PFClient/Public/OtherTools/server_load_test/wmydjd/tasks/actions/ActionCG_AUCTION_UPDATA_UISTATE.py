# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_AUCTION_UPDATA_UISTATE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_AUCTION_UPDATA_UISTATE(self.person)
        # params begin ( don't move this line )

        packet['bState'] = self.person['bState']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_AUCTION_UPDATA_UISTATE")
        return res
