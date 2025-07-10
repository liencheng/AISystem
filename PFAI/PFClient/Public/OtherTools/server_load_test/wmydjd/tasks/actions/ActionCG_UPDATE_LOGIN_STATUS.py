# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UPDATE_LOGIN_STATUS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UPDATE_LOGIN_STATUS(self.person)
        # params begin ( don't move this line )

        packet['openkey'] = self.person['openkey']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UPDATE_LOGIN_STATUS")
        return res
