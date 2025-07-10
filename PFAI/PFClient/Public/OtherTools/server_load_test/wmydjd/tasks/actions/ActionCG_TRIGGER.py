# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_TRIGGER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_TRIGGER(self.person)
        # params begin ( don't move this line )

        packet['trigger_type'] = self.person['trigger_type']
        packet['trigger_id'] = self.person['trigger_id']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_TRIGGER")
        return res
