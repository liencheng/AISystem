# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ITEM_DECOMPOSE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ITEM_DECOMPOSE(self.person)
        # params begin ( don't move this line )

        packet['itemguid'] = self.person['itemguid']
        # packet['itemcount'] = self.person['itemcount']
        # packet['isauto'] = self.person['isauto']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ITEM_DECOMPOSE")
        return res
