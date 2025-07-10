# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions
import loadlog


class ActionCG_ENTER_SCENE_OK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ENTER_SCENE_OK(self.person)
        # params begin ( don't move this line )

        packet['isOK'] = self.person['isOK']
        packet['OKCount'] = self.person['OKCount']
        packet['noticetip'] = self.person['noticetip']
        packet['noticecon'] = self.person['noticecon']
        packet['restype'] = self.person['restype']
        packet['ressubtype'] = self.person['ressubtype']
        packet['resData'] = self.person['resData']
        # params end ( don't move this line)
        loadlog.debug(f"account {self.person['account']} : send packet CG_ENTER_SCENE_OK")
        res = Functions.send_packet(packet)
        if res[0]:
            return Functions.wait_for_packet(self.person, "GC_ENTER_SCENE", contiue=True)
        return res
