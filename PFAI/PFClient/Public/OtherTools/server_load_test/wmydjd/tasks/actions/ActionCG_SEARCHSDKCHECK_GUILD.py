# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SEARCHSDKCHECK_GUILD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SEARCHSDKCHECK_GUILD(self.person)
        # params begin ( don't move this line )

        packet['keystring'] = self.person['keystring']
        packet['pageuid'] = self.person['pageuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SEARCHSDKCHECK_GUILD")
        return res
