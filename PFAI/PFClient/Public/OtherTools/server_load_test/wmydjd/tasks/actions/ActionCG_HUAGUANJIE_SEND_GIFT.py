# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HUAGUANJIE_SEND_GIFT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HUAGUANJIE_SEND_GIFT(self.person)
        # params begin ( don't move this line )

        packet['receiverGuid'] = self.person['receiverGuid']
        packet['receiverName'] = self.person['receiverName']
        packet['giftId'] = self.person['giftId']
        packet['giftCount'] = self.person['giftCount']
        packet['type'] = self.person['type']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HUAGUANJIE_SEND_GIFT")
        return res
