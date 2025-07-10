# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_PAYACT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_PAYACT(self.person)
        # params begin ( don't move this line )

        packet['prizeType'] = self.person['prizeType']
        packet['prizeParam1'] = self.person['prizeParam1']
        packet['prizeParam2'] = self.person['prizeParam2']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_PAYACT")
        return res
