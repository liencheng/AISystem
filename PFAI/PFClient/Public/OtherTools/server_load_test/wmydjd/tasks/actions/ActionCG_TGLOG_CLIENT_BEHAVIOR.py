# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TGLOG_CLIENT_BEHAVIOR:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TGLOG_CLIENT_BEHAVIOR(self.person)
        # params begin ( don't move this line )

        packet['guideid'] = self.person['guideid']
        packet['name'] = self.person['name']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TGLOG_CLIENT_BEHAVIOR")
        return res
