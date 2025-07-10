# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_STALL_REVIEW_DELETE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_STALL_REVIEW_DELETE(self.person)
        # params begin ( don't move this line )

        packet['StallGuid'] = self.person['StallGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_STALL_REVIEW_DELETE")
        return res
