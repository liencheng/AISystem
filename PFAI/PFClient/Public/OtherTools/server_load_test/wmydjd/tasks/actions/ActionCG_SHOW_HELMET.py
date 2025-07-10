# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SHOW_HELMET:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SHOW_HELMET(self.person)
        # params begin ( don't move this line )

        packet['showhelmet'] = self.person['showhelmet']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SHOW_HELMET")
        return res
