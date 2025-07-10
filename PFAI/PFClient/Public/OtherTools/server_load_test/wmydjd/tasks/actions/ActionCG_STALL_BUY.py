# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_STALL_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_STALL_BUY(self.person)
        # params begin ( don't move this line )

        packet['stallguid'] = self.person['stallguid']
        # packet['count'] = self.person['count']
        # packet['itemid'] = self.person['itemid']
        # packet['price'] = self.person['price']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_STALL_BUY")
        return res
