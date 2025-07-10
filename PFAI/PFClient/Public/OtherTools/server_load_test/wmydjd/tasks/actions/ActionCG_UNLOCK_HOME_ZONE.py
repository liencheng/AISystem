# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UNLOCK_HOME_ZONE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UNLOCK_HOME_ZONE(self.person)
        # params begin ( don't move this line )

        packet['m_HomeGuid'] = self.person['m_HomeGuid']
        packet['m_ZoneIndex'] = self.person['m_ZoneIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UNLOCK_HOME_ZONE")
        return res
