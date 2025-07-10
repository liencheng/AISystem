# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_YINZHEN_LEVELUP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_YINZHEN_LEVELUP(self.person)
        # params begin ( don't move this line )

        packet['yinzhenId'] = self.person['yinzhenId']
        packet['itemId'] = self.person['itemId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_YINZHEN_LEVELUP")
        return res
