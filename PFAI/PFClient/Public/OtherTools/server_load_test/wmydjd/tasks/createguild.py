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

Guild_Guid_Dic = {}

class createguild():
    def __init__(self, person):
        self.person = person

    def run(self, account = 10):
        #num = int(self.person['accounts'][1:])
        num = int(str(self.person['account'][2:]))
        accountindex = num % account
        if accountindex == 0:
            self.person['is_guild_captain'] = True
            self.person['guild_captain_account'] = num
        else:
            #帮会成员保存队长账号
            self.person['is_guild_captain'] = False
            captain_index = num - accountindex
            self.person['guild_captain_account'] = captain_index

        res = self.person.ActionCG_GUILD_REQ_INFO()
        gevent.sleep(2)

        # 没有帮派，创建
        if self.person['is_guild_captain']:
            if self.has_guild_info():
                Guild_Guid_Dic[self.person['guild_captain_account']] = self.person['guildGuid']
                loadlog.debug(f"{self.person['account']}: master have guild {self.person['guildGuid']} already ")
                return
            # add money
            self.add_money()
            loadlog.debug(f"{self.person['account']}: create guild ")
            self.person['guildName'] = self.gen_unicode(4)+u'帮'
            self.person['guildNotice'] = self.gen_unicode(5)
            self.person['guildShortName'] = self.gen_unicode()
            self.person['guildShortNameColor'] = 1
            res = self.person.ActionCG_GUILD_CREATE()
            if not res[0]:
                loadlog.error(f"{self.person['account']}: create guild failed, {res[2]}")
                return
            # 确保收到服务器刷来创建帮派的guid，队员才能申请加入
            while (self.person['guildGuid'] is None):
                Functions.heartbeat(self.person)
                gevent.sleep(1)
            Guild_Guid_Dic[self.person['guild_captain_account']] = self.person['guildGuid']
            loadlog.debug(f"{self.person['account']}: guild created guid-{self.person['guildGuid']}")
            res = self.person.ActionCG_GUILD_REQ_INFO()
            Functions.heartbeat(self.person)
        else:
            while not self.person['guild_captain_account'] in Guild_Guid_Dic:
                gevent.sleep(3)
                Functions.heartbeat(self.person)
            guildid = Guild_Guid_Dic[self.person['guild_captain_account']]
            #print(self.person['account'] + ": join guild " + str(guildid))
            self.person['guildGuid'] = guildid
            loadlog.debug(f"{self.person['account']}: req join guild guid-{self.person['guildGuid']}")

            res = self.person.ActionCG_GUILD_JOIN()
            if res[0]:
                loadlog.info(f"{self.person['account']}: guild joined guid-{self.person['guildGuid']}")
            else:
                loadlog.error(f"{self.person['account']}: guild join failed. guid-{self.person['guildGuid']}")
            gevent.sleep(1)
            Functions.heartbeat(self.person)
            self.person.ActionCG_GUILD_REQ_INFO()
            Functions.heartbeat(self.person)

    def has_guild_info(self):
        if self.person.getdata('guildGuid') and self.person['guildGuid']:
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
