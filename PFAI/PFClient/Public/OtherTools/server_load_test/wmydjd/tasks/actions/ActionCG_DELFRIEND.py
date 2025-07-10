# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DELFRIEND:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DELFRIEND(self.person)
        # params begin ( don't move this line )

        packet['guid'] = self.person['guid']
        packet['delType'] = self.person['delType']
        packet['reportFriend'] = self.person['reportFriend']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DELFRIEND")
        return res
