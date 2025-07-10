# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REPLACE_ENCHANT_RESULT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REPLACE_ENCHANT_RESULT(self.person)
        # params begin ( don't move this line )

        packet['isReplace'] = self.person['isReplace']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REPLACE_ENCHANT_RESULT")
        return res
