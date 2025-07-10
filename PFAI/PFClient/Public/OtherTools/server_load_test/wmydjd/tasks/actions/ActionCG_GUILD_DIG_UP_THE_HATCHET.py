# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_DIG_UP_THE_HATCHET:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_DIG_UP_THE_HATCHET(self.person)
        # params begin ( don't move this line )

        packet['targetGuildGuid'] = self.person['targetGuildGuid']
        packet['initiateType'] = self.person['initiateType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_DIG_UP_THE_HATCHET")
        return res
