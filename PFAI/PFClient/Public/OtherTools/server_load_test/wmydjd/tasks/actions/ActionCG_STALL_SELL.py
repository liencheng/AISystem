# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_STALL_SELL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_STALL_SELL(self.person)
        # params begin ( don't move this line )

        packet['sellguid'] = self.person['sellguid']
        packet['selltype'] = self.person['selltype']
        packet['sellprice'] = self.person['sellprice']
        packet['sellcount'] = self.person['sellcount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_STALL_SELL")
        return res
