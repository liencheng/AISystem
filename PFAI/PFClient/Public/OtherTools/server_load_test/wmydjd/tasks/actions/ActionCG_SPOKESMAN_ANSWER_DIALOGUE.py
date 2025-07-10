# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SPOKESMAN_ANSWER_DIALOGUE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SPOKESMAN_ANSWER_DIALOGUE(self.person)
        # params begin ( don't move this line )

        packet['CurrentDialogueGroup'] = self.person['CurrentDialogueGroup']
        packet['CurrentDialogueId'] = self.person['CurrentDialogueId']
        packet['DialogueAnswerIndex'] = self.person['DialogueAnswerIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SPOKESMAN_ANSWER_DIALOGUE")
        return res
