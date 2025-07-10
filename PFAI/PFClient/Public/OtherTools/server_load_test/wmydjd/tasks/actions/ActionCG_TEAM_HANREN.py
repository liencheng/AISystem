# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TEAM_HANREN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TEAM_HANREN(self.person)
        # params begin ( don't move this line )

        packet['content'] = self.person['content']
        packet['sceneID'] = self.person['sceneID']
        packet['grade'] = self.person['grade']
        packet['channel'] = self.person['channel']
        # packet['title'] = self.person['title']
        # packet['isActivity'] = self.person['isActivity']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TEAM_HANREN")
        return res
