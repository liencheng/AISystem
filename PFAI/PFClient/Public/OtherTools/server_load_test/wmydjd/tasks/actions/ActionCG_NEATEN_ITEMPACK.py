# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_NEATEN_ITEMPACK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_NEATEN_ITEMPACK(self.person)
        # params begin ( don't move this line )

        packet['PackType'] = self.person['PackType']
        packet['OpType'] = self.person['OpType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_NEATEN_ITEMPACK")
        return res
