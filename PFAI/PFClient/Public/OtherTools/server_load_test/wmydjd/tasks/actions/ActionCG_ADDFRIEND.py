# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ADDFRIEND:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ADDFRIEND(self.person)
        # params begin ( don't move this line )

        packet['guid'] = self.person['add_friend_guid']
        packet['realAddFrienType'] = self.person['realAddFrienType']
        # packet['checkSignCode'] = self.person['checkSignCode']
        # packet['addfriendmsg'] = self.person['addfriendmsg']
        # packet['checkcreditscore'] = self.person['checkcreditscore']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ADDFRIEND")
        return res
