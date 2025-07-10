# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_INTERACT_JUMP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_INTERACT_JUMP(self.person)
        # params begin ( don't move this line )

        packet['inviteeServerID'] = self.person['inviteeServerID']
        packet['interactType'] = self.person['interactType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_INTERACT_JUMP")
        return res
