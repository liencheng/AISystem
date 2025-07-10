#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
=======================================================================


=======================================================================
'''
import random
import gevent
import Actions

class impart():
    def __init__(self, person):
        self.client = person

    def run(self): 
        #师傅与NPC司马云交互
        self.client.ACGChangeCombatTarget(self.client['npc_guid_simayun'])
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        self.client.ACGBottingSuspend(1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()   
        self.client.ACGBottingSuspend(1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()         
        self.client.ACGInteractive(self.client['npc_guid_simayun'], 1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()  
        self.client.ACGBottingSuspend(1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()
        self.client.ACGBottingSuspend(0)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        self.client.ACGBottingSuspend(0)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()         
        self.client.ACGInteractiveFinish(self.client['npc_guid_simayun'])
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()

        #师傅查询师徒信息并申请传功
        self.client.ACGMyMentorInfoReq()
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()        
        self.client.ACGMentorImpartReq(1, self.client['other_person']['playerId'])
        self.client.ACGIdle()
        #self.client['other_person'].ACGIdle()
        
        #徒弟等待GCDialogView，回复CGDialogConfirm开始传功
        res1 = Actions.Functions.wait_for_packet(self.client['other_person'], "GCDialogView", 2)
        while (res1[0] == False) :
            gevent.sleep(3)
            self.client.ACGIdle()
            self.client['other_person'].AHeartBeat() #等待期间，继续idle发送心跳包
            res = Actions.Functions.wait_for_packet(self.client['other_person'], "GCDialogView", 2)
          
 
        self.client['other_person'].ACGDialogConfirm(12, 0, 1, '')
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        
        self.client.ACGChangeCombatTarget(-1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        
        self.client.ACGEnterSceneOk(2)         
        self.client.ACGIdle()
        self.client['other_person'].ACGEnterSceneOk(2)  
        self.client['other_person'].ACGIdle() 
        gevent.sleep(2)
     
      
        self.client.ACGGetSceneFieldofvision(400007)        
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client['other_person'].ACGGetSceneFieldofvision(400007)        
        self.client['other_person'].ACGIdle()
        gevent.sleep(2)




