# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REPLY_INTERACT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REPLY_INTERACT(self.person)
        # params begin ( don't move this line )

        packet['inviteeServerID'] = self.person['inviteeServerID']
        packet['isAgree'] = self.person['isAgree']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REPLY_INTERACT")
        return res
