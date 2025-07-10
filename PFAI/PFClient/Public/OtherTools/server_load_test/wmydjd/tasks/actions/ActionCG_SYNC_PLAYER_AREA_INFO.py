# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SYNC_PLAYER_AREA_INFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SYNC_PLAYER_AREA_INFO(self.person)
        # params begin ( don't move this line )

        # packet['self'] = self.person['self']
        # packet['friend'] = self.person['friend']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SYNC_PLAYER_AREA_INFO")
        return res
