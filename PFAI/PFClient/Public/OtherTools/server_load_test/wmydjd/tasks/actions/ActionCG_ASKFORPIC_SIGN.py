# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASKFORPIC_SIGN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASKFORPIC_SIGN(self.person)
        # params begin ( don't move this line )

        packet['filePath'] = self.person['filePath']
        packet['reqSignType'] = self.person['reqSignType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASKFORPIC_SIGN")
        return res
