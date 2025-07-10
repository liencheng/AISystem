# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_FAIRY_RAISE_ACTION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_FAIRY_RAISE_ACTION(self.person)
        # params begin ( don't move this line )

        packet['fairyGuid'] = self.person['fairyGuid']
        packet['actionType'] = self.person['actionType']
        packet['actionRepeatCount'] = self.person['actionRepeatCount']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_FAIRY_RAISE_ACTION")
        return res
