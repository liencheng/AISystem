# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SKILLZHUANJING_OPEN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SKILLZHUANJING_OPEN(self.person)
        # params begin ( don't move this line )

        packet['SkillZhuanjingLine'] = self.person['SkillZhuanjingLine']
        packet['OrignSkill'] = self.person['OrignSkill']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SKILLZHUANJING_OPEN")
        return res
