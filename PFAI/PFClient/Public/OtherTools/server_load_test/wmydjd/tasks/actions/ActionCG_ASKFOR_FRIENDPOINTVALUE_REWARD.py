# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASKFOR_FRIENDPOINTVALUE_REWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASKFOR_FRIENDPOINTVALUE_REWARD(self.person)
        # params begin ( don't move this line )

        packet['friendGuid'] = self.person['friendGuid']
        packet['rewardindex'] = self.person['rewardindex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASKFOR_FRIENDPOINTVALUE_REWARD")
        return res
