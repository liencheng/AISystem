# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TONGTIANTREASURE_REQOP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TONGTIANTREASURE_REQOP(self.person)
        # params begin ( don't move this line )

        packet['optype'] = self.person['optype']
        packet['mapid'] = self.person['mapid']
        packet['param1'] = self.person['param1']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TONGTIANTREASURE_REQOP")
        return res
