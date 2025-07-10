# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TXMQ_OP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TXMQ_OP(self.person)
        # params begin ( don't move this line )

        packet['op'] = self.person['op']
        packet['MQId'] = self.person['MQId']
        # packet['MWId'] = self.person['MWId']
        # packet['tmpMWId'] = self.person['tmpMWId']
        # packet['autoRecast'] = self.person['autoRecast']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TXMQ_OP")
        return res
