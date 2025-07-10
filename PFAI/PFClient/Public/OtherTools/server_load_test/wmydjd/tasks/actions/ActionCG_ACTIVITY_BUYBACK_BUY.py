# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ACTIVITY_BUYBACK_BUY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ACTIVITY_BUYBACK_BUY(self.person)
        # params begin ( don't move this line )

        packet['activityID'] = self.person['activityID']
        packet['isAll'] = self.person['isAll']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ACTIVITY_BUYBACK_BUY")
        return res
