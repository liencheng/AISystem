# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_PUBLISH_HOME_LINK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_PUBLISH_HOME_LINK(self.person)
        # params begin ( don't move this line )

        packet['HomeGuid'] = self.person['HomeGuid']
        packet['ChannelId'] = self.person['ChannelId']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_PUBLISH_HOME_LINK")
        return res
