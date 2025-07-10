# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_QIXISTAR_SAVE_MUSIC:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_QIXISTAR_SAVE_MUSIC(self.person)
        # params begin ( don't move this line )

        packet['op'] = self.person['op']
        # packet['star'] = self.person['star']
        # packet['speed'] = self.person['speed']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_QIXISTAR_SAVE_MUSIC")
        return res
