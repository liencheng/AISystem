# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_ASK_GUILDPROCLAIMWAR_DETAILDATA:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_ASK_GUILDPROCLAIMWAR_DETAILDATA(self.person)
        # params begin ( don't move this line )
        packet['reqtype'] = self.person['reqtype']
        packet['startnumtime'] = self.person['startnumtime']
        packet['srcguildguid'] = self.person['srcguildguid']
        packet['targuildguid'] = self.person['targuildguid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet_with_heartbeat(self.person, "CG_ASK_GUILDPROCLAIMWAR_DETAILDATA")
        return res
