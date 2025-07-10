# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_RANK_ASK_FAIRYINFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_RANK_ASK_FAIRYINFO(self.person)
        # params begin ( don't move this line )

        packet['playerguid'] = self.person['playerguid']
        packet['fairyguid'] = self.person['fairyguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_RANK_ASK_FAIRYINFO")
        return res
