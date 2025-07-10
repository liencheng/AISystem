# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILDFIGHT_WORLDBOSS_PURIFY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILDFIGHT_WORLDBOSS_PURIFY(self.person)
        # params begin ( don't move this line )

        packet['PurifyStage'] = self.person['PurifyStage']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILDFIGHT_WORLDBOSS_PURIFY")
        return res
