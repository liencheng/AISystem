# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_RESET_FAIRY_ATTR_POINTS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_RESET_FAIRY_ATTR_POINTS(self.person)
        # params begin ( don't move this line )

        packet['fairyguid'] = self.person['fairyguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_RESET_FAIRY_ATTR_POINTS")
        return res
