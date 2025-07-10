# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MOUNT_UNMOUNT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MOUNT_UNMOUNT(self.person)
        # params begin ( don't move this line )

        packet['MountID'] = self.person['MountID']
        # packet['flag'] = self.person['flag']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MOUNT_UNMOUNT")
        return res
