# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BATTLEFIELD_LEAVE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BATTLEFIELD_LEAVE(self.person)
        # params begin ( don't move this line )

        packet['SignupID'] = self.person['SignupID']
        packet['BFSceneClassID'] = self.person['BFSceneClassID']
        packet['BFSceneInstID'] = self.person['BFSceneInstID']
        packet['BFSceneOpenIstID'] = self.person['BFSceneOpenIstID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BATTLEFIELD_LEAVE")
        return res
