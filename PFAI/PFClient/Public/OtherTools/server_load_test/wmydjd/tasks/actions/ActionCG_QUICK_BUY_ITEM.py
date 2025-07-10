# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_QUICK_BUY_ITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_QUICK_BUY_ITEM(self.person)
        # params begin ( don't move this line )
        packet['itemId'] = self.person['itemId']
        packet['itemCount'] = self.person['itemCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_QUICK_BUY_ITEM")
        return res
