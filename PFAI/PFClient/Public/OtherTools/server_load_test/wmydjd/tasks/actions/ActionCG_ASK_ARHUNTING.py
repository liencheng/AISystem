# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_ARHUNTING:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_ARHUNTING(self.person)
        # params begin ( don't move this line )

        packet['itemguid'] = self.person['itemguid']
        packet['huntingmode'] = self.person['huntingmode']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_ARHUNTING")
        return res
