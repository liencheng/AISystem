# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_EQUIP_INHERIT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_EQUIP_INHERIT(self.person)
        # params begin ( don't move this line )

        packet['packtype'] = self.person['packtype']
        packet['mainguid'] = self.person['mainguid']
        packet['stufguid'] = self.person['stufguid']
        packet['lackTransItem'] = self.person['lackTransItem']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_EQUIP_INHERIT")
        return res
