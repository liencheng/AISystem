# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ENTER_NEW_PRESTIGE_BOSS_SCENE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ENTER_NEW_PRESTIGE_BOSS_SCENE(self.person)
        # params begin ( don't move this line )

        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ENTER_NEW_PRESTIGE_BOSS_SCENE")
        return res
