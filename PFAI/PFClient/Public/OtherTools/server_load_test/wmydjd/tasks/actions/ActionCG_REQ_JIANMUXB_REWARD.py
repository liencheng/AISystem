# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_JIANMUXB_REWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_JIANMUXB_REWARD(self.person)
        # params begin ( don't move this line )

        packet['rewardId'] = self.person['rewardId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_JIANMUXB_REWARD")
        return res
