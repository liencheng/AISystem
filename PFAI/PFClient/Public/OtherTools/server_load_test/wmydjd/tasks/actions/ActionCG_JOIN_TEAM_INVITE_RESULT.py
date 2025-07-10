# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_JOIN_TEAM_INVITE_RESULT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_JOIN_TEAM_INVITE_RESULT(self.person)
        # params begin ( don't move this line )

        packet['result'] = self.person['result']
        packet['sysreply'] = self.person['sysreply']
        packet['inviterGuid'] = self.person['inviterGuid']
        packet['inviterName'] = self.person['inviterName']
        packet['inviterSignCode'] = self.person['inviterSignCode']
        packet['armyID'] = self.person['armyID']
        packet['bFullTeamInvite'] = self.person['bFullTeamInvite']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_JOIN_TEAM_INVITE_RESULT")
        return res
