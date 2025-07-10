# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SAVE_HOME_BUILDING:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SAVE_HOME_BUILDING(self.person)
        # params begin ( don't move this line )

        packet['HomeGuid'] = self.person['HomeGuid']
        packet['MasterGuid'] = self.person['MasterGuid']
        # packet['BuildingList'] = self.person['BuildingList']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SAVE_HOME_BUILDING")
        return res
