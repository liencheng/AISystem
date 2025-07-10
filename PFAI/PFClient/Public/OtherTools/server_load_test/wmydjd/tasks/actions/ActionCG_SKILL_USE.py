# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SKILL_USE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SKILL_USE(self.person)
        # params begin ( don't move this line )

        packet['skillId'] = self.person['skillId']
        # packet['targetId'] = self.person['targetId']
        packet['posx'] = self.person['posx']
        packet['posy'] = self.person['posy']
        packet['posz'] = self.person['posz']
        packet['curFaceto'] = self.person['curFaceto']
        packet['vDirectionX'] = self.person['vDirectionX']
        packet['vDirectionY'] = self.person['vDirectionY']
        packet['vDirectionZ'] = self.person['vDirectionZ']
        packet['vTargetX'] = self.person['vTargetX']
        packet['vTargetY'] = self.person['vTargetY']
        packet['vTargetZ'] = self.person['vTargetZ']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SKILL_USE")
        return res
