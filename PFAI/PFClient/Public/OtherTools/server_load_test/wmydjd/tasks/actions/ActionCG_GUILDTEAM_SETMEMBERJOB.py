# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_GUILDTEAM_SETMEMBERJOB:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_GUILDTEAM_SETMEMBERJOB(self.person)
        # params begin ( don't move this line )

        packet['playerGuid'] = self.person['playerGuid']
        packet['GuildTeamIndex'] = self.person['GuildTeamIndex']
        packet['ntype'] = self.person['ntype']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_GUILDTEAM_SETMEMBERJOB")
        return res
