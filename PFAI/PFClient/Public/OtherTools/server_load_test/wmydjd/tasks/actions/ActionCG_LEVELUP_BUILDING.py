# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_LEVELUP_BUILDING:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_LEVELUP_BUILDING(self.person)
        # params begin ( don't move this line )

        packet['m_HomeGuid'] = self.person['m_HomeGuid']
        packet['m_BuildingGuid'] = self.person['m_BuildingGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_LEVELUP_BUILDING")
        return res
