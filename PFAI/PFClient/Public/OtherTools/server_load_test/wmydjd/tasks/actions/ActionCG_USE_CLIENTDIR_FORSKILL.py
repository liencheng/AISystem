# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_USE_CLIENTDIR_FORSKILL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_USE_CLIENTDIR_FORSKILL(self.person)
        # params begin ( don't move this line )

        # packet['skillid'] = self.person['skillid']
        # packet['facedir'] = self.person['facedir']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_USE_CLIENTDIR_FORSKILL")
        return res
