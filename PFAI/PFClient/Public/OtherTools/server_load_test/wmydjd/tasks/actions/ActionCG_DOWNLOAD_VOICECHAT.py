# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_DOWNLOAD_VOICECHAT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_DOWNLOAD_VOICECHAT(self.person)
        # params begin ( don't move this line )

        packet['VoiceIndex'] = self.person['VoiceIndex']
        packet['Channel'] = self.person['Channel']
        packet['SenderGuid'] = self.person['SenderGuid']
        packet['PlayVoice'] = self.person['PlayVoice']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_DOWNLOAD_VOICECHAT")
        return res
