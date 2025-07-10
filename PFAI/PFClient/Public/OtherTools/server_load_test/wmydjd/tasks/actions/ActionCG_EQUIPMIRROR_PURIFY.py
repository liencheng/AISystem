# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_EQUIPMIRROR_PURIFY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_EQUIPMIRROR_PURIFY(self.person)
        # params begin ( don't move this line )

        packet['mainmirrorguid'] = self.person['mainmirrorguid']
        packet['assistmirrorguid'] = self.person['assistmirrorguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_EQUIPMIRROR_PURIFY")
        return res
