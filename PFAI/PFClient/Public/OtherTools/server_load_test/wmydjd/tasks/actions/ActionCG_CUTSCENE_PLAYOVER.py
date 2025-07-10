# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CUTSCENE_PLAYOVER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CUTSCENE_PLAYOVER(self.person)
        # params begin ( don't move this line )

        packet['cutSceneID'] = self.person['cutSceneID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CUTSCENE_PLAYOVER")
        return res
