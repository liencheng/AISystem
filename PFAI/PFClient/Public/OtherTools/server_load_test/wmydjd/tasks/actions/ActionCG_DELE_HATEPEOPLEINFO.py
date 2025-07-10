# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DELE_HATEPEOPLEINFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DELE_HATEPEOPLEINFO(self.person)
        # params begin ( don't move this line )

        packet['HateGuid'] = self.person['HateGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DELE_HATEPEOPLEINFO")
        return res
