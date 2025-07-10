# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DIG_TREASURE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DIG_TREASURE(self.person)
        # params begin ( don't move this line )

        packet['itemguid'] = self.person['itemguid']
        packet['backtype'] = self.person['backtype']
        packet['posX'] = self.person['posX']
        packet['posY'] = self.person['posY']
        packet['posZ'] = self.person['posZ']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DIG_TREASURE")
        return res
