# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_ALL_ROUND_GREETING_REWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_ALL_ROUND_GREETING_REWARD(self.person)
        # params begin ( don't move this line )

        packet['round'] = self.person['round']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_ALL_ROUND_GREETING_REWARD")
        return res
