# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_REQ_DEL_HOME_HORDE_COLLECTION:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_REQ_DEL_HOME_HORDE_COLLECTION(self.person)
        # params begin ( don't move this line )

        packet['homeGuid'] = self.person['homeGuid']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_REQ_DEL_HOME_HORDE_COLLECTION")
        return res
