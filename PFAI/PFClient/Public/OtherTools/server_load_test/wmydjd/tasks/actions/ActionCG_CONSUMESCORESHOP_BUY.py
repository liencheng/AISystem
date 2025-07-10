# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CONSUMESCORESHOP_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CONSUMESCORESHOP_BUY(self.person)
        # params begin ( don't move this line )
        packet['BuyShopItmeId'] = self.person['BuyShopItmeId']
        packet['BuyCount'] = self.person['BuyCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_CONSUMESCORESHOP_BUY")
        return res
