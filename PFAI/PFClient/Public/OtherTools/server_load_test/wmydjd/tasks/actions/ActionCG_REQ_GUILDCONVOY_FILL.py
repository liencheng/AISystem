# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GUILDCONVOY_FILL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GUILDCONVOY_FILL(self.person)
        # params begin ( don't move this line )

        packet['operateType'] = self.person['operateType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GUILDCONVOY_FILL")
        return res
