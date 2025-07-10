# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_CHALLENGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_CHALLENGE(self.person)
        # params begin ( don't move this line )

        packet['opponentGuid'] = self.person['opponentGuid']
        packet['rankpos'] = self.person['rankpos']
        packet['chanllengeName'] = self.person['chanllengeName']
        packet['isQuickChanllenge'] = self.person['isQuickChanllenge']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_CHALLENGE")
        return res
