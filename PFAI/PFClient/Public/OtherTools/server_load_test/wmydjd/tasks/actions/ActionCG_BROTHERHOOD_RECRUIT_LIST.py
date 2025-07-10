# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BROTHERHOOD_RECRUIT_LIST:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BROTHERHOOD_RECRUIT_LIST(self.person)
        # params begin ( don't move this line )

        packet['pageId'] = self.person['pageId']
        packet['prof'] = self.person['prof']
        packet['memberCount'] = self.person['memberCount']
        # packet['onlyActiveBrotherhood'] = self.person['onlyActiveBrotherhood']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BROTHERHOOD_RECRUIT_LIST")
        return res
