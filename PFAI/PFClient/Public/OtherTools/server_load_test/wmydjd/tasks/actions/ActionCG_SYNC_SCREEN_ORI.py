# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SYNC_SCREEN_ORI:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SYNC_SCREEN_ORI(self.person)
        # params begin ( don't move this line )

        packet['ori'] = self.person['ori']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SYNC_SCREEN_ORI")
        return res
