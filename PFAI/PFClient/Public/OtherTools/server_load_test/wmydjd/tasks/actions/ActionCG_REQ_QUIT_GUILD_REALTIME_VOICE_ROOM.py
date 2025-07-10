# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_QUIT_GUILD_REALTIME_VOICE_ROOM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_QUIT_GUILD_REALTIME_VOICE_ROOM(self.person)
        # params begin ( don't move this line )

        packet['roomId'] = self.person['roomId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_QUIT_GUILD_REALTIME_VOICE_ROOM")
        return res
