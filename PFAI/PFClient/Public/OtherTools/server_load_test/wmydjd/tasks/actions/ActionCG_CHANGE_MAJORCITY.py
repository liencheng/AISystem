# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CHANGE_MAJORCITY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CHANGE_MAJORCITY(self.person)
        # params begin ( don't move this line )

        packet['type'] = self.person['type']
        # packet['pos_x'] = self.person['pos_x']
        # packet['pos_y'] = self.person['pos_y']
        # packet['pos_z'] = self.person['pos_z']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CHANGE_MAJORCITY")
        return res
