# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FLY_AIRCRAFT_MARK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FLY_AIRCRAFT_MARK(self.person)
        # params begin ( don't move this line )

        packet['AircraftID'] = self.person['AircraftID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FLY_AIRCRAFT_MARK")
        return res
