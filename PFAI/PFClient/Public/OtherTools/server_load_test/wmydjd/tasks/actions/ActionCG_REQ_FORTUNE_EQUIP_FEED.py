# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_FORTUNE_EQUIP_FEED:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_FORTUNE_EQUIP_FEED(self.person)
        # params begin ( don't move this line )

        packet['targetIndex'] = self.person['targetIndex']
        # packet['materialIndex'] = self.person['materialIndex']
        packet['targetPackIndex'] = self.person['targetPackIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_FORTUNE_EQUIP_FEED")
        return res
