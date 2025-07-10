# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REGRESS_NOTICE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REGRESS_NOTICE(self.person)
        # params begin ( don't move this line )

        packet['OperaType'] = self.person['OperaType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REGRESS_NOTICE")
        return res
