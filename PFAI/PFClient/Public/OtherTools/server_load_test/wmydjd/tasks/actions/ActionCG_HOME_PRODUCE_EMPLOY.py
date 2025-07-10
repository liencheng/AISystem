# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HOME_PRODUCE_EMPLOY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HOME_PRODUCE_EMPLOY(self.person)
        # params begin ( don't move this line )

        packet['HomeGuid'] = self.person['HomeGuid']
        packet['PlayerGuid'] = self.person['PlayerGuid']
        packet['EmployeeGuid'] = self.person['EmployeeGuid']
        packet['BuildingGuid'] = self.person['BuildingGuid']
        packet['bOperate'] = self.person['bOperate']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HOME_PRODUCE_EMPLOY")
        return res
