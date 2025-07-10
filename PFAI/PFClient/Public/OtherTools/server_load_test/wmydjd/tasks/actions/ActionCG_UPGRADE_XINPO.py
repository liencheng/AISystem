# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UPGRADE_XINPO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UPGRADE_XINPO(self.person)
        # params begin ( don't move this line )

        packet['pos'] = self.person['pos']
        packet['type'] = self.person['type']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UPGRADE_XINPO")
        return res
