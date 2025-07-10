# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_STALL_COUNT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_STALL_COUNT(self.person)
        # params begin ( don't move this line )

        # packet['index'] = self.person['index']
        # packet['isPublic'] = self.person['isPublic']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_STALL_COUNT")
        return res
