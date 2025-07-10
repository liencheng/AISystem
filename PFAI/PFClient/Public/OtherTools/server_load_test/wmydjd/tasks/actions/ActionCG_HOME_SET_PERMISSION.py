# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_HOME_SET_PERMISSION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_HOME_SET_PERMISSION(self.person)
        # params begin ( don't move this line )

        packet['nPermissionType'] = self.person['nPermissionType']
        packet['bIsPermit'] = self.person['bIsPermit']
        packet['nRelationType'] = self.person['nRelationType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_HOME_SET_PERMISSION")
        return res
