# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REPORT_TOGM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REPORT_TOGM(self.person)
        # params begin ( don't move this line )

        packet['charguid'] = self.person['charguid']
        packet['charname'] = self.person['charname']
        packet['charchat'] = self.person['charchat']
        packet['profession'] = self.person['profession']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REPORT_TOGM")
        return res
