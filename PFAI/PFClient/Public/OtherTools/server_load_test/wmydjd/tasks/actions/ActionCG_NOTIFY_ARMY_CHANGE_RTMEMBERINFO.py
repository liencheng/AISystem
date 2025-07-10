# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_NOTIFY_ARMY_CHANGE_RTMEMBERINFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_NOTIFY_ARMY_CHANGE_RTMEMBERINFO(self.person)
        # params begin ( don't move this line )

        packet['rtMemberInfo'] = self.person['rtMemberInfo']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_NOTIFY_ARMY_CHANGE_RTMEMBERINFO")
        return res
