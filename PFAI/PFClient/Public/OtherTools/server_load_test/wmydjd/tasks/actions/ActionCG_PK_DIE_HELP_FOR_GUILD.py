# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_PK_DIE_HELP_FOR_GUILD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_PK_DIE_HELP_FOR_GUILD(self.person)
        # params begin ( don't move this line )

        packet['targetName'] = self.person['targetName']
        packet['targetGuildName'] = self.person['targetGuildName']
        # packet['helpType'] = self.person['helpType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_PK_DIE_HELP_FOR_GUILD")
        return res
