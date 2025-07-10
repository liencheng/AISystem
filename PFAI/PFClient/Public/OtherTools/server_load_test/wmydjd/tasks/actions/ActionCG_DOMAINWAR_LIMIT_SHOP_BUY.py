# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DOMAINWAR_LIMIT_SHOP_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DOMAINWAR_LIMIT_SHOP_BUY(self.person)
        # params begin ( don't move this line )

        packet['shopItemId'] = self.person['shopItemId']
        packet['shopItemCount'] = self.person['shopItemCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DOMAINWAR_LIMIT_SHOP_BUY")
        return res
