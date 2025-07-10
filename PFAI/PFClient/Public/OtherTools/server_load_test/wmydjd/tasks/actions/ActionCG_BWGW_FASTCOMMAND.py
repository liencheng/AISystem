# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BWGW_FASTCOMMAND:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BWGW_FASTCOMMAND(self.person)
        # params begin ( don't move this line )

        packet['dicId'] = self.person['dicId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BWGW_FASTCOMMAND")
        return res
