# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_CHANGEPROFESSION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_CHANGEPROFESSION(self.person)
        # params begin ( don't move this line )

        packet['targetprofession'] = self.person['targetprofession']
        packet['targetsex'] = self.person['targetsex']
        # packet['exchangeZhuanJing'] = self.person['exchangeZhuanJing']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_CHANGEPROFESSION")
        return res
