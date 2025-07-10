# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HONGBAO_CHARGE_SEND:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HONGBAO_CHARGE_SEND(self.person)
        # params begin ( don't move this line )

        packet['strDesc'] = self.person['strDesc']
        packet['nMaxCount'] = self.person['nMaxCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HONGBAO_CHARGE_SEND")
        return res
