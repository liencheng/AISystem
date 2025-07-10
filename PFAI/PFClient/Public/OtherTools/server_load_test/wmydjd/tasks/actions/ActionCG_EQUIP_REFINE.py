# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_EQUIP_REFINE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_EQUIP_REFINE(self.person)
        # params begin ( don't move this line )

        packet['packtype'] = self.person['packtype']
        packet['equipguid'] = self.person['equipguid']
        packet['refinetool'] = self.person['refinetool']
        # packet['blessingtool'] = self.person['blessingtool']
        # packet['forother'] = self.person['forother']
        # packet['blesstooltype'] = self.person['blesstooltype']
        # packet['npcserverid'] = self.person['npcserverid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_EQUIP_REFINE")
        return res
