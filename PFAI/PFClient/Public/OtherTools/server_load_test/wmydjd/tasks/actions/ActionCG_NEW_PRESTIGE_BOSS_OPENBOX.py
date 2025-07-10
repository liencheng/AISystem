# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_NEW_PRESTIGE_BOSS_OPENBOX:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_NEW_PRESTIGE_BOSS_OPENBOX(self.person)
        # params begin ( don't move this line )

        packet['targetNPCId'] = self.person['targetNPCId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_NEW_PRESTIGE_BOSS_OPENBOX")
        return res
