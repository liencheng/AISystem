# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MILITARY_REQ_BUYITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MILITARY_REQ_BUYITEM(self.person)
        # params begin ( don't move this line )

        packet['id'] = self.person['id']
        packet['count'] = self.person['count']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MILITARY_REQ_BUYITEM")
        return res
