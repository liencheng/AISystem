# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CHAT_PERSONAL:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CHAT_PERSONAL(self.person)
        # params begin ( don't move this line )

        packet['Content'] = self.person['Content']
        # packet['Link'] = self.person['Link']
        # packet['LinkData'] = self.person['LinkData']
        packet['ReciverGuid'] = self.person['ReciverGuid']
        # packet['VoiceFile'] = self.person['VoiceFile']
        # packet['VoiceDuration'] = self.person['VoiceDuration']
        # packet['LinkItemGuid'] = self.person['LinkItemGuid']
        # packet['LinkFairyGuid'] = self.person['LinkFairyGuid']
        # packet['LinkTitleId'] = self.person['LinkTitleId']
        # packet['LinkFashionId'] = self.person['LinkFashionId']
        # packet['LinkPetId'] = self.person['LinkPetId']
        # packet['VoiceLanguage'] = self.person['VoiceLanguage']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_CHAT_PERSONAL")
        return res
