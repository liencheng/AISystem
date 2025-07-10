# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_QL_GETREWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_QL_GETREWARD(self.person)
        # params begin ( don't move this line )

        packet['type'] = self.person['type']
        packet['index'] = self.person['index']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_QL_GETREWARD")
        return res
