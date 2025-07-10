# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CACHELOG:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CACHELOG(self.person)
        # params begin ( don't move this line )

        packet['name'] = self.person['name']
        # packet['key'] = self.person['key']
        # packet['value'] = self.person['value']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CACHELOG")
        return res
