# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_TYPE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_TYPE(self.person)
        # params begin ( don't move this line )

        packet['GRTVRMemberGuid'] = self.person['GRTVRMemberGuid']
        packet['GRTVRMemberName'] = self.person['GRTVRMemberName']
        packet['GRTVRMemberType'] = self.person['GRTVRMemberType']
        packet['GRTVRoomId'] = self.person['GRTVRoomId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_TYPE")
        return res
