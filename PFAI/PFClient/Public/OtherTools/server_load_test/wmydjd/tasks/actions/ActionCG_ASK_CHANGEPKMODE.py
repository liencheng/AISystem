# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_CHANGEPKMODE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_CHANGEPKMODE(self.person)
        # params begin ( don't move this line )

        packet['isProtectGuild'] = self.person['isProtectGuild']
        packet['isProtectFamily'] = self.person['isProtectFamily']
        packet['isProtectWhite'] = self.person['isProtectWhite']
        packet['isProtectRedAndOrang'] = self.person['isProtectRedAndOrang']
        packet['isProtectSameServer'] = self.person['isProtectSameServer']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_CHANGEPKMODE")
        return res
