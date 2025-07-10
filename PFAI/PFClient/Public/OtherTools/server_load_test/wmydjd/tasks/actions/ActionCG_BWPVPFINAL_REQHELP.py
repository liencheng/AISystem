# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BWPVPFINAL_REQHELP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BWPVPFINAL_REQHELP(self.person)
        # params begin ( don't move this line )

        packet['isReqGuild'] = self.person['isReqGuild']
        packet['isReqWorld'] = self.person['isReqWorld']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BWPVPFINAL_REQHELP")
        return res
