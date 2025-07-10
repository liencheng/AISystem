# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SELECT_ROLE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SELECT_ROLE(self.person)
        # params begin ( don't move this line )
        packet['roleguid'] = self.person['guid']
        print(f"ActionCG_SELECT_ROLE {packet['roleguid']}")
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        res = Functions.wait_for_packet(self.person, "GC_SELECT_ROLE_RET")
        if res[0] == True:
            if self.person['selectresult'] != 0:
                res[0] = False
                res[2] = "Select Role Failed"
        return res
