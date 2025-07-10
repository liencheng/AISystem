# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_EXCHANGE_CHOOSEREWARDBOX:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_EXCHANGE_CHOOSEREWARDBOX(self.person)
        # params begin ( don't move this line )

        packet['BoxGuid'] = self.person['BoxGuid']
        packet['ExchangeCount'] = self.person['ExchangeCount']
        # packet['ChooseIndexList'] = self.person['ChooseIndexList']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_EXCHANGE_CHOOSEREWARDBOX")
        return res
