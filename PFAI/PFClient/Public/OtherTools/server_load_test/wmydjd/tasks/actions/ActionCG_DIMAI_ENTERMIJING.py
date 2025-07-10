# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DIMAI_ENTERMIJING:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DIMAI_ENTERMIJING(self.person)
        # params begin ( don't move this line )

        packet['enterType'] = self.person['enterType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DIMAI_ENTERMIJING")
        return res
