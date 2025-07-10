# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_PK_DEATHAID:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_PK_DEATHAID(self.person)
        # params begin ( don't move this line )

        packet['sceneId'] = self.person['sceneId']
        packet['sceneInst'] = self.person['sceneInst']
        packet['posX'] = self.person['posX']
        packet['posY'] = self.person['posY']
        packet['posZ'] = self.person['posZ']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_PK_DEATHAID")
        return res
