# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_JOIN_OTHERPLAYER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_JOIN_OTHERPLAYER(self.person)
        # params begin ( don't move this line )

        packet['userGuid'] = self.person['userGuid']
        packet['userName'] = self.person['userName']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_JOIN_OTHERPLAYER")
        return res
