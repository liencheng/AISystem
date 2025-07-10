# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_HOME_SETTLE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_HOME_SETTLE(self.person)
        # params begin ( don't move this line )

        packet['RegionIndex'] = self.person['RegionIndex']
        packet['HordeIndex'] = self.person['HordeIndex']
        packet['HomeIndex'] = self.person['HomeIndex']
        packet['Cost'] = self.person['Cost']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_HOME_SETTLE")
        return res
