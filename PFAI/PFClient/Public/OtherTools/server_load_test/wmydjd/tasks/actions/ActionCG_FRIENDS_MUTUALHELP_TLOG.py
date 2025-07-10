# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FRIENDS_MUTUALHELP_TLOG:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FRIENDS_MUTUALHELP_TLOG(self.person)
        # params begin ( don't move this line )

        packet['nMutualHelpType'] = self.person['nMutualHelpType']
        packet['bShared'] = self.person['bShared']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FRIENDS_MUTUALHELP_TLOG")
        return res
