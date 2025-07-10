# -*- coding: utf-8 -*-
from tasks.actions import net_packets
from tasks.actions import Functions


class ActionCG_AUCTION_LOOK:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_AUCTION_LOOK(self.person)
        # params begin ( don't move this line )

        packet['page'] = self.person['page']
        packet['publictime'] = self.person['publictime']
        packet['order'] = self.person['order']
        packet['classid'] = self.person['classid']
        packet['subclassid'] = self.person['subclassid']
        packet['treasure'] = self.person['treasure']
        packet['quality'] = self.person['quality']
        packet['profession'] = self.person['profession']
        packet['minlevel'] = self.person['minlevel']
        packet['maxlevel'] = self.person['maxlevel']
        packet['otherclass'] = self.person['otherclass']
        packet['itemid'] = self.person['itemid']
        packet['attr'] = self.person['attr']
        packet['thirdclassid'] = self.person['thirdclassid']
        # packet['reserved'] = self.person['reserved']
        # packet['reserved1'] = self.person['reserved1']
        packet['color'] = self.person['color']
        packet['sellmoneytype'] = self.person['sellmoneytype']
        packet['ismulti'] = self.person['ismulti']
        packet['minprice'] = self.person['minprice']
        packet['maxprice'] = self.person['maxprice']
        packet['keystring'] = self.person['keystring']
        # packet['issearch'] = self.person['issearch']
        packet['noCD'] = self.person['noCD']
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        # Functions.wait_for_packet(self.person, "CG_AUCTION_LOOK")
        return res
