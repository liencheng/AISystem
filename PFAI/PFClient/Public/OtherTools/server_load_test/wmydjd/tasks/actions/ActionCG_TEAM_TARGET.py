# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TEAM_TARGET:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TEAM_TARGET(self.person)
        # params begin ( don't move this line )

        packet['targetID'] = self.person['targetID']
        packet['minLevel'] = self.person['minLevel']
        packet['maxLevel'] = self.person['maxLevel']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TEAM_TARGET")
        return res
