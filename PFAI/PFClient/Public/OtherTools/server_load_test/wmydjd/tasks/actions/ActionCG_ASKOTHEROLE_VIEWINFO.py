# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASKOTHEROLE_VIEWINFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASKOTHEROLE_VIEWINFO(self.person)
        # params begin ( don't move this line )

        packet['roleguid'] = self.person['roleguid']
        # packet['optype'] = self.person['optype']
        # packet['intparam1'] = self.person['intparam1']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASKOTHEROLE_VIEWINFO")
        return res
