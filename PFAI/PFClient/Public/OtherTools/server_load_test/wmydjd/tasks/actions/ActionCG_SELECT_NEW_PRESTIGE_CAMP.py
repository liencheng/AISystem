# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SELECT_NEW_PRESTIGE_CAMP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SELECT_NEW_PRESTIGE_CAMP(self.person)
        # params begin ( don't move this line )

        packet['newPrestigeCamp'] = self.person['newPrestigeCamp']
        packet['selectType'] = self.person['selectType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SELECT_NEW_PRESTIGE_CAMP")
        return res
