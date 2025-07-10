# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_LINGSHI_BOARD_CHANGEPOS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_LINGSHI_BOARD_CHANGEPOS(self.person)
        # params begin ( don't move this line )

        packet['boardId'] = self.person['boardId']
        packet['oldInstallInfo'] = self.person['oldInstallInfo']
        packet['newInstallInfo'] = self.person['newInstallInfo']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_LINGSHI_BOARD_CHANGEPOS")
        return res
