# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_POSTERSTAR_GET_AWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_POSTERSTAR_GET_AWARD(self.person)
        # params begin ( don't move this line )

        packet['targetNPC'] = self.person['targetNPC']
        packet['awardIdx'] = self.person['awardIdx']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_POSTERSTAR_GET_AWARD")
        return res
