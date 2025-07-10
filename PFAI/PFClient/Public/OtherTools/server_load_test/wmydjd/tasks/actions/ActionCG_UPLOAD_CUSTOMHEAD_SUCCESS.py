# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_UPLOAD_CUSTOMHEAD_SUCCESS:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_UPLOAD_CUSTOMHEAD_SUCCESS(self.person)
        # params begin ( don't move this line )

        packet['filePath'] = self.person['filePath']
        packet['uploadresult'] = self.person['uploadresult']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_UPLOAD_CUSTOMHEAD_SUCCESS")
        return res
