# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SKILL_SWITCH_TYPE_SKILL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SKILL_SWITCH_TYPE_SKILL(self.person)
        # params begin ( don't move this line )

        packet['baseID'] = self.person['baseID']
        packet['bIsOpen'] = self.person['bIsOpen']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SKILL_SWITCH_TYPE_SKILL")
        return res
