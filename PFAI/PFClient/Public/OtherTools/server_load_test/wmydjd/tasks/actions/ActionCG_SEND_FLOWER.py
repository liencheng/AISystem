# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SEND_FLOWER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SEND_FLOWER(self.person)
        # params begin ( don't move this line )

        packet['receiverGuid'] = self.person['receiverGuid']
        packet['receiverName'] = self.person['receiverName']
        packet['itemId'] = self.person['itemId']
        packet['itemCount'] = self.person['itemCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SEND_FLOWER")
        return res
