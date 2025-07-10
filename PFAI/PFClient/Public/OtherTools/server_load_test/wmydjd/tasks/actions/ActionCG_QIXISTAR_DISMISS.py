# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_QIXISTAR_DISMISS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_QIXISTAR_DISMISS(self.person)
        # params begin ( don't move this line )

        packet['targetGuid'] = self.person['targetGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_QIXISTAR_DISMISS")
        return res
