# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ADDBLACKLIST:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ADDBLACKLIST(self.person)
        # params begin ( don't move this line )

        packet['guid'] = self.person['guid']
        packet['Name'] = self.person['Name']
        packet['Level'] = self.person['Level']
        packet['Prof'] = self.person['Prof']
        packet['Combat'] = self.person['Combat']
        packet['State'] = self.person['State']
        packet['TimeInfo'] = self.person['TimeInfo']
        packet['PlayerSex'] = self.person['PlayerSex']
        packet['LittleHeadPicName'] = self.person['LittleHeadPicName']
        # packet['Reserved'] = self.person['Reserved']
        packet['ReportFlag'] = self.person['ReportFlag']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_ADDBLACKLIST")
        return res
