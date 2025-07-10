# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TIANSHU_COMPOSE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TIANSHU_COMPOSE(self.person)
        # params begin ( don't move this line )

        packet['dataId'] = self.person['dataId']
        packet['preferUnbind'] = self.person['preferUnbind']
        # packet['composeCount'] = self.person['composeCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TIANSHU_COMPOSE")
        return res
