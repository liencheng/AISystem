# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ARTIFACT_PROVE_REWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ARTIFACT_PROVE_REWARD(self.person)
        # params begin ( don't move this line )

        packet['ProveRewardId'] = self.person['ProveRewardId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ARTIFACT_PROVE_REWARD")
        return res
