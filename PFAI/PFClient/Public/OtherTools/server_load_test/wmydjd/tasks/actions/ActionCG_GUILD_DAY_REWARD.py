# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_DAY_REWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_DAY_REWARD(self.person)
        # params begin ( don't move this line )
        packet['type'] = self.person['type']
        packet['activityId'] = self.person['activityId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_GUILD_DAY_REWARD")
        return res
