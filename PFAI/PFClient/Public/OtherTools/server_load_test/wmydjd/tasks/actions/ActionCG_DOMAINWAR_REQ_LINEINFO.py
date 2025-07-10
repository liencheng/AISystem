# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DOMAINWAR_REQ_LINEINFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DOMAINWAR_REQ_LINEINFO(self.person)
        # params begin ( don't move this line )

        packet['domainId'] = self.person['domainId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DOMAINWAR_REQ_LINEINFO")
        return res
