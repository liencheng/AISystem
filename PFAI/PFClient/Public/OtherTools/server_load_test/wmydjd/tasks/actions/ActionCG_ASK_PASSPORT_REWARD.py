# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_PASSPORT_REWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_PASSPORT_REWARD(self.person)
        # params begin ( don't move this line )

        packet['passlevel'] = self.person['passlevel']
        packet['passidx'] = self.person['passidx']
        packet['rewardall'] = self.person['rewardall']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_PASSPORT_REWARD")
        return res
