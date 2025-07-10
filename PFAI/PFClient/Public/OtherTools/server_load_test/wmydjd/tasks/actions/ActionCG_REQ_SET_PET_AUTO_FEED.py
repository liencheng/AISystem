# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_SET_PET_AUTO_FEED:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_SET_PET_AUTO_FEED(self.person)
        # params begin ( don't move this line )

        # packet['tagList'] = self.person['tagList']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_SET_PET_AUTO_FEED")
        return res
