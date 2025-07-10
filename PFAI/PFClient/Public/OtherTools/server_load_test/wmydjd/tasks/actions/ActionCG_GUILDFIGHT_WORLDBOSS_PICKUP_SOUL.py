# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILDFIGHT_WORLDBOSS_PICKUP_SOUL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILDFIGHT_WORLDBOSS_PICKUP_SOUL(self.person)
        # params begin ( don't move this line )

        packet['ObjId'] = self.person['ObjId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILDFIGHT_WORLDBOSS_PICKUP_SOUL")
        return res
