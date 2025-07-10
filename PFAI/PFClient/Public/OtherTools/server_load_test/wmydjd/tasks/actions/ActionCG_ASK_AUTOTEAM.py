# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_AUTOTEAM:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_AUTOTEAM(self.person)
        # params begin ( don't move this line )

        packet['targetID'] = self.person['targetID']
        # packet['sceneClassID'] = self.person['sceneClassID']
        # packet['difficulty'] = self.person['difficulty']
        # packet['minLevel'] = self.person['minLevel']
        # packet['maxLevel'] = self.person['maxLevel']
        # packet['isUsingDefaultProfessionOrientation'] = self.person['isUsingDefaultProfessionOrientation']
        # packet['professionOrientationParentID'] = self.person['professionOrientationParentID']
        # packet['professionOrientationChildID'] = self.person['professionOrientationChildID']
        packet['bAutoArmy'] = self.person['bAutoArmy']
        packet['bAutoSet'] = self.person['bAutoSet']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_AUTOTEAM")
        return res
