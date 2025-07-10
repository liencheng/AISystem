# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UNLOCK_HOME_PLAN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UNLOCK_HOME_PLAN(self.person)
        # params begin ( don't move this line )

        packet['PlanIndex'] = self.person['PlanIndex']
        packet['HomeGuid'] = self.person['HomeGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UNLOCK_HOME_PLAN")
        return res
