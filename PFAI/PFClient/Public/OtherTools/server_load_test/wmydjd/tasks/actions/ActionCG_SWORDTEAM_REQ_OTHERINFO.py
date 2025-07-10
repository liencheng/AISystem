# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SWORDTEAM_REQ_OTHERINFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SWORDTEAM_REQ_OTHERINFO(self.person)
        # params begin ( don't move this line )

        packet['requester'] = self.person['requester']
        packet['tarSwordTeamGuid'] = self.person['tarSwordTeamGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SWORDTEAM_REQ_OTHERINFO")
        return res
