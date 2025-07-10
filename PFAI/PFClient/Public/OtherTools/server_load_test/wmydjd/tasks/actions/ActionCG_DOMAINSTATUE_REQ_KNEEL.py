# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DOMAINSTATUE_REQ_KNEEL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DOMAINSTATUE_REQ_KNEEL(self.person)
        # params begin ( don't move this line )

        packet['kneelType'] = self.person['kneelType']
        packet['kneelState'] = self.person['kneelState']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DOMAINSTATUE_REQ_KNEEL")
        return res
