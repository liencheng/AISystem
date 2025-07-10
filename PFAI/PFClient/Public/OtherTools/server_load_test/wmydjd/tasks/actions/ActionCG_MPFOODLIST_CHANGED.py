# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MPFOODLIST_CHANGED:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MPFOODLIST_CHANGED(self.person)
        # params begin ( don't move this line )

        # packet['MPFoodlist'] = self.person['MPFoodlist']
        packet['MPAutoValue'] = self.person['MPAutoValue']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MPFOODLIST_CHANGED")
        return res
