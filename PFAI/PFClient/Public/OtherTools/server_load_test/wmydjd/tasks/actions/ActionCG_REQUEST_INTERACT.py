# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQUEST_INTERACT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQUEST_INTERACT(self.person)
        # params begin ( don't move this line )

        packet['inviteeServerID'] = self.person['inviteeServerID']
        packet['interactType'] = self.person['interactType']
        packet['objType'] = self.person['objType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQUEST_INTERACT")
        return res
