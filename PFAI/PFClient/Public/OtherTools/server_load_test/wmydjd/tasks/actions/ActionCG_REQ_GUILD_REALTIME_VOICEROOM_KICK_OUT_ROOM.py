# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM(self.person)
        # params begin ( don't move this line )

        packet['KickOutMemberGuid'] = self.person['KickOutMemberGuid']
        packet['KickOutMemberName'] = self.person['KickOutMemberName']
        packet['KickOutRoomId'] = self.person['KickOutRoomId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM")
        return res
