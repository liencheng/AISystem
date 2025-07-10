# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CHAT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CHAT(self.person)
        # params begin ( don't move this line )

        packet['Content'] = self.person['Content']
        packet['Channel'] = self.person['Channel']
        # packet['Link'] = self.person['Link']
        # packet['LinkData'] = self.person['LinkData']
        # packet['VoiceFile'] = self.person['VoiceFile']
        # packet['VoiceDuration'] = self.person['VoiceDuration']
        # packet['LinkItemGuid'] = self.person['LinkItemGuid']
        # packet['LinkFairyGuid'] = self.person['LinkFairyGuid']
        # packet['LinkTitleId'] = self.person['LinkTitleId']
        # packet['LinkFashionId'] = self.person['LinkFashionId']
        # packet['ReceiverGuid'] = self.person['ReceiverGuid']
        # packet['ReceiverName'] = self.person['ReceiverName']
        # packet['ChannelParam'] = self.person['ChannelParam']
        # packet['EmotionUnlock'] = self.person['EmotionUnlock']
        # packet['LinkPetId'] = self.person['LinkPetId']
        # packet['LinkGodWeapon'] = self.person['LinkGodWeapon']
        # packet['VoiceLanguage'] = self.person['VoiceLanguage']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            return Functions.wait_for_packet(self.person, "GC_CHAT")
        return res
