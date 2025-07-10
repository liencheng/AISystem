# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_PASSPORT_BUY_LEVEL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_PASSPORT_BUY_LEVEL(self.person)
        # params begin ( don't move this line )

        packet['passlevel'] = self.person['passlevel']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_PASSPORT_BUY_LEVEL")
        return res
