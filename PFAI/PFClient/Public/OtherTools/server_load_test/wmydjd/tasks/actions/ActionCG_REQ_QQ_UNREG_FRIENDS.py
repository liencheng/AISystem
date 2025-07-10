# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_QQ_UNREG_FRIENDS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_QQ_UNREG_FRIENDS(self.person)
        # params begin ( don't move this line )

        packet['friendsCount'] = self.person['friendsCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_QQ_UNREG_FRIENDS")
        return res
