# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_NEW_PLAYER_BEHAVIOR_UI:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_NEW_PLAYER_BEHAVIOR_UI(self.person)
        # params begin ( don't move this line )

        packet['UIName'] = self.person['UIName']
        packet['TabName'] = self.person['TabName']
        packet['Guidindex'] = self.person['Guidindex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_NEW_PLAYER_BEHAVIOR_UI")
        return res
