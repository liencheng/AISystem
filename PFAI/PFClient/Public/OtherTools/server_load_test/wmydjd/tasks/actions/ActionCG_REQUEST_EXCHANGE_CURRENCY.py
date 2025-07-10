# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQUEST_EXCHANGE_CURRENCY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQUEST_EXCHANGE_CURRENCY(self.person)
        # params begin ( don't move this line )

        packet['currencyType'] = self.person['currencyType']
        packet['exchangeCurrencyType'] = self.person['exchangeCurrencyType']
        packet['amount'] = self.person['amount']
        packet['index'] = self.person['index']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQUEST_EXCHANGE_CURRENCY")
        return res
