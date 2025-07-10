# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FIRST_OPEN_DIMAI_UI:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FIRST_OPEN_DIMAI_UI(self.person)
        # params begin ( don't move this line )

        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FIRST_OPEN_DIMAI_UI")
        return res
