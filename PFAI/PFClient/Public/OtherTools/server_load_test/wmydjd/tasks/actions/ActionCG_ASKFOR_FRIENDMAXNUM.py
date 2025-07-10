# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASKFOR_FRIENDMAXNUM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASKFOR_FRIENDMAXNUM(self.person)
        # params begin ( don't move this line )

        packet['optionCode'] = self.person['optionCode']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASKFOR_FRIENDMAXNUM")
        return res
