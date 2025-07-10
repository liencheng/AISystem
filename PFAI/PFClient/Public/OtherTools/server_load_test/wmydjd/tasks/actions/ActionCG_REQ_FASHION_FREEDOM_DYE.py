# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_FASHION_FREEDOM_DYE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_FASHION_FREEDOM_DYE(self.person)
        # params begin ( don't move this line )

        packet['fashionId'] = self.person['fashionId']
        packet['slotId'] = self.person['slotId']
        packet['Part1'] = self.person['Part1']
        packet['Part2'] = self.person['Part2']
        packet['Part3'] = self.person['Part3']
        packet['Part4'] = self.person['Part4']
        packet['onlySwitch'] = self.person['onlySwitch']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_FASHION_FREEDOM_DYE")
        return res
