# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE(self.person)
        # params begin ( don't move this line )

        packet['targetPosX'] = self.person['targetPosX']
        packet['targetPosY'] = self.person['targetPosY']
        packet['targetPosZ'] = self.person['targetPosZ']
        packet['nSceneId'] = self.person['nSceneId']
        packet['nSceneInstanceId'] = self.person['nSceneInstanceId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE")
        return res
