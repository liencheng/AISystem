# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DRAW_SHARE_GAME_GIFT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DRAW_SHARE_GAME_GIFT(self.person)
        # params begin ( don't move this line )

        packet['nShareType'] = self.person['nShareType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DRAW_SHARE_GAME_GIFT")
        return res
