# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_QINYOU_FRIEND:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_QINYOU_FRIEND(self.person)
        # params begin ( don't move this line )

        # packet['account'] = self.person['account']
        # packet['nickname'] = self.person['nickname']
        # packet['iconurl'] = self.person['iconurl']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_QINYOU_FRIEND")
        return res
