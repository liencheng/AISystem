# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_BINGXUEJIE_FIREWORK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_BINGXUEJIE_FIREWORK(self.person)
        # params begin ( don't move this line )
        packet['id'] = self.person['id']
        packet['type'] = self.person['type']
        packet['picId'] = self.person['picId']
        # packet['text'] = self.person['text']
        # packet['hornStyle'] = self.person['hornStyle']
        packet['posX'] = self.person['posX']
        packet['posY'] = self.person['posY']
        packet['posZ'] = self.person['posZ']
        packet['faceDir'] = self.person['faceDir']
        packet['picRandIndex'] = self.person['picRandIndex']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_REQ_BINGXUEJIE_FIREWORK")
        return res
