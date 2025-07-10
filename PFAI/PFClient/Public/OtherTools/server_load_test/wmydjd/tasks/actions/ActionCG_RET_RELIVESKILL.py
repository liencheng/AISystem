# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_RET_RELIVESKILL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_RET_RELIVESKILL(self.person)
        # params begin ( don't move this line )

        packet['isaccept'] = self.person['isaccept']
        # packet['buffID'] = self.person['buffID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_RET_RELIVESKILL")
        return res
