# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SET_GUILD_ACTIVITY_OPEN_TIME:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SET_GUILD_ACTIVITY_OPEN_TIME(self.person)
        # params begin ( don't move this line )

        packet['hour'] = self.person['hour']
        packet['minute'] = self.person['minute']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SET_GUILD_ACTIVITY_OPEN_TIME")
        return res
