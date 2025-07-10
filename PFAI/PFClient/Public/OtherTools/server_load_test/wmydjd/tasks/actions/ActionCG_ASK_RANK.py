# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_RANK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_RANK(self.person)
        # params begin ( don't move this line )

        packet['nType'] = self.person['nType']
        packet['nPage'] = self.person['nPage']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet(self.person, "GC_RET_RANK")
        return res