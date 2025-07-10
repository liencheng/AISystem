# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_USE_REDLINE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_USE_REDLINE(self.person)
        # params begin ( don't move this line )

        packet['targetGuid'] = self.person['targetGuid']
        packet['itemCount'] = self.person['itemCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_USE_REDLINE")
        return res
