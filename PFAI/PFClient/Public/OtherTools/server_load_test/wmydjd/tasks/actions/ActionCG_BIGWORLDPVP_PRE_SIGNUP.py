# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BIGWORLDPVP_PRE_SIGNUP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BIGWORLDPVP_PRE_SIGNUP(self.person)
        # params begin ( don't move this line )

        packet['signupType'] = self.person['signupType']
        # packet['matchOpenOrClose'] = self.person['matchOpenOrClose']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BIGWORLDPVP_PRE_SIGNUP")
        return res
