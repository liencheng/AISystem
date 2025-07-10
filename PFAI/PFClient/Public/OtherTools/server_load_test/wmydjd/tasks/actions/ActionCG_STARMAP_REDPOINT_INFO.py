# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_STARMAP_REDPOINT_INFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_STARMAP_REDPOINT_INFO(self.person)
        # params begin ( don't move this line )

        packet['isClick'] = self.person['isClick']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_STARMAP_REDPOINT_INFO")
        return res
