# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MONSTER_NIAN_DRIVEAWAY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MONSTER_NIAN_DRIVEAWAY(self.person)
        # params begin ( don't move this line )

        packet['Id'] = self.person['Id']
        packet['UseItemCount'] = self.person['UseItemCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MONSTER_NIAN_DRIVEAWAY")
        return res
