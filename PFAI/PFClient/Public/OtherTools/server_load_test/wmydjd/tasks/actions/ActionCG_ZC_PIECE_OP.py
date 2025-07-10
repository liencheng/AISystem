# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ZC_PIECE_OP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ZC_PIECE_OP(self.person)
        # params begin ( don't move this line )

        packet['type'] = self.person['type']
        # packet['pieceId'] = self.person['pieceId']
        # packet['targetGuid'] = self.person['targetGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ZC_PIECE_OP")
        return res
