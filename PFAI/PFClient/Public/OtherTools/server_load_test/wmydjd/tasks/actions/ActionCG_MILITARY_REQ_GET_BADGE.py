# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MILITARY_REQ_GET_BADGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MILITARY_REQ_GET_BADGE(self.person)
        # params begin ( don't move this line )

        packet['rank'] = self.person['rank']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MILITARY_REQ_GET_BADGE")
        return res
