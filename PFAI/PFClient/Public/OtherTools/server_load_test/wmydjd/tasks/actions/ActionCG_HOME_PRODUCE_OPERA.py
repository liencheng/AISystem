# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HOME_PRODUCE_OPERA:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HOME_PRODUCE_OPERA(self.person)
        # params begin ( don't move this line )

        packet['m_HomeGuid'] = self.person['m_HomeGuid']
        packet['m_HomeOwnerGuid'] = self.person['m_HomeOwnerGuid']
        packet['m_BuildingGuid'] = self.person['m_BuildingGuid']
        packet['m_Operate'] = self.person['m_Operate']
        packet['m_Param0'] = self.person['m_Param0']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HOME_PRODUCE_OPERA")
        return res
