# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ADD_HATEPEOPLE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ADD_HATEPEOPLE(self.person)
        # params begin ( don't move this line )

        packet['DuelGuid'] = self.person['DuelGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ADD_HATEPEOPLE")
        return res
