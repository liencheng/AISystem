# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BUY_BLACKMARKETITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BUY_BLACKMARKETITEM(self.person)
        # params begin ( don't move this line )

        packet['ItemIndex'] = self.person['ItemIndex']
        packet['curpage'] = self.person['curpage']
        # packet['currencyType'] = self.person['currencyType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BUY_BLACKMARKETITEM")
        return res
