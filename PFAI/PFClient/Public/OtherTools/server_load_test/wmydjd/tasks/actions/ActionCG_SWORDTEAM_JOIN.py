# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SWORDTEAM_JOIN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SWORDTEAM_JOIN(self.person)
        # params begin ( don't move this line )

        packet['swordteamGuid'] = self.person['swordteamGuid']
        # packet['joinbylink'] = self.person['joinbylink']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SWORDTEAM_JOIN")
        return res
