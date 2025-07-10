# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BWPVPFINAL_ASKVIEW:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BWPVPFINAL_ASKVIEW(self.person)
        # params begin ( don't move this line )

        packet['MemAGuid'] = self.person['MemAGuid']
        packet['MemBGuid'] = self.person['MemBGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BWPVPFINAL_ASKVIEW")
        return res
