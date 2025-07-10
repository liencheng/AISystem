# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CHECK_GUILDSTUDIO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CHECK_GUILDSTUDIO(self.person)
        # params begin ( don't move this line )

        packet['jointype'] = self.person['jointype']
        packet['guid'] = self.person['guid']
        packet['szname'] = self.person['szname']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CHECK_GUILDSTUDIO")
        return res
