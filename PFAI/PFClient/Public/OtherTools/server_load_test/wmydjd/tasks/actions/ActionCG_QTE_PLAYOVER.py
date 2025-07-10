# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_QTE_PLAYOVER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_QTE_PLAYOVER(self.person)
        # params begin ( don't move this line )

        packet['QTEID'] = self.person['QTEID']
        packet['Result'] = self.person['Result']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_QTE_PLAYOVER")
        return res
