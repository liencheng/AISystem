# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_AUTOTEAM_BW:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_AUTOTEAM_BW(self.person)
        # params begin ( don't move this line )

        packet['scene'] = self.person['scene']
        packet['grade'] = self.person['grade']
        # packet['minLevel'] = self.person['minLevel']
        # packet['maxLevel'] = self.person['maxLevel']
        # packet['qyLv'] = self.person['qyLv']
        # packet['hhfLv'] = self.person['hhfLv']
        # packet['gwLv'] = self.person['gwLv']
        # packet['tyLv'] = self.person['tyLv']
        packet['target'] = self.person['target']
        # packet['paramarray'] = self.person['paramarray']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ASK_AUTOTEAM_BW")
        return res
