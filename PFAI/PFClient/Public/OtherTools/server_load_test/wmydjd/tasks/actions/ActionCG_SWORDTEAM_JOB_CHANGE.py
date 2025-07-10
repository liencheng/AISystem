# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SWORDTEAM_JOB_CHANGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SWORDTEAM_JOB_CHANGE(self.person)
        # params begin ( don't move this line )

        packet['approver'] = self.person['approver']
        packet['jobID'] = self.person['jobID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SWORDTEAM_JOB_CHANGE")
        return res
