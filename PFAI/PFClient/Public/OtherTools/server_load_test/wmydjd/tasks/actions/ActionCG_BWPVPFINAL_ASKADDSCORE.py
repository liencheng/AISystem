# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BWPVPFINAL_ASKADDSCORE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BWPVPFINAL_ASKADDSCORE(self.person)
        # params begin ( don't move this line )

        packet['HelpMemGuid'] = self.person['HelpMemGuid']
        packet['HelpType'] = self.person['HelpType']
        # packet['isAdd10Times'] = self.person['isAdd10Times']
        packet['HelpName'] = self.person['HelpName']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BWPVPFINAL_ASKADDSCORE")
        return res
