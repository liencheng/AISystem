# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_STALL_SEARCH:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_STALL_SEARCH(self.person)
        # params begin ( don't move this line )

        packet['ispublic'] = self.person['ispublic']
        packet['curpage'] = self.person['curpage']
        packet['keystring'] = self.person['keystring']
        packet['order'] = self.person['order']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_STALL_SEARCH")
        return res
