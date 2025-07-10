# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BOUNTY_PICK_ITEM_NPC:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BOUNTY_PICK_ITEM_NPC(self.person)
        # params begin ( don't move this line )

        packet['npcID'] = self.person['npcID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BOUNTY_PICK_ITEM_NPC")
        return res
