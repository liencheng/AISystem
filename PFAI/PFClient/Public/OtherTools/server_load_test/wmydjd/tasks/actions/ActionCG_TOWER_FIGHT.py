# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TOWER_FIGHT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TOWER_FIGHT(self.person)
        # params begin ( don't move this line )

        packet['CurFloor'] = self.person['CurFloor']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TOWER_FIGHT")
        return res
