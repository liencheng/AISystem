# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_LIFESKILL_LIANDAN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_LIFESKILL_LIANDAN(self.person)
        # params begin ( don't move this line )

        packet['material1'] = self.person['material1']
        packet['material2'] = self.person['material2']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_LIFESKILL_LIANDAN")
        return res
