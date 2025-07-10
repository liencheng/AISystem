# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_PUT_CONVO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_PUT_CONVO(self.person)
        # params begin ( don't move this line )

        packet['ItemGuid'] = self.person['ItemGuid']
        packet['ItemCOunt'] = self.person['ItemCOunt']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_PUT_CONVO")
        return res
