# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_WEDDING_CREATE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_WEDDING_CREATE(self.person)
        # params begin ( don't move this line )

        packet['type'] = self.person['type']
        packet['targetguid'] = self.person['targetguid']
        # packet['WeddingCustomId'] = self.person['WeddingCustomId']
        # packet['WeddingCustomOptional'] = self.person['WeddingCustomOptional']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_WEDDING_CREATE")
        return res
