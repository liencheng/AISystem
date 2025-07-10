# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HELP_TIANYIN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HELP_TIANYIN(self.person)
        # params begin ( don't move this line )

        packet['sceneclassid'] = self.person['sceneclassid']
        packet['sceneinstid'] = self.person['sceneinstid']
        packet['posX'] = self.person['posX']
        packet['posY'] = self.person['posY']
        packet['posZ'] = self.person['posZ']
        packet['diePlayerGuid'] = self.person['diePlayerGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HELP_TIANYIN")
        return res
