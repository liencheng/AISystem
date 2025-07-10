# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF(self.person)
        # params begin ( don't move this line )

        packet['chiefGuid'] = self.person['chiefGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF")
        return res
