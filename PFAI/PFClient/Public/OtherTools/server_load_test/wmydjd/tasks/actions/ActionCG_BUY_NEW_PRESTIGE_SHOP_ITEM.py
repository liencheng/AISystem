# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BUY_NEW_PRESTIGE_SHOP_ITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BUY_NEW_PRESTIGE_SHOP_ITEM(self.person)
        # params begin ( don't move this line )

        packet['goodId'] = self.person['goodId']
        packet['goodCount'] = self.person['goodCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BUY_NEW_PRESTIGE_SHOP_ITEM")
        return res
