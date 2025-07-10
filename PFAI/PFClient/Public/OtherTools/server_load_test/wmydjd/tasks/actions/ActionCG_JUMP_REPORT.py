# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_JUMP_REPORT:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_JUMP_REPORT(self.person)
        # params begin ( don't move this line )

        packet['jump_times'] = self.person['jump_times']
        packet['x'] = self.person['x']
        packet['y'] = self.person['y']
        packet['z'] = self.person['z']
        packet['nowTime'] = self.person['nowTime']
        packet['curJumpSection'] = self.person['curJumpSection']
        packet['dir_x'] = self.person['dir_x']
        packet['dir_y'] = self.person['dir_y']
        packet['dir_z'] = self.person['dir_z']
        packet['deltaTime'] = self.person['deltaTime']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_JUMP_REPORT")
        return res
