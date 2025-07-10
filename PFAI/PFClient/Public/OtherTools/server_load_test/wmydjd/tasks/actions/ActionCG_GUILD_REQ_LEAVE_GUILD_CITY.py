# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILD_REQ_LEAVE_GUILD_CITY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILD_REQ_LEAVE_GUILD_CITY(self.person)
        # params begin ( don't move this line )

        packet['sceneid'] = self.person['sceneid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILD_REQ_LEAVE_GUILD_CITY")
        return res
