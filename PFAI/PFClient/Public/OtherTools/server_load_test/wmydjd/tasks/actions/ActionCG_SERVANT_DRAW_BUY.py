# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SERVANT_DRAW_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SERVANT_DRAW_BUY(self.person)
        # params begin ( don't move this line )

        packet['buyItem'] = self.person['buyItem']
        packet['buyCnt'] = self.person['buyCnt']
        packet['type'] = self.person['type']
        packet['op'] = self.person['op']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SERVANT_DRAW_BUY")
        return res
