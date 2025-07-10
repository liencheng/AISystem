# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_NEW_PRESTIGE_CAMP_ROLE_NUMER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_NEW_PRESTIGE_CAMP_ROLE_NUMER(self.person)
        # params begin ( don't move this line )

        packet['reqType'] = self.person['reqType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_NEW_PRESTIGE_CAMP_ROLE_NUMER")
        return res
