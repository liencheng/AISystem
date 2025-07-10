# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HOLIDAY_REDPOINT_REQ:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HOLIDAY_REDPOINT_REQ(self.person)
        # params begin ( don't move this line )

        packet['HolidaySmallType'] = self.person['HolidaySmallType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HOLIDAY_REDPOINT_REQ")
        return res
