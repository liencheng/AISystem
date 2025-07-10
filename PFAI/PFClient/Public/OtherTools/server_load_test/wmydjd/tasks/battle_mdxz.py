# -*- coding: utf-8 -*-
'''
=======================================================================

=======================================================================
'''
import gevent
import random

class battle_mdxz():
    def __init__(self, person):
        self.person = person

    def run(self):
        if self.person['state'] == "start":
            if len(self.person['unitInfo_dict']) == 0:
                #self.msg2consle('no monster, searching...')
                self.person['state'] = "wait"
            else:
                self.person['state'] = 'battle'

        if self.person['state'] == "wait":
            self.person.ACGIdle()
            return

        if self.person['state'] == 'battle':
            if len(self.person['battle_monster']) > 0:
                npc_guid = random.choice(self.person['battle_monster'].keys())
                #self.msg2consle('battling monster boss...')
                self.person.ACGUseSkill2Obj(11000000, 1, npc_guid)
                self.person.ACGIdle()
                self.person['state'] = 'start'
            gevent.sleep(0)
            self.person.ACGIdle()
            return
        else:
            print ("self.person['state']:", self.person['state'])
            print ("state error!")
            exit(1)

    def msg2consle(self, msg):
        #if self.person['__loadflag']:
        print ("%s---------------->%s" %(self.person['accounts'], msg))
