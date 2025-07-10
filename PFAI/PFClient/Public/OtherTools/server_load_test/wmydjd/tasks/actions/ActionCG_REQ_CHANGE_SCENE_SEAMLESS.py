# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_CHANGE_SCENE_SEAMLESS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_CHANGE_SCENE_SEAMLESS(self.person)
        # params begin ( don't move this line )

        packet['sceneId'] = self.person['sceneId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_CHANGE_SCENE_SEAMLESS")
        return res
