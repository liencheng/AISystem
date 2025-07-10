# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_AID_RESOPNSE_CONFIG:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_AID_RESOPNSE_CONFIG(self.person)
        # params begin ( don't move this line )

        packet['guid'] = self.person['guid']
        packet['misID'] = self.person['misID']
        packet['ret'] = self.person['ret']
        packet['memguid'] = self.person['memguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_AID_RESOPNSE_CONFIG")
        return res
