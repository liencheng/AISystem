# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UNFORGETABLE_PROMISE_GET_REWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UNFORGETABLE_PROMISE_GET_REWARD(self.person)
        # params begin ( don't move this line )

        packet['IsAllPlayerReward'] = self.person['IsAllPlayerReward']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UNFORGETABLE_PROMISE_GET_REWARD")
        return res
