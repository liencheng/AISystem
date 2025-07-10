# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GOODLUCK_OP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GOODLUCK_OP(self.person)
        # params begin ( don't move this line )

        packet['giftid'] = self.person['giftid']
        packet['optype'] = self.person['optype']
        packet['pa'] = self.person['pa']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GOODLUCK_OP")
        return res
