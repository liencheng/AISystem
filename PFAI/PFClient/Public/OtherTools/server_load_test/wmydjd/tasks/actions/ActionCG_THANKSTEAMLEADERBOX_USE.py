# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_THANKSTEAMLEADERBOX_USE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_THANKSTEAMLEADERBOX_USE(self.person)
        # params begin ( don't move this line )

        packet['boxGuid'] = self.person['boxGuid']
        packet['teamLeaderGuid'] = self.person['teamLeaderGuid']
        packet['msgConteng'] = self.person['msgConteng']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_THANKSTEAMLEADERBOX_USE")
        return res
