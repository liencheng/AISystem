# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILDTEAM_APPLYFASTTEAM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILDTEAM_APPLYFASTTEAM(self.person)
        # params begin ( don't move this line )

        packet['m_nTeamId'] = self.person['m_nTeamId']
        # packet['playerGuid'] = self.person['playerGuid']
        packet['m_nTargetId'] = self.person['m_nTargetId']
        packet['m_nMinLv'] = self.person['m_nMinLv']
        packet['m_nMaxLv'] = self.person['m_nMaxLv']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILDTEAM_APPLYFASTTEAM")
        return res
