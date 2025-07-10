# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HPFOODLIST_CHANGED:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HPFOODLIST_CHANGED(self.person)
        # params begin ( don't move this line )

        # packet['HPFoodlist'] = self.person['HPFoodlist']
        packet['HPAutoValue'] = self.person['HPAutoValue']
        # packet['MPFoodlist'] = self.person['MPFoodlist']
        packet['MPAutoValue'] = self.person['MPAutoValue']
        packet['HPAutoSwitch'] = self.person['HPAutoSwitch']
        packet['MPAutoSwitch'] = self.person['MPAutoSwitch']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HPFOODLIST_CHANGED")
        return res
