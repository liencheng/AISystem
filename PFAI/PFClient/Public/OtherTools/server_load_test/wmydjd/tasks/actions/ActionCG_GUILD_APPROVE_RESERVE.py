# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_APPROVE_RESERVE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_APPROVE_RESERVE(self.person)
        # params begin ( don't move this line )

        packet['approver'] = self.person['approver']
        packet['isAgree'] = self.person['isAgree']
        # packet['checkcredit'] = self.person['checkcredit']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_APPROVE_RESERVE")
        return res
