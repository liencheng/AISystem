# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GATHER_POINT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GATHER_POINT(self.person)
        # params begin ( don't move this line )

        packet['posid'] = self.person['posid']
        packet['index'] = self.person['index']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GATHER_POINT")
        return res
