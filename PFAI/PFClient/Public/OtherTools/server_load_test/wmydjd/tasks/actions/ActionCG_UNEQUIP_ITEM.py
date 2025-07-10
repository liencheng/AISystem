# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UNEQUIP_ITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UNEQUIP_ITEM(self.person)
        # params begin ( don't move this line )

        packet['equipguid'] = self.person['equipguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UNEQUIP_ITEM")
        return res
