# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ITEM_SUBSCRIBE_OPERATION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ITEM_SUBSCRIBE_OPERATION(self.person)
        # params begin ( don't move this line )

        packet['operationType'] = self.person['operationType']
        packet['shopType'] = self.person['shopType']
        packet['shopId'] = self.person['shopId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ITEM_SUBSCRIBE_OPERATION")
        return res
