# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_SWORDTEAM_INVITE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_SWORDTEAM_INVITE(self.person)
        # params begin ( don't move this line )

        # packet['guid'] = self.person['guid']
        packet['targetId'] = self.person['targetId']
        packet['minLv'] = self.person['minLv']
        packet['maxLv'] = self.person['maxLv']
        packet['invitetype'] = self.person['invitetype']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_SWORDTEAM_INVITE")
        return res
