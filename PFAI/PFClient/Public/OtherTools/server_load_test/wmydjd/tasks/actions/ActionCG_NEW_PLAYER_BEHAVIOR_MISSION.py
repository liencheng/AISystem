# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_NEW_PLAYER_BEHAVIOR_MISSION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_NEW_PLAYER_BEHAVIOR_MISSION(self.person)
        # params begin ( don't move this line )

        packet['missionID'] = self.person['missionID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_NEW_PLAYER_BEHAVIOR_MISSION")
        return res
