# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CHANGE_FAIRY_NAME:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CHANGE_FAIRY_NAME(self.person)
        # params begin ( don't move this line )

        packet['fairyguid'] = self.person['fairyguid']
        packet['name'] = self.person['name']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CHANGE_FAIRY_NAME")
        return res
