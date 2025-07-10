# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GUILD_ADDITION_LEVELUP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GUILD_ADDITION_LEVELUP(self.person)
        # params begin ( don't move this line )

        packet['index'] = self.person['index']
        packet['guildGuid'] = self.person['guildGuid']
        packet['type'] = self.person['type']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GUILD_ADDITION_LEVELUP")
        return res
