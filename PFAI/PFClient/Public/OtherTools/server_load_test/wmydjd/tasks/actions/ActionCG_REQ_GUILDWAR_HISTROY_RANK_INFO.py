# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_GUILDWAR_HISTROY_RANK_INFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_GUILDWAR_HISTROY_RANK_INFO(self.person)
        # params begin ( don't move this line )

        packet['clientVersion'] = self.person['clientVersion']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_GUILDWAR_HISTROY_RANK_INFO")
        return res
