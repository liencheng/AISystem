# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ADVENTURE_REQ_BUY_ITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ADVENTURE_REQ_BUY_ITEM(self.person)
        # params begin ( don't move this line )

        packet['itemId'] = self.person['itemId']
        packet['num'] = self.person['num']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ADVENTURE_REQ_BUY_ITEM")
        return res
