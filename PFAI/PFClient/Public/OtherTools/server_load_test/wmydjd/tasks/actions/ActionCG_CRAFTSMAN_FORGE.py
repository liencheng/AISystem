# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CRAFTSMAN_FORGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CRAFTSMAN_FORGE(self.person)
        # params begin ( don't move this line )

        packet['formulaId'] = self.person['formulaId']
        packet['enhanced'] = self.person['enhanced']
        packet['allowBind'] = self.person['allowBind']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CRAFTSMAN_FORGE")
        return res
