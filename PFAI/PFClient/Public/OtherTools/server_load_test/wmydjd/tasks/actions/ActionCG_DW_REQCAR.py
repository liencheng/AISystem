# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DW_REQCAR:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DW_REQCAR(self.person)
        # params begin ( don't move this line )

        packet['optType'] = self.person['optType']
        packet['carId'] = self.person['carId']
        packet['carObjId'] = self.person['carObjId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DW_REQCAR")
        return res
