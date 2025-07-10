# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILDMONSTER_UNLOCK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILDMONSTER_UNLOCK(self.person)
        # params begin ( don't move this line )

        packet['GuildMonsterId'] = self.person['GuildMonsterId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILDMONSTER_UNLOCK")
        return res
