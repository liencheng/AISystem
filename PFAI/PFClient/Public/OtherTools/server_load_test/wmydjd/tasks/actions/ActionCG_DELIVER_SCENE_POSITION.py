# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DELIVER_SCENE_POSITION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DELIVER_SCENE_POSITION(self.person)
        # params begin ( don't move this line )

        packet['sceneID'] = self.person['sceneID']
        packet['positionX'] = self.person['positionX']
        packet['positionY'] = self.person['positionY']
        packet['positionZ'] = self.person['positionZ']
        packet['missionID'] = self.person['missionID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DELIVER_SCENE_POSITION")
        return res
