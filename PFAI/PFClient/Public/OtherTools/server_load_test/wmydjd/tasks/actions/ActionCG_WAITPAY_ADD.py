# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_WAITPAY_ADD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_WAITPAY_ADD(self.person)
        # params begin ( don't move this line )

        packet['FriendGuid'] = self.person['FriendGuid']
        packet['GoodsId'] = self.person['GoodsId']
        packet['GoodsCount'] = self.person['GoodsCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_WAITPAY_ADD")
        return res
