# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REPLY_MMOUNT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REPLY_MMOUNT(self.person)
        # params begin ( don't move this line )
        packet['sourceServerID'] = self.person['sourceServerID']
        packet['inviteType'] = self.person['inviteType']
        packet['isAgree'] = self.person['isAgree']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_REPLY_MMOUNT")
        return res
