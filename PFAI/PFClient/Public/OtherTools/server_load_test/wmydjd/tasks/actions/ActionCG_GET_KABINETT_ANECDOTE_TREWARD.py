# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GET_KABINETT_ANECDOTE_TREWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GET_KABINETT_ANECDOTE_TREWARD(self.person)
        # params begin ( don't move this line )

        packet['misid'] = self.person['misid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GET_KABINETT_ANECDOTE_TREWARD")
        return res
