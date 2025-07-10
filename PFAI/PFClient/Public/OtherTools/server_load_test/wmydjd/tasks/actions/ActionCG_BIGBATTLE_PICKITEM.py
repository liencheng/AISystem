# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BIGBATTLE_PICKITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BIGBATTLE_PICKITEM(self.person)
        # params begin ( don't move this line )

        packet['targetId'] = self.person['targetId']
        packet['bigBattleType'] = self.person['bigBattleType']
        packet['sceneClassID'] = self.person['sceneClassID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BIGBATTLE_PICKITEM")
        return res
