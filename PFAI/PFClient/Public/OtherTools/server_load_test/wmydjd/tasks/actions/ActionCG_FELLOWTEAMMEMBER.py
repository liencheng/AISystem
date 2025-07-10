# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FELLOWTEAMMEMBER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FELLOWTEAMMEMBER(self.person)
        # params begin ( don't move this line )

        packet['targetguid'] = self.person['targetguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FELLOWTEAMMEMBER")
        return res
