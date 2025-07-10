# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GODWEAPON_QILING_LVUP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GODWEAPON_QILING_LVUP(self.person)
        # params begin ( don't move this line )

        packet['BaseId'] = self.person['BaseId']
        packet['Index'] = self.person['Index']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GODWEAPON_QILING_LVUP")
        return res
