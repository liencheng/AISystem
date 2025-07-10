# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ACTIVITY_REWARD_BUYONE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ACTIVITY_REWARD_BUYONE(self.person)
        # params begin ( don't move this line )

        packet['IsPerfect'] = self.person['IsPerfect']
        packet['BuyId'] = self.person['BuyId']
        packet['ConfirmUseYuanBao'] = self.person['ConfirmUseYuanBao']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ACTIVITY_REWARD_BUYONE")
        return res
