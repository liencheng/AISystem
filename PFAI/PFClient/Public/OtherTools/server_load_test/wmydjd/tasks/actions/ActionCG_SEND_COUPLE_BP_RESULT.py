# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SEND_COUPLE_BP_RESULT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SEND_COUPLE_BP_RESULT(self.person)
        # params begin ( don't move this line )

        packet['nOrderId'] = self.person['nOrderId']
        packet['nWorkSingleResult'] = self.person['nWorkSingleResult']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SEND_COUPLE_BP_RESULT")
        return res
