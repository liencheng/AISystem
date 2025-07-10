# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_VERIFYCODE_INPUT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_VERIFYCODE_INPUT(self.person)
        # params begin ( don't move this line )

        packet['typeId'] = self.person['typeId']
        packet['posIndex'] = self.person['posIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_VERIFYCODE_INPUT")
        return res
