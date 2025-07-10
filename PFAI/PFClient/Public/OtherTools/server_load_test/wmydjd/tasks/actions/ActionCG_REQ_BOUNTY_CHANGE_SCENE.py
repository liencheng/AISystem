# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_BOUNTY_CHANGE_SCENE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_BOUNTY_CHANGE_SCENE(self.person)
        # params begin ( don't move this line )

        packet['sceneClassID'] = self.person['sceneClassID']
        packet['sceneInstID'] = self.person['sceneInstID']
        packet['posx'] = self.person['posx']
        packet['posy'] = self.person['posy']
        packet['posz'] = self.person['posz']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_BOUNTY_CHANGE_SCENE")
        return res
