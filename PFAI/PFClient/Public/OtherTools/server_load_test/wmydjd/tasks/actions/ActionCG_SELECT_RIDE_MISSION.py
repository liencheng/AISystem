# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SELECT_RIDE_MISSION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SELECT_RIDE_MISSION(self.person)
        # params begin ( don't move this line )

        # packet['selectType'] = self.person['selectType']
        # packet['RideIndex'] = self.person['RideIndex']
        # packet['colorIndex'] = self.person['colorIndex']
        # packet['qteCorrectNum'] = self.person['qteCorrectNum']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SELECT_RIDE_MISSION")
        return res
