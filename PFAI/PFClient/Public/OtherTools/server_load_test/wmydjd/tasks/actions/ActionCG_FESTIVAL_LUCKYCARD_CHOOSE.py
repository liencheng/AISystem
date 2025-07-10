# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FESTIVAL_LUCKYCARD_CHOOSE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FESTIVAL_LUCKYCARD_CHOOSE(self.person)
        # params begin ( don't move this line )

        packet['Id'] = self.person['Id']
        packet['ChooseNum'] = self.person['ChooseNum']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FESTIVAL_LUCKYCARD_CHOOSE")
        return res
