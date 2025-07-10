# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_STATICSYSTEMSHOP_BUYBACK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_STATICSYSTEMSHOP_BUYBACK(self.person)
        # params begin ( don't move this line )

        packet['shopid'] = self.person['shopid']
        packet['itemguid'] = self.person['itemguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_STATICSYSTEMSHOP_BUYBACK")
        return res
