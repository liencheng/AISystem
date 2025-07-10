# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SET_MARRIAGE_PERSONAL_IDENTIFICATIONID:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SET_MARRIAGE_PERSONAL_IDENTIFICATIONID(self.person)
        # params begin ( don't move this line )

        packet['nIdentificationID'] = self.person['nIdentificationID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SET_MARRIAGE_PERSONAL_IDENTIFICATIONID")
        return res
