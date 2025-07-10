# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DOMAINPLUNDER_BOARD_INFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DOMAINPLUNDER_BOARD_INFO(self.person)
        # params begin ( don't move this line )
        packet['domainId'] = self.person['domainId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_DOMAINPLUNDER_BOARD_INFO")
        return res
