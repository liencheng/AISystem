# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TIANSHUBOARD_SETUP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TIANSHUBOARD_SETUP(self.person)
        # params begin ( don't move this line )

        packet['slot'] = self.person['slot']
        packet['dataId'] = self.person['dataId']
        packet['bind'] = self.person['bind']
        packet['action'] = self.person['action']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TIANSHUBOARD_SETUP")
        return res
