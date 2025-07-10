# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_MOUNT_MOUNT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_MOUNT_MOUNT(self.person)
        # params begin ( don't move this line )

        packet['MountID'] = self.person['MountID']
        # packet['MountEffect'] = self.person['MountEffect']
        # packet['MountMCount'] = self.person['MountMCount']
        # packet['MountHColor'] = self.person['MountHColor']
        # packet['MountBColor'] = self.person['MountBColor']
        # packet['MountFColor'] = self.person['MountFColor']
        # packet['MountData'] = self.person['MountData']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_MOUNT_MOUNT")
        return res
