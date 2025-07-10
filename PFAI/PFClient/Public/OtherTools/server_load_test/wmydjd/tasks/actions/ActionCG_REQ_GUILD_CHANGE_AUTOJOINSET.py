# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GUILD_CHANGE_AUTOJOINSET:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GUILD_CHANGE_AUTOJOINSET(self.person)
        # params begin ( don't move this line )

        packet['senderGuid'] = self.person['senderGuid']
        packet['guildGuid'] = self.person['guildGuid']
        packet['autoJoinLevel'] = self.person['autoJoinLevel']
        packet['autoJoinCombatVal'] = self.person['autoJoinCombatVal']
        # packet['isAutoRejectNonEligible'] = self.person['isAutoRejectNonEligible']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GUILD_CHANGE_AUTOJOINSET")
        return res
