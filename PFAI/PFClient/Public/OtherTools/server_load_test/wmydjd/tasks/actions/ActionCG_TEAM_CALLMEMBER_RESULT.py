# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TEAM_CALLMEMBER_RESULT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TEAM_CALLMEMBER_RESULT(self.person)
        # params begin ( don't move this line )

        packet['result'] = self.person['result']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TEAM_CALLMEMBER_RESULT")
        return res
