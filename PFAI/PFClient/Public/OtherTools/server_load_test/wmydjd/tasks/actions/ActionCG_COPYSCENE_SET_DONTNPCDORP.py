# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_COPYSCENE_SET_DONTNPCDORP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_COPYSCENE_SET_DONTNPCDORP(self.person)
        # params begin ( don't move this line )

        packet['bDontNpcDrop'] = self.person['bDontNpcDrop']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_COPYSCENE_SET_DONTNPCDORP")
        return res
