# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MULPVP_LEADEROPT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MULPVP_LEADEROPT(self.person)
        # params begin ( don't move this line )

        packet['inviterPlayerGuid'] = self.person['inviterPlayerGuid']
        packet['optType'] = self.person['optType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MULPVP_LEADEROPT")
        return res
