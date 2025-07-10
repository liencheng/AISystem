# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SECPASSWORD_RELEASELOCK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SECPASSWORD_RELEASELOCK(self.person)
        # params begin ( don't move this line )

        packet['optiontype'] = self.person['optiontype']
        packet['releastype'] = self.person['releastype']
        packet['PlayerGuid'] = self.person['PlayerGuid']
        packet['Password'] = self.person['Password']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SECPASSWORD_RELEASELOCK")
        return res
