# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_PA_OPERATE_RESPONSE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_PA_OPERATE_RESPONSE(self.person)
        # params begin ( don't move this line )

        packet['OperateCode'] = self.person['OperateCode']
        packet['IsAdult'] = self.person['IsAdult']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_PA_OPERATE_RESPONSE")
        return res
