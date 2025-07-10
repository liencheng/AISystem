# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MOVE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MOVE(self.person)
        # params begin ( don't move this line )

        packet['posx'] = self.person['posx']
        packet['posy'] = self.person['posy']
        packet['posz'] = self.person['posz']
        packet['ismoving'] = self.person['ismoving']
        # packet['exState'] = self.person['exState']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MOVE")
        return res
