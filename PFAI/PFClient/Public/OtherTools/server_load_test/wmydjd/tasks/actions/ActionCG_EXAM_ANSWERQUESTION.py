# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_EXAM_ANSWERQUESTION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_EXAM_ANSWERQUESTION(self.person)
        # params begin ( don't move this line )

        # packet['answer'] = self.person['answer']
        packet['questionIndex'] = self.person['questionIndex']
        packet['examType'] = self.person['examType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_EXAM_ANSWERQUESTION")
        return res
