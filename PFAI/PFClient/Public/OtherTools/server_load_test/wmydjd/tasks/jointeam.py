#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
=======================================================================

=======================================================================
'''
import random
import gevent

Team_Dic = {}

class jointeam():
    '''多人加入同一个队伍'''
    def __init__(self, person):
        self.person = person

    def run(self, account = 5):
        num = int(self.person['accounts'][1:])
        accountindex = num % account
        if accountindex == 0:
            self.person['is_team_captain'] = True
            self.person['team_captain_account'] = num
        else:
            #保存队长账号
            self.person['is_team_captain'] = False
            captain_index = num - accountindex
            self.person['team_captain_account'] = captain_index

        self.person.ActionCG_GET_TeamGetTeamList()
        self.person.ACGIdle()

        if self.person['is_team_captain']:
            self.person.ACGTeamCreate()
            self.person.ACGIdle()
            self.person.ACGApplyList()
            self.person.ACGIdle()             
            self.person.ACGChangeAutoAccept()
            self.person.ACGIdle()

            # 确保收到服务器刷来创建帮派的guid，队员才能申请加入
            while (self.person['teamGuid'] is None):
                self.person.ACGIdle()
                gevent.sleep(1)
            Team_Dic[self.person['team_captain_account']] = self.person['teamGuid']
            
            for i in range(10):
                gevent.sleep(1)
                self.person.ACGIdle()
        else:
            while not self.person['team_captain_account'] in Team_Dic:
                gevent.sleep(3)
                self.person.ACGIdle()

            teamGuid = Team_Dic[self.person['team_captain_account']]
            self.person.ACGTeamApply(teamGuid)
            gevent.sleep(1)
            self.person.ACGIdle()

