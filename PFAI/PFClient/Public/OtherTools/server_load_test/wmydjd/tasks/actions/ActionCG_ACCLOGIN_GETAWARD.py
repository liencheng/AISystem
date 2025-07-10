# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ACCLOGIN_GETAWARD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ACCLOGIN_GETAWARD(self.person)
        # params begin ( don't move this line )

        packet['version'] = self.person['version']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ACCLOGIN_GETAWARD")
        return res
