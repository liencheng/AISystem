# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DONATE_BUILDING:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DONATE_BUILDING(self.person)
        # params begin ( don't move this line )

        packet['HomeGuid'] = self.person['HomeGuid']
        packet['MasterGuid'] = self.person['MasterGuid']
        # packet['FurnitureIds'] = self.person['FurnitureIds']
        # packet['FurnitureNums'] = self.person['FurnitureNums']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DONATE_BUILDING")
        return res
