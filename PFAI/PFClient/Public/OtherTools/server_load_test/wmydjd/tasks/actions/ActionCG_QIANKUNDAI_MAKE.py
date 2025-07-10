# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_QIANKUNDAI_MAKE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_QIANKUNDAI_MAKE(self.person)
        # params begin ( don't move this line )

        # packet['StuffGuid'] = self.person['StuffGuid']
        # packet['StuffCount'] = self.person['StuffCount']
        # packet['MakeCount'] = self.person['MakeCount']
        # packet['StuffDataId'] = self.person['StuffDataId']
        # packet['IsInMaterialBag'] = self.person['IsInMaterialBag']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_QIANKUNDAI_MAKE")
        return res
