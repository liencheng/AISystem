# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_JOIN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_JOIN(self.person)
        # params begin ( don't move this line )

        packet['guildGuid'] = self.person['guildGuid']
        # packet['guildtype'] = self.person['guildtype']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet(self.person, "GC_GUILD_RET_QUICKJOIN")
        return res
