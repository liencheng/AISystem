#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
=======================================================================

=======================================================================
'''
import loadlog
import random
import gevent

from tasks.actions import Functions

Team_Guid_Dic = {}
TeamCount = 5


class create_team():
    def __init__(self, person):
        self.person = person

    def run(self):
        #num = int(self.person['accounts'][1:])
        num = int(str(self.person['account'][2:]))
        accountindex = num % TeamCount
        if accountindex == 0:
            self.person['is_team_captain'] = True
            self.person['team_captain_account'] = num
        else:
            #成员保存队长账号
            self.person['is_team_captain'] = False
            captain_index = num - accountindex
            self.person['team_captain_account'] = captain_index

        # 没有，创建
        if self.person['is_team_captain']:
            if self.has_team_info():
                Team_Guid_Dic[self.person['team_captain_account']] = self.person['teamGuid']
                loadlog.debug(f"{self.person['account']}: master have team {self.person['teamGuid']} already ")
                return

            loadlog.debug(f"{self.person['account']}: create team ")
            self.person['guidlist'] = [18446744073709551615]
            self.person['targetId'] = -1
            self.person['minLv'] = 1
            self.person['maxLv'] = 429
            self.person['invitetype'] = 0
            res = self.person.ActionCG_REQ_TEAM_INVITE()
            if not res[0]:
                loadlog.error(f"{self.person['account']}: create team failed, {res[2]}")
                return
            res = Functions.wait_for_packet(self.person, 'GC_TEAM_SYNC_TEAMINFO')
            if not res[0]:
                return res
            # 确保收到服务器刷来创建的guid，队员才能申请加入
            if self.person['teamGuid']:
                Team_Guid_Dic[self.person['team_captain_account']] = self.person['teamGuid']
                loadlog.debug(f"{self.person['account']}: team created guid-{self.person['teamGuid']}")
            else:
                return False,0,"no teamID found"
            return res
        else:
            while not self.person['team_captain_account'] in Team_Guid_Dic:
                gevent.sleep(3)
                Functions.heartbeat(self.person)
            teamID = Team_Guid_Dic[self.person['team_captain_account']]
            #print(self.person['account'] + ": join guild " + str(teamID))
            self.person['teamGuid'] = teamID
            loadlog.debug(f"{self.person['account']}: req join team guid-{self.person['teamGuid']}")
            self.person['isOneTeamMember'] = False
            self.person['teamMemberGuidList'] = [teamID]
            self.person['bJoinArmy'] = False
            res = self.person.ActionCG_REQ_TEAM_JOIN()
            if not res or not res[0]:
                loadlog.error(f"{self.person['account']}: team join failed. guid-{self.person['teamGuid']}")
            else:
                loadlog.info(f"{self.person['account']}: team joined guid-{self.person['teamGuid']}")
                res = Functions.wait_for_packet(self.person, 'GC_TEAM_SYNC_TEAMINFO')
                if not res or res[0]:
                    return res
            gevent.sleep(1)
            return res

    def has_team_info(self):
        if self.person.getdata('teamID') and self.person['teamID']:
            return True
        return False

    def add_money(self):
        self.person['cmdstr'] = 'scoin,1000'
        res = self.person.ActionCG_GMCMDSTR()
        gevent.sleep(1)
        self.person['cmdstr'] = 'gcoin,1000'
        res = self.person.ActionCG_GMCMDSTR()
        gevent.sleep(1)
        self.person['cmdstr'] = 'yuanbao,1000'
        res = self.person.ActionCG_GMCMDSTR()
        gevent.sleep(1)
        self.person['cmdstr'] = 'yuanbaosilver,1000'
        res = self.person.ActionCG_GMCMDSTR()
        gevent.sleep(1)
        self.person['cmdstr'] = 'yuanbaobind,1000'
        res = self.person.ActionCG_GMCMDSTR()
        gevent.sleep(1)

    def gen_unicode(self, count=1):
        ustr = u''
        for i in range(count):
            val = random.randint(0x4e00, 0x9fbf)
            ustr += chr(val)
        return ustr
