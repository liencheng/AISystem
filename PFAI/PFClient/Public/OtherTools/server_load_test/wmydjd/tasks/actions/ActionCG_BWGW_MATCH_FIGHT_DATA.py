# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BWGW_MATCH_FIGHT_DATA:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BWGW_MATCH_FIGHT_DATA(self.person)
        # params begin ( don't move this line )

        packet['divisionId'] = self.person['divisionId']
        packet['battleRound'] = self.person['battleRound']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BWGW_MATCH_FIGHT_DATA")
        return res
