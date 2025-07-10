# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_AID_PUBLISH:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_AID_PUBLISH(self.person)
        # params begin ( don't move this line )

        packet['misID'] = self.person['misID']
        packet['misName'] = self.person['misName']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_AID_PUBLISH")
        return res
