# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions
import time

class ActionXX_RESPONSE_HEARTBEAT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.XX_RESPONSE_HEARTBEAT(self.person)
        # params begin ( don't move this line )

        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "XX_RESPONSE_HEARTBEAT")
        if res[0]:
            self.person['heartbeat_time'] = time.time()
        return res
