# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_KICK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_KICK(self.person)
        # params begin ( don't move this line )

        packet['kicked'] = self.person['kicked']
        packet['kickreason'] = self.person['kickreason']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_KICK")
        return res
