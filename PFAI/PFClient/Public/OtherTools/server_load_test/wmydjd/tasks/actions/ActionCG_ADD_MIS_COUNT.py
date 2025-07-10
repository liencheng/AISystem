# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ADD_MIS_COUNT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ADD_MIS_COUNT(self.person)
        # params begin ( don't move this line )

        packet['passtype'] = self.person['passtype']
        packet['passcount'] = self.person['passcount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ADD_MIS_COUNT")
        return res
