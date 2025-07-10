# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_RANDOM_OPPONENT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_RANDOM_OPPONENT(self.person)
        # params begin ( don't move this line )

        packet['none'] = self.person['none']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_RANDOM_OPPONENT")
        return res
