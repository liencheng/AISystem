# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQUIRE_PLAT_FORM_MESSAGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQUIRE_PLAT_FORM_MESSAGE(self.person)
        # params begin ( don't move this line )

        packet['bRefresh'] = self.person['bRefresh']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQUIRE_PLAT_FORM_MESSAGE")
        return res
