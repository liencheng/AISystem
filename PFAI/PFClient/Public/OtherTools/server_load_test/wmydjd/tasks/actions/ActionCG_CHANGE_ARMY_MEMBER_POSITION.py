# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CHANGE_ARMY_MEMBER_POSITION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CHANGE_ARMY_MEMBER_POSITION(self.person)
        # params begin ( don't move this line )

        packet['memberGuid'] = self.person['memberGuid']
        packet['teamindex'] = self.person['teamindex']
        packet['teammemberindex'] = self.person['teammemberindex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CHANGE_ARMY_MEMBER_POSITION")
        return res
