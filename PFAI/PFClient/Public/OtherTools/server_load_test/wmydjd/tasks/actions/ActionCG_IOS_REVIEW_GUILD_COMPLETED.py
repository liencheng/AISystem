# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_IOS_REVIEW_GUILD_COMPLETED:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_IOS_REVIEW_GUILD_COMPLETED(self.person)
        # params begin ( don't move this line )

        packet['nCurClientVersion'] = self.person['nCurClientVersion']
        packet['nEventId'] = self.person['nEventId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_IOS_REVIEW_GUILD_COMPLETED")
        return res
