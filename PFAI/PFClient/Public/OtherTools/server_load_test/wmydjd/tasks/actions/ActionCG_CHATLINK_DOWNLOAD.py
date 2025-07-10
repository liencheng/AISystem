# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CHATLINK_DOWNLOAD:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CHATLINK_DOWNLOAD(self.person)
        # params begin ( don't move this line )

        packet['LinkType'] = self.person['LinkType']
        packet['DownloadIndex'] = self.person['DownloadIndex']
        packet['Channel'] = self.person['Channel']
        # packet['RealIdx'] = self.person['RealIdx']
        packet['SenderGuid'] = self.person['SenderGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CHATLINK_DOWNLOAD")
        return res
