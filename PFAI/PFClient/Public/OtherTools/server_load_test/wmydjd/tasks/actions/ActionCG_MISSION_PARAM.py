# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MISSION_PARAM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MISSION_PARAM(self.person)
        # params begin ( don't move this line )

        packet['nMisID'] = self.person['nMisID']
        packet['nTargetIndex'] = self.person['nTargetIndex']
        packet['nParamIndex'] = self.person['nParamIndex']
        packet['nVal'] = self.person['nVal']
        # packet['nAnswerCount'] = self.person['nAnswerCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MISSION_PARAM")
        return res
