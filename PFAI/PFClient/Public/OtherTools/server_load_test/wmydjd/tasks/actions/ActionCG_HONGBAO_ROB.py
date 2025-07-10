# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HONGBAO_ROB:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HONGBAO_ROB(self.person)
        # params begin ( don't move this line )

        packet['Guid'] = self.person['Guid']
        packet['nChannel'] = self.person['nChannel']
        packet['nMoneyType'] = self.person['nMoneyType']
        packet['strKouLing'] = self.person['strKouLing']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HONGBAO_ROB")
        return res
