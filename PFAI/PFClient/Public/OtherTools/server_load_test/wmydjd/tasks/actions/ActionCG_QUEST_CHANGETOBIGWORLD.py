# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_QUEST_CHANGETOBIGWORLD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_QUEST_CHANGETOBIGWORLD(self.person)
        # params begin ( don't move this line )

        packet['questtype'] = self.person['questtype']
        packet['sceneclassid'] = self.person['sceneclassid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_QUEST_CHANGETOBIGWORLD")
        return res
