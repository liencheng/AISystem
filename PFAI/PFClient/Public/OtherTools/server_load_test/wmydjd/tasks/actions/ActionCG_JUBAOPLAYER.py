# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_JUBAOPLAYER:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_JUBAOPLAYER(self.person)
        # params begin ( don't move this line )

        packet['guid'] = self.person['guid']
        packet['jubaoid'] = self.person['jubaoid']
        packet['info'] = self.person['info']
        packet['jubaotype'] = self.person['jubaotype']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_JUBAOPLAYER")
        return res
