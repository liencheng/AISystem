# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_EQUIP_EQUIP_REBIRTH:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_EQUIP_EQUIP_REBIRTH(self.person)
        # params begin ( don't move this line )

        packet['nSlotType'] = self.person['nSlotType']
        packet['nToolType'] = self.person['nToolType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_EQUIP_EQUIP_REBIRTH")
        return res
