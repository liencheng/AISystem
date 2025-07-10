# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MAIL_OPERATION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MAIL_OPERATION(self.person)
        # params begin ( don't move this line )

        packet['OperationType'] = self.person['OperationType']
        packet['MailGuid'] = self.person['MailGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MAIL_OPERATION")
        return res
