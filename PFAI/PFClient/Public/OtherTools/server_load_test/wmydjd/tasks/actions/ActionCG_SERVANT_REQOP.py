# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SERVANT_REQOP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SERVANT_REQOP(self.person)
        # params begin ( don't move this line )

        packet['m_OpType'] = self.person['m_OpType']
        packet['m_ServantId'] = self.person['m_ServantId']
        packet['m_Param0'] = self.person['m_Param0']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SERVANT_REQOP")
        return res
