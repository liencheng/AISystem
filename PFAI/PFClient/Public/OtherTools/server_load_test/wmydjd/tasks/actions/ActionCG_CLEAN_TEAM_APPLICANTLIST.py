# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CLEAN_TEAM_APPLICANTLIST:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CLEAN_TEAM_APPLICANTLIST(self.person)
        # params begin ( don't move this line )

        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CLEAN_TEAM_APPLICANTLIST")
        return res
