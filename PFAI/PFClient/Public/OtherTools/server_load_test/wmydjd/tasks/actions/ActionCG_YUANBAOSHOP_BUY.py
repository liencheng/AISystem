# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_YUANBAOSHOP_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_YUANBAOSHOP_BUY(self.person)
        # params begin ( don't move this line )

        packet['GoodsId'] = self.person['GoodsId']
        packet['BuyCount'] = self.person['BuyCount']
        packet['IsBind'] = self.person['IsBind']
        packet['BuyCost'] = self.person['BuyCost']
        # packet['extraOptionType'] = self.person['extraOptionType']
        # packet['extraOptionId'] = self.person['extraOptionId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_YUANBAOSHOP_BUY")
        return res
