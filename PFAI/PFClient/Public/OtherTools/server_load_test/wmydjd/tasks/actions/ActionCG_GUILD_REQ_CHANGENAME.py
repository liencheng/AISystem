# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_REQ_CHANGENAME:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_REQ_CHANGENAME(self.person)
        # params begin ( don't move this line )

        packet['changeName'] = self.person['changeName']
        packet['changeShortName'] = self.person['changeShortName']
        packet['changeShortNameColor'] = self.person['changeShortNameColor']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_REQ_CHANGENAME")
        return res
