# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_ITEM_SUBSCRIBE_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_ITEM_SUBSCRIBE_BUY(self.person)
        # params begin ( don't move this line )

        # packet['shopType'] = self.person['shopType']
        # packet['shopId'] = self.person['shopId']
        # packet['itemCount'] = self.person['itemCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_ITEM_SUBSCRIBE_BUY")
        return res
