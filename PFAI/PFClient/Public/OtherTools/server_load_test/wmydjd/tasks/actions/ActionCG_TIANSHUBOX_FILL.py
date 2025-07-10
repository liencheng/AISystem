# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TIANSHUBOX_FILL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TIANSHUBOX_FILL(self.person)
        # params begin ( don't move this line )

        packet['boxID'] = self.person['boxID']
        packet['slotIndex'] = self.person['slotIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TIANSHUBOX_FILL")
        return res
