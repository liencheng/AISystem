# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UPGRADE_PRACTICE_REQUEST:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UPGRADE_PRACTICE_REQUEST(self.person)
        # params begin ( don't move this line )

        packet['nPracticeId'] = self.person['nPracticeId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UPGRADE_PRACTICE_REQUEST")
        return res
