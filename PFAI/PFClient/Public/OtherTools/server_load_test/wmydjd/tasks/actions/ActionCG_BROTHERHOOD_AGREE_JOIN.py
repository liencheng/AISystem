# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BROTHERHOOD_AGREE_JOIN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BROTHERHOOD_AGREE_JOIN(self.person)
        # params begin ( don't move this line )

        packet['inviterGuid'] = self.person['inviterGuid']
        packet['isAgree'] = self.person['isAgree']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BROTHERHOOD_AGREE_JOIN")
        return res
