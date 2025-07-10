# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_SiQingRedPacket_TLOG:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_SiQingRedPacket_TLOG(self.person)
        # params begin ( don't move this line )

        packet['nActType'] = self.person['nActType']
        packet['nSubType'] = self.person['nSubType']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_SiQingRedPacket_TLOG")
        return res
