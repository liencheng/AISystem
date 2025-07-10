# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SWORDTEAM_INVITE_CONFIRM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SWORDTEAM_INVITE_CONFIRM(self.person)
        # params begin ( don't move this line )

        packet['inviterGuid'] = self.person['inviterGuid']
        packet['inviterswordteamGuid'] = self.person['inviterswordteamGuid']
        packet['agree'] = self.person['agree']
        packet['inviterName'] = self.person['inviterName']
        # packet['job'] = self.person['job']
        packet['inviterSignCode'] = self.person['inviterSignCode']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SWORDTEAM_INVITE_CONFIRM")
        return res
