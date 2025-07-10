# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DRAW_GROWTHUP_MARASARA:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DRAW_GROWTHUP_MARASARA(self.person)
        # params begin ( don't move this line )

        packet['nMarasaraIdex'] = self.person['nMarasaraIdex']
        packet['nDrawLevel'] = self.person['nDrawLevel']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DRAW_GROWTHUP_MARASARA")
        return res
