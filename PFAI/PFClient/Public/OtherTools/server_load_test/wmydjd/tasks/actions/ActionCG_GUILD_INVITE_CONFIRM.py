# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_INVITE_CONFIRM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_INVITE_CONFIRM(self.person)
        # params begin ( don't move this line )

        packet['inviterGuid'] = self.person['inviterGuid']
        packet['inviterGuildGuid'] = self.person['inviterGuildGuid']
        packet['agree'] = self.person['agree']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_INVITE_CONFIRM")
        return res
