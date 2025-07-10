# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ADD_FAIRY_ATTR_POINTS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ADD_FAIRY_ATTR_POINTS(self.person)
        # params begin ( don't move this line )

        packet['fairyguid'] = self.person['fairyguid']
        packet['nAddStrength'] = self.person['nAddStrength']
        packet['nAddAgility'] = self.person['nAddAgility']
        packet['nAddVitality'] = self.person['nAddVitality']
        packet['nAddSpiritual'] = self.person['nAddSpiritual']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ADD_FAIRY_ATTR_POINTS")
        return res
