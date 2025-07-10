# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_READY_CONFIRM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_READY_CONFIRM(self.person)
        # params begin ( don't move this line )

        packet['bLeaderReq'] = self.person['bLeaderReq']
        packet['memberGuid'] = self.person['memberGuid']
        packet['state'] = self.person['state']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_READY_CONFIRM")
        return res
