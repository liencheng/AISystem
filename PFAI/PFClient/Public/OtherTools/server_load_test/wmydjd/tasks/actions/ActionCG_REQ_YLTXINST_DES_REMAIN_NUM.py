# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_YLTXINST_DES_REMAIN_NUM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_YLTXINST_DES_REMAIN_NUM(self.person)
        # params begin ( don't move this line )

        packet['isEnterScene'] = self.person['isEnterScene']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_YLTXINST_DES_REMAIN_NUM")
        return res
