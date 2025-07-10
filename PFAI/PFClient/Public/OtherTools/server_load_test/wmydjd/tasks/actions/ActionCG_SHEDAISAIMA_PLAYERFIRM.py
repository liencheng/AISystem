# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SHEDAISAIMA_PLAYERFIRM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SHEDAISAIMA_PLAYERFIRM(self.person)
        # params begin ( don't move this line )

        packet['isok'] = self.person['isok']
        packet['optype'] = self.person['optype']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SHEDAISAIMA_PLAYERFIRM")
        return res
