# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MARRIAGE_PROCESS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MARRIAGE_PROCESS(self.person)
        # params begin ( don't move this line )

        packet['type'] = self.person['type']
        packet['targetguid'] = self.person['targetguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MARRIAGE_PROCESS")
        return res
