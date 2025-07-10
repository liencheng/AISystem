# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SEND_PLAYANDGO_ERROR_LOG:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SEND_PLAYANDGO_ERROR_LOG(self.person)
        # params begin ( don't move this line )

        packet['errorType'] = self.person['errorType']
        packet['errorMsg'] = self.person['errorMsg']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SEND_PLAYANDGO_ERROR_LOG")
        return res
