# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MIS_QIYU_REVIEW:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MIS_QIYU_REVIEW(self.person)
        # params begin ( don't move this line )

        packet['time'] = self.person['time']
        packet['review'] = self.person['review']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MIS_QIYU_REVIEW")
        return res
