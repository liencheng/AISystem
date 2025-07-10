# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REBATE_ASKFORBONUS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REBATE_ASKFORBONUS(self.person)
        # params begin ( don't move this line )

        packet['consume'] = self.person['consume']
        packet['everyday'] = self.person['everyday']
        packet['bonus'] = self.person['bonus']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REBATE_ASKFORBONUS")
        return res
