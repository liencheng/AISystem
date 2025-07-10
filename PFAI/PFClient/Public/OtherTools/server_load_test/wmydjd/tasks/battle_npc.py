# -*- coding: utf-8 -*-
'''
=======================================================================


=======================================================================
'''
import random
import math
import gevent

COUNT = 0
COUNTF = 0

outputDebug = False
class battle_npc():
    '''与指定NPC战斗'''
    def __init__(self, person):
        self.person = person

    def run(self, npc_guid, npc_pos):
        '''
        在给定坐标点发现npc并战斗
        npc_guid: 指定怪物guid
        npc_pos: 怪物坐标（字典格式）
        '''
           
        if self.person['state'] == "start":
            if len(self.person['unitInfo_dict']) == 0:
                self.msg2consle('no monster, searching...')
                self.person['state'] = "search"
            if self.person['unitInfo_dict'].has_key(npc_guid) == False:
                self.msg2consle('not found monster[%s], searching...' %str(npc_guid))
                self.person['state'] = 'search'
            if self.person['unitInfo_dict'].has_key(npc_guid) == True:
                self.person['state'] = 'walk'
            
        if self.person['state'] == "search":       
            #self.moveAroundPos(npc_pos) #与 goto单位不一样
            self.person['cmdstr'] = 'trsco,%s,%s,%s'%(str(npc_pos['x']), str(npc_pos['y']), str(npc_pos['z'])
            res = self.person.ActionCG_GMCMDSTR()

            self.msg2consle('go to %s:%s to search monster[%s]...' %(str(npc_pos['x']), str(npc_pos['z']), str(npc_guid)))
            self.person['state'] = 'start'
            gevent.sleep(2)
            return
        
        if self.person['state'] == "walk":
            self.msg2consle('walk...')
            res = self.person.ACGMove2Obj(npc_guid)
            self.person['state'] = 'battle'
            self.person.ACGIdle()
            gevent.sleep(2) 
            
        if self.person['state'] == 'battle':
            self.msg2consle('battling...')
            self.person.ACGUseSkill2Obj(11000000, 1, npc_guid)
            self.person['state'] = 'start'
            self.person.ACGIdle()
            gevent.sleep(2)             
            return
        if self.person['state'] == 'exit':
            self.msg2consle('exit...')
            #已经死亡，退出剧情副本
            self.person.ACGChangeCombatTarget(-1)
            self.exitFromCopyScene()
            self.person['state'] = 'start'
            self.person.ACGIdle()
            gevent.sleep(3) 
            self.person.ACGIdle()
            gevent.sleep(3)
            return
        else:
            print "self.person['state']:", self.person['state']
            print "state error!"
            exit(1)
    def moveAroundPos(self, pos):
        '''给定坐标范围内移动一次尝试搜索指定npc'''
        targetPos = {'x': pos['x'] + random.randint(-2, 2), 'y': pos['y'] + random.randint(-2, 2), 'z': pos['z'] + random.randint(-2, 2)}
        self.person.ACGSendMove(targetPos)
        gevent.sleep(3) 
        
    def getNewMonster(self):
        while True:
            guid = random.choice(self.person['unitInfo_dict'].keys())
            x = self.person['posx'] - self.person['unitInfo_dict'][guid][0]
            y = self.person['posy'] - self.person['unitInfo_dict'][guid][1]
            z = self.person['posz'] - self.person['unitInfo_dict'][guid][2]
            #print self.person['accounts']  +" getNewMonster " + str(self.person['unitInfo_dict'][guid]) + " in " + str(math.sqrt(x*x + y*y + z*z))
            
            if math.sqrt(x*x + y*y + z*z) < 200000:
                print self.person['accounts']  +" getNewMonster distance is ok" + str(self.person['unitInfo_dict'][guid])
                return guid

            print "distance:" + str(math.sqrt(x*x + y*y + z*z))

    #由服务器触发离开剧情副本的处理方式
    def exitFromCopyScene(self):
        print "player is exitFromCopyScene..."
        res = Actions.Functions.wait_for_packet(self.person, "GCPlayerEnterScene", 2)
        while (res[0] == False) :
            gevent.sleep(1)
            self.person.AHeartBeat() #等待期间，继续发送心跳包
            res = Actions.Functions.wait_for_packet(self.person, "GCPlayerEnterScene", 2)
            
        self.person.ACGEnterSceneOk(2)        
        self.person.ACGIdle()
        gevent.sleep(3)        
    def msg2consle(self, msg):
        if outputDebug: 
            print "%s->%s" %(self.person['accounts'], msg)