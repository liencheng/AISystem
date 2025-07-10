# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_LINGSHI_REDUCTION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_LINGSHI_REDUCTION(self.person)
        # params begin ( don't move this line )

        # packet['itemGuid'] = self.person['itemGuid']
        # packet['itemCount'] = self.person['itemCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_LINGSHI_REDUCTION")
        return res
