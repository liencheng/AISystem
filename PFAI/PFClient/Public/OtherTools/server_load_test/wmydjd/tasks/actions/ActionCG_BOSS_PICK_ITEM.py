# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BOSS_PICK_ITEM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BOSS_PICK_ITEM(self.person)
        # params begin ( don't move this line )

        packet['serverid'] = self.person['serverid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BOSS_PICK_ITEM")
        return res
