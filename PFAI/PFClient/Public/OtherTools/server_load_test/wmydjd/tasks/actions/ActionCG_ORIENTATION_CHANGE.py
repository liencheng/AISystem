# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ORIENTATION_CHANGE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ORIENTATION_CHANGE(self.person)
        # params begin ( don't move this line )

        packet['professionOrientationIndex'] = self.person['professionOrientationIndex']
        packet['professionOrientationParentID'] = self.person['professionOrientationParentID']
        packet['professionOrientationChildID'] = self.person['professionOrientationChildID']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ORIENTATION_CHANGE")
        return res
