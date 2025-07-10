# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TAKE_ITEM_STORAGEPACK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TAKE_ITEM_STORAGEPACK(self.person)
        # params begin ( don't move this line )

        packet['guid'] = self.person['guid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TAKE_ITEM_STORAGEPACK")
        return res
