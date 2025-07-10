# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_APPOINT_OPEN_PLAYER_GZONE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_APPOINT_OPEN_PLAYER_GZONE(self.person)
        # params begin ( don't move this line )

        packet['openType'] = self.person['openType']
        packet['targetGuid'] = self.person['targetGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_APPOINT_OPEN_PLAYER_GZONE")
        return res
