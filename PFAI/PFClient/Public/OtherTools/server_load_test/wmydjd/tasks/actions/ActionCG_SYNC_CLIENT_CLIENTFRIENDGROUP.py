# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SYNC_CLIENT_CLIENTFRIENDGROUP:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SYNC_CLIENT_CLIENTFRIENDGROUP(self.person)
        # params begin ( don't move this line )
        # packet['groupname'] = self.person['groupname']
        # packet['defaultgroupguid'] = self.person['defaultgroupguid']
        # packet['fristgroupguid'] = self.person['fristgroupguid']
        # packet['secondgroupguid'] = self.person['secondgroupguid']
        # packet['thirdgroupguid'] = self.person['thirdgroupguid']
        packet['iscover'] = self.person['iscover']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_SYNC_CLIENT_CLIENTFRIENDGROUP")
        return res
