# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_BROTHERHOOD_RANK_INFO:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_BROTHERHOOD_RANK_INFO(self.person)
        # params begin ( don't move this line )

        packet['brotherhoodGuid'] = self.person['brotherhoodGuid']
        packet['brotherhoodName'] = self.person['brotherhoodName']
        packet['combatVal'] = self.person['combatVal']
        # packet['memberGuid'] = self.person['memberGuid']
        # packet['memberName'] = self.person['memberName']
        # packet['memberProf'] = self.person['memberProf']
        # packet['memberPos'] = self.person['memberPos']
        # packet['memberSex'] = self.person['memberSex']
        # packet['memberTitle'] = self.person['memberTitle']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_BROTHERHOOD_RANK_INFO")
        return res
