# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MIDAS_REQUEST_BUYGOODS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MIDAS_REQUEST_BUYGOODS(self.person)
        # params begin ( don't move this line )

        packet['RechargeId'] = self.person['RechargeId']
        # packet['param'] = self.person['param']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MIDAS_REQUEST_BUYGOODS")
        return res
