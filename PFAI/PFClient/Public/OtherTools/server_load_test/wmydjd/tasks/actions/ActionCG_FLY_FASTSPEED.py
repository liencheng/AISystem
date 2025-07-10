# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FLY_FASTSPEED:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FLY_FASTSPEED(self.person)
        # params begin ( don't move this line )

        packet['opType'] = self.person['opType']
        # packet['openAutoFly'] = self.person['openAutoFly']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FLY_FASTSPEED")
        return res
