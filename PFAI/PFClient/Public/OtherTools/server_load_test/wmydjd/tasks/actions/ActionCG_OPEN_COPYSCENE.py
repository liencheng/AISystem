# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_OPEN_COPYSCENE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_OPEN_COPYSCENE(self.person)
        # params begin ( don't move this line )

        packet['SceneID'] = self.person['SceneID']
        packet['Mode'] = self.person['Mode']
        # packet['Grade'] = self.person['Grade']
        # packet['EnterType'] = self.person['EnterType']
        # packet['Layer'] = self.person['Layer']
        # packet['Difficulty'] = self.person['Difficulty']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_OPEN_COPYSCENE")
        return res
