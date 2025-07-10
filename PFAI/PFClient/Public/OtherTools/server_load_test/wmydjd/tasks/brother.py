#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
=======================================================================


=======================================================================
'''
import random
import math, string  
import gevent
import actions
import struct
import sys

outputDebug = False            
class brother():
    def __init__(self, person):
        self.client = person
    def get_chinese(self, num):
        s = ""
        while num:
            a = random.randint(0xbf, 0xd7)
            b = random.randint(0xa1, 0xfe)
            c = struct.pack("BB",a,b)
            try:
                s += c.decode("gb2312")
                num -= 1
            except UnicodeDecodeError:
                pass 
        return s


    def run(self): 
        #师傅与NPC薄云天交互
        while( self.client['npc_guid_boyuntian'] == None):
            self.client.ACGIdle()
            self.client['other_person'].ACGIdle( )
            self.msg2consle("not found boyuntian, try again...")
            gevent.sleep(2)
            
        self.client.ACGChangeCombatTarget(self.client['npc_guid_boyuntian'])
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        self.client.ACGBottingSuspend(1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()   
        self.client.ACGBottingSuspend(1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()    
        
        self.client.ACGInteractive(self.client['npc_guid_boyuntian'], 1)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()
        
        self.client.ACGSwornRequest()
        res = Actions.Functions.wait_for_packet(self.client, "GCSwornProcessSync", 2)
        self.msg2consle("brother1 sent ACGSwornRequest...")
        while (res[0] == False) :
            gevent.sleep(3)
            self.client.AHeartBeat() #等待期间，继续idle发送心跳包
            self.client['other_person'].AHeartBeat() #等待期间，继续idle发送心跳包
            res = Actions.Functions.wait_for_packet(self.client, "GCSwornProcessSync", 2)
          
        self.msg2consle("brother1 got GCSwornProcessSync")  
        res1 = Actions.Functions.wait_for_packet(self.client['other_person'], "GCSwornProcessSync", 2)
        while (res1[0] == False) :
            gevent.sleep(3)
            self.client.AHeartBeat() #等待期间，继续idle发送心跳包
            self.client['other_person'].AHeartBeat() #等待期间，继续idle发送心跳包
            res = Actions.Functions.wait_for_packet(self.client['other_person'], "GCSwornProcessSync", 2)
            
        self.msg2consle("brother2 got GCSwornProcessSync") 
        self.client.ACGBottingSuspend(0)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        self.client.ACGBottingSuspend(0)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()         
        self.client.ACGInteractiveFinish(self.client['npc_guid_boyuntian'])
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()
        
        #结拜确认阶段
        self.client.ACGSwornProcessResult(1, '1')
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()        
        self.client['other_person'].ACGSwornProcessResult(1, '1')
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()
        self.msg2consle("CGSwornProcessResult 1") 
        #长幼排序阶段
        self.client.ACGSwornProcessResult(2, str(self.client['playerId'])) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()        
        self.client['other_person'].ACGSwornProcessResult(2, str(self.client['playerId'])) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()  
        self.msg2consle("CGSwornProcessResult 2") 
        #长幼重排序阶段
        self.client.ACGSwornProcessResult(3, '1') 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()        
        self.client['other_person'].ACGSwornProcessResult(3, '1')
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        self.msg2consle("CGSwornProcessResult 3") 
        #老大起结拜名号阶段        
        #genChar = RandomChar()
        #tempStr = genChar.randChinese(4)
        tempStr = self.get_chinese(4)
        self.client.ACGSwornProcessResult(4, tempStr) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()  
        self.msg2consle("CGSwornProcessResult 4") 
        #结拜组成员起字号阶段
        tempStr = self.get_chinese(2)
        self.client.ACGSwornProcessResult(5, tempStr) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()  
        tempStr = self.get_chinese(2)
        self.client['other_person'].ACGSwornProcessResult(5, tempStr)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()  
        self.msg2consle("CGSwornProcessResult 5") 
        #结拜展示阶段、
        self.client.ACGSwornProcessResult(6, '1') 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()        
        self.client['other_person'].ACGSwornProcessResult(6, '1')
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()
        self.msg2consle("CGSwornProcessResult 6") 
        #结拜展示阶段
        self.client.ACGStoryStart(113) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()        
        self.client['other_person'].ACGStoryStart(113) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()
        self.client.ACGBottingSuspend(0)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        self.client.ACGBottingSuspend(0)
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle() 
        gevent.sleep(5)
        self.client.ACGStoryFinish(0, 113) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()        
        self.client['other_person'].ACGStoryFinish(0,113) 
        self.client.ACGIdle()
        self.client['other_person'].ACGIdle()
        self.msg2consle("end!!!") 
    def msg2consle(self, msg):
        if outputDebug: 
            print "%s->%s" %(self.client['accounts'], msg)
        
class RandomChar():
    """用于随机生成汉字"""
    @staticmethod
    def Unicode():
        val = random.randint(0x4E00, 0x9FBF)
        return unichr(val)  
    @staticmethod
    def GB2312():
        head = random.randint(0xB0, 0xCF)
        body = random.randint(0xA, 0xF)
        tail = random.randint(0, 0xF)
        val = ( head << 8 ) | (body << 4) | tail
        str = "%x" % val
        return str.decode('hex').decode('gb2312') 
    @staticmethod
    def randomGB2312():    
        head = random.randint(0xB0, 0xDF)    
        body = random.randint(0xA, 0xF)    
        tail = random.randint(0, 0xF)    
        val = ( head << 0x8 ) | (body << 0x4 ) | tail    
        str = '%x' % val    
        return str.decode('hex').decode('gb2312')    

    def randChinese(self, num):
        tempStr = ''
        for i in range(0, num):
            char = RandomChar().Unicode() 
            tempStr = tempStr + char
        return tempStr
       
       
       