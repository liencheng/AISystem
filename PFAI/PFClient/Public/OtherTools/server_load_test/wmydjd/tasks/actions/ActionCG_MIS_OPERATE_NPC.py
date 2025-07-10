# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MIS_OPERATE_NPC:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MIS_OPERATE_NPC(self.person)
        # params begin ( don't move this line )

        packet['nMisId'] = self.person['nMisId']
        # packet['nLogicID'] = self.person['nLogicID']
        packet['nNpcType'] = self.person['nNpcType']
        packet['nNpcServerID'] = self.person['nNpcServerID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MIS_OPERATE_NPC")
        return res
