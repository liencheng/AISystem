# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FASHION_CHANGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FASHION_CHANGE(self.person)
        # params begin ( don't move this line )

        packet['FashionId'] = self.person['FashionId']
        # packet['ColorIndex'] = self.person['ColorIndex']
        # packet['ChangeMainColor'] = self.person['ChangeMainColor']
        # packet['ChangeCommColor'] = self.person['ChangeCommColor']
        # packet['OneKeyFashionIds'] = self.person['OneKeyFashionIds']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FASHION_CHANGE")
        return res
