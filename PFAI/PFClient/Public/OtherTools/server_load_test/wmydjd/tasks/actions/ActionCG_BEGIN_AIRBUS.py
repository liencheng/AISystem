# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BEGIN_AIRBUS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BEGIN_AIRBUS(self.person)
        # params begin ( don't move this line )

        packet['nAirLineID'] = self.person['nAirLineID']
        packet['posX'] = self.person['posX']
        packet['posY'] = self.person['posY']
        packet['posZ'] = self.person['posZ']
        packet['nextAirPathIdx'] = self.person['nextAirPathIdx']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BEGIN_AIRBUS")
        return res
