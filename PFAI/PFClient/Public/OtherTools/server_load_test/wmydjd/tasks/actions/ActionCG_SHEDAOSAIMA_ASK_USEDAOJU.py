# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SHEDAOSAIMA_ASK_USEDAOJU:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SHEDAOSAIMA_ASK_USEDAOJU(self.person)
        # params begin ( don't move this line )

        packet['DaoJuId'] = self.person['DaoJuId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SHEDAOSAIMA_ASK_USEDAOJU")
        return res
