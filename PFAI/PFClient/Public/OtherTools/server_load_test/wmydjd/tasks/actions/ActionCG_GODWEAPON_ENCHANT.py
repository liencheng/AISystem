# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GODWEAPON_ENCHANT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GODWEAPON_ENCHANT(self.person)
        # params begin ( don't move this line )

        packet['SourcePackPos'] = self.person['SourcePackPos']
        packet['TargetPackPos'] = self.person['TargetPackPos']
        packet['SourceAttrIndex'] = self.person['SourceAttrIndex']
        packet['TargetAttrIndex'] = self.person['TargetAttrIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GODWEAPON_ENCHANT")
        return res
