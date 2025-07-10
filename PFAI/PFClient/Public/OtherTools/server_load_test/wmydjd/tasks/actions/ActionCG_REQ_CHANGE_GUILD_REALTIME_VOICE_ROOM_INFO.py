# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_CHANGE_GUILD_REALTIME_VOICE_ROOM_INFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_CHANGE_GUILD_REALTIME_VOICE_ROOM_INFO(self.person)
        # params begin ( don't move this line )

        packet['RoomId'] = self.person['RoomId']
        packet['IsChangeIcon'] = self.person['IsChangeIcon']
        packet['IconId'] = self.person['IconId']
        packet['IsChangeRoomName'] = self.person['IsChangeRoomName']
        packet['RoomName'] = self.person['RoomName']
        packet['IsChangeRoomDesc'] = self.person['IsChangeRoomDesc']
        packet['RoomDesc'] = self.person['RoomDesc']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_CHANGE_GUILD_REALTIME_VOICE_ROOM_INFO")
        return res
