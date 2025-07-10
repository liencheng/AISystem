# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_COPYSCENE_INVITE_RET:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_COPYSCENE_INVITE_RET(self.person)
        # params begin ( don't move this line )

        packet['SceneID'] = self.person['SceneID']
        packet['Ret'] = self.person['Ret']
        # packet['Tier'] = self.person['Tier']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_COPYSCENE_INVITE_RET")
        return res
