# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_TEAM_CHANGE_LEADER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_TEAM_CHANGE_LEADER(self.person)
        # params begin ( don't move this line )

        packet['teamMemberGuid'] = self.person['teamMemberGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_TEAM_CHANGE_LEADER")
        return res
