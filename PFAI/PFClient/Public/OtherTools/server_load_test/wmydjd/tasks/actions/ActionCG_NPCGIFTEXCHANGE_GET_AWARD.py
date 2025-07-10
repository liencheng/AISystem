# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_NPCGIFTEXCHANGE_GET_AWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_NPCGIFTEXCHANGE_GET_AWARD(self.person)
        # params begin ( don't move this line )

        packet['targetNPC'] = self.person['targetNPC']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_NPCGIFTEXCHANGE_GET_AWARD")
        return res
