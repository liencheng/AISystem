# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_CHALLENGE_RANK_SWAP_INFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_CHALLENGE_RANK_SWAP_INFO(self.person)
        # params begin ( don't move this line )

        packet['OldFakePos'] = self.person['OldFakePos']
        packet['OldRankPos'] = self.person['OldRankPos']
        packet['NewFakePos'] = self.person['NewFakePos']
        packet['NewRankPos'] = self.person['NewRankPos']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_CHALLENGE_RANK_SWAP_INFO")
        return res
