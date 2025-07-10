# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SECPASSWORD_REDPOINTREADED:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SECPASSWORD_REDPOINTREADED(self.person)
        # params begin ( don't move this line )

        packet['param'] = self.person['param']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SECPASSWORD_REDPOINTREADED")
        return res
