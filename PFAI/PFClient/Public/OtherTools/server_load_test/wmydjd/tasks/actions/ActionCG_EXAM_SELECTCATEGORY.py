# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_EXAM_SELECTCATEGORY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_EXAM_SELECTCATEGORY(self.person)
        # params begin ( don't move this line )

        packet['categoryType'] = self.person['categoryType']
        packet['examType'] = self.person['examType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_EXAM_SELECTCATEGORY")
        return res
