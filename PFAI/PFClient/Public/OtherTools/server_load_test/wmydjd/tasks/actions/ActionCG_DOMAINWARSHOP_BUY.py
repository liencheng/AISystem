# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DOMAINWARSHOP_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DOMAINWARSHOP_BUY(self.person)
        # params begin ( don't move this line )

        packet['npcid'] = self.person['npcid']
        packet['itemindex'] = self.person['itemindex']
        packet['itemnum'] = self.person['itemnum']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DOMAINWARSHOP_BUY")
        return res
