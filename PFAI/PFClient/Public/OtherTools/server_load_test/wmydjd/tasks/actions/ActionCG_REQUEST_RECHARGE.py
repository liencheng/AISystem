# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQUEST_RECHARGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQUEST_RECHARGE(self.person)
        # params begin ( don't move this line )

        packet['producttype'] = self.person['producttype']
        packet['productid'] = self.person['productid']
        packet['productnum'] = self.person['productnum']
        # packet['param'] = self.person['param']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQUEST_RECHARGE")
        return res
