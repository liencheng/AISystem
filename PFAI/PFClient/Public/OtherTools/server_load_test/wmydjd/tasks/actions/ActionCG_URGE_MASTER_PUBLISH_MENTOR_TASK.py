# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_URGE_MASTER_PUBLISH_MENTOR_TASK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_URGE_MASTER_PUBLISH_MENTOR_TASK(self.person)
        # params begin ( don't move this line )

        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_URGE_MASTER_PUBLISH_MENTOR_TASK")
        return res
