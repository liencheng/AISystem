# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_COMMONACTIVITYINFO_USEITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_COMMONACTIVITYINFO_USEITEM(self.person)
        # params begin ( don't move this line )

        packet['itemid'] = self.person['itemid']
        packet['itemcount'] = self.person['itemcount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_COMMONACTIVITYINFO_USEITEM")
        return res
