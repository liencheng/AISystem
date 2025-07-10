# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SKILLZHUANJING_LEVEL_UP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SKILLZHUANJING_LEVEL_UP(self.person)
        # params begin ( don't move this line )

        packet['SkillZhuanjingId'] = self.person['SkillZhuanjingId']
        packet['transformType'] = self.person['transformType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SKILLZHUANJING_LEVEL_UP")
        return res
