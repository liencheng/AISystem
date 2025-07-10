# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_OPERATE_GEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_OPERATE_GEM(self.person)
        # params begin ( don't move this line )

        packet['operateType'] = self.person['operateType']
        packet['tabSlotId'] = self.person['tabSlotId']
        # packet['gemGuid'] = self.person['gemGuid']
        # packet['gemDataId'] = self.person['gemDataId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_OPERATE_GEM")
        return res
