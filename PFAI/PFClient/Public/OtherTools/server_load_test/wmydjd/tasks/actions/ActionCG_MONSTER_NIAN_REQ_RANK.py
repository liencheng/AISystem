# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MONSTER_NIAN_REQ_RANK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MONSTER_NIAN_REQ_RANK(self.person)
        # params begin ( don't move this line )

        packet['Page'] = self.person['Page']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MONSTER_NIAN_REQ_RANK")
        return res
