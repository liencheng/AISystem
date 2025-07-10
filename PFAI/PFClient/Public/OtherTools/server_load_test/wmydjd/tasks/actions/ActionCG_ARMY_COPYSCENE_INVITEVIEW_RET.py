# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ARMY_COPYSCENE_INVITEVIEW_RET:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ARMY_COPYSCENE_INVITEVIEW_RET(self.person)
        # params begin ( don't move this line )

        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ARMY_COPYSCENE_INVITEVIEW_RET")
        return res
