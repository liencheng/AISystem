# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_EQUIP_REBIRTH_RECASE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_EQUIP_REBIRTH_RECASE(self.person)
        # params begin ( don't move this line )

        packet['nSlotType'] = self.person['nSlotType']
        packet['nEquipGuid'] = self.person['nEquipGuid']
        packet['nItemId'] = self.person['nItemId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_EQUIP_REBIRTH_RECASE")
        return res
