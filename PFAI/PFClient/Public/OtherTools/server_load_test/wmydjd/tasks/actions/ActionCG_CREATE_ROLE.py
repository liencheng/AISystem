# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_CREATE_ROLE:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_CREATE_ROLE(self.person)
        # params begin ( don't move this line )
        role_count = len(self.person['roleguidlist'])
        packet['name'] = Functions.get_role_name_with_account(self.person['account'], role_count)
        packet['sex'] = Functions.gen_sex()
        packet['profession'] = self.person["profession"] if self.person["profession"] else Functions.gen_profession()
        packet['defaulthairvisual'] = Functions.gen_default_visual()
        packet['defaultfacevisual'] = Functions.gen_default_visual()
        packet['defaultbodyvisual'] = Functions.gen_default_body_visual()

        packet['NieRenValue'].extend(Functions.gen_nieren_info())
        packet['isuserprecreate'] = False
        packet['relatfriendnum'] = 0
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if not res[0]:
            return res
        res = Functions.wait_packet_with_heartbeat(self.person, "GC_CREATE_ROLE_RET", 60)
        return res
