# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CPS_PICKUP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CPS_PICKUP(self.person)
        # params begin ( don't move this line )

        packet['m_ServerId'] = self.person['m_ServerId']
        packet['m_DataId'] = self.person['m_DataId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CPS_PICKUP")
        return res
