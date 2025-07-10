# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_CREATE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_CREATE(self.person)
        # params begin ( don't move this line )

        packet['guildName'] = self.person['guildName']
        packet['guildNotice'] = self.person['guildNotice']
        packet['guildShortName'] = self.person['guildShortName']
        packet['guildShortNameColor'] = self.person['guildShortNameColor']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_packet_with_heartbeat(self.person, "GC_GUILD_CREATE")
        return res
