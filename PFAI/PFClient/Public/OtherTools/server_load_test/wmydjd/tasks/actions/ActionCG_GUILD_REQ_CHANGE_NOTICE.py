# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_REQ_CHANGE_NOTICE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_REQ_CHANGE_NOTICE(self.person)
        # params begin ( don't move this line )

        packet['guildNotice'] = self.person['guildNotice']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_REQ_CHANGE_NOTICE")
        return res
