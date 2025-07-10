# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_MERGE_INSCRP0TION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_MERGE_INSCRP0TION(self.person)
        # params begin ( don't move this line )

        packet['bIsInlay'] = self.person['bIsInlay']
        packet['itemGuid'] = self.person['itemGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_MERGE_INSCRP0TION")
        return res
