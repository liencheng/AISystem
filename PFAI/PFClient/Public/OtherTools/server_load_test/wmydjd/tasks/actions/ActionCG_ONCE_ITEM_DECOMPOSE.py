# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ONCE_ITEM_DECOMPOSE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ONCE_ITEM_DECOMPOSE(self.person)
        # params begin ( don't move this line )

        packet['itemcolor'] = self.person['itemcolor']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ONCE_ITEM_DECOMPOSE")
        return res
