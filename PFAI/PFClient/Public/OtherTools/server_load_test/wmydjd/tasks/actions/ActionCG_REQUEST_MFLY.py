# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQUEST_MFLY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQUEST_MFLY(self.person)
        # params begin ( don't move this line )

        packet['targetServerID'] = self.person['targetServerID']
        packet['inviteType'] = self.person['inviteType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQUEST_MFLY")
        return res
