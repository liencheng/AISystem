# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_BOUNTY_REFREST_STATE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_BOUNTY_REFREST_STATE(self.person)
        # params begin ( don't move this line )

        packet['refreshID'] = self.person['refreshID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_BOUNTY_REFREST_STATE")
        return res
