# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BROTHERHOOD_INVITE_BIRTHDAY:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BROTHERHOOD_INVITE_BIRTHDAY(self.person)
        # params begin ( don't move this line )

        packet['birthday'] = self.person['birthday']
        packet['agree'] = self.person['agree']
        packet['inviterGuid'] = self.person['inviterGuid']
        packet['inviterName'] = self.person['inviterName']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BROTHERHOOD_INVITE_BIRTHDAY")
        return res
