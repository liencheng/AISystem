# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_CANCEL_APPLICANT_TEAM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_CANCEL_APPLICANT_TEAM(self.person)
        # params begin ( don't move this line )

        # packet['armyID'] = self.person['armyID']
        # packet['teamID'] = self.person['teamID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_CANCEL_APPLICANT_TEAM")
        return res
