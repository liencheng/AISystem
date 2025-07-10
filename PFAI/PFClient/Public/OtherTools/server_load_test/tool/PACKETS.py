# -*- coding: utf-8 -*-
from Packet import Packet
import time
import hashlib

class GCActivityClosedIds (Packet): pass
class ActivityData (Packet):
	pass
class GCActivityData (Packet):
    def handle(self):
        for item in self['activitiesData']:
            if item.activityId == 52:
                self.person['fashionweek_ready'] = True
class GCMyStorage (Packet):
	def handle(self):
		# self.person['sell_guid'] = None
		if len(self['items'])>0:
			self.person['sell_guid'] = self['items'][0].guid
class GCTradeBankInfo  (Packet):
	def handle(self):
		tradeBankItemsPriceDict = {}
		if len(self['itemInfo']) > 0 :
			for item in self['itemInfo']:
				tradeBankItemsPriceDict[str(item.tabId)] = int(item.nowPrice)
			self.person['tradeBankItemsPriceDict'] = tradeBankItemsPriceDict

class EinherjarData (Packet):
	pass
class GCActivateEinherjarReply (Packet):
	pass
class GCGameSwitchFuction (Packet):
	pass
class CGHandshake (Packet):
	pass
class GCHandshake (Packet):
	def handle(self):
		self.person['handshake_array'] = self['handshake_array'] # 102
		dhkey_low = self['dhkey_low']
		dhkey_high = self['dhkey_high']
		if 0!=dhkey_low and 0!=dhkey_high :
			another_public_key = DHExchange.DHKey128(0)
			another_public_key.set_low(dhkey_low)
			another_public_key.set_high(dhkey_high)
			my_private_key = self.person['private_key']
	
			#calculate the secret key
			secret_key = DHExchange.generate_key_secret(my_private_key, another_public_key)
			self.person['secret_key'] = secret_key
			secret_key_low = secret_key.get_low()
			secret_key_high = secret_key.get_high()
	
			self.person['encoder'] = XorShift128.XorShift128(secret_key_low, secret_key_high)

class GCTrumpDeleteBack (Packet):
	pass
class CGTrumpExchange (Packet):
	pass
class CGTip (Packet):
	pass
class GCTip (Packet):
	pass
# GCNetItem: item will store in bag, save guid and index in dict and used in sell back item action
class GCNewItem (Packet):# 23042
	def handle(self):
		bagsSlotDict = {}
		if len(self['newItemVoList']) > 0 :
			for slot in self['newItemVoList']:
				bagsSlotDict[int(slot.slotIndex)] = str(slot.guid)
			self.person['bags_slots'] = bagsSlotDict
			#add by luoyunpeng
			self.person['last_item_slotindex'] = self['newItemVoList'][0].slotIndex
			# print "last_item_slotindex:",self.person['last_item_slotindex']
			self.person['last_item_slot_itemguid'] = str(self['newItemVoList'][0].guid)

class GCPlayerEgg (Packet):
	def handle(self):
		self.person['egg_playerGuid'] = self['egg'].playerGuid
		self.person['egg_eggGuid'] = self['egg'].eggGuid

class GCSyncItemInfo (Packet):
	def handle(self):
		if self.person['GCSyncItemInfoList'] == None:
			self.person['GCSyncItemInfoList'] = []
		for item in self['itemVo']:
			self.person['GCSyncItemInfoList'].append(item)

class LCLoginQueueStatus (Packet):
	def handle(self):
		self.person['LoginQueueStatus'] = self['status']
class LCLoginBack (Packet):
	def handle(self):
		if len(self['playerList'])==0:
			self.person['playerId'] = 0
		else:
			self.person['playerId'] = self['playerList'][0].playerId
		temp = hashlib.md5()
		temp.update(str(self['token']))
		self.person['token'] = temp.hexdigest()
class LCCreatePlayerBack (Packet):
	def handle(self):
#        print self['playerInfo']
		self.person['playerId'] = self['playerInfo'].playerId
class CLPlayerLoginGameSvr (Packet):
	pass

class GCCharObjDieBack (Packet):
	def handle(self):
		dieObjs = self['objIds']
		for dieObjGuid in dieObjs:
			#print "monster " + str(dieObjGuid) +" dead..."
			if dieObjGuid in self.person['inCombatRangeObjList']:
				self.person['inCombatRangeObjList'].remove(dieObjGuid)
			if self.person['unitInfo_dict'].has_key(dieObjGuid):
				del self.person['unitInfo_dict'][dieObjGuid]

class CGFixPosSend (Packet):
	#20016;
	def handle(self):
		self.person['guildGuid'] = self.obj.playerSelfInfo.guildInfo.guildId
		self.person['posx'] = self.obj.playerSelfInfo.position.x
		self.person['posy'] = self.obj.playerSelfInfo.position.y
		self.person['posz'] = self.obj.playerSelfInfo.position.z
class GCPlayerEnterScene (Packet):
	def handle(self):
		self.person['newPlayer'] = 'change'
		self.person['guildGuid'] = self.obj.playerSelfInfo.guildInfo.guildId
		self.person['posx'] = self.obj.playerSelfInfo.position.x
		self.person['posy'] = self.obj.playerSelfInfo.position.y
		self.person['posz'] = self.obj.playerSelfInfo.position.z
		self.person['onlyId'] = self.obj.onlyId
		self.person['EnterSceneGuajixiulian'] = True
class GCObjectFaceState (Packet):
	pass

class GCObjectEnterVisualRange (Packet):
	def handle(self):
		if self.person['beidou_dic'] == None:
			self.person['beidou_dic'] = {}
		objectInfosList = self['objectInfos'] # got objectInfos from coming socket and save in list
		if (len(objectInfosList)) > 0:
			# convert bytes array  to string

			'''
            for comingInfo in objectInfosList:
                bytesStr = comingInfo.name
                comingInfo.name = bytesStr
            '''
			# handle objectinfos

			for comingInfo in objectInfosList:
				if comingInfo.unitType == 2:
					if comingInfo.name == u'杨硕':
						self.person['npc_guid_dlcm'] = comingInfo.guid
					if u'饕餮' in comingInfo.name:
						self.person['monster_guid_qiongqi'] = comingInfo.guid
						#print "found npc: %s" %comingInfo.name
					
				if comingInfo.unitType == 4:
					if comingInfo.name == u'明鬼':
						self.person['npc_guid'] = comingInfo.guid
					if comingInfo.name == u'神笔马良':
						self.person['npc_guid_sbml'] = comingInfo.guid
					if comingInfo.name == u'天外村使者':
						self.person['npc_guid_twcsz'] = comingInfo.guid
					if comingInfo.name == u'拓跋木真':
						self.person['npc_guid_yuer'] = comingInfo.guid
					if comingInfo.name == u'雷小雨':
						self.person['npc_guid_fyzd'] = comingInfo.guid
					if comingInfo.name == u'申老板':
						self.person['npc_guid_mdxz'] = comingInfo.guid
					#if comingInfo.name == u'北斗中星君' and self.person['goto_x_pos'] == comingInfo.position.x and self.person['goto_z_pos'] == comingInfo.position.z:
					if comingInfo.name == u'北斗中星君':
						self.person['beidou_dic'][str(comingInfo.position.x) + str(comingInfo.position.z)] = comingInfo.guid
						if self.person['beidou_dic'].has_key(str(self.person['goto_x_pos']) + str(self.person['goto_z_pos'])):
							self.person['npc_guid_tgcf'] = self.person['beidou_dic'][str(self.person['goto_x_pos']) + str(self.person['goto_z_pos'])]
					if comingInfo.name == u'鸾鸟':
						self.person['npc_guid_ln'] = comingInfo.guid
					if comingInfo.name == u'符鬼蛋':
						#print self.person['account']  +" found " + comingInfo.name + " guid: " + str(comingInfo.guid)
						self.person['npc_guid_fuguidan'] = comingInfo.guid
					if u'司马云' in comingInfo.name:
						self.person['npc_guid_simayun'] = comingInfo.guid
						#print self.person['account']  +" found simayun: " + str(comingInfo.guid)
					if u'薄云天' in comingInfo.name:
						self.person['npc_guid_boyuntian'] = comingInfo.guid
					#print self.person['account']  +" found " + comingInfo.name
					if u'帮派大盗' in comingInfo.name:
						self.person['npc_guid_bangpaidadao'] = comingInfo.guid	
					if u'陈靖仇' in comingInfo.name:
						self.person['npc_guid_chenjinchou'] = comingInfo.guid
						#print self.person['account']  +" found " + comingInfo.name
				if comingInfo.unitType == 6:
					if self.person['drop_dict'] == None:
						self.person['drop_dict'] = []
					self.person['drop_dict'].append(comingInfo.guid)
				if comingInfo.currentHp == 0:
					#continue
					pass

				pos = []
				if comingInfo.HasField('navInfo') and comingInfo.navInfo.HasField('moveMode'):
					if comingInfo.navInfo.moveMode == -1:
						pos = [comingInfo.navInfo.startPos.x, comingInfo.navInfo.startPos.y, comingInfo.navInfo.startPos.z]
					else:
						pos = [comingInfo.navInfo.targetPos.x,comingInfo.navInfo.targetPos.y, comingInfo.navInfo.targetPos.z]
				else:
					pos = [comingInfo.position.x, comingInfo.position.y, comingInfo.position.z]
				# u'强制记录搜到npc当前坐标，暂不考虑navInfo，'
				if int(comingInfo.position.y) > 1000000: # u'2018/05/18: 排查y坐标过高问题'
					print("GCObjectEnterVisualRange:%s-> %s, %s, %s" %(self.person['account'], str(comingInfo.position.x), str(comingInfo.position.y), str(comingInfo.position.z)))
				pos = [comingInfo.position.x, comingInfo.position.y, comingInfo.position.z]
				#target monster doesn't in list, just add
				self.person['unitInfo_dict'][comingInfo.guid] = pos
				if comingInfo.unitType != 2:
					continue
				#print "add object " + str(comingInfo.guid) + " into unitInfo_dict"

class GCObjectLeaveVisualRange (Packet):
	def handle(self):
		objList = self['objectGuid'] # got objectInfos from coming socket and save in list
		for targetguild in objList:
			if self.person['unitInfo_dict'].has_key(targetguild):
				del self.person['unitInfo_dict'][targetguild]
			if self.person['battle_monster'].has_key(targetguild):
				del self.person['battle_monster'][targetguild]
			#print "remove monster " + str(targetguild) + " from unitInfo_dict as GCObjectLeaveVisualRange"

class GCUnitPublicInfoSync (Packet):
	def handle(self):
		# convert bytes array  to string
		'''
		for comingInfo in objectInfosList:
		    bytesStr = comingInfo.name
		    comingInfo.name = bytesStr.decode('utf8')
		'''
		unitInfoList = self['unitInfo']
		for comingInfo in unitInfoList:
			if comingInfo.unitType == 2:
				if comingInfo.guid in self.person['unitInfo_dict']:
					if comingInfo.HasField('currentHp') and comingInfo.currentHp == 0:
						self.person['unitInfo_dict'].pop(comingInfo.guid)
					if comingInfo.HasField('navInfo') and comingInfo.navInfo.HasField('moveMode'):
						if comingInfo.navInfo.moveMode == -1:
							self.person['unitInfo_dict'][comingInfo.guid] = [comingInfo.navInfo.startPos.x, comingInfo.navInfo.startPos.y, comingInfo.navInfo.startPos.z]
						else:
							self.person['unitInfo_dict'][comingInfo.guid] = [comingInfo.navInfo.targetPos.x,comingInfo.navInfo.targetPos.y, comingInfo.navInfo.targetPos.z]
					elif comingInfo.skillParam.HasField('skillId'):
						self.person['unitInfo_dict'][comingInfo.guid] = [comingInfo.skillParam.attackerPos.x,
						                                                 comingInfo.skillParam.attackerPos.y,
						                                                 comingInfo.skillParam.attackerPos.z]
				# add by luoyunpeng
				if comingInfo.HasField('navInfo') and comingInfo.navInfo.HasField('targetPos'):
					dis_x = self.person['posx'] - comingInfo.navInfo.targetPos.x
					dis_z = self.person['posz'] - comingInfo.navInfo.targetPos.z
					if -22000 <= dis_x <= 22000 and -22000 <= dis_z <= 22000:
						self.person['battle_monster'][comingInfo.guid] = (comingInfo.navInfo.targetPos.x,comingInfo.navInfo.targetPos.y,comingInfo.navInfo.targetPos.z)
					else:
						if self.person['battle_monster'].has_key(comingInfo.guid):
							del self.person['battle_monster'][comingInfo.guid]
				if comingInfo.HasField('currentHp') and comingInfo.currentHp == 0:
					if self.person['battle_monster'].has_key(comingInfo.guid):
						del self.person['battle_monster'][comingInfo.guid]

			elif comingInfo.unitType == 1:
				if comingInfo.HasField('navInfo') and comingInfo.navInfo.HasField('targetPos'):
					dis_x = self.person['posx'] - comingInfo.navInfo.targetPos.x
					dis_z = self.person['posz'] - comingInfo.navInfo.targetPos.z
					if -22000 <= dis_x <= 22000 and -22000 <= dis_z <= 22000:
						self.person['battle_player'][comingInfo.guid] = (comingInfo.navInfo.targetPos.x,comingInfo.navInfo.targetPos.y,comingInfo.navInfo.targetPos.z)
					elif self.person['battle_player'].has_key(comingInfo.guid):
						del self.person['battle_player'][comingInfo.guid]

class GCUnitPrivateInfoSync (Packet):
	def handle(self):
		comingInfo = self['playerInfo']
		if comingInfo.unitType == 1:
			if comingInfo.guid == self.person['playerId']: #记录角色当前私有信息，比如hp
				if comingInfo.HasField('currentHp'):
					self.person['currentHp'] = comingInfo.currentHp
					if self.person['currentHp'] == 0:
						self.person['state'] = 'exit'
						
				if comingInfo.HasField('position'):
					if int(comingInfo.position.y) > 1000000: #2018/05/18: 排查y坐标过高问题
						print("GCUnitPrivateInfoSync:%s-> position X: %s,  position Y: %s,  position Z: %s" %(self.person['account'], str(comingInfo.position.x), str(comingInfo.position.y), str(comingInfo.position.z)))
					

class GCMapSyncData (Packet):
	"""地图信息同步，目前帮派大盗会用到npc坐标更新"""
	def handle(self):
		for item in self['mapSyncDataList']:
			guid = item.guid
			pos = [item.pos.x, item.pos.y, item.pos.z]
			self.person['unitInfo_dict'][guid] = pos

class GCRecommendFriendList (Packet):
	def handle(self):
		if self.person['friendplayerId'] == None:#如果person里面没有friendplayerid的值
			self.person['friendplayerId'] =[]#建立一个空的friendplayerid
			for i in self['recommendedFriend']:#取recommendedFriend里面元素的个数
				self.person['friendplayerId'].append(i.playerId)#把里面的playerId传给person里面的friendplayerid
		else:
			for i in self['recommendedFriend']:
				self.person['friendplayerId'].append(i.playerId)
class XX_REQUEST_HEARTBEAT (Packet):
	pass
class XX_RESPONSE_HEARTBEAT (Packet):
	pass
class CB_REQ_GONGGAO_ADDR (Packet):
	pass
class BC_RET_GONGGAO_ADDR (Packet):
	pass
class CB_REQ_FREEFLOW (Packet):
	pass
class BC_RET_FREEFLOW (Packet):
	pass
class CB_REQ_FRIEND_LIST (Packet):
	pass
class BC_RET_FRIEND_LIST (Packet):
	pass
class CB_TEST_CMD (Packet):
	pass
class CB_REQ_CHAR_LIST (Packet):
	pass
class BC_RET_CHAR_LIST (Packet):
	pass
class CB_WHITE_ACCOUNT (Packet):
	pass
class BC_WHITE_ACCOUNT (Packet):
	pass
class CG_REQUEST_PRAYEXP_SYNC (Packet):
	pass
class CG_URGE_MASTER_PUBLISH_MENTOR_TASK (Packet):
	pass
class GC_SYN_FAIRY_INFO (Packet):
	pass
class CG_SWORDTEAM_REQ_INFO (Packet):
	pass
class GC_RET_SIGNININFO_DAYLY (Packet):
	pass
class CG_REQUEST_FIRSTRECHARGE_BONUS (Packet):
	pass
class GC_RES_JIANMUXB_INFO (Packet):
	pass
class GC_MILITARY_SYNC_MILITARYRANK (Packet):
	pass
class GC_RET_MATCH_OP (Packet):
	pass
class GC_REQUEST_INTERACT (Packet):
	pass
class GC_GIVESIGN_FORPICDEL (Packet):
	pass
class GC_SYNC_HUANGHUNSHENGDAN_COPY_SCENE_STATE (Packet):
	pass
class GC_DOMAIN_SYNC_LINEEVT (Packet):
	pass
class CG_BROTHERHOOD_DELETE_ALL_RECRUIT_APPLY (Packet):
	pass
class GC_MISSION_SYNC_LIST (Packet):
	pass
class CG_ACCLOGIN_ASKINFO (Packet):
	pass
class GC_RES_MENTOR_RECURIT (Packet):
	pass
class CG_REQ_GUILDCONVOY_FOLLOW (Packet):
	pass
class GC_TONGTIANTREASURE_RETOP (Packet):
	pass
class GC_NOTICE_CONST (Packet):
	pass
class CG_ASK_TGCFAWARD (Packet):
	pass
class CG_CLIENT_BEHAVIOR (Packet):
	pass
class GC_ISINSELFWILDDUELLIST (Packet):
	pass
class CG_STALL_REVIEW_DELETE (Packet):
	pass
class CG_SINGLE_INTERACT (Packet):
	pass
class GC_ISINTARGETWILDDUELLIST (Packet):
	pass
class GC_SHOW_ITEMPROMPT (Packet):
	pass
class CG_BROTHERHOOD_RECRUIT_MY (Packet):
	pass
class CG_BROTHERHOOD_RANK_INFO (Packet):
	pass
class GC_PRESTIGE_NEWREWARD (Packet):
	pass
class GC_BUFF_REMOVE_INFO (Packet):
	pass
class GC_RES_PET_SUMMON_OR_CALLBACK (Packet):
	pass
class CG_TIANSHU_COMPOSE (Packet):
	pass
class CG_GUILD_DIG_UP_THE_HATCHET (Packet):
	pass
class CG_ASK_FOLLOW (Packet):
	pass
class GC_SYNC_RUBKI_CUBE_INFO (Packet):
	pass
class GC_MIDAS_REQUEST_BALANCE_RESULT (Packet):
	pass
class GC_TIANSHU_MASTER_INFO (Packet):
	pass
class GC_SYNC_SERVANT (Packet):
	pass
class CG_ASK_AUTOTEAM_QUIT_BW (Packet):
	pass
class GC_RET_FRIEND_USERINFO (Packet):
	pass
class CG_EXAM_ANSWERQUESTION (Packet):
	pass
class GC_JXGZAWARD_DATA (Packet):
	pass
class CG_GUILD_BINDGROUP_SUCESS (Packet):
	pass
class CG_SWORDTEAM_REQ_LIST (Packet):
	pass
class GC_PLAY_BOSS_PLAYED_PROMPT (Packet):
	pass
class CG_REQ_PUBLISH_APPRENTICE_TASK (Packet):
	pass
class GC_RET_YLTXDROP_INFO (Packet):
	pass
class GC_CHAT_REMOVE_GUID (Packet):
	pass
class GC_COPYSCENE_INVITEVIEW (Packet):
	pass
class GC_GUILD_ALLIANCE_RESULT (Packet):
	pass
class CG_REQ_QINGYIVALUE_DAILY_INFO (Packet):
	pass
class GC_RET_RANK (Packet):
	pass
class GC_TIANSHU_EXCHANGE (Packet):
	pass
class CG_DW_RETURNHOME (Packet):
	pass
class CG_ASK_SELFROLEVIEWINFO (Packet):
	pass
class CG_TOURNAMENT_OPERATE_MATCH (Packet):
	pass
class GC_ADVENTURE_SYNC_SHOP_OPEN (Packet):
	pass
class CG_EQUIP_EQUIP_REBIRTH (Packet):
	pass
class CG_LIMITSHOP_BUY (Packet):
	pass
class GC_SYNC_MASK_WORD (Packet):
	pass
class CG_CANCEL_INTERACT (Packet):
	pass
class CG_CDKEY_APPLY (Packet):
	pass
class CG_REQ_GUILDCONVOY_FILL (Packet):
	pass
class GC_SYNC_LIFESKILLCOUNT (Packet):
	pass
class CG_REQ_TEAMMEMBER_APPLY_LEADER (Packet):
	pass
class GC_SYNC_REDPOINT_ONE (Packet):
	pass
class CG_THROW_ITEM (Packet):
	pass
class GC_SYNC_GAMECONFIG (Packet):
	pass
class GC_RET_CHANNELINFO (Packet):
	pass
class GC_GUILDMONSTER_STATE (Packet):
	pass
class GC_TEAM_CALLMEMBER (Packet):
	pass
class GC_CHANGENAME_RET (Packet):
	pass
class GC_NPCGIFTEXCHANGE_SYNC_STATUE (Packet):
	pass
class CG_DW_REQCAR (Packet):
	pass
class GC_SYNC_NPC_TITLE (Packet):
	pass
class GC_SWORDTEAM_RET_INFO (Packet):
	pass
class GC_CHALLENGE_REWARD (Packet):
	pass
class CG_BROTHERHOOD_ABDICANT (Packet):
	pass
class CG_BWPVPFINAL_ASKGOTOBIGWORLD (Packet):
	pass
class CG_SWORDTEAM_APPROVE_RESERVE (Packet):
	pass
class GC_CANCEL_INTERACT (Packet):
	pass
class GC_FLIGHT (Packet):
	pass
class CG_DONATE_BUILDING (Packet):
	pass
class GC_SYNC_SPECIAL_POISON_TIME (Packet):
	pass
class GC_BWPVPFINAL_RETGROUPINFO (Packet):
	pass
class GC_RES_JIANMUXB_HELP (Packet):
	pass
class CG_ASK_USE_FIREWORKS_ITEM (Packet):
	pass
class CG_REQ_PET_RENAME (Packet):
	pass
class CG_ASK_PAYACT (Packet):
	pass
class CG_REPLY_MFLY (Packet):
	pass
class CG_RET_RELIVESKILL (Packet):
	pass
class GC_FASHION_CHANGE (Packet):
	pass
class CG_CANCEL_MFLY (Packet):
	pass
class CG_MULPVP_ANSWER (Packet):
	pass
class GC_SYNC_SUPER_R_TIPS (Packet):
	pass
class GC_RET_EQUIP_REBIRTH_RECASE (Packet):
	pass
class GC_ADD_LOUDSPEAKER (Packet):
	pass
class CG_GUILDFIGHT_WORLDBOSS_PURIFY (Packet):
	pass
class GC_RET_FAIRY_LASTRECAST_INFO (Packet):
	pass
class GC_CHANGE_MAJORCITY_RET (Packet):
	pass
class GC_BWPVP_ROUND_RESULT (Packet):
	pass
class GC_GUILD_NEW_TISHI (Packet):
	pass
class CG_REQ_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM (Packet):
	pass
class GC_AUCTION_RETRECORD (Packet):
	pass
class CG_GUILD_CREATE (Packet):
	pass
class CG_TEAM_CALLMEMBER (Packet):
	pass
class GC_GIVESIGN_FORPIC (Packet):
	pass
class CG_FAIRY_RECAST_REPLACEATTR (Packet):
	pass
class GC_RET_USE_SKILL_XML (Packet):
	pass
class CG_UPDATE_AUTOCOMBAT (Packet):
	pass
class GC_FORCE_SETPOS (Packet):
	pass
class GC_TEAM_LEAVE (Packet):
	pass
class GC_SYN_SKILLCOUNT (Packet):
	pass
class CG_TOURNAMENT_REQ_INFO (Packet):
	pass
class GC_PLAY_SNARE_EFFECT (Packet):
	pass
class CG_CHANGE_ARMY_MEMBER_POSITION (Packet):
	pass
class GC_NOTICE_ADDED_FRIEND (Packet):
	pass
class GC_PRESTIGE_TODAYEXPLOITMAX (Packet):
	pass
class GC_SYNC_PET_ATTR (Packet):
	pass
class CG_MILITARY_REQ_EQUIPDONATE (Packet):
	pass
class GC_GUILD_RET_INFO (Packet):
	pass
class CG_REQ_EYESSTAR_TEN_TIMES (Packet):
	pass
class GC_ATTACKFLY (Packet):
	pass
class CG_TIANSHU_MASTER_INFO (Packet):
	pass
class CG_ASURA_GET_KEY_ITEM (Packet):
	pass
class CG_ChangeMentorDeclName (Packet):
	pass
class CG_SUBMIT_SAMSARA_PRE_ITEM (Packet):
	pass
class CG_ACHIEVEMENT_INFO (Packet):
	pass
class CG_PLAYSTORY_OVER (Packet):
	pass
class GC_HUILIU_STATE (Packet):
	pass
class GC_SYNC_HOME_DATA (Packet):
	pass
class CG_AUCTION_CANCELSELL (Packet):
	pass
class CG_AID_PUBLISH (Packet):
	pass
class CG_HOME_DEL_BLACK (Packet):
	pass
class GC_RET_HOME_FITMENT (Packet):
	pass
class GC_START_CAMERA_RESET (Packet):
	pass
class CG_CHANGE_HOME_NAME (Packet):
	pass
class CG_AID_RESOPNSE_CONFIG (Packet):
	pass
class CG_GODWEAPON_DECOMPOSE (Packet):
	pass
class CG_REQ_HOME_PRAY (Packet):
	pass
class CG_ASK_SUBSCIBE_DAY_BONUS (Packet):
	pass
class CG_REQ_HOME_HORDE_INFO (Packet):
	pass
class CG_COPYSCENE_HIDINGBOSS_OPEN_RET (Packet):
	pass
class CG_GUILD_DELTITLE (Packet):
	pass
class CG_GUILD_REQ_CANCELBUILD (Packet):
	pass
class CG_PGL_REQUEST_DAN_AWARD (Packet):
	pass
class GC_RET_GUILD_THIEF_ISACTIVE (Packet):
	pass
class CG_OPEN_RUBKI_CUBE_ACTIVITY (Packet):
	pass
class CG_FIRE_MERCENARY (Packet):
	pass
class CG_READ_XIAOYUE_TIPS (Packet):
	pass
class GC_MAKE_MFLY (Packet):
	pass
class CG_MENTOR_BUY_ITEM (Packet):
	pass
class GC_PGL_RESPONSE_DAN_AWARD (Packet):
	pass
class GC_COPYSCENE_HIDINGBOSS_SHOW_SELECT_OPEN_WINDOW (Packet):
	pass
class GC_NOTICE_MESSAGE (Packet):
	pass
class GC_GM_PRINT_DEBUG (Packet):
	pass
class CG_MOUNT_MOUNT (Packet):
	pass
class CG_UNLOCK_HOME_ZONE (Packet):
	pass
class GC_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF (Packet):
	pass
class GC_START_RUBKICUBE_PLAY (Packet):
	pass
class CG_MPFOODLIST_CHANGED (Packet):
	pass
class CG_AUCTION_ASKRECORD (Packet):
	pass
class CG_REQ_AUTO_DECOMPOSE (Packet):
	pass
class GC_GUILDFIGHT_WORLDBOSS_STATE (Packet):
	pass
class GC_START_CAMERA_MOVE (Packet):
	pass
class GC_PGL_SYNC_GROUP_INFO (Packet):
	pass
class GC_TODAY_FIRST_LOGIN (Packet):
	pass
class CG_BWPVPFINAL_ASKHELPMEMINFO (Packet):
	pass
class CG_REQ_WORLDBOSS_NUM (Packet):
	pass
class GC_PRESENT_DEL (Packet):
	pass
class CG_ASKTRACKPLAYER (Packet):
	pass
class CG_COPYSCENE_INVITE_RET (Packet):
	pass
class CG_UPDATE_COMMUNITY_REDDOT (Packet):
	pass
class GC_CREATE_PET (Packet):
	pass
class CG_ASKFOR_FRIENDMAXNUM (Packet):
	pass
class GC_COPYSCENE_BOSSTIME (Packet):
	pass
class CG_HONGBAO_ROB (Packet):
	pass
class GC_TELEMOVE (Packet):
	pass
class CG_REQ_ACCEPT_RECRUIT (Packet):
	pass
class CG_REQ_SYNC_HOME_COLLECTION (Packet):
	pass
class CG_REQ_CHANNELINFO (Packet):
	pass
class GC_MIDAS_RESPONSE_BUYGOODS (Packet):
	pass
class GC_PRESTIGE_TODAYWILDNUM (Packet):
	pass
class GC_SYNC_GODWEAPON_DATA (Packet):
	pass
class GC_DEATH_LETHAL_DAMAGE_LIST_INFO (Packet):
	pass
class CG_RESET_FAIRY_ATTR_POINTS (Packet):
	pass
class CG_SYNC_BOUNTY_ITEM_POS_LIST (Packet):
	pass
class CG_EQUIPMIRROR_PURIFY (Packet):
	pass
class GC_PRESTIGE_SYNCINFO (Packet):
	pass
class CG_REQ_ENTER_GUILD_WAR (Packet):
	pass
class GC_MILITARY_SYNC_LIMITINFO (Packet):
	pass
class GC_GET_GUILD_CONTRIBUTE (Packet):
	pass
class GC_RET_USE_SKILL (Packet):
	pass
class GC_REQ_APPRENTICE_CONFIGM_RECRUIT (Packet):
	pass
class CG_BWPVPVIEW_SETPOS (Packet):
	pass
class GC_RET_QQ_UNREG_FRIENDS (Packet):
	pass
class CG_FASHION_COLOR (Packet):
	pass
class GC_SYNC_BOUNTY_ITEM_POS_LIST (Packet):
	pass
class GC_FRIENDPOINTVALUE_REWARDSTATUS_UPDATE (Packet):
	pass
class GC_ISOPEN_SIGNINANDOLDLOGIN (Packet):
	pass
class CG_REPLY_INTERACT (Packet):
	pass
class CG_SPOKESMAN_GIVEGIFT (Packet):
	pass
class CG_TEAM_TARGET (Packet):
	pass
class CG_ASKFOR_FRIENDPOINTVALUE_REWARD (Packet):
	pass
class CG_SYSTEMTRADE_CANSELLLIST (Packet):
	pass
class GC_SYNC_REACHEDSCENE (Packet):
	pass
class GC_QIANKUNDAI_MAKE (Packet):
	pass
class CG_WAITPAY_REFUSE (Packet):
	pass
class GC_SYN_SKILLINFO (Packet):
	pass
class GC_CRAFTMAN_FORGE_RET (Packet):
	pass
class CG_SET_SOCIALUI_IS_NEEDTO_UPDATE (Packet):
	pass
class GC_PLAYCG (Packet):
	pass
class GC_RET_MIRROR_QUICKCOMPOND_RESULT (Packet):
	pass
class GC_UPDATE_TITLE (Packet):
	pass
class CG_SWORDTEAM_REQ_OTHERINFO (Packet):
	pass
class GC_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE (Packet):
	pass
class GC_DOMAIN_SYNC_DECLAREINFO (Packet):
	pass
class GC_GUILD_INVITE_CONFIRM (Packet):
	pass
class CG_HONGBAO_FESTIVAL_SEND (Packet):
	pass
class GC_GUILD_RET_CANCELBUILD (Packet):
	pass
class GC_RET_LASTRECAST_INFO (Packet):
	pass
class CG_MERCENARY_REQ (Packet):
	pass
class GC_UPDATE_PART_COMBATVAL (Packet):
	pass
class GC_GUILD_RET_SET_QUICKJOIN (Packet):
	pass
class GC_SYNC_EQUIP_REBIRTH_DATA (Packet):
	pass
class GC_MOUNT_MARK_RET (Packet):
	pass
class GC_RESIZE_FAIRY_PACK (Packet):
	pass
class GC_SYNC_GUILDCONVOY_CONVOY (Packet):
	pass
class CG_TAKE_CONVO (Packet):
	pass
class CG_BROTHERHOOD_CHANGE_NAME (Packet):
	pass
class CG_REQ_JIANMUXB_FILLING (Packet):
	pass
class CG_REQ_FORTUNE_EQUIP_UNEQUIP (Packet):
	pass
class GC_MOVE (Packet):
	pass
class CG_HUILIU_GOAL_GET_AWARD (Packet):
	pass
class GC_GUILDMONSTER_DANGERFISH (Packet):
	pass
class CG_REQ_HOME_HORDE_RENAME (Packet):
	pass
class GC_TOWER_BUY_RESULT (Packet):
	pass
class CG_ASK_LEVELREWARD (Packet):
	pass
class GC_GUILDCHECK_UPDATE (Packet):
	pass
class CG_DIG_TREASURE (Packet):
	pass
class CG_DIRECTIVE_INFO (Packet):
	pass
class CG_REQ_FIGHT_YUANLINGTUXI (Packet):
	pass
class CG_COMMONCOMMAND (Packet):
	pass
class GC_UPDATE_SKILLZHUANJING_ACTIVE_INFO (Packet):
	pass
class CG_JOIN_TEAM_INVITE_RESULT (Packet):
	pass
class CG_SWITCH_HOME_PLAN (Packet):
	pass
class CG_ASKCOLORCORRECTIONMAIL (Packet):
	pass
class GC_REMOVEEFFECT (Packet):
	pass
class CG_SHOW_HELMET (Packet):
	pass
class GC_CANCEL_MFLY (Packet):
	pass
class CG_ASKTRACKCHANGE (Packet):
	pass
class GC_PGL_RESPONSE_INFO (Packet):
	pass
class CG_ASK_CHRISTMASMONSTERLIST_DATA (Packet):
	pass
class CG_BROTHERHOOD_INVITE_BIRTHDAY (Packet):
	pass
class CG_DOMAIN_REQ_ENTERLINE (Packet):
	pass
class GC_PRESENT_NEW (Packet):
	pass
class GC_BROTHERHOOD_CHANGE_TITLE (Packet):
	pass
class GC_RET_ATTR_ADD_NOTICE (Packet):
	pass
class GC_SCENE_SPECIAL_OPERATE (Packet):
	pass
class CG_COMBATLIMITSHOP_BUY (Packet):
	pass
class CG_PRESENT_ADD (Packet):
	pass
class GC_BROTHERHOOD_INVITE_CONFIRM (Packet):
	pass
class GC_RET_GUILD_MONSTER_LASTTIME (Packet):
	pass
class CG_UPGRADE_PRACTICE_REQUEST (Packet):
	pass
class CG_MULPVP_INVITE (Packet):
	pass
class CG_BIGBATTLE_ENROLL (Packet):
	pass
class GC_WATERMELON_SYNC_COMBAT_STATUS (Packet):
	pass
class CG_REQ_FAIRY_NEIDAN_INLAY (Packet):
	pass
class GC_QTE_PLAY (Packet):
	pass
class CG_BROTHERHOOD_RECRUIT_APPLY_BY_PLAYERGUID (Packet):
	pass
class GC_SHEDAOSAIMA_GETDAOJU (Packet):
	pass
class CG_TIANSHUBOARD_INFO_SYNC (Packet):
	pass
class GC_PRESENT_RECEIVE (Packet):
	pass
class GC_SYNC_DAY_CARD (Packet):
	pass
class CG_MIDAS_REQUEST_BUYGOODS (Packet):
	pass
class CG_REQ_BOUNTY_CHANGE_SCENE (Packet):
	pass
class GC_ROLE_ONLINE (Packet):
	pass
class CG_BROTHERHOOD_RECRUIT_SETUP (Packet):
	pass
class GC_AUCTION_RETSELLLIST (Packet):
	pass
class GC_DISCONNECT_NOTIFY (Packet):
	pass
class CG_DOMAINWAR_REQ_DECLAREINFO (Packet):
	pass
class CG_SET_OR_MODIFY_SECPASSWORD (Packet):
	pass
class CG_TIANSHU_MASTER_LEVELUP (Packet):
	pass
class GC_FASHION_ADD (Packet):
	pass
class GC_EYECATCHING_NOTICE (Packet):
	pass
class GC_SCREDITSCORE_NOTICE (Packet):
	pass
class GC_CVFIREFLY_SYNC_MEMBER_DATA (Packet):
	pass
class GC_BUFF_CLEAR (Packet):
	pass
class CG_REQ_PAYACT_CONFIG_DATA (Packet):
	pass
class GC_GUILDWAR_MEMBER_BATTLE_INFO (Packet):
	pass
class GC_BWPVPFINAL_SHOWICON (Packet):
	pass
class GC_SYNC_RECENT_FINISH_ALL_ACHIEVEMENT_INFO (Packet):
	pass
class CG_RECEIVE_ACHIEVEMENT_REWARD (Packet):
	pass
class GC_SYC_FULL_APPLY_LIST (Packet):
	pass
class GC_RES_PET_RENAME (Packet):
	pass
class GC_SYNC_FIREWORKS_RANK_CONFIG (Packet):
	pass
class GC_SYNC_GEM_SLOT (Packet):
	pass
class GC_SAVE_HOME_PLAN (Packet):
	pass
class CG_SKILLZHUANJING_ACTIVE (Packet):
	pass
class CG_REQ_GUILD_ADDITION_LEVELUP (Packet):
	pass
class CG_ONCE_ITEM_DECOMPOSE (Packet):
	pass
class CG_GMCMDSTR (Packet):
	pass
class CG_BROTHERHOOD_CREATE_TRY (Packet):
	pass
class CG_GODWEAPON_QILING_LVUP (Packet):
	pass
class GC_RET_APPLY_LEADER_VOTE (Packet):
	pass
class CG_HOME_PRODUCE_EMPLOY (Packet):
	pass
class GC_SYNC_TEAM_MERCENARY (Packet):
	pass
class GC_IDIP_SYNC_BAN_CHAT_REASON (Packet):
	pass
class CG_ENTER_HOME (Packet):
	pass
class GC_SYNC_NATIONALDAY_TRIBUTE_CONFIG (Packet):
	pass
class GC_EXAM_UPDATESTATE (Packet):
	pass
class GC_SET_ISINPKATTACKLIST (Packet):
	pass
class GC_PRESTIGE_TODAYEXPLOIT (Packet):
	pass
class GC_ASK_COMMONFLAG_RET (Packet):
	pass
class GC_RET_MARRIAGE_DIVORCE (Packet):
	pass
class GC_CHAT_SYNC_BUBBLESTYLE (Packet):
	pass
class CG_ADD_FAIRY_PACK_SIZE (Packet):
	pass
class GC_SYNC_WAKEUP_DATA (Packet):
	pass
class GC_SHEDAOSAIMA_RET_USEDAOJU (Packet):
	pass
class GC_SYNC_EQUIP_SLOT_OPEN (Packet):
	pass
class GC_BROTHERHOOD_RECRUIT_MY (Packet):
	pass
class CG_DRAW_PHOTORANDOM_SHARE_GIFT (Packet):
	pass
class CG_SET_SELECT_PET (Packet):
	pass
class GC_RES_MIDSENDLANTERN (Packet):
	pass
class GC_BROTHERHOOD_INVITE_TITLE (Packet):
	pass
class GC_SYNC_PVPZOMBIE_MEMBERINFO (Packet):
	pass
class GC_GUILD_RET_SET_FULLACCEPT (Packet):
	pass
class GC_SYNC_SPECIAL_CIRTICAL_TIME (Packet):
	pass
class GC_UPDATE_FRIENDMAXNUM (Packet):
	pass
class GC_LOGIN_QUEUE_STATUS (Packet):
	pass
class CG_REQ_CANCEL_APPLICANT_TEAM (Packet):
	pass
class GC_PGL_FIGHT_RESULT (Packet):
	pass
class CG_ASK_RECOVER (Packet):
	pass
class CG_DEVICECLASSFY (Packet):
	pass
class GC_REQUEST_MFLY (Packet):
	pass
class GC_REFINE_RET_REFINEMETER (Packet):
	pass
class GC_MENTOR_SHOP_INFO (Packet):
	pass
class GC_RET_RANDOMNAMES (Packet):
	pass
class CG_AUCTION_SELL (Packet):
	pass
class GC_ASURA_SHOW_KILLINFO (Packet):
	pass
class GC_COPYSCENE_STATISTICS (Packet):
	pass
class GC_SYNC_MERCENARY_HP (Packet):
	pass
class GC_HOLIDAY_REDPOINT (Packet):
	pass
class GC_WAITPAY_NEW (Packet):
	pass
class GC_SYNC_GUILD_THITF_AWARD (Packet):
	pass
class CG_WISHING_REQUEST_DATA (Packet):
	pass
class GC_DOWNLOAD_VOICECHAT (Packet):
	pass
class GC_ASK_CONTINUE_CATCHGHOST (Packet):
	pass
class GC_RES_PET_LOCK (Packet):
	pass
class CG_EQUIP_RECASTINHERIT (Packet):
	pass
class GC_RET_ACTIVENESSINFO (Packet):
	pass
class CG_BUY_BLACKMARKETITEM (Packet):
	pass
class CG_ASK_BOUNTY_REFREST_STATE (Packet):
	pass
class GC_PLAY_WORLD_DARKNESS (Packet):
	pass
class CG_REQ_RANDOMNAMES (Packet):
	pass
class GC_UPDATE_XIUZHEN_COPYSCENE_DATA (Packet):
	pass
class GC_SYNC_FORTUNE_LEVEL_EXP (Packet):
	pass
class CG_ASK_WORLD_BOSS_STATE (Packet):
	pass
class CG_HONGBAO_CHARGE_SEND (Packet):
	pass
class CG_REQ_EYESSTAR (Packet):
	pass
class GC_RET_ADVENTURE_COMPLETED (Packet):
	pass
class CG_CHAT (Packet):
	pass
class GC_START_CATCHGHOST (Packet):
	pass
class GC_SYNC_PLAYER_HOMEGIFT_DATA (Packet):
	pass
class GC_SET_BLOCK_FRIENDAPPLY (Packet):
	pass
class CG_TAKE_ITEM_STORAGEPACK (Packet):
	pass
class CG_ASK_BACK_LOGIN_AWARD (Packet):
	pass
class GC_FRIENDSENDFLOWER (Packet):
	pass
class CG_BROTHERHOOD_CHANGE_TITLE (Packet):
	pass
class GC_SYNC_XIUZHEN_LEVEL_REWARD (Packet):
	pass
class GC_RELATION_OPTIONPANELINFO_RET (Packet):
	pass
class GC_BATTLEFIELD_LEAVE_BF (Packet):
	pass
class CG_SERVANT_REQOP (Packet):
	pass
class CG_REQ_TEAM_LEAVE (Packet):
	pass
class CG_RELATFRIEND_RECV_GIFT (Packet):
	pass
class GC_COPYSCENE_RESULT (Packet):
	pass
class CG_ASK_AUTOTEAM (Packet):
	pass
class CG_MULPVP_LEADEROPT (Packet):
	pass
class CG_EQUIP_RECAST (Packet):
	pass
class CG_STALL_ASKSELLLIST (Packet):
	pass
class CG_REQ_APPRENTICE (Packet):
	pass
class CG_GUILD_ALLIANCE_RESPONSE (Packet):
	pass
class CG_FASHION_COLOR_CHANGE (Packet):
	pass
class CG_YUANBAOSHOP_BUY (Packet):
	pass
class GC_TOWER_FIGHT_RESULT (Packet):
	pass
class CG_QUIT_GAME (Packet):
	pass
class CG_GUILD_REQ_CHANGE_ACTIVITY_NOTICE (Packet):
	pass
class GC_RETTRACKPLAYER (Packet):
	pass
class CG_REQ_YLTXINST_DES_REMAIN_NUM (Packet):
	pass
class GC_CLEAR_ITEMPACK_NEWLIST (Packet):
	pass
class GC_STOP_RUBKICUBE_SUB_PLAY (Packet):
	pass
class CG_SKILLZHUANJING_LEVEL_UP (Packet):
	pass
class CG_ASKFOR_RELATION_OPTIONPANELINFO (Packet):
	pass
class GC_COMBATLIMITSHOP_SYNC (Packet):
	pass
class GC_MISSION_STATE (Packet):
	pass
class CG_GUILD_APPROVE_RESERVE (Packet):
	pass
class GC_LOGIN_RET (Packet):
	pass
class GC_AUTO_TEAMFOLLOW_AFTER_KILLTARGET (Packet):
	pass
class GC_LOCK_CURTITLE (Packet):
	pass
class GC_UPDATEITEM (Packet):
	pass
class CG_REQ_WILDSCENEDUEL (Packet):
	pass
class GC_CHANGE_FAIRY_NAME_RET (Packet):
	pass
class CG_EQUIP_ENGRAVE (Packet):
	pass
class GC_SYNC_OTHERTEAMINFO (Packet):
	pass
class GC_NOTICE_PET_TAME (Packet):
	pass
class GC_REQUEST_SECOND_INTERACT (Packet):
	pass
class CG_ASURA_ENROLL (Packet):
	pass
class GC_RET_CHRISTMASMONSTERLIST_DATA (Packet):
	pass
class GC_BROTHERHOOD_RECRUIT_SYNC_APPLICANTS (Packet):
	pass
class GC_BATTLEFIELD_TOTAL_INFO (Packet):
	pass
class GC_SYNC_GROWTHUP_MARASARA_DATA (Packet):
	pass
class CG_GUILD_WAR_AGREE_SIGN_UP (Packet):
	pass
class CG_SET_MARRIAGE_PERSONAL_IDENTIFICATIONID (Packet):
	pass
class CG_ASK_COUPLE_BPCP_OPEN (Packet):
	pass
class GC_SYNC_EQUIP_ENGRAVE_DATA (Packet):
	pass
class CG_REQ_SCROLL_EXCHANGE (Packet):
	pass
class GC_RECOVERYFOODINFO_SYNC (Packet):
	pass
class CG_ADD_MIS_COUNT (Packet):
	pass
class CG_DELIVER_SCENE_POSITION (Packet):
	pass
class GC_GUILDWAR_POINT_INFO (Packet):
	pass
class CG_REQ_SET_GUILD_ADDITION (Packet):
	pass
class CG_ASK_COMMUNICATEWITHNPC (Packet):
	pass
class CG_FASHION_CHANGE (Packet):
	pass
class GC_OPEN_TIANSHUCHEST (Packet):
	pass
class CG_GET_REDPACKETRAIN_AWARD (Packet):
	pass
class CG_CRAFTSMAN_FORGE (Packet):
	pass
class CG_REQ_HOME_FORTUNE_TELLING (Packet):
	pass
class CG_GET_REFINE_QILING_AWARD (Packet):
	pass
class CG_NIEREN_SUPER (Packet):
	pass
class GC_RES_JIANMUXB_CLICKLINK (Packet):
	pass
class GC_MILITARY_SYNC_PINGMO (Packet):
	pass
class CG_SAVE_HOME_PLAN (Packet):
	pass
class GC_CREATE_CHRISTMAS_COLLECT_BOX (Packet):
	pass
class GC_SYNC_ARTIFACT_INFO (Packet):
	pass
class GC_FASHION_SHOW (Packet):
	pass
class GC_UPDATE_SKILL_LEVELUP_INFO (Packet):
	pass
class CG_ASK_GETREWARDFORSIGNIN_DAILY (Packet):
	pass
class GC_SYNC_ADD_DA_VALUE (Packet):
	pass
class GC_SYNC_FIRSTCHARGEFLAG (Packet):
	pass
class GC_MULPVP_INVITE_MEM (Packet):
	pass
class GC_SYNC_CHINESE_VALENTINE_DATA (Packet):
	pass
class GC_AUCTION_RETFAVORITE (Packet):
	pass
class GC_SYNC_PAYACT_DATA (Packet):
	pass
class CG_DOMAINSTATUE_REQ_KNEEL (Packet):
	pass
class CG_TIANSHU_MASTER_UNLOCK (Packet):
	pass
class GC_TIANSHU_COMPOSE (Packet):
	pass
class CG_ASK_BLACKMARKETITEMINFO (Packet):
	pass
class CG_REQ_NATIONALDAY_TRIBUTE_STATE (Packet):
	pass
class GC_HUILIULIMITSHOP_SYNC (Packet):
	pass
class GC_PLAYER_MOVETO (Packet):
	pass
class GC_SYNC_JIAZHEN_RUBKICUBE_INFO (Packet):
	pass
class GC_MISSION_PARAM (Packet):
	pass
class CG_PGL_REQUEST_INFO (Packet):
	pass
class GC_SyncShangGuEMoEnergy (Packet):
	pass
class GC_DROPITEM_INFO (Packet):
	pass
class CG_JUMP_REPORT (Packet):
	pass
class GC_SYNC_COMBATVALUE (Packet):
	pass
class GC_GUILDWAR_RESULT (Packet):
	pass
class GC_PGL_NOTICE_TEAM_JOIN (Packet):
	pass
class CG_DELE_HATEPEOPLEINFO (Packet):
	pass
class GC_BWPP_CONFIRMMATCH (Packet):
	pass
class GC_MISSION_ABANDON_RET (Packet):
	pass
class CG_NPCGIFTEXCHANGE_SEND_GIFT (Packet):
	pass
class GC_CHAT_PERSONAL (Packet):
	pass
class CG_WAITPAY_ADD (Packet):
	pass
class GC_COPYSCENE_DEATHNOTICE (Packet):
	pass
class GC_BUFF_SYNC_INFO (Packet):
	pass
class GC_RET_LIFESKILL_LEVELUP (Packet):
	pass
class GC_BATTLEFIELD_ACHIEVEMENT_UPDATE (Packet):
	pass
class CG_BROTHERHOOD_INVITE_JOIN (Packet):
	pass
class GC_UPDATE_ACHIEVEMENT_INFO (Packet):
	pass
class GC_CVFIREFLY_UPDATE_SCORE (Packet):
	pass
class CG_ASKCHANGETOELITENPC (Packet):
	pass
class CG_ASK_COPYSCENE_STATISTICS (Packet):
	pass
class CG_REQ_MILITARY_EXCHANGE (Packet):
	pass
class CG_WEDDING_EXIT (Packet):
	pass
class GC_PLAYER_LEVELUP_MANUAL_RET (Packet):
	pass
class GC_RET_AUTOTEAM (Packet):
	pass
class GC_SEARCH_ACTOR (Packet):
	pass
class CG_REQ_CHANGENAME (Packet):
	pass
class CG_BATTLEFIELD_ENTER (Packet):
	pass
class CG_MISSION_COMMIT (Packet):
	pass
class CG_PRESTIGESHOPBUYITEM (Packet):
	pass
class GC_BROTHERHOOD_INVITE_JOIN (Packet):
	pass
class GC_GROUPPHOTO_REPONSE (Packet):
	pass
class CG_REQ_SKILLSOUL_GET (Packet):
	pass
class GC_RECENT_FINISH_ACHIEVEMENT_INFO (Packet):
	pass
class GC_REFINETRANS_CONFIRM_RET (Packet):
	pass
class GC_FASHION_RANDOM_COLOR_RET (Packet):
	pass
class GC_AUCTION_RETBUY (Packet):
	pass
class GC_MERCENARY_EMPLOYLIST (Packet):
	pass
class CG_SEND_FLOWER (Packet):
	pass
class CG_ASK_MERGE_INSCRP0TION (Packet):
	pass
class CG_REQ_ARMY_CHANGE_RTROLE_NOTICE_LEADER (Packet):
	pass
class GC_RECHARGESCORESHOP_SYNC (Packet):
	pass
class GC_SYNC_SCROLL_EXCHANGE_DATA (Packet):
	pass
class CG_HOME_PRODUCE_OPERA (Packet):
	pass
class GC_SWORDTEAM_RET_OTHERINFO (Packet):
	pass
class GC_YINZHEN_LEVELUP (Packet):
	pass
class CG_SWORDTEAM_CREATE (Packet):
	pass
class GC_SWORDTEAM_JOIN (Packet):
	pass
class GC_DOMAINWAR_DECLAREINFO (Packet):
	pass
class CG_REQUEST_INTERACT (Packet):
	pass
class CG_ASK_CHANGESKILLBAR (Packet):
	pass
class CG_REQ_JOIN_GUILD_REALTIME_VOICE_ROOM (Packet):
	pass
class CG_STALL_ASKINFO (Packet):
	pass
class CG_GUILD_REQ_QUICKJOIN (Packet):
	pass
class CG_REQ_FORTUNE_EQUIP_FEED (Packet):
	pass
class CG_AID_PUBLISH_CONFIG (Packet):
	pass
class CG_LEAVE_COPYSCENE (Packet):
	pass
class GC_SHEDAISAIMA_RET_PLAYERAPPLYMATCH (Packet):
	pass
class GC_SYNC_GUILDCONVOY_FILL (Packet):
	pass
class GC_JUBAOPLAYER_RET (Packet):
	pass
class CG_GUILD_SEND_GROUP_MSG (Packet):
	pass
class GC_RET_RELATFRIEND_SEND_GIFT (Packet):
	pass
class GC_CHALLENGE_HISTORY (Packet):
	pass
class CG_CHANGE_TO_NEXT_RUBKI_CUBE (Packet):
	pass
class CG_SWORDTEAM_KICK (Packet):
	pass
class GC_DAMAGEBOARD_INFO (Packet):
	pass
class GC_COMPOUND_GEM_RET (Packet):
	pass
class GC_PLAY_BULLET_EFFECT (Packet):
	pass
class CG_BATTLEFIELD_CANCEL_SIGNUP (Packet):
	pass
class CG_FLY_LAND (Packet):
	pass
class GC_PUSH_RECOMMOND_FRIEND_LIST (Packet):
	pass
class CG_SWORDTEAM_LEAVE (Packet):
	pass
class CG_REQ_COMBATVALUE (Packet):
	pass
class CG_MAIL_OPERATION (Packet):
	pass
class GC_COPYSCENE_LEFTIME (Packet):
	pass
class CG_EQUIP_LEVELUP (Packet):
	pass
class CG_NOTIFY_SHARE_EVENT (Packet):
	pass
class GC_SET_SELECT_PET (Packet):
	pass
class GC_FLY_AIRCRAFT_MARK_RET (Packet):
	pass
class CG_REQ_CANCEL_CUTOF_MENTOR (Packet):
	pass
class GC_MERGE_INSCRP0TION_RESEPONSE (Packet):
	pass
class CG_REQ_GUILDMONSTER_DANGERFISH (Packet):
	pass
class GC_BATTLEFIELD_PLAYER_UPDATE (Packet):
	pass
class GC_SYNC_COUNTRESETINFO (Packet):
	pass
class CG_ASK_PASSPORT_REWARD (Packet):
	pass
class GC_UPDATE_GUILD_BINGGROUP_STATE (Packet):
	pass
class CG_GUILD_REQ_INFO (Packet):
	pass
class GC_AUTO_COMMIT_GUILD_MONSTER_ITEM (Packet):
	pass
class CG_SWORDTEAM_JOIN (Packet):
	pass
class GC_FINDPLAYER (Packet):
	pass
class CG_ASK_USE_SWEEP_ITEM (Packet):
	pass
class CG_REQ_SYNC_HOME (Packet):
	pass
class CG_GUILD_KICK (Packet):
	pass
class GC_GUILD_BUILDING_CD (Packet):
	pass
class CG_BROTHERHOOD_INVITE_TITLE (Packet):
	pass
class CG_GUILD_REQ_THIEF_FIGHT (Packet):
	pass
class GC_RES_AUCTION_FAVORITE_LOOK (Packet):
	pass
class CG_REQ_GUILDCONVOY_MAP_POS (Packet):
	pass
class CG_GUILD_REQ_LEVELUP (Packet):
	pass
class GC_SYN_DIRTY_MENTOR_INFO (Packet):
	pass
class CG_DOMAINWAR_REQ_LINEINFO (Packet):
	pass
class GC_SYNC_PHONE_BIND_DATA (Packet):
	pass
class CG_EQUIPMIRROR_QUICK_COMPOUND (Packet):
	pass
class GC_EMOTION_LOCKINFO (Packet):
	pass
class GC_STALL_RETSELLLIST (Packet):
	pass
class GC_CUTSCENE_PLAY (Packet):
	pass
class CG_STALL_BUY (Packet):
	pass
class GC_PGL_SYNC_TEAM_MEM_INFO (Packet):
	pass
class GC_RET_TEAMMEMBER_APPLY_LEADER (Packet):
	pass
class CG_OPEN_RUBKI_CUBE_PLAY (Packet):
	pass
class GC_SYC_FRIEND_INFO (Packet):
	pass
class CG_BEGIN_AIRBUS (Packet):
	pass
class CG_PUT_COLOR_ITEM_STORAGE (Packet):
	pass
class GC_WEDDING_SYNC_INFO (Packet):
	pass
class GC_BWPPCOMBAT_RESULT (Packet):
	pass
class CG_REQUEST_ARMYLEADER_POSITION (Packet):
	pass
class CG_ARTIFACT_PROVE_REWARD (Packet):
	pass
class GC_RET_PK_KILLINFO (Packet):
	pass
class CG_SYSTEMTRADE_BUY (Packet):
	pass
class GC_RES_MARRAY_RECURIT (Packet):
	pass
class GC_EQUIPMIRROR_RET_RESULT (Packet):
	pass
class GC_UPDATE_ANIMATION_STATE (Packet):
	pass
class CG_ADD_HATEPEOPLE (Packet):
	pass
class CG_BATTLEFIELD_REQ_FIGHTDATA (Packet):
	pass
class CG_TOURNAMENT_ENTER_LOBBY (Packet):
	pass
class CG_BROTHERHOOD_RECRUIT_APPLY (Packet):
	pass
class CG_SET_BATTLE_FAIRY (Packet):
	pass
class GC_MARRIAGE_SYNC (Packet):
	pass
class GC_ANSWER_WORLD_BOSS_STATE (Packet):
	pass
class CG_USE_CHILDRENSDAY_BALLON (Packet):
	pass
class GC_FASHION_PAIR_SAVE_RET (Packet):
	pass
class GC_REQ_APPRENTICE_CONFIGM_TEACHER (Packet):
	pass
class GC_STALL_RETSEARCH (Packet):
	pass
class CG_REQ_GUILD_THIEF_ISACTIVE (Packet):
	pass
class GC_SHOW_KILLINFO_VIEW (Packet):
	pass
class CG_ACCLOGIN_GETAWARD (Packet):
	pass
class CG_GUILD_REQ_ENTER_GUILD_WILD (Packet):
	pass
class CG_MERCENARY_LIST_REQ (Packet):
	pass
class GC_MARRIAGE_PROCESS (Packet):
	pass
class CG_REQ_MATCH_OP (Packet):
	pass
class GC_NOTICE_CATCHGHOST_NEED_ASSEMBLE (Packet):
	pass
class GC_SWORDTEAM_CREATE (Packet):
	pass
class CG_REQ_ARMY_INVITE (Packet):
	pass
class CG_REQ_EXCHANGE_CHOOSEREWARDBOX (Packet):
	pass
class CG_SWORDTEAM_INVITE (Packet):
	pass
class GC_SYNC_ADVENTURE_EVENT_HISTORY (Packet):
	pass
class GC_TIANSHU_BACKPACK_INFO (Packet):
	pass
class CG_DELRECENTCONTACTLIST (Packet):
	pass
class GC_LOUDSPEAKER_USE (Packet):
	pass
class GC_ITEMCOMPENSATE_SYNCINFO (Packet):
	pass
class CG_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF (Packet):
	pass
class CG_REQ_HOME_PRAY_ATTR_GIVEUP (Packet):
	pass
class CG_GUILD_REQ_CHANGE_JOBNAME (Packet):
	pass
class CG_BATTLEFIELD_REQ_SIGNUPLIST (Packet):
	pass
class CG_REQ_APPOINT_OPEN_PLAYER_GZONE (Packet):
	pass
class GC_PGL_TEAM_REQ_FAILED (Packet):
	pass
class GC_SYNC_FORTUNE_EQUIP (Packet):
	pass
class CG_ITEM_MERGE (Packet):
	pass
class CG_ASK_SYN_FAIRY_PACK (Packet):
	pass
class CG_SKILL_USE (Packet):
	pass
class GC_ASK_PAYACT_RET (Packet):
	pass
class CG_LUCKY_CONNECT_DRAW_AUTO (Packet):
	pass
class CG_ACCLOGIN_ASKSTATUS (Packet):
	pass
class CG_FLY_AIRCRAFT_MARK (Packet):
	pass
class CG_REQ_GUILD_REALTIME_VOICE_ROOM_INFO (Packet):
	pass
class GC_NOTICE (Packet):
	pass
class CG_UNBIND_GUILDGROUP (Packet):
	pass
class GC_SYNC_WXSUPERR_PRIVILEGE (Packet):
	pass
class CG_ASK_FIREWORKS_AWARD (Packet):
	pass
class CG_ASKOTHEROLE_VIEWINFO (Packet):
	pass
class GC_TOWER_INFO (Packet):
	pass
class CG_BATTLEFIELD_LEAVE (Packet):
	pass
class GC_TRIGGER (Packet):
	pass
class GC_PRESTIGE_RET_GETREWARD (Packet):
	pass
class GC_ASURA_RESULT_UI (Packet):
	pass
class GC_CAMERA_COLORMASK_OPERATE (Packet):
	pass
class CG_REQ_FORTURE_EQUIP_GENERATE (Packet):
	pass
class CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_TYPE (Packet):
	pass
class GC_SYNC_HOME_ATTRIBUTE (Packet):
	pass
class CG_GETFLYMISREWARD (Packet):
	pass
class GC_BWPVPFINAL_UPDATEFINALSTATE (Packet):
	pass
class GC_SWORDTEAM_RET_LIST (Packet):
	pass
class GC_RET_APPOINT_OPEN_PLAYER_GZONE (Packet):
	pass
class CG_ASK_COLLECT (Packet):
	pass
class GC_OPERATE_AIRWALL (Packet):
	pass
class GC_START_AUTOCOMBAT (Packet):
	pass
class GC_OPTUI (Packet):
	pass
class GC_UI_NEWGUIDE (Packet):
	pass
class GC_TEAM_TARGET (Packet):
	pass
class CG_RELATFRIEND_SEND_GIFT (Packet):
	pass
class CG_ENTER_SCENE_OK (Packet):
	pass
class CG_COPYSCENE_NAVIGATION (Packet):
	pass
class GC_REBATE_RANKCONFIG (Packet):
	pass
class CG_REQ_CHANGEPROFESSION (Packet):
	pass
class GC_GUILDCONVOY_GMCMD (Packet):
	pass
class CG_GODWEAPON_COORDINATION (Packet):
	pass
class GC_CREATE_SKILL_ENTITY (Packet):
	pass
class GC_BATTLEFIELD_GROUPSCORE_UPDATE (Packet):
	pass
class CG_ASK_JXGZAWARD (Packet):
	pass
class CG_FASHION_SHOW (Packet):
	pass
class GC_RES_UPDATE_AUCTION_ONE (Packet):
	pass
class GC_BWPVPFINAL_MEMINFOINVIEW (Packet):
	pass
class CG_SKILLZHUANJING_WASH (Packet):
	pass
class GC_CREATE_CUTSCENE_TRIGGER (Packet):
	pass
class GC_SYNC_EQUIP_ENCHANTING_DATA (Packet):
	pass
class GC_STOP_SOUND (Packet):
	pass
class CG_ENTER_CATCHGHOST (Packet):
	pass
class GC_BROTHERHOOD_MY (Packet):
	pass
class GC_RELEASE_FAIRY_RET (Packet):
	pass
class GC_TOURNAMENT_SYNC_MATCH_RESULT (Packet):
	pass
class CG_GUILD_REQ_CHANGE_NOTICE (Packet):
	pass
class CG_ASK_SELOBJ_INFO (Packet):
	pass
class CG_ADD_FAIRY_ATTR_POINTS (Packet):
	pass
class CG_REQ_CHANGE_SCENE_SEAMLESS (Packet):
	pass
class CG_MISSION_SPECIALOPERATE (Packet):
	pass
class GC_COUPLEBP_SUCCESSCOUNT_SYNC (Packet):
	pass
class GC_APIFIXACTIONSTR_FORQCLOUDPIC (Packet):
	pass
class CG_CACHELOG (Packet):
	pass
class CG_REQ_SWITCH_PET_FIGHT_STATE (Packet):
	pass
class GC_SYNC_DAMAGE_SHOW_HP (Packet):
	pass
class GC_DIRECTIVE_INFO (Packet):
	pass
class CG_REQ_RECOMMEND_MEMBER_INFO (Packet):
	pass
class GC_BOSSDIE_NOTICE (Packet):
	pass
class GC_RES_GUILD_JIANMUXB_LIST (Packet):
	pass
class CG_SKILLLEVUP_RECOMMEND (Packet):
	pass
class GC_SYC_FRIEND_STATE (Packet):
	pass
class GC_SYN_SKILLZHUANJINGINFO (Packet):
	pass
class GC_SYNC_AUTOTEAM_BW (Packet):
	pass
class GC_AUCTION_RETSELLINFO (Packet):
	pass
class GC_WISHING_RESPONSE_DATA (Packet):
	pass
class CG_BROTHERHOOD_MY (Packet):
	pass
class GC_CVFIREFLY_SYNC_RESULT (Packet):
	pass
class GC_SERVANT_SYNC_KIZUNA (Packet):
	pass
class CG_AUCTION_REVIEW_ASK (Packet):
	pass
class GC_RES_GUILDCONVOY_MAP_POS (Packet):
	pass
class GC_FLY_DATA (Packet):
	pass
class CG_RECHARGESCORESHOP_REQ (Packet):
	pass
class GC_UPDATE_IMMORTAILTY_INFO (Packet):
	pass
class CG_REQ_GET_SIQINGREDENVELOPE (Packet):
	pass
class GC_TOURNAMENT_TEAM_REQ_FAILED (Packet):
	pass
class GC_CDTIME_UPDATE (Packet):
	pass
class CG_REQ_DEL_HOME_HORDE_COLLECTION (Packet):
	pass
class CG_GUILD_CHANGETITLE (Packet):
	pass
class GC_ADD_GUILDLOUDSPEAKER (Packet):
	pass
class CG_GWSKILL_HELP (Packet):
	pass
class CG_FELLOWTEAMMEMBER (Packet):
	pass
class CG_CHANGE_SCENE_INST (Packet):
	pass
class CG_USE_ITEM (Packet):
	pass
class GC_DOMAIN_HISTORYLIST (Packet):
	pass
class GC_NEAR_PLAYERLIST (Packet):
	pass
class GC_SYNC_QQVIP_DATA (Packet):
	pass
class CG_STATICSYSTEMSHOP_SELL (Packet):
	pass
class GC_SYNC_DANCE_INFO (Packet):
	pass
class CG_ASK_CHANGEPKMODE (Packet):
	pass
class CG_ASK_COPYPLAYERINFO (Packet):
	pass
class CG_REPORT_TOGM (Packet):
	pass
class CG_ADDAPPLYLIST (Packet):
	pass
class GC_SYNC_REGION_HOME_NUM (Packet):
	pass
class CG_QIANKUNDAI_MAKE (Packet):
	pass
class CG_REQ_GUILDCONVOY_FILLINFO (Packet):
	pass
class CG_REBATE_ASKFORBONUS (Packet):
	pass
class GC_NIEREN_CHANGE (Packet):
	pass
class GC_BWPP_GROUP_CHANGED (Packet):
	pass
class GC_ADDFRIEND (Packet):
	pass
class GC_SYNC_SUBSCIBE_INFO (Packet):
	pass
class GC_ADDRECENTCONTACTLIST (Packet):
	pass
class CG_REQ_GUILDAUCTION_INFO (Packet):
	pass
class GC_HONGBAO_ROB (Packet):
	pass
class GC_RECEIVEFLOWER_PLAYEFFECT (Packet):
	pass
class CG_ASK_FIREWORKS_DATA (Packet):
	pass
class CG_ARMY_LEADER_CALL_MEMBER (Packet):
	pass
class CG_WEDDING_ASKINFO (Packet):
	pass
class GC_KEEP_ROTATE (Packet):
	pass
class GC_LIMITSHOP_SYNC (Packet):
	pass
class GC_USE_DIRECTSENDGIDT (Packet):
	pass
class GC_NPCGIFTEXCHANGE_GET_AWARD (Packet):
	pass
class CG_SET_GUILD_ACTIVITY_OPEN_TIME (Packet):
	pass
class CG_REPLACE_ENCHANT_RESULT (Packet):
	pass
class GC_ISINSELFHATEPEOPLELIST (Packet):
	pass
class CG_FASHION_RANDOM_COLOR_COMFIRM (Packet):
	pass
class GC_TONGTIANTREASURE_SYNC (Packet):
	pass
class CG_REQ_CUTOF_MENTOR (Packet):
	pass
class GC_BROADCAST_YLTX (Packet):
	pass
class GC_RESET_FAIRY_ATTR_POINTS_RET (Packet):
	pass
class CG_BREAKCURSKILL (Packet):
	pass
class GC_MILITARY_SYNC_REPUTATION (Packet):
	pass
class CG_GUILD_REQ_WORSHIP_CHIEFMODEL (Packet):
	pass
class GC_SYN_MENTOR_INFO (Packet):
	pass
class GC_XIANDAN_EQUIP_RET (Packet):
	pass
class GC_PET_FLY_STATE (Packet):
	pass
class CG_ASKFORPIC_SIGN (Packet):
	pass
class GC_RET_GUILDLOG (Packet):
	pass
class CG_DEATH_ASKFOR_LETHAL_DAMAGE_LIST (Packet):
	pass
class GC_SYNC_ENERMYPOS (Packet):
	pass
class CG_QUEST_CHANGETOBIGWORLD (Packet):
	pass
class GC_BATTLEFIELD_FLAG_UPDATE (Packet):
	pass
class GC_PGL_SYNC_RANK (Packet):
	pass
class CG_REQ_HOME_PRAY_CHANGE_ATTR (Packet):
	pass
class GC_PLAY_ANIMATION (Packet):
	pass
class CG_ASK_SETCOMMONFLAG (Packet):
	pass
class CG_STALL_ASKRECORD (Packet):
	pass
class GC_SYNC_PERSONALREBATE (Packet):
	pass
class CG_GUILD_APPROVE_ALLRESERVE (Packet):
	pass
class CG_NEATEN_ITEMPACK (Packet):
	pass
class GC_REPLY_PASSPORT_DATA (Packet):
	pass
class CG_CHANGE_ARMY_MEMBER_BIAOJI (Packet):
	pass
class GC_SYN_COLOR_ITEM_STORAGE (Packet):
	pass
class GC_RET_CHAT_PLAYERINFO (Packet):
	pass
class CG_BWPVPFINAL_ASKMEMINFOINVIEW (Packet):
	pass
class GC_SYNC_DIRTY_KIT_PACK (Packet):
	pass
class GC_ACTIVITYNOTICE (Packet):
	pass
class CG_DOMAINWARSHOP_BUY (Packet):
	pass
class GC_WAITPAY_PAY (Packet):
	pass
class CG_STALL_ASKITEM_SELLINFO (Packet):
	pass
class CG_TOWER_FIGHT (Packet):
	pass
class CG_RANDOM_OPPONENT (Packet):
	pass
class GC_SWEEP_REWARD (Packet):
	pass
class CG_GUILD_DISMISS (Packet):
	pass
class CG_REQ_HOME_SETTLE (Packet):
	pass
class GC_BWPVPFINAL_HELPMEMINFO (Packet):
	pass
class CG_DOMAINWAR_OP (Packet):
	pass
class CG_BOUNTY_PICK_ITEM_NPC (Packet):
	pass
class GC_PA_OPERATE_REQUEST (Packet):
	pass
class CG_REQ_FAIRY_NEIDAN_FORGET (Packet):
	pass
class GC_INFINITEDREAMLAND_INFO (Packet):
	pass
class GC_BATTLEFIELD_CANCEL_SIGNUP (Packet):
	pass
class GC_SYC_FULL_FRIEND_LIST (Packet):
	pass
class CG_ASK_ZHUGUO_INFO (Packet):
	pass
class GC_SYNC_EQUIP_REBIRTH_RECASE_INFO (Packet):
	pass
class GC_JOIN_TEAM_INVITE (Packet):
	pass
class GC_BANGHUA_CAGE_INFO (Packet):
	pass
class CG_MIS_QIYU_REVIEW (Packet):
	pass
class CG_PRESTIGE_ASK_GETREWARD (Packet):
	pass
class CG_BROTHERHOOD_AGREE_JOIN (Packet):
	pass
class CG_CLIENT_TRIGGER_FRIENDS_MUTUALHELP (Packet):
	pass
class CG_LIMITSHOP_REQ (Packet):
	pass
class GC_ARMY_COPYSCENE_INVITEVIEW (Packet):
	pass
class GC_IDIP_ROLL_NOTICE (Packet):
	pass
class GC_RESPONSE_RECHARGE (Packet):
	pass
class GC_SYNC_RECHARGE_DATA (Packet):
	pass
class CG_REQ_GUILDCONVOY_NEXT_POINT (Packet):
	pass
class GC_SNARESTATE_BROADCAST (Packet):
	pass
class GC_RET_RELIVE (Packet):
	pass
class CG_HONGBAO_ASK_UPDATE (Packet):
	pass
class CG_GUILD_GRANTTITLE (Packet):
	pass
class GC_RESPONSE_ZHUGUO_INFO (Packet):
	pass
class GC_SYNC_GROWWAY_INFO (Packet):
	pass
class GC_FLY_LANDING (Packet):
	pass
class GC_HOME_SYNC_PERMISSION_DATA (Packet):
	pass
class CG_GUILDFIGHT_WORLDBOSS_ASK_SOULS (Packet):
	pass
class GC_NOTIF_WORLDBOSS_STRIVE (Packet):
	pass
class GC_UPDATE_BATTLE_FAIRY (Packet):
	pass
class GC_SYNC_KXJFAWARDTABLE (Packet):
	pass
class CG_BUY_CHALLENGE_TIMES (Packet):
	pass
class GC_TIANSHUBOARD_SETUP (Packet):
	pass
class CG_SEARCH_ACTOR (Packet):
	pass
class GC_ACCLOGIN_SYNCSTATUS (Packet):
	pass
class CG_REQ_SAMSARA_PRE_DATA (Packet):
	pass
class CG_ITEM_DECOMPOSE (Packet):
	pass
class CG_REQ_PART_COMBATVAL (Packet):
	pass
class CG_BWPVPFINAL_ASKVIEW (Packet):
	pass
class CG_ASK_INLAY_INSCRIPTION (Packet):
	pass
class CG_REQ_FORTUNE_EQUIP_EQUIP (Packet):
	pass
class GC_CHANGE_STEWARD_NAME (Packet):
	pass
class CG_SYNC_PLAYER_AREA_INFO (Packet):
	pass
class GC_SYN_CHARGE_COUNT_INFO (Packet):
	pass
class GC_FAIRY_RAISE_SYNC_FEED_TIME (Packet):
	pass
class CG_ASK_AUTOTEAM_BW (Packet):
	pass
class CG_CHANGE_MAJORCITY (Packet):
	pass
class CG_STOP_KIT_PACK (Packet):
	pass
class GC_ADDBLACKLIST (Packet):
	pass
class CG_ASK_ELITENPCCREATECD (Packet):
	pass
class GC_STOP_RUBKICUBE_PLAY (Packet):
	pass
class GC_STALL_RETINFO (Packet):
	pass
class GC_DOMAINWAR_UPDATECAR (Packet):
	pass
class GC_RETENEMYMEMINFO (Packet):
	pass
class CG_REQ_GUILDCONVOY_CALL_LINE (Packet):
	pass
class CG_PK_DIE_HELP_FOR_GUILD (Packet):
	pass
class CG_LUCKY_CONNECT_DRAW (Packet):
	pass
class GC_SWORDTEAM_INVITE_CONFIRM (Packet):
	pass
class GC_SELECT_ROLE_RET (Packet):
	pass
class GC_RET_YLTX_POS (Packet):
	pass
class GC_STALL_SYNC (Packet):
	pass
class CG_REQ_QUIT_GUILD_REALTIME_VOICE_ROOM (Packet):
	pass
class GC_AID_PUBLISH_CONFIG (Packet):
	pass
class CG_BWPVPFINAL_ASKGROUPINFO (Packet):
	pass
class CG_ASK_PERSONALREBATE (Packet):
	pass
class GC_ACHIEVEMENT_REWARD_INFO (Packet):
	pass
class GC_MULPVP_ANSWERLISTINFO (Packet):
	pass
class GC_TEAM_RET_ACCEPT (Packet):
	pass
class CG_PUBLISH_MENTOR_MESSAGE (Packet):
	pass
class CG_REQ_SCROLL_EXCHANGE_DATA (Packet):
	pass
class CG_TOWER_FIGHT_NEXT (Packet):
	pass
class GC_FASHION_PROLONG_RET (Packet):
	pass
class CG_REQ_JIANMUXB_HELP (Packet):
	pass
class GC_GUILD_UPDATE_AUTHORITY (Packet):
	pass
class CG_ITEMCOMPENSATE_GET (Packet):
	pass
class GC_SYC_FULL_RECENTCONTACT_LIST (Packet):
	pass
class GC_GUILD_JOIN (Packet):
	pass
class GC_RET_WORLDBOSS (Packet):
	pass
class CG_REQ_QINYOU_FRIEND (Packet):
	pass
class CG_REQ_ACCEPT_TEACHER (Packet):
	pass
class CG_GODWEAPON_EQUIP (Packet):
	pass
class GC_ZHENFA_LEVELUP (Packet):
	pass
class CG_LOGIN (Packet):
	pass
class GC_RET_RECEIVE_GUILD_GIFTPACKAGE (Packet):
	pass
class GC_EQUIP_ENGRAVE_RESULT (Packet):
	pass
class GC_SPOKESMAN_SYNC_INFO (Packet):
	pass
class CG_REQ_LUCKY_CONNECT_SYNC (Packet):
	pass
class CG_ARMY_LEADER_RESET_COPYSCENE (Packet):
	pass
class CG_ASK_BUY_EXCITEM (Packet):
	pass
class GC_ORIENTATION_CHANGE (Packet):
	pass
class CG_REQ_FRIEND_USERINFO (Packet):
	pass
class CG_REQ_CHAT_PLAYERINFO (Packet):
	pass
class GC_COPYSCENE_NAVIGATION (Packet):
	pass
class CG_BROTHERHOOD_LEAVE (Packet):
	pass
class GC_STOP (Packet):
	pass
class GC_UPDATE_CIRCLEDATA (Packet):
	pass
class GC_ACHIEVEMENT_VALUE_INFO (Packet):
	pass
class GC_ADD_FAIRY_ATTR_POINTS_RET (Packet):
	pass
class GC_PRESENT_ADD (Packet):
	pass
class CG_HOME_MANAGER_GUSET (Packet):
	pass
class GC_PLAYERTIPSCHANGE (Packet):
	pass
class CG_STALL_SELLINFO (Packet):
	pass
class GC_EXAM_ANSWERRESULT (Packet):
	pass
class CG_WEDDING_CLOSE (Packet):
	pass
class GC_GWSKILL_SHOWHELP (Packet):
	pass
class CG_WISHING_REQUEST_LOTTERY (Packet):
	pass
class GC_FLY_FASTSPEED_RET (Packet):
	pass
class CG_REQ_GUILD_CHANGE_AUTOJOINSET (Packet):
	pass
class CG_ASK_CDTIME (Packet):
	pass
class GC_REBATE_STEPCONFIG (Packet):
	pass
class GC_UPDATE_FAIRY_FORMATION (Packet):
	pass
class CG_REQ_CHANGE_FAIRY_VISUAL (Packet):
	pass
class GC_ASURA_TIME_SYNC (Packet):
	pass
class GC_WAITPAY_DEL (Packet):
	pass
class GC_SYNC_JXGZAWARDTABLE (Packet):
	pass
class GC_CHANGESCENE_DYNAMICLEVEL (Packet):
	pass
class GC_SYNC_PAYACT_CONFIG_DATA (Packet):
	pass
class CG_SHEDAOSAIMA_ASK_USEDAOJU (Packet):
	pass
class CG_SKILL_SWITCH_TYPE_SKILL (Packet):
	pass
class CG_AUCTION_ASKSELLLIST (Packet):
	pass
class GC_RET_RELATFRIEND_STATUS (Packet):
	pass
class CG_ASK_CHRISTMAS_DATA (Packet):
	pass
class CG_UPLOAD_CUSTOMHEAD_SUCCESS (Packet):
	pass
class GC_SYNC_LEVELUP_RED_POINT (Packet):
	pass
class CG_ZHENFA_LEVELUP (Packet):
	pass
class CG_BUILD_BUILDING (Packet):
	pass
class CG_HOME_SET_GUEST_PERMISSION (Packet):
	pass
class CG_AUCTION_SELLINFO (Packet):
	pass
class GC_UPDATE_FAIRY (Packet):
	pass
class GC_BROTHERHOOD_INVITE_BIRTHDAY (Packet):
	pass
class GC_READY_CONFIRM_RET (Packet):
	pass
class CG_EQUIPMIRROR_PURIFY_REPLACEATTR (Packet):
	pass
class GC_USE_SKILL_XML_MainPlayer (Packet):
	pass
class GC_BATTLEFIELD_RES_UPDATE (Packet):
	pass
class GC_SYNC_HOME_PRAY_ATTR (Packet):
	pass
class CG_TONGTIANTREASURE_REQOP (Packet):
	pass
class CG_FASHION_RANDOM_COLOR (Packet):
	pass
class GC_FAIRY_USE_SKILL (Packet):
	pass
class CG_HUILIU_STATE (Packet):
	pass
class CG_GUILDMONSTER_UNLOCK (Packet):
	pass
class GC_SUCCESS_BP_COUPLE (Packet):
	pass
class GC_SYNC_XCTJAWARDTABLE (Packet):
	pass
class GC_UPDATE_SKILLZHUANJING_UNLOCK_INFO (Packet):
	pass
class CG_REQ_HOME_HORDE_COLLECTION (Packet):
	pass
class GC_RET_WORLD_GROUPINFO (Packet):
	pass
class GC_GUILD_RET_SETADDITION_TIME (Packet):
	pass
class CG_REQ_USE_GUILD_FLAG (Packet):
	pass
class CG_MOVE (Packet):
	pass
class CG_NOTIFY_ARMY_CHANGE_RTMEMBERINFO (Packet):
	pass
class GC_RET_ADVENTURE_ACCEPT (Packet):
	pass
class GC_MERCENARY_LIST_RES (Packet):
	pass
class CG_SWORDTEAM_INVITE_CONFIRM (Packet):
	pass
class GC_CANCEL_AUTOCOMBAT (Packet):
	pass
class CG_REQUEST_SECOND_INTERACT (Packet):
	pass
class CG_CVFIREFLY_REQ_SIGNUP (Packet):
	pass
class CG_CLEAN_TEAM_APPLICANTLIST (Packet):
	pass
class CG_BROTHERHOOD_RECRUIT_LIST (Packet):
	pass
class GC_RET_SHOWRECHARGE (Packet):
	pass
class GC_ADDAPPLYLIST (Packet):
	pass
class CG_HOME_SET_PERMISSION (Packet):
	pass
class CG_TEAM_CALLMEMBER_RESULT (Packet):
	pass
class CG_GUILD_REQ_WELFARE (Packet):
	pass
class CG_REPLY_SECOND_INTERACT (Packet):
	pass
class CG_SKILLZHUANJING_OPEN (Packet):
	pass
class GC_GUILD_LEAVE (Packet):
	pass
class GC_STALL_REVIEW_ADD (Packet):
	pass
class GC_SHEDAISAIMA_PLAYERRACEHLINE (Packet):
	pass
class GC_SYNC_GODWEAPON_PACK (Packet):
	pass
class GC_RET_EXCHANGE_GUILD_MONSTER_BUFF (Packet):
	pass
class GC_SYNC_IOS_REVIEW_EVENT (Packet):
	pass
class CG_NPCGIFTEXCHANGE_SYNC_STATUE (Packet):
	pass
class GC_SYNC_INSCRIPTION_SLOT_DATA (Packet):
	pass
class CG_GUILD_JOIN (Packet):
	pass
class GC_PLAY_SOUND (Packet):
	pass
class CG_REQ_NEAR_LIST (Packet):
	pass
class GC_BATTLEFIELD_STATE (Packet):
	pass
class CG_PICK_COLOR_ITEM_STORAGE (Packet):
	pass
class CG_UPDATE_XIAOK_REDDOT (Packet):
	pass
class GC_SYNC_GUILD_REAMTIME_VOICEROOM_MEMBERINFO (Packet):
	pass
class CG_REQ_EQUIP_ENCHANT (Packet):
	pass
class CG_PUT_CONVO (Packet):
	pass
class GC_NOTIFY_CHANGETOBIGWORLD (Packet):
	pass
class GC_SYNC_IDIP_REDDOT_TIPS (Packet):
	pass
class GC_BROTHERHOOD_CREATE_TRY (Packet):
	pass
class GC_SYNC_RUBKICUE_ENERGY_COUNT (Packet):
	pass
class GC_GUILD_RET_LIST (Packet):
	pass
class GC_LEVELUP_BUILDING (Packet):
	pass
class CG_REQ_MARRAY_RECURIT (Packet):
	pass
class GC_SKILL_FINISH (Packet):
	pass
class GC_DOMAINWAR_SCENENINFO (Packet):
	pass
class CG_PGL_REQ_MATCH (Packet):
	pass
class CG_ZHENFA_UNLOCK (Packet):
	pass
class CG_RET_ROLE_SHARE_DATA (Packet):
	pass
class GC_PRESTIGE_TODAYWILDNUMMAX (Packet):
	pass
class CG_REQ_CLEAR_HOME_GIFT (Packet):
	pass
class CG_THANKSTEAMLEADERBOX_USE (Packet):
	pass
class CG_MISSION_ACCEPT (Packet):
	pass
class CG_CHAT_PERSONAL (Packet):
	pass
class GC_SYNC_FREE_HOME_SETTLE (Packet):
	pass
class CG_REQ_JIANMUXB_INFO (Packet):
	pass
class CG_GODWEAPON_USESKILL (Packet):
	pass
class CG_GUILD_REQ_LEAVE_GUILD_WILD (Packet):
	pass
class CG_HUILIULIMITSHOP_BUY (Packet):
	pass
class GC_SEND_FAIRY_EGG_RESULT (Packet):
	pass
class CG_PUBLISH_HOME_LINK (Packet):
	pass
class GC_RES_JIANMUXB_REWARD (Packet):
	pass
class CG_ASK_COMMIT_GUILD_MONSTER_ITEM (Packet):
	pass
class GC_AIRBUS_DATA (Packet):
	pass
class GC_RET_MIRRORLASTPURIFY_INFO (Packet):
	pass
class CG_ADDFRIEND (Packet):
	pass
class CG_WISHING_UPDATE_SELECTED_STATUS (Packet):
	pass
class CG_PASSPORT_BUY_LEVEL (Packet):
	pass
class CG_EQUIP_RECAST_REPLACEATTR (Packet):
	pass
class GC_RET_FAIRY_EVOLVE (Packet):
	pass
class GC_MAIL_DELETE (Packet):
	pass
class GC_CLIENT_RELIVE (Packet):
	pass
class GC_GODWEAPON_SYNC_CD (Packet):
	pass
class CG_GET_WORDREDPACKETRAIN_AWARD (Packet):
	pass
class GC_SECPASSWORD_CLIENTINFO (Packet):
	pass
class GC_GUILD_ASK_DIG_UP_THE_HATCHET (Packet):
	pass
class GC_COPYSCENE_EXITEFFECT (Packet):
	pass
class CG_BATTLEFIELD_SIGNUP (Packet):
	pass
class CG_DOMAIN_REQ_DECLAREWAR (Packet):
	pass
class GC_GUILD_RET_LEVELUPFINISH (Packet):
	pass
class GC_SYNC_FIRST_ENTERCOPYSCENE (Packet):
	pass
class GC_CREATE_ZOMBIEPLAYER (Packet):
	pass
class GC_BEGIN_CHOOSE_REWARDBOX (Packet):
	pass
class GC_PRAYEXP_SYNC (Packet):
	pass
class GC_DEBUGSYNCPOS (Packet):
	pass
class CG_REBATE_ASKINFO (Packet):
	pass
class CG_REQ_HOME_REGION_INFO (Packet):
	pass
class CG_HUILIULIMITSHOP_REQ (Packet):
	pass
class GC_REMIND_SET_OR_INPUT_SECPASSWORD (Packet):
	pass
class CG_REQ_RESET_HOME_STYLE (Packet):
	pass
class CG_GUILD_REQ_STOP_DEMISE (Packet):
	pass
class GC_STALL_RETRECORD (Packet):
	pass
class GC_STALL_APPEAL (Packet):
	pass
class GC_ACCLOGIN_SYNCINFO (Packet):
	pass
class GC_SYNC_GUILD_ACTIVITY_OPEN_TIME (Packet):
	pass
class GC_SHEDAOSAIMA_USEDAOJUMESSAGE (Packet):
	pass
class GC_FLY_AIRCRAFTCOLLECTED_FLAG (Packet):
	pass
class CG_QUEST_CHANGETO_ORIGINWORLD (Packet):
	pass
class CG_REQ_GUILD_WAR_SIGN_UP (Packet):
	pass
class CG_GUILD_INVITE_CONFIRM (Packet):
	pass
class GC_SYNC_FRIENDS_MUTUALHELP_DATA (Packet):
	pass
class GC_RES_JIANMUXB_FILLING (Packet):
	pass
class CG_REQ_SHOWRECHARGE (Packet):
	pass
class CG_ACCPET_IMMORTALITY_WAY_REWARD (Packet):
	pass
class GC_NPC_PAOPAOCHAT (Packet):
	pass
class GC_REQ_ARMY_CHANGE_RTROLE (Packet):
	pass
class GC_SYNC_MIS_QIYU_INFO (Packet):
	pass
class CG_FAIRY_SKILL_LEVEL_UP (Packet):
	pass
class CG_REQUEST_MFLY (Packet):
	pass
class CG_FAIRY_RECAST (Packet):
	pass
class CG_ITEMCOMPENSATE_REQ (Packet):
	pass
class CG_GUILD_GET_CREATEGROUP_MONEY (Packet):
	pass
class GC_SYSTEMTRADE_BUY (Packet):
	pass
class CG_COPYSCENE_SET_DONTNPCDORP (Packet):
	pass
class CG_REQ_CHANGEINST (Packet):
	pass
class GC_STALL_RETITEM_SELLINFO (Packet):
	pass
class CG_ASK_GETREWARDFORSIGNIN (Packet):
	pass
class GC_CAMERA_LOCK (Packet):
	pass
class GC_GUILDLOG_RET (Packet):
	pass
class CG_ASK_WILDSCENEDUELINFO (Packet):
	pass
class CG_REQ_FAIRY_EVOLVE (Packet):
	pass
class GC_WEATHER (Packet):
	pass
class CG_MOUNT_UNMOUNT (Packet):
	pass
class CG_MISSION_PICK_ITEM (Packet):
	pass
class GC_RET_PICKUP_ITEM (Packet):
	pass
class CG_SYSTEMTRADE_ASKSELLLIST (Packet):
	pass
class GC_RET_GUILDWAR_HISTROY_RANK_INFO (Packet):
	pass
class GC_COMMONACTIVITYINFO_USEITEM (Packet):
	pass
class GC_SYNC_XIUZHEN_PRACTICE_DATA (Packet):
	pass
class GC_TARGET_ALREADYHASTEAM (Packet):
	pass
class GC_NEAR_TEAMLIST (Packet):
	pass
class GC_SYNC_CHRISTMAS_DATA (Packet):
	pass
class GC_SYNC_QIANZHUANG_DATA (Packet):
	pass
class GC_SYNC_SHARE_GAME_DATA (Packet):
	pass
class GC_UPDATEACTIVITY_POINT (Packet):
	pass
class CG_RECOMMEND_FRIEND (Packet):
	pass
class CG_NIEREN_CHANGE (Packet):
	pass
class GC_REQ_CHANGETOBIGWORLD (Packet):
	pass
class GC_SYNC_IMMORTALITY_INFO (Packet):
	pass
class CG_ASK_ACTIVENESSINFO (Packet):
	pass
class GC_NIEREN_SUPER (Packet):
	pass
class CG_START_CATCHGHOST (Packet):
	pass
class CG_YINZHEN_LEVELUP (Packet):
	pass
class CG_GUILD_REQ_ENTER_GUILD_CITY (Packet):
	pass
class GC_SYNC_XIAOYUE_TIPS (Packet):
	pass
class GC_RET_WILDSCENEDUELINFO (Packet):
	pass
class GC_DOMAINSTATUE_RET_KNEEL (Packet):
	pass
class GC_SYNSELTRAGET_ATTR (Packet):
	pass
class GC_WAITPAY_REFUSE (Packet):
	pass
class CG_GWSKILL_STARTSKILL (Packet):
	pass
class CG_CANCEL_SECPASSWORD (Packet):
	pass
class GC_RECASTINHERIT_GUIDE_RET (Packet):
	pass
class CG_MISSION_ABANDON (Packet):
	pass
class CG_STATICSYSTEMSHOP_BUY (Packet):
	pass
class GC_SYNC_COMMONDATA64 (Packet):
	pass
class GC_MOUNTCOLLECTED_FLAG (Packet):
	pass
class GC_BROTHERHOOD_CREATE_FAILED (Packet):
	pass
class GC_REQ_MASTER_CONFIGM_APPRENTICE (Packet):
	pass
class GC_EQUIP_ENCHANT_RESULT (Packet):
	pass
class CG_UPDATE_LOGIN_STATUS (Packet):
	pass
class CG_BROTHERHOOD_APPROVE_APPLY (Packet):
	pass
class CG_ACCRECHARGE_REQUEST_DATA (Packet):
	pass
class CG_WORLDBOSS_FIGHT (Packet):
	pass
class GC_RET_MIS_QIYU_HISTORY (Packet):
	pass
class GC_GET_HONORCOIN (Packet):
	pass
class GC_GIVESIGN_FORPICDETECTION (Packet):
	pass
class GC_SYNC_PET_BASE_INFO (Packet):
	pass
class GC_MERCENARY_LEFTTIMES (Packet):
	pass
class CG_ASK_RANK (Packet):
	pass
class GC_WISHING_REQUEST_LOTTERY_RESULT (Packet):
	pass
class GC_SYNC_OTHERTEAMINFOATTR (Packet):
	pass
class CG_REQUIRE_PLAT_FORM_MESSAGE (Packet):
	pass
class GC_UPDATE_NEEDIMPACTINFO (Packet):
	pass
class CG_REQ_CHANGEPROFESSIONCONDITIONINFO (Packet):
	pass
class CG_REQ_GET_HOMEGIFT (Packet):
	pass
class GC_NOTICE_WARPATH_FULL (Packet):
	pass
class GC_SYN_COOLDOWN_LAYER_INFO (Packet):
	pass
class GC_CLOSE_BLACKMARKET (Packet):
	pass
class CG_SHEDAISAIMA_PLAYERFIRM (Packet):
	pass
class CG_REQUEST_EXCHANGE_CURRENCY (Packet):
	pass
class CG_DOWNLOAD_VOICECHAT (Packet):
	pass
class CG_OBCELEBRATION_WISH_AWARD (Packet):
	pass
class CG_GUILD_REQ_LIST (Packet):
	pass
class CG_CHALLENGERANKLIST_REQ (Packet):
	pass
class CG_COMMONACTIVITYINFO_REQUSEITEMINFO (Packet):
	pass
class GC_SESSION (Packet):
	pass
class GC_KICK_OUT_NOTICE (Packet):
	pass
class GC_SYS_PRESTIGEREWARDINFO (Packet):
	pass
class CG_COMPOUND_GEM (Packet):
	pass
class CG_MISSION_PARAM (Packet):
	pass
class GC_TGCFAWARD_DATA (Packet):
	pass
class CG_VERIFYCODE_INPUT (Packet):
	pass
class CG_OPEN_COPYSCENE (Packet):
	pass
class CG_TGLOG_CLIENT_BEHAVIOR (Packet):
	pass
class GC_DELIVER_FINISH (Packet):
	pass
class GC_TSS_ANTI_SEND_DATA (Packet):
	pass
class GC_PLAT_FORM_MESSAGE (Packet):
	pass
class CG_NEW_PLAYER_BEHAVIOR_UI (Packet):
	pass
class GC_SYNC_DESTINY_ATTRIBUTE (Packet):
	pass
class CG_ASK_PLAYERAPPLYMATCH (Packet):
	pass
class GC_RES_QINGYIVALUE_DAILY_INFO (Packet):
	pass
class CG_LIFESKILL_MAKE (Packet):
	pass
class GC_SYNC_REDPOINT (Packet):
	pass
class CG_SiQingRedPacket_TLOG (Packet):
	pass
class CG_TEAM_HANREN (Packet):
	pass
class CG_RESET_RUBKI_CBE_ACTIVITY (Packet):
	pass
class GC_REQUEST_ARMYLEADER_POSITION_RET (Packet):
	pass
class GC_MIDAS_QUERY_SUBSCRIBE (Packet):
	pass
class CG_REQ_CHANGE_SCENE_TELEPORT (Packet):
	pass
class GC_SYNC_GUILDCONVOY_STATE (Packet):
	pass
class CG_MIDAS_QUERY_SUBSCRIBE (Packet):
	pass
class GC_UPDATE_CHAR_IMPACT_INFO (Packet):
	pass
class GC_SYNC_REDPACKETRAIN_INFO (Packet):
	pass
class CG_GUILD_REQ_CHANGEAUTHORITY (Packet):
	pass
class CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE (Packet):
	pass
class GC_OPERATE_SCENE_BUILDING (Packet):
	pass
class CG_ARMY_COPYSCENE_INVITEVIEW_RET (Packet):
	pass
class GC_DEL_GATHER_POINT (Packet):
	pass
class CG_BROTHERHOOD_DELETE_RECRUIT_APPLY (Packet):
	pass
class CG_REQUEST_SWTICH_HOME_EXTERIOR (Packet):
	pass
class GC_RET_HATEPEOPLEINFO (Packet):
	pass
class GC_GUILD_CREATE (Packet):
	pass
class GC_PLAY_TIMESCALE (Packet):
	pass
class GC_RET_GETREWARDFORSIGNIN_DAILY (Packet):
	pass
class CG_GUILD_REQ_LEAVE_GUILD_CITY (Packet):
	pass
class GC_PLAYER_PAOPAOCHAT (Packet):
	pass
class GC_QUIT_GAME_RET (Packet):
	pass
class CG_WATERMELON_GET_KEY_ITEM (Packet):
	pass
class GC_REQ_ROLE_SHARE_DATA (Packet):
	pass
class GC_UNLOCK_HOME_ZONE (Packet):
	pass
class CG_ASK_HATEPEOPLEINFO (Packet):
	pass
class GC_SYNC_AUTOTEAM_BW_NUMBER (Packet):
	pass
class CG_MOUNT_MARK (Packet):
	pass
class CG_USE_MIDSENDLANTERN (Packet):
	pass
class GC_SYNC_TGCFAWARDTABLE (Packet):
	pass
class GC_HideModel (Packet):
	pass
class GC_SYNC_RUBKICUBE_SCENE_INFO (Packet):
	pass
class GC_SYNC_RUBKICUBE_AWAY_INFO (Packet):
	pass
class GC_CHALLENGERANKLIST (Packet):
	pass
class GC_REBATE_STEPDATA (Packet):
	pass
class GC_RET_SELOBJ_INFO (Packet):
	pass
class CG_ASK_FORDETECTION_SIGN (Packet):
	pass
class GC_PLAYSTORY (Packet):
	pass
class CG_ITEM_COMPOUND (Packet):
	pass
class GC_XCTJAWARD_DATA (Packet):
	pass
class GC_GUILDFIGHT_WORLDBOSS_SOUL (Packet):
	pass
class CG_GODWEAPON_STUNT_LVUP (Packet):
	pass
class CG_MULPVP_AGREEAGAIN (Packet):
	pass
class GC_PROMOTE_FRIENDMAXNUM_RET (Packet):
	pass
class GC_SYNC_IOS_REVIEW_GUILD_DATA (Packet):
	pass
class GC_SET_ORMODIFY_SECPASSWORD_SUCCESS (Packet):
	pass
class GC_STALL_RETBUY (Packet):
	pass
class CG_READY_CONFIRM (Packet):
	pass
class CG_NATIONALDAY_TRIBUTE_HAND_IN (Packet):
	pass
class GC_RET_ARTIFACT_PROVE_REWARD (Packet):
	pass
class CG_AUCTION_LOOK (Packet):
	pass
class CG_SYSTEMTRADE_SELL (Packet):
	pass
class GC_MSG_BOX (Packet):
	pass
class GC_EXIT_COPY_SCENE_ENVIROMENT (Packet):
	pass
class CG_CHANGE_FAIRY_NAME (Packet):
	pass
class CG_WEDDING_OPEN_FEAST (Packet):
	pass
class GC_ISHATEPEOPLEONLINE (Packet):
	pass
class GC_UPDATE_HOME_PRODUCE_STATE (Packet):
	pass
class GC_SYNC_PAPER_TIPS (Packet):
	pass
class CG_BOSS_PICK_ITEM (Packet):
	pass
class CG_REQ_RECEIVE_GUILD_GIFTPACKAGE (Packet):
	pass
class GC_GUILD_WAR_SYNC_SIGN_UP_MEMBERS (Packet):
	pass
class GC_STOP_LIGHTNING_EFFECT (Packet):
	pass
class GC_GUILD_ROBBERS_RANK (Packet):
	pass
class GC_EQUIPMIRROR_FORGE_INFO (Packet):
	pass
class GC_WEDDING_RETINFO (Packet):
	pass
class GC_ITEMSCRIPT_RET (Packet):
	pass
class CG_COMMONACTIVITYINFO_USEITEM (Packet):
	pass
class CG_MULPVP_ANSWER_MEM (Packet):
	pass
class CG_GUILDLOG_REQ (Packet):
	pass
class GC_TEAM_SYNC_MEMBERINFO (Packet):
	pass
class CG_ZHENFA_SELECT (Packet):
	pass
class CG_REQ_GUILD_JIANMUXB_LIST (Packet):
	pass
class CG_REQ_BUY_HOME_GIFT (Packet):
	pass
class CG_COMBATLIMITSHOP_REQ (Packet):
	pass
class GC_SYNC_FIREWORKS_CONFIG (Packet):
	pass
class GC_PLAYCOUNTDOWNEFFECT (Packet):
	pass
class GC_SHOW_HELMET (Packet):
	pass
class CG_HPFOODLIST_CHANGED (Packet):
	pass
class GC_RET_SELFROLEVIEWINFO (Packet):
	pass
class GC_FACETOLOOKPOINT (Packet):
	pass
class GC_RET_WORLDBOSS_NUM (Packet):
	pass
class CG_ASK_QUITFOLLOW (Packet):
	pass
class GC_RET_GUILD_THIEF_NUM (Packet):
	pass
class CG_SECPASSWORD_RELEASELOCK (Packet):
	pass
class CG_REQ_YLTX_SCENELIST (Packet):
	pass
class CG_REQ_JIANMUXB_REWARD (Packet):
	pass
class GC_NOTICE_PLAYER_AUTOTEAM_TIMEOUT (Packet):
	pass
class CG_REQ_ACCEPT_APPRENTICE_TASK (Packet):
	pass
class CG_PANDORA_TLOG (Packet):
	pass
class GC_RES_PET_FEED (Packet):
	pass
class GC_SYNC_HOME_HORDE_SHOP (Packet):
	pass
class CG_TRIGGER (Packet):
	pass
class CG_REQ_SET_PET_AUTO_FEED (Packet):
	pass
class GC_JOIN_TEAM_REQUEST (Packet):
	pass
class GC_BROTHERHOOD_RECRUIT_LIST (Packet):
	pass
class GC_FORCE_STOP_JUMP (Packet):
	pass
class GC_GUILDAUCTION_ATTEND_INFO (Packet):
	pass
class GC_DOMAIN_RET_DECLAREWAR (Packet):
	pass
class GC_MERGE_FAIRY_RET (Packet):
	pass
class GC_SYNC_RUBKICUBE_REWARD_COUNT (Packet):
	pass
class GC_ACTIVITYMULTI_SYNC (Packet):
	pass
class CG_REQ_ENTER_HOME_SHOWROOM (Packet):
	pass
class GC_SEND_IMPACT (Packet):
	pass
class CG_SKILL_WASH (Packet):
	pass
class CG_TIANSHUBOARD_SETUP (Packet):
	pass
class GC_LUCKY_CONNECT_ACTIVE_DATA (Packet):
	pass
class GC_SYNC_LEVELREWARDINFO (Packet):
	pass
class CG_FRIENDS_MUTUALHELP_TLOG (Packet):
	pass
class GC_PRESENT_WAITPAY_SYNC (Packet):
	pass
class CG_REQ_GUILDLOG (Packet):
	pass
class GC_DOMAINWAR_RESULT (Packet):
	pass
class CG_EQUIP_INHERIT (Packet):
	pass
class CG_REQ_MARRIAGE_DIVORCE (Packet):
	pass
class GC_UPDATE_SKILL_UNLOCK_INFO (Packet):
	pass
class CG_LOCK_FAIRY (Packet):
	pass
class CG_TELEPORT_INSCENE (Packet):
	pass
class CG_REQ_HOME_INFO_HORDE (Packet):
	pass
class CG_CUTSCENE_PLAYOVER (Packet):
	pass
class CG_OPERATE_SCENE_BUILDING (Packet):
	pass
class GC_GET_ITEM (Packet):
	pass
class GC_KXJFAWARD_DATA (Packet):
	pass
class CG_USE_ITEM_PETAGG (Packet):
	pass
class GC_GUILDFIGHT_WORLDBOSS_RANK (Packet):
	pass
class GC_SKILLBAR_EXTRA_CD (Packet):
	pass
class GC_BROADCAST_ATTR (Packet):
	pass
class GC_SYNC_BIGBATTLE_TIMES (Packet):
	pass
class CG_GUILD_REQ_CHANGENAME (Packet):
	pass
class CG_ASK_SUBSCIBE_INFO (Packet):
	pass
class GC_TIANSHU_DECOMPOSE (Packet):
	pass
class GC_COPYSCENE_COMBATSTATE (Packet):
	pass
class CG_MIS_OPERATE_NPC (Packet):
	pass
class GC_GET_EXP (Packet):
	pass
class GC_GET_XX (Packet):
	pass
class GC_PLAY_EFFECT (Packet):
	pass
class GC_RET_ADVENTURE_EVENT_COMPLETED (Packet):
	pass
class CG_FASHION_RANDOM_COLOR_CHANGE (Packet):
	pass
class GC_SyncXueChiState (Packet):
	pass
class CG_SET_BLOCK_FRIENDAPPLY (Packet):
	pass
class CG_CHANGE_TITLE (Packet):
	pass
class GC_MISSION_IGNOREMISPREFLAG (Packet):
	pass
class CG_ACCEPT_XIUZHEN_LEVEL_REWARD (Packet):
	pass
class GC_UPDATE_PRODUCE_OBJ_DATA (Packet):
	pass
class CG_XIUZHEN_INCREASE (Packet):
	pass
class CG_MILITARY_REQ_GET_BADGE (Packet):
	pass
class CG_REQ_GUILD_THIEF_NUM (Packet):
	pass
class GC_RET_PKNOTICE (Packet):
	pass
class GC_SPOKESMAN_SYNC_DIALOGUE (Packet):
	pass
class GC_SYNC_SKILL_LAYER_CD (Packet):
	pass
class CG_SKILL_ACTIVE (Packet):
	pass
class CG_REQ_GUILDWAR_HISTROY_RANK_INFO (Packet):
	pass
class CG_FAIRY_RAISE_ACTION (Packet):
	pass
class GC_PLAY_BULLET_IN_CONFIG (Packet):
	pass
class GC_RET_GUILD_ADDITION (Packet):
	pass
class GC_REPLY_YIRONG_CARD (Packet):
	pass
class CG_REQUEST_BUY_HOME_EXTERIOR (Packet):
	pass
class GC_RET_SIGNININFO (Packet):
	pass
class CG_REQ_ACCEPT_APPRENTICE (Packet):
	pass
class CG_ASK_KXJFAWARD (Packet):
	pass
class CG_MISSION_STATE (Packet):
	pass
class GC_CHAT (Packet):
	pass
class CG_DELFRIEND (Packet):
	pass
class CG_LOCK_FAIRY_SKILL (Packet):
	pass
class GC_GODWEAPON_EQUIP (Packet):
	pass
class GC_BIGWORLDPVP_PRE_RET_LIST (Packet):
	pass
class GC_ENTER_COPY_SCENE_ENVIROMENT (Packet):
	pass
class CG_REQ_FAIRY_NEIDAN_LEVELUP (Packet):
	pass
class GC_MENTOR_BUY_RESULT (Packet):
	pass
class GC_RET_GUILDCONVOY_CONFIRM (Packet):
	pass
class CG_UNEQUIP_ITEM (Packet):
	pass
class CG_REQ_TEAM_JOIN (Packet):
	pass
class CG_ASKENEMYMEMINFO (Packet):
	pass
class GC_BREAK_LIFESKILL_PREOCESS (Packet):
	pass
class GC_OFFLINE_CHAT_PERSONAL (Packet):
	pass
class GC_RES_SET_PET_AUTO_FEED (Packet):
	pass
class CG_STALL_SELL (Packet):
	pass
class CG_STALL_SEARCH (Packet):
	pass
class GC_MAKE_INTERACT (Packet):
	pass
class GC_SYNC_COMMONFLAG (Packet):
	pass
class CG_SKILL_LEVEL_UP (Packet):
	pass
class GC_UPDATE_XIUZHEN_PRACTICE_DATA (Packet):
	pass
class GC_SWITCH_HOME_PLAN (Packet):
	pass
class CG_ACCRECHARGE_REQUEST_BONUS (Packet):
	pass
class CG_OPERATE_GEM (Packet):
	pass
class CG_USE_CHILDRENSDAY_TRANSFORMER (Packet):
	pass
class CG_REQ_GUILDCONVOY_CONFIRM (Packet):
	pass
class CG_REQ_LIFESKILL_LEVELUP (Packet):
	pass
class GC_ASK_RELIVESKILL (Packet):
	pass
class GC_INTERACT_JUMP (Packet):
	pass
class GC_SYNC_FIREWORKS_DATA (Packet):
	pass
class GC_SYNCFLYMISREWARD (Packet):
	pass
class CG_SEARCHSDKCHECK_GUILD (Packet):
	pass
class GC_BATTLEFIELD_REWARD (Packet):
	pass
class CG_DELBLACKLIST (Packet):
	pass
class GC_BUY_NIEREN_SUPER (Packet):
	pass
class GC_RET_REPLACE_EQUIP_REBIRTH_RECASE_TRICK (Packet):
	pass
class GC_CREATE_ROLE_RET (Packet):
	pass
class GC_TOURNAMENT_SYNC_INFO (Packet):
	pass
class GC_SYSTEMTRADE_RETSELLLIST (Packet):
	pass
class CG_USE_CONVO_CD_SKILL_TRIGER (Packet):
	pass
class CG_REQ_CV_MARRIAGE_GIFT (Packet):
	pass
class GC_CHALLENGE_MYDATA (Packet):
	pass
class CG_DELE_WILDSCENEDUELINFO (Packet):
	pass
class GC_CHAR_FACEDIR (Packet):
	pass
class CG_LEAVE_HOME_SCENE (Packet):
	pass
class GC_GUILD_ON_BANGHUA_ACTIVE (Packet):
	pass
class GC_RES_GUILDAUCTION_INFO (Packet):
	pass
class GC_STALL_RETLOOK (Packet):
	pass
class GC_SYNC_WORDREDPACKETRAIN_INFO (Packet):
	pass
class GC_SYNC_ACHIEVEMENT_INFO (Packet):
	pass
class CG_BIGWORLDPVP_PRE_REQ_LIST (Packet):
	pass
class GC_BATTLEFIELD_RESULT (Packet):
	pass
class CG_WAITPAY_PAY (Packet):
	pass
class CG_ADDRECENTCONTACTLIST (Packet):
	pass
class GC_UPDATE_XIUZHEN_LEVEL_REWARD (Packet):
	pass
class GC_SYNC_RECHARGEDOUBLE (Packet):
	pass
class CG_REQ_BUY_HOME_HORDE_SHOP (Packet):
	pass
class GC_SYNC_SAMSARA_PRE_DATA (Packet):
	pass
class CG_BROTHERHOOD_TEAMUP (Packet):
	pass
class CG_REQ_SHARE_GAME_DATA (Packet):
	pass
class GC_TOWER_FIGHT_TIME (Packet):
	pass
class GC_TOURNAMENT_SYNC_BATTLE_RESULT (Packet):
	pass
class CG_REQ_UPDATE_AUCTION_ONE (Packet):
	pass
class CG_HOLIDAY_REDPOINT_REQ (Packet):
	pass
class GC_MOVABLE_STORAGEPACK_INFO (Packet):
	pass
class CG_GATHER_POINT (Packet):
	pass
class CG_PA_OPERATE_RESPONSE (Packet):
	pass
class CG_UPDATE_SUPERR_REDDOT (Packet):
	pass
class GC_UPDATE_SKILL_ACTIVE_INFO (Packet):
	pass
class GC_SYSTEMTRADE_SELL (Packet):
	pass
class GC_BANGHUA_SYNCSCORE (Packet):
	pass
class CG_STALL_LOOK (Packet):
	pass
class GC_GWSKILL_ASKHELP (Packet):
	pass
class CG_ASK_SAMSARA_PRE_REWARD (Packet):
	pass
class GC_SYNC_SURVEY_INFO (Packet):
	pass
class GC_SYNC_KIT_PACK (Packet):
	pass
class CG_FLY_FLY (Packet):
	pass
class CG_PRESENT_RECEIVE (Packet):
	pass
class GC_GUILDWAR_SCORE (Packet):
	pass
class GC_CHATLINK_DOWNLOAD (Packet):
	pass
class GC_USE_REDLINE (Packet):
	pass
class CG_SELECT_ROLE (Packet):
	pass
class GC_RET_GUILDWAR_HISTROY_BATTLE_INFO (Packet):
	pass
class GC_BROTHERHOOD_CREATE_SUCCESS (Packet):
	pass
class CG_SWORDTEAM_RECRUIT (Packet):
	pass
class GC_JUMP_NOTIFY (Packet):
	pass
class GC_FAIRY_RAISE_ACTION_RET (Packet):
	pass
class CG_GODWEAPON_ENCHANT (Packet):
	pass
class GC_SYNC_GUILD_REAMTIME_VOICEROOM_CHANGEINFO (Packet):
	pass
class GC_MISSION_COMMIT_RET (Packet):
	pass
class CG_REQ_MIS_QIYU_HISTORY (Packet):
	pass
class GC_RET_HOME_REGION_INFO (Packet):
	pass
class CG_GUILD_REQ_SET_FULLACCEPT (Packet):
	pass
class GC_UPDATE_POS (Packet):
	pass
class GC_SYNC_EXCHANGECOUNT (Packet):
	pass
class CG_LUCKY_CONNECT_RESET (Packet):
	pass
class CG_REQ_CHALLENGE (Packet):
	pass
class CG_SECPASSWORD_REDPOINTREADED (Packet):
	pass
class CG_HONGBAO_SEND (Packet):
	pass
class GC_BWPVPFINAL_COPYSCENERET (Packet):
	pass
class CG_REQUEST_RECOVERYFOODINFO (Packet):
	pass
class CG_CVFIREFLY_CANCEL_SIGNUP (Packet):
	pass
class GC_FASHION_SYNC (Packet):
	pass
class GC_SYNC_SUPER_R_LVEL (Packet):
	pass
class GC_WEDDING_SYC_CONFIG (Packet):
	pass
class GC_SHEDAOSAIMA_SYSDAOJU (Packet):
	pass
class CG_RECEIVE_ACHIEVEMENT_RECORD_REWARD (Packet):
	pass
class CG_REQ_GUILDCONVOY_FINISH (Packet):
	pass
class CG_START_KIT_PACK (Packet):
	pass
class GC_GUILDWAR_BATTLE_START (Packet):
	pass
class CG_BROTHERHOOD_INVITE_CONFIRM (Packet):
	pass
class GC_SYNC_BOUNTY_REFREST_STATE (Packet):
	pass
class CG_REQUEST_RECHARGE (Packet):
	pass
class GC_RET_GUILD_MONSTER_RANK_INFO (Packet):
	pass
class CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE_NOTICE_LEADER (Packet):
	pass
class CG_LUCKY_CONNECT_GAIN_REWARD (Packet):
	pass
class GC_SYNC_MONITOR_NPC_INFO (Packet):
	pass
class GC_SYNC_XIUZHEN_COPYSCENE_DATA (Packet):
	pass
class CG_MILITARY_REQ_BUYITEM (Packet):
	pass
class GC_SYNC_CHANGEPROFESSIONCONDITIONINFO (Packet):
	pass
class GC_YAOSHOU_CHANGE_TRIGER_NOTICE (Packet):
	pass
class GC_SYNC_STATISTICS_DATA (Packet):
	pass
class GC_SEND_RUBKICUBE_RESULT (Packet):
	pass
class GC_RANK_RET_FAIRYINFO (Packet):
	pass
class CG_REQ_AUCTION_BID (Packet):
	pass
class CG_REQ_PET_DELETE (Packet):
	pass
class GC_HOMEBUILDING_PLAY (Packet):
	pass
class CG_ASK_ACTIVENESSAWARD (Packet):
	pass
class CG_JOIN_TEAM_REQUEST_RESULT (Packet):
	pass
class CG_HOMEBUILDING_PLAY (Packet):
	pass
class GC_RET_ARTIFACT_EXCHANGE (Packet):
	pass
class GC_NEWPRESTIGEUNLOCK (Packet):
	pass
class GC_TEAM_SYNC_TEAMINFO (Packet):
	pass
class GC_RET_VIEWOTHERROLEINFO (Packet):
	pass
class GC_WILDWORLDBOSS_NUM (Packet):
	pass
class GC_BATTLEFIELD_SIGNUP_INFO (Packet):
	pass
class CG_GUILDFIGHT_WORLDBOSS_RANK (Packet):
	pass
class GC_RET_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM (Packet):
	pass
class GC_GUILD_RET_WORSHIP_CHIEFMODEL (Packet):
	pass
class GC_TOURNAMENT_SYNC_MY_INFO (Packet):
	pass
class GC_SYNC_SQRE_RESULT (Packet):
	pass
class GC_DELFRIEND (Packet):
	pass
class CG_NOTIFY_GUILD_REALTIME_VOICEROOM_CHANGE_RTMEMBERINFO (Packet):
	pass
class CG_REQ_CHANGE_GUILD_REALTIME_VOICE_ROOM_INFO (Packet):
	pass
class GC_STALL_RETSELLINFO (Packet):
	pass
class CG_REQ_ARTIFACT_INFO (Packet):
	pass
class GC_MISSION_ACCEPT_RET (Packet):
	pass
class CG_UNLOCK_HOME_PLAN (Packet):
	pass
class CG_SHOW_TAIL (Packet):
	pass
class GC_AUTOFORWARDMOVE (Packet):
	pass
class GC_HOME_SYNC_GUEST_DATA (Packet):
	pass
class CG_TEAM_INVITEFOLLOW (Packet):
	pass
class CG_BWPVPFINAL_ASKADDSCORE (Packet):
	pass
class CG_FLY_LANDING (Packet):
	pass
class GC_RET_BLACKMARKETITEMINFO (Packet):
	pass
class CG_CHANGE_STEWARD_NAME (Packet):
	pass
class CG_ASK_MOVETO_WILDWORLDBOSS (Packet):
	pass
class CG_REQ_APPLY_LEADER_VOTE (Packet):
	pass
class GC_SYNC_PLAYER_RUBKICUBE_OXYGEN_INFO (Packet):
	pass
class GC_SYC_FULL_BLACK_LIST (Packet):
	pass
class GC_CREATE_PLAYER (Packet):
	pass
class GC_USE_CONVO_EFFECT (Packet):
	pass
class GC_DELRECENTCONTACTLIST (Packet):
	pass
class GC_QBZ_USE_ITEM_RESULT (Packet):
	pass
class GC_TRIGGER_FRIENDS_MUTUALHELP (Packet):
	pass
class GC_OPPONENT_LIST (Packet):
	pass
class CG_BWPVPFINAL_REQHELP (Packet):
	pass
class GC_BROTHERHOOD_CHANGE_NAME (Packet):
	pass
class CG_SELECT_RIDE_MISSION (Packet):
	pass
class GC_SYNC_CUSTOMHEAD_RESULT (Packet):
	pass
class CG_REQ_EXCHANGE_GUILD_MONSTER_BUFF (Packet):
	pass
class GC_UPDATE_SKILLZHUANJING_LEVELUP_INFO (Packet):
	pass
class GC_SWORDTEAM_LEAVE (Packet):
	pass
class CG_ASK_PASSPORT_DATA (Packet):
	pass
class GC_RESPOND_EXCHANGE_CURRENCY (Packet):
	pass
class GC_SYNC_GUILD_REALTIME_VOICE_ROOM_INFO (Packet):
	pass
class CG_PUT_ITEM_STORAGEPACK (Packet):
	pass
class GC_CHANGE_ARMY_MEMBER_POSITION_OVER (Packet):
	pass
class GC_SYNC_NPCPICKUP_STATE (Packet):
	pass
class GC_COMMONCOMMAND (Packet):
	pass
class CG_REQ_QIANZHUANG_DATA (Packet):
	pass
class CG_REQ_TIMELIMITACTSCENE_ENTER (Packet):
	pass
class GC_VERIFYCODE_SYNC (Packet):
	pass
class CG_REQ_RECRUIT (Packet):
	pass
class GC_LUCKY_CONNECT_SYNC (Packet):
	pass
class GC_EQUIP_REFINE_RET (Packet):
	pass
class GC_STALL_REVIEW_UPDATE (Packet):
	pass
class GC_SYNC_FEEDBACK_INFO (Packet):
	pass
class CG_REQ_GUILD_MONSTER_DATA (Packet):
	pass
class GC_SYNC_FREEZE_SKILL_RELEASE (Packet):
	pass
class GC_SHEDAOSAIMA_RANK (Packet):
	pass
class CG_STALL_APPEAL (Packet):
	pass
class CG_BUY_NIEREN_SUPER (Packet):
	pass
class GC_SHOW_DEVICE_INFO (Packet):
	pass
class CG_ADVENTURE_REQ_BUY_ITEM (Packet):
	pass
class GC_SYSTEMTRADE_CANSELLLIST (Packet):
	pass
class GC_StopShangGuEMoEnergy (Packet):
	pass
class GC_CREATE_SNARE (Packet):
	pass
class CG_REQ_PET_FEED (Packet):
	pass
class CG_PICK_RANDOM_COLOR_ITEM_STORAGE (Packet):
	pass
class GC_WISHING_UPDATE_SELECTED_STATUS_RESULT (Packet):
	pass
class GC_GUILDWAR_MATCH_RESULT (Packet):
	pass
class GC_PLAYER_CHANGESCENE_MOVETO (Packet):
	pass
class CG_REQ_DESTINY_ATTRIBUTE (Packet):
	pass
class CG_REQ_QQ_UNREG_FRIENDS (Packet):
	pass
class GC_BOSS_PICK_ITEM_RET (Packet):
	pass
class GC_FAIRY_RAISE_OPEN_BUY_FEED_TIME_UI (Packet):
	pass
class CG_SAVE_HOME_BUILDING (Packet):
	pass
class CG_NEW_PLAYER_BEHAVIOR_MISSION (Packet):
	pass
class GC_START_RUBKICUBE_SUB_PLAY (Packet):
	pass
class CG_FAIRY_BREAK_LEVEL_LIMIT (Packet):
	pass
class CG_COPYSCENE_HIDINGBOSS_SELECT_OPEN_TYPE (Packet):
	pass
class CG_REQUIRE_JOIN_COPY_SCENE (Packet):
	pass
class CG_ITEMPACK_UNLOCK (Packet):
	pass
class GC_PLAY_TIANJIEGU_EFFECT (Packet):
	pass
class GC_WAITPAY_ADD (Packet):
	pass
class GC_TOURNAMENT_RET_LOTTERY (Packet):
	pass
class CG_ASK_YIRONG_CARD (Packet):
	pass
class CG_GUILD_REQ_SET_QUICKJOIN (Packet):
	pass
class GC_ASURA_UPDATE_BATTLE_INFO (Packet):
	pass
class GC_TEAMFOLLOW_SEAMLESS (Packet):
	pass
class GC_SHOW_ACHIEVEMENT (Packet):
	pass
class GC_SYNC_TEAM_PVPZOMBIE (Packet):
	pass
class CG_EQUIPMIRROR_FORGE (Packet):
	pass
class CG_TOURNAMENT_TAKE_REWARD (Packet):
	pass
class GC_BEGIN_CHANGENAME (Packet):
	pass
class GC_RET_FAIRY_SKILL_LEVEL_UP_RESULT (Packet):
	pass
class GC_SYNC_COMMONDATA (Packet):
	pass
class GC_SYNC_HOME_FORTUNE_TELLING_RESULT (Packet):
	pass
class GC_DOMAIN_UPDATEEVT (Packet):
	pass
class CG_ChangeMentorName (Packet):
	pass
class GC_AUTOTEAM_OVERTIME_REQUEST (Packet):
	pass
class GC_COLLECT_INFO (Packet):
	pass
class GC_MULPVP_INVITE (Packet):
	pass
class CG_REQ_FAIRY_NEIDAN_FEED (Packet):
	pass
class CG_REQ_ARMY_CHANGE_RTROLE (Packet):
	pass
class GC_UPDATE_GROWWAY_INFO (Packet):
	pass
class GC_BATTLEFIELD_BROADCAST (Packet):
	pass
class CG_SKILL_UNLOCK (Packet):
	pass
class CG_FINDPLAYER (Packet):
	pass
class CG_MIDAS_REQUEST_BALANCE (Packet):
	pass
class CG_DRAW_GROWTHUP_MARASARA (Packet):
	pass
class CG_REQ_TIMELIMITACTSCENE_EXIT (Packet):
	pass
class GC_MULPVP_FIGHTSTATE (Packet):
	pass
class GC_TOWER_ENTER_NEXT (Packet):
	pass
class GC_RECOMMEND_FRIENDRET (Packet):
	pass
class CG_SWORDTEAM_JOIN_OTHERPLAYER (Packet):
	pass
class CG_ACTIVITY_BUYBACK_ASK_DATA (Packet):
	pass
class CG_BROTHERHOOD_RECRUIT_PUBLISH (Packet):
	pass
class GC_BWPVPFINAL_MEMINFOINCOPYSCENE (Packet):
	pass
class GC_GET_CURRENCY (Packet):
	pass
class CG_TOURNAMENT_REQ_LOTTERY (Packet):
	pass
class GC_HONGBAO_SEND (Packet):
	pass
class GC_SEARCHSDKCHECK_GUILD_RET (Packet):
	pass
class CG_REQ_GUILDWAR_HISTROY_BATTLE_INFO (Packet):
	pass
class CG_REQ_TEAM_INVITE (Packet):
	pass
class CG_ASK_TEAMPLATFORMINFO (Packet):
	pass
class CG_ASK_XCTJAWARD (Packet):
	pass
class GC_COPYSCENE_PROGRESS (Packet):
	pass
class GC_SERVANT_RETOP (Packet):
	pass
class CG_SEND_COUPLE_BP_RESULT (Packet):
	pass
class CG_DOMAIN_REQ_HISTORYLIST (Packet):
	pass
class GC_BROADCAST_GUILDSHORTNAME (Packet):
	pass
class GC_SYNC_FAIRY_SKILL_LOCK (Packet):
	pass
class GC_DELAPPLYLIST (Packet):
	pass
class GC_SYNC_SKILLSOUL_STATE (Packet):
	pass
class CG_FASHION_PROLONG (Packet):
	pass
class GC_DOMAINWAR_OP_RET (Packet):
	pass
class CG_CHATLINK_DOWNLOAD (Packet):
	pass
class CG_EQUIP_REFINE (Packet):
	pass
class CG_REQ_REPLACE_EQUIP_REBIRTH_RECASE_TRICK (Packet):
	pass
class GC_RET_AUCTION_LOOK (Packet):
	pass
class CG_EQUIPMIRROR_COMPOUND (Packet):
	pass
class CG_WEDDING_CREATE (Packet):
	pass
class GC_SYNC_SKILLBARINFO (Packet):
	pass
class GC_CREATE_NPC (Packet):
	pass
class GC_ON_DIE_KILLER_ID (Packet):
	pass
class CG_REQ_WORLD_GROUPINFO (Packet):
	pass
class GC_RET_COPYPLAYERINFO (Packet):
	pass
class GC_SET_PET_HUNGER (Packet):
	pass
class CG_REQUEST_LASTRECAST_INFO (Packet):
	pass
class GC_SYNC_COPYSCENE_ENTERCOUNT (Packet):
	pass
class CG_CREATE_ROLE (Packet):
	pass
class CG_REQ_CHANGE_SCENE_FEITIAN (Packet):
	pass
class CG_REQ_CHANGE_SCENE_WORLDMAP (Packet):
	pass
class CG_LIFESKILL_LIANDAN (Packet):
	pass
class CG_INTERACT_JUMP (Packet):
	pass
class GC_RET_GETREWARDFORSIGNIN (Packet):
	pass
class GC_COPYSCENE_HIDINGBOSS (Packet):
	pass
class CG_ASK_PICKUP_ITEM (Packet):
	pass
class GC_ACTIVITY_BUYBACK_SYNC_DATA (Packet):
	pass
class GC_RES_RECOMMEND_MEMBER_INFO (Packet):
	pass
class CG_STALL_CANCELSELL (Packet):
	pass
class GC_PLAY_WARN_EFFECT (Packet):
	pass
class GC_SYNC_OBCELEBRATION_INFO (Packet):
	pass
class GC_SYNC_AUTO_DECOMPOSE (Packet):
	pass
class GC_MISSION_DONE (Packet):
	pass
class GC_RET_ADVENTURE_EVENT_ACCEPT (Packet):
	pass
class CG_TSS_ANTI_RECV_DATA (Packet):
	pass
class CG_QTE_PLAYOVER (Packet):
	pass
class CG_STARMAP_REDPOINT_INFO (Packet):
	pass
class GC_MOUNT_DATA (Packet):
	pass
class CG_BANGHUA_INTERACTIVE (Packet):
	pass
class GC_SYNC_COMMONACTIVITYINFO (Packet):
	pass
class CG_ASK_RELIVE (Packet):
	pass
class GC_ENTER_SCENE (Packet):
	pass
class CG_AID_RESPONSE (Packet):
	pass
class GC_CREATE_SCENE_GATHER (Packet):
	pass
class GC_RET_YLTXINST_DES_REMAIN_NUM (Packet):
	pass
class CG_USE_REDLINE (Packet):
	pass
class CG_GODWEAPON_STUNT_REPLACE (Packet):
	pass
class CG_RANK_ASK_FAIRYINFO (Packet):
	pass
class CG_ADDBLACKLIST (Packet):
	pass
class GC_UPDATE_BATTLE_FAIRY_LIST (Packet):
	pass
class CG_MILITARY_REQ_PROMOTERANK (Packet):
	pass
class GC_SYNC_TITLEINFO (Packet):
	pass
class GC_DELETE_CUTSCENE_TRIGGER (Packet):
	pass
class CG_REQ_JIANMUXB_FILLING_HELP (Packet):
	pass
class GC_RET_JOIN_GUILD_REALTIME_VOICE_ROOM (Packet):
	pass
class GC_BROADCAST_CURTITLE (Packet):
	pass
class CG_BROTHERHOOD_CREATE (Packet):
	pass
class CG_MARRIAGE_PROCESS (Packet):
	pass
class CG_WATERMELON_ENROLL (Packet):
	pass
class CG_GUILD_JOB_CHANGE (Packet):
	pass
class CG_ACCPET_IMMORTALITY_FINAL_REWARD (Packet):
	pass
class CG_REQ_FRIENDS_MUTUALHELP_DATA (Packet):
	pass
class GC_GUILD_ALLIANCE_APPLY_LIST (Packet):
	pass
class CG_GROUPPHOTO_REQUEST (Packet):
	pass
class CG_REQ_AUCTION_FAVORITE (Packet):
	pass
class CG_USE_DIRECTSENDGIDT (Packet):
	pass
class GC_SINGLE_INTERACT (Packet):
	pass
class GC_FASHION_DEL (Packet):
	pass
class GC_STALL_REVIEW_DELETE (Packet):
	pass
class GC_SKILL_SWITCH_TYPE_SKILL (Packet):
	pass
class GC_SYNC_HOME_HORDE_COLLECTION (Packet):
	pass
class CG_GUILD_ALLIANCE_APPLY (Packet):
	pass
class GC_RET_COPYSCENE_REWARD (Packet):
	pass
class GC_DIG_TREASURE_RESULT (Packet):
	pass
class CG_PLAYER_LEVELUP_MANUAL (Packet):
	pass
class GC_SYC_CUSTOMHEAD_INFO (Packet):
	pass
class GC_UPDATE_FRIEND_OR_RECENTCONTACT_LIST (Packet):
	pass
class GC_STALL_RETFAVORITE (Packet):
	pass
class CG_SERVANT_REQADDEXP (Packet):
	pass
class CG_REQ_TEAM_CHANGE_LEADER (Packet):
	pass
class GC_SYNC_LIFESKILL_LEVEL (Packet):
	pass
class CG_XIANDAN_EQUIP (Packet):
	pass
class GC_RET_QUIT_GUILD_REALTIME_VOICE_ROOM (Packet):
	pass
class CG_GUILD_WORSHIP_OVER (Packet):
	pass
class GC_JOIN_TEAM_APPLICANT_INFO (Packet):
	pass
class GC_SYNC_CENTERCONTROL_OPERATE (Packet):
	pass
class CG_EQUIP_ITEM (Packet):
	pass
class GC_RET_NATIONALDAY_TRIBUTE_STATE (Packet):
	pass
class CG_JUBAOPLAYER (Packet):
	pass
class CG_TITLE_UNEQUIP (Packet):
	pass
class GC_STALL_REVIEW_SYNC (Packet):
	pass
class GC_EQUIP_RECOIN_RET (Packet):
	pass
class CG_REQ_PK_DEATHAID (Packet):
	pass
class CG_STATICSYSTEMSHOP_BUYBACK (Packet):
	pass
class GC_UPDATEFRIEND_POINTVALUE (Packet):
	pass
class GC_UPDATE_FOLLOWSTATE (Packet):
	pass
class CG_IOS_REVIEW_GUILD_COMPLETED (Packet):
	pass
class CG_REQ_HOME_FITMENT (Packet):
	pass
class GC_ASURA_ENROLL (Packet):
	pass
class CG_APPLY_SHOWROOM (Packet):
	pass
class GC_GUILD_RET_PRESERVE_LIST (Packet):
	pass
class CG_REQ_YUANLINGNPC_POS (Packet):
	pass
class GC_SYNC_WEEKSCARD_STATE (Packet):
	pass
class GC_MAKE_SECOND_INTERACT (Packet):
	pass
class CG_BWPP_GOTOBIGWORLD (Packet):
	pass
class CG_REQ_EQUIP_REBIRTH_INFO (Packet):
	pass
class GC_YAOSHOU_CHANGE_TRIGER_GUIDE (Packet):
	pass
class CG_OPEN_LUCKYEGG (Packet):
	pass
class GC_EQUIP_REBIRTH_RESULT (Packet):
	pass
class GC_UPGRADE_PRACTICE_RESPONSE (Packet):
	pass
class CG_BROTHERHOOD_KICK (Packet):
	pass
class CG_NATIONALDAY_TRIBUTE_GET_REWARD (Packet):
	pass
class GC_TOURNAMENT_SYNC_MATCH_INFO (Packet):
	pass
class CG_GUILDFIGHT_WORLDBOSS_PICKUP_SOUL (Packet):
	pass
class CG_GUILD_ROBBERS_RANK (Packet):
	pass
class CG_ASK_BACK_AWARD (Packet):
	pass
class GC_FASHION_COLOR (Packet):
	pass
class CG_REQ_PHOTORANDOM_SHARE_DATA (Packet):
	pass
class GC_WATERMELON_SYNC_PLAY_COUNT (Packet):
	pass
class GC_ASURA_ASK_ENROLL (Packet):
	pass
class GC_SHOW_TAIL_PAK (Packet):
	pass
class CG_GUILD_WAR_REFUSE_SIGN_UP (Packet):
	pass
class CG_AUCTION_UPDATA_UISTATE (Packet):
	pass
class CG_GODWEAPON_CONCRETE (Packet):
	pass
class GC_GUILDWAR_UPDATE_STATE (Packet):
	pass
class GC_TEAM_SYNC_APPLICANTINFO (Packet):
	pass
class CG_FLY_FASTSPEED (Packet):
	pass
class CG_SPOKESMAN_ANSWER_DIALOGUE (Packet):
	pass
class CG_ORIENTATION_CHANGE (Packet):
	pass
class GC_DELETE_OBJ (Packet):
	pass
class GC_SYNC_PHOTORANDOM_SHARE_DATA (Packet):
	pass
class GC_HONGBAO_RET_UPDATE (Packet):
	pass
class GC_RET_HOME_HORDE_INFO (Packet):
	pass
class CG_DELAPPLYLIST (Packet):
	pass
class CG_AUTOTEAM_OVERTIME_REQUEST_RESULT (Packet):
	pass
class GC_RET_TEAMPLATFORMINFO (Packet):
	pass
class CG_GODWEAPON_BASE_LEVALUP (Packet):
	pass
class GC_AUCTION_SYNC (Packet):
	pass
class GC_REQ_ADD_HOMEGUEST (Packet):
	pass
class CG_REQ_JIANMUXB_CLICKLINK (Packet):
	pass
class CG_REQUEST_FAIRY_LASTRECAST_INFO (Packet):
	pass
class CG_BIGWORLDPVP_PRE_SIGNUP (Packet):
	pass
class CG_NPCGIFTEXCHANGE_GET_AWARD (Packet):
	pass
class GC_DELBLACKLIST (Packet):
	pass
class GC_GUILDBANGHUA_RESULT (Packet):
	pass
class GC_VOICE_OVER (Packet):
	pass
class GC_RET_GUILD_MONSTER_DATA (Packet):
	pass
class GC_OPERATE_GEM_RET (Packet):
	pass
class GC_GUILD_RET_LEVELUP (Packet):
	pass
class GC_SYNC_ORIGINALTOREAL_WORLDID (Packet):
	pass
class CG_REQ_REGION_HOME_NUM (Packet):
	pass
class GC_SYNC_STARMAP_ALL_INFO (Packet):
	pass
class GC_SYNC_BIGBATTLE_STATUS (Packet):
	pass
class CG_REQ_TEACHER (Packet):
	pass
class CG_REQ_ARTIFACT_EXCHANGE (Packet):
	pass
class GC_PUBLISH_MENTOR_MESSAGE (Packet):
	pass
class CG_GUILD_JOIN_OTHERPLAYER (Packet):
	pass
class CG_BIGBATTLE_PICKITEM (Packet):
	pass
class GC_ACCRECHARGE_RESPONSE_DATA (Packet):
	pass
class CG_GUILD_INVITE (Packet):
	pass
class CG_HELP_TIANYIN (Packet):
	pass
class CG_REQ_GUILDCONVOY_PATH (Packet):
	pass
class CG_REQ_GET_HOME_GIFTBOX (Packet):
	pass
class CG_DRAW_SHARE_GAME_GIFT (Packet):
	pass
class CG_LEVELUP_BUILDING (Packet):
	pass
class GC_AID_RESOPNSE_CONFIG (Packet):
	pass
class GC_PLAY_LIGHTNING_EFFECT (Packet):
	pass
class CG_LOCK_CURTITLE (Packet):
	pass
class GC_REBATE_RANKDATA (Packet):
	pass
class CG_REQ_MENTOR_RECURIT (Packet):
	pass
class GC_GUILDWAR_SYNC_SIGNUPMEMBER_COUNT (Packet):
	pass
class GC_FASHION_COLOR_CHANGE (Packet):
	pass
class GC_MAIL_UPDATE (Packet):
	pass
class CG_ACTIVITY_BUYBACK_BUY (Packet):
	pass
class CG_RELEASE_FAIRY (Packet):
	pass
class CG_LEARN_FAIRY_SKILL (Packet):
	pass
class GC_COPYSCENE_INVITE (Packet):
	pass
class CG_WEDDING_JOIN (Packet):
	pass
class GC_EQUIPMIRROR_FORGE_RESULT (Packet):
	pass
class GC_SYNC_USER_CHRISTMAS_DATA (Packet):
	pass
class CG_REQ_PET_LOCK (Packet):
	pass
class CG_RECHARGESCORESHOP_BUY (Packet):
	pass
class CG_TOWER_BUY_ITEM (Packet):
	pass
class CG_REQ_TEAM_KICK_MEMBER (Packet):
	pass
class GC_GUILD_RET_QUICKJOIN (Packet):
	pass
class CG_EXAM_SELECTCATEGORY (Packet):
	pass
class GC_ITEMPACK_RESIZE (Packet):
	pass
class GC_DOMAINWAR_LINEINFO (Packet):
	pass
class CG_GUILDMONSTER_ACTIVE (Packet):
	pass
class GC_RET_YLTX_SCENELIST (Packet):
	pass
class CG_EQUIP_RECOIN (Packet):
	pass
class GC_ASK_FISH_RET (Packet):
	pass
class CG_ACCPET_GROWWAY_REWARD (Packet):
	pass
class GC_MULPVP_CACEL (Packet):
	pass
class GC_TIANSHU_PACK (Packet):
	pass
class CG_REQ_EQUIP_REBIRTH_RECASE (Packet):
	pass
class GC_RET_ELITENPCCREATECD (Packet):
	pass
class GC_REQ_SWITCH_PET_FIGHT_STATE (Packet):
	pass
class CG_SWORDTEAM_JOB_CHANGE (Packet):
	pass
class CG_GUILD_LEAVE (Packet):
	pass
class GC_RET_BOUNTY_CHANGE_SCENE (Packet):
	pass
class CG_TOWER_SWEEP (Packet):
	pass
class GC_SYNC_AIRWALL_INFO (Packet):
	pass
class GC_SYN_ATTR (Packet):
	pass
class CG_REQ_PET_SUMMON_OR_CALLBACK (Packet):
	pass
class GC_BATTLEFIELD_MATCHINFO (Packet):
	pass
class CG_ASK_REMOVE_INSCRIPTION (Packet):
	pass
class GC_TEST_MUTIL_VARIABLE (Packet):
	pass
class GC_TP_NOTICE_ONLINE (Packet):
	pass
class GC_TP_KICK_PLAYE (Packet):
	pass
class CG_CHECK_GUILDSTUDIO (Packet):
	pass
class GC_CHECK_GUILDSTUDIO_RET (Packet):
	pass
class GC_SYNC_OPEN_SERVER_ACTIVITY_TASK_INFO (Packet):
	pass
class GC_SYNC_DIRTY_OPSERVER_ACTIVITY_TASK_INFO (Packet):
	pass
class CG_ACCEPT_OPSERVER_TASK_REWARD (Packet):
	pass
class CG_ACCEPT_FUNY_REWARD (Packet):
	pass
class CG_REQ_SWORDTEAM_INVITE (Packet):
	pass
class CG_BuyStarItem (Packet):
	pass
class GC_SYNC_LIMITBESTSELLER_DATA (Packet):
	pass
class GC_SYNC_SEVEN_DAY_GIFT (Packet):
	pass
class CG_REQ_GET_SEVEN_DAY_GIFT (Packet):
	pass
class CG_ACCEPT_OPEN_SERVER_CAHRGE_REWARD (Packet):
	pass
class CG_RET_BIND_PHONE_SUCCESS (Packet):
	pass
class CG_RET_REAL_NAME_CHECK_SUCCESS (Packet):
	pass
class GC_SYNC_BIND_PHONE_AWARD (Packet):
	pass
class GC_SYNC_REAL_NAME_CHECK_AWARD (Packet):
	pass
class CG_ACCEPT_QIANZHUANG_SHOUYI (Packet):
	pass
class CG_ACCEPT_QIANZHUANG_DAJIANG (Packet):
	pass
class CG_PERSONALREBATE_START (Packet):
	pass
class CG_REQ_GET_HISTORY_RECHARGE_BINDGIFT (Packet):
	pass
class GC_SYNC_HISTORY_RECHARGE_BINDGIFT (Packet):
	pass
class CG_REQ_GET_HISTORY_RECHARGE_REPAYGIFT (Packet):
	pass
class GC_SYNC_HISTORY_RECHARGE_REPAYGIFT (Packet):
	pass
class CG_REQ_PSSURVEY_REWARD (Packet):
	pass
class GC_SYNC_PSSURVEY_PLAYER_VERSION (Packet):
	pass
class CG_REQ_GET_HISTORY_RECHARGE_REPAYRECHARGE (Packet):
	pass
class GC_SYNC_HISTORY_RECHARGE_REPAYRECHARGE (Packet):
	pass
class CG_REQ_GET_HISTORY_RECHARGE_LEVELDRAW (Packet):
	pass
class GC_SYNC_HISTORY_RECHARGE_LEVELDRAW (Packet):
	pass
class GC_RET_HISTORY_RECHARGE_LEVELDRAW_RESULT (Packet):
	pass
class CG_REQ_HISTORY_RECHARGE_BIND (Packet):
	pass
class CG_POSTERSTAR_SEND_GIFT (Packet):
	pass
class CG_POSTERSTAR_GET_AWARD (Packet):
	pass
class CG_POSTERSTAR_SYNC_STATUE (Packet):
	pass
class GC_POSTERSTAR_SYNC_STATUE (Packet):
	pass
class GC_SYNC_CAWARD_INFO (Packet):
	pass
class CG_ACCEPT_CAWARD (Packet):
	pass
class CG_REQ_BIND_HISTORY_RECHARGE (Packet):
	pass
class GC_RET_HISTORY_RECHARGE_BIND_INFO (Packet):
	pass
class CG_ASK_ARHUNTING (Packet):
	pass
class GC_RET_ARHUNTING (Packet):
	pass
class GC_SYNC_DROPINFO (Packet):
	pass
class CG_CLEARN_USE_SKILL_CD (Packet):
	pass
class GC_NEWYEAR_WISH (Packet):
	pass
class CG_REQ_SEND_NARRIAGE_LINK (Packet):
	pass
class CG_USE_SENDLANTERN (Packet):
	pass
class GC_WORDREDPACKETRAIN_ROLLNOTICE (Packet):
	pass
class CG_REQ_HOLIDAY_TIMELIMITACTSCENE_ENTER (Packet):
	pass
class CG_REQ_HOLIDAY_TIMELIMITACTSCENE_EXIT (Packet):
	pass
class GC_RET_RECHARGE_ORDER_OVER (Packet):
	pass
class GC_REQ_PAYUSER_LOG (Packet):
	pass
class CG_SEND_PLAYANDGO_ERROR_LOG (Packet):
	pass
class GC_RET_JOIN_TEAM (Packet):
	pass
class GC_NOTICE_DLC_VERSION_VIEW (Packet):
	pass
class GC_SYNC_DLC_VERSION_DATA (Packet):
	pass
class CG_ACCEPT_DLC_VIEW_REWARD (Packet):
	pass
class CG_ACCEPT_DLC_SEVEN_REWARD (Packet):
	pass
class CG_REPLACE_ACCEPT_DLC_SEVERN_DAY_REWARD (Packet):
	pass
class CG_GOODLUCK_OP (Packet):
	pass
class GC_GOODLUCK_SYNC (Packet):
	pass
class CG_DLC_CLICK_FUNCTION_BTN (Packet):
	pass
class CG_DLC_CLICK_DLC_VIEW_DETAIL (Packet):
	pass
class CG_CLICK_DLC_VIEW_GO (Packet):
	pass
class GC_SYNC_ONE_CHARGE_GIFT_DATA (Packet):
	pass
class GC_SYNC_TOTAL_COSUME_GIFT_DATA (Packet):
	pass
class CG_ACCEPT_COSUME_GIFT (Packet):
	pass
class CG_REQ_GET_FLASH_SALES_AWARD (Packet):
	pass
class GC_SYNC_FLASH_SALES_DATA (Packet):
	pass
class CG_REQ_BUY_DISCOUNT_GIFT (Packet):
	pass
class GC_SYNC_DISCOUNT_GIFT_DATA (Packet):
	pass
class CG_REQ_VIVO_GIFT (Packet):
	pass
class GC_RET_VIVO_GIFT (Packet):
	pass
class GC_SYNC_VIVO_GIFT_GET_TIME (Packet):
	pass
class GC_GM_LOGON_NOTICE (Packet):
	pass
class GC_GUILD_WORLDBOSS_STATE (Packet):
	pass
class CG_GUILD_WORLDBOSS_RANK (Packet):
	pass
class GC_GUILD_WORLDBOSS_RANK (Packet):
	pass
class CG_GUILD_WORLDBOSS_PERSONAL_RANK (Packet):
	pass
class GC_GUILD_WORLDBOSS_PERSONAL_RANK (Packet):
	pass
class GC_EQUIP_ENCHANT_ITEMDETAIL (Packet):
	pass
class GC_SYNC_NEW_IMMORTALITY_INFO (Packet):
	pass
class GC_SYNC_DIRTY_NEW_IMMORTALITY_INFO (Packet):
	pass
class CG_ACCEPT_NEW_IMMORTALITY_WAY_REWARD (Packet):
	pass
class CG_ACCEPT_NEW_IMMORTALITY_STAGE_REWARD (Packet):
	pass
class CG_SELECT_NEW_PRESTIGE_CAMP (Packet):
	pass
class CG_BUY_NEW_PRESTIGE_SHOP_ITEM (Packet):
	pass
class CG_ACCEPT_NEW_PRESTIGE_LEVEL_REWARD (Packet):
	pass
class GC_SYNC_PLAYER_NEW_PRESTIGE_INFO (Packet):
	pass
class CG_REQ_SERVER_NEW_PRESTIGE_INFO (Packet):
	pass
class GC_SYNC_SERVER_NEW_PRESTIGE_INFO (Packet):
	pass
class CG_GUILD_REQ_LIST_BY_LABEL (Packet):
	pass
class GC_SYNC_GUILD_LABEL (Packet):
	pass
class GC_SYNC_DAILY_LEVEL (Packet):
	pass
class CG_REQ_TOWER_FRIEND_RANK (Packet):
	pass
class GC_RET_TOWER_FRIEND_RANK (Packet):
	pass
class CG_REQ_NEW_PRESTIGE_CAMP_ROLE_NUMER (Packet):
	pass
class GC_RESP_NEW_PRESTIGE_CAMP_ROLE_NUMBER (Packet):
	pass
class GC_SYNC_VIEW_PLAYER_NEW_PRESTIGE_CAMP (Packet):
	pass
class GC_SELECT_NEW_PRESTIGE_CAMP_RET (Packet):
	pass
class GC_SYNC_NEW_PRESTIGE_ELITE_SCENE_INFO (Packet):
	pass
class CG_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE (Packet):
	pass
class GC_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE_OK (Packet):
	pass
class CG_GET_ALL_ACTIVENESS_BONUS_ITEM (Packet):
	pass
class GC_COMMON_RWARD_ITEM_SHOW (Packet):
	pass
class GC_NOTICE_FIRST_CHANGE_WINDOW (Packet):
	pass
class GC_KICKOUT_MERCENARY_LEAVE_TEAM (Packet):
	pass
class CG_REQ_CHANGE_FRIEND_GROUPNAME (Packet):
	pass
class GC_RET_CHANGENAME_FRIEND_GROUPNAME (Packet):
	pass
class GC_SYNC_NEW_PRESTIGE_BOSS_INFO (Packet):
	pass
class CG_ENTER_NEW_PRESTIGE_BOSS_SCENE (Packet):
	pass
class CG_REQ_GET_PLAYANDGO_AWARD (Packet):
	pass
class GC_SYNC_PLAYANDGO_INFO (Packet):
	pass
class CG_NEW_PRESTIGE_BOSS_OPENBOX (Packet):
	pass
class CG_REQ_SHAKE_REWARD (Packet):
	pass
class CG_RET_SHAKE_REWARD (Packet):
	pass
class GC_SYNC_SHAKE_ACTIVITY_INFO (Packet):
	pass
class CG_SHAKE_SHOP_BUY (Packet):
	pass
class GC_SHAKE_SHOP_BUY_RET (Packet):
	pass
class GC_RET_SHAKE_REWARD (Packet):
	pass
class GC_SYNC_GUILD_ROBBER_RUN (Packet):
	pass
class GC_SYNC_GUILDFIGHT_BOSS_RUN (Packet):
	pass
class GC_SYNC_GUILD_WORD_BOSS_RUN (Packet):
	pass
class GC_SYNC_MONSTER_NIAN (Packet):
	pass
class CG_MONSTER_NIAN_DRIVEAWAY (Packet):
	pass
class GC_MONSTER_NIAN_DRIVEAWAY (Packet):
	pass
class CG_MONSTER_NIAN_REQ_RANK (Packet):
	pass
class GC_MONSTER_NIAN_REQ_RANK (Packet):
	pass
class CG_MONSTER_NIAN_ACCEPT_STAGE_REWARD (Packet):
	pass
class CG_FESTIVAL_LUCKYCARD_CHOOSE (Packet):
	pass
class GC_FESTIVAL_LUCKYCARD_CHOOSE_RESULT (Packet):
	pass
class GC_FESTIVAL_LUCKYCARD_INFO (Packet):
	pass
class CG_REQ_FESTIVAL_LUCKCARD_INFO (Packet):
	pass
class GC_SYNC_HUADENGCHUSHANG_INFO (Packet):
	pass
class GC_ActivyCanBuyBackRewardAllInfo (Packet):
	pass
class CG_ActivityRewardBuyBackNotice (Packet):
	pass
class CG_ActivyRewardBuyOne (Packet):
	pass
class CG_ActivityRewardBuyAll (Packet):
	pass
class GC_ActivityRewardBuyBackNotice (Packet):
	pass
class GC_ACTIVITY_CAN_BUYBACK_REWARD_ALLINFO (Packet):
	pass
class GC_ACTIVITY_REWARD_BUYBACK_NOTICE (Packet):
	pass
class CG_ACTIVITY_REWARD_BUYONE (Packet):
	pass
class CG_ACTIVITY_REWARD_BUY_ALL (Packet):
	pass
class CG_REQ_GET_WMKEFU_TRIAL_ITEM (Packet):
	pass
class GC_SYNC_GET_WMKEFU_TRIAL_ITEM (Packet):
	pass
class GC_SYNC_GIVE_GIFT_RANK_ACTIVITY_INFO (Packet):
	pass
class CG_REQ_GIVE_GIFT_RANK_LIKE (Packet):
	pass
class GC_RESP_GIVE_GIFT_RANK_LIKE (Packet):
	pass
class CG_REQ_GIVE_RANK_GIFT (Packet):
	pass
class GC_RESP_GIVE_RANK_GIFT (Packet):
	pass
class CG_REQ_GET_HUADENGCHUSHANG_ITEM (Packet):
	pass
class CG_REQ_OPEN_LIUSHUIXI (Packet):
	pass
class CG_REQ_GET_LIUSHUIXI_ITEM (Packet):
	pass
class GC_UNFORGETABLE_PROMISE_INFO (Packet):
	pass
class CG_UNFORGETABLE_PROMISE_GET_REWARD (Packet):
	pass
class GC_SYNC_SHAKE_CHALLENGE_DATA (Packet):
	pass
class CG_GET_SHAKE_CHALLENGE_REWARD (Packet):
	pass
class GC_GET_SHAKE_CHALLENGE_REWARD_RET (Packet):
	pass
class CG_REQ_GET_HUADENGCHUSHANG_USE_ITEM_AWARD (Packet):
	pass
class GC_MONSTER_NIAN_STAGE_REWARD_STATE (Packet):
	pass
class GC_FESTIVAL_LUCKCARD_AWARD (Packet):
	pass
class GC_SYNC_DIMAI_TANXIAN_INFO (Packet):
	pass
class CG_DIMAI_TANXIAN_OPTION (Packet):
	pass
class CG_DIMAI_TANXIAN_OPTION (Packet):
	pass
class CG_GET_REGRESS_REWARD (Packet):
	pass
class CG_GET_CONDITION_REWARD (Packet):
	pass
class CG_GET_REGRESS_LOGIN_REWARD (Packet):
	pass
class CG_REGRESS_NOTICE (Packet):
	pass
class GC_SYNC_REGRESS_INFO (Packet):
	pass
class CG_FirstOpenDiMaiUI (Packet):
	pass
class GC_SYNC_DIMAI_CHALLENGE_INFO (Packet):
	pass
class CG_REQUEST_DIMAI_CHALLENGE (Packet):
	pass
class CG_ACCEPT_DIMAI_AUTO_REWARD (Packet):
	pass
class GC_DIMAI_CHALLENGE_RESULT (Packet):
	pass
class CG_FIRST_OPEN_DIMAI_UI (Packet):
	pass
class GC_SYNC_DIMAIJINGLUO (Packet):
	pass
class CG_REQ_DIMAIJINGLUO_ACTIVATE (Packet):
	pass
class GC_RESP_DIMAIJINGLUO_ACTIVATE (Packet):
	pass
class GC_DIMAI_TANXIAN_OPTION_RESULT (Packet):
	pass
class CG_GET_FREE_REGRESS_GIFT (Packet):
	pass
class GC_ENTER_DIMAI_CHALLENGE_STAGE (Packet):
	pass
class CG_CHALLENGEFRIENDRANKLIST_REQ (Packet):
	pass
class GC_CHALLENGEFRIENDRANKLIST (Packet):
	pass
class GC_SYNC_SHILIAN_INFO (Packet):
	pass
class GC_SHILIAN_CITIAO (Packet):
	pass
class CG_SHILIAN_CITIAO_SELECT (Packet):
	pass
class GC_SHILIAN_FIGHT_RESULT (Packet):
	pass
class CG_REQ_CHALLENGE_RANK_SWAP_INFO (Packet):
	pass
class GC_RESP_CHALLENGE_RANK_SWAP (Packet):
	pass
class GC_SHOW_LIVEBROADCAST_RED (Packet):
	pass
class CG_REQ_TIANSHU_RECOMMEND (Packet):
	pass
class GC_RESP_TIANSHU_RECOMMEND (Packet):
	pass
class CG_SHILIAN_FIGHT (Packet):
	pass
class CG_REQ_FRIEND_RANK (Packet):
	pass
class CG_SYNC_SCREEN_ORI (Packet):
	pass
class CG_GUILDTEAM_APPLYFASTTEAM (Packet):
	pass
class CG_GUILDTEAM_SETMEMBERJOB (Packet):
	pass
class CG_GUILDTEAM_APPLYJIONTEAM (Packet):
	pass
class CG_REQ_EVERYDAYBANK_GET_AWARD (Packet):
	pass
class GC_SYNC_EVERYDAYBANK_INFO (Packet):
	pass
class CG_TREASURE_COMPASS_DRAW (Packet):
	pass
class GC_TREASURE_COMPASS_DRAW_RET (Packet):
	pass
class GC_SYNC_TREASRE_COMPASS_INFO (Packet):
	pass
class CG_GUILDTEAM_AWARD (Packet):
	pass
class GC_SYNC_CHARM_VALUE (Packet):
	pass
class CG_ASK_NOTIFICATION_REWARD (Packet):
	pass
class GC_SYNC_NOTIFICATION_REWARD_INFO (Packet):
	pass
class CG_REQ_CHARM_BUYITEM (Packet):
	pass
class GC_SYNC_CHARM_LIMITINFO (Packet):
	pass
class GC_SERVANT_SYNC_FATE (Packet):
	pass
class CG_REQ_FASHION_FREEDOM_DYE (Packet):
	pass
class GC_RET_FASHION_FREEDOM_DYE (Packet):
	pass
class CG_REQ_BWGW_SIGN_UP (Packet):
	pass
class CG_DRAW_BWGW_REWARD (Packet):
	pass
class CG_REQ_BWGW_SELF_RANK (Packet):
	pass
class GC_RET_BWGW_SELF_RANK_DATA (Packet):
	pass
class CG_REQ_REJOIN_BWGW_SCENE (Packet):
	pass
class GC_SYNC_BWGW_ACTIVITY_DATA (Packet):
	pass
class GC_SYNC_BWGW_ARMY_BLOCK (Packet):
	pass
class GC_BWGW_MATCH_RESULT (Packet):
	pass
class CG_REQ_BWGW_JOIN_ARMY (Packet):
	pass
class CG_AGREE_BWGW_JOIN_ARMY (Packet):
	pass
class CG_REQ_REJOIN_BWGW_COPYSCENE (Packet):
	pass
class CG_REQ_BWGW_REWARD (Packet):
	pass
class CG_WD_OPENWDUI (Packet):
	pass
class GC_WD_RETURNDATA (Packet):
	pass
class CG_WD_BUYWD (Packet):
	pass
class CG_WD_UPGRADEINFO (Packet):
	pass
class GC_WD_UPGRADEINFO (Packet):
	pass
class CG_WD_TRUE_UPGRADE (Packet):
	pass
class CG_WD_GETLOGINREWARD (Packet):
	pass
class CG_WD_GETBOXREWARD (Packet):
	pass
class CG_WD_GETALLREWARD (Packet):
	pass
class GC_WD_ISVALIDBUY (Packet):
	pass
class CG_WD_BUQIAN (Packet):
	pass
class CG_GET_COTWARMUP_REWARD (Packet):
	pass
class GC_SYNC_PHOTOFRAME (Packet):
	pass
class CG_REQ_SET_PHOTOFRAME (Packet):
	pass
class GC_SYNC_COTWARMUP_REWARD (Packet):
	pass
class CG_REQUEST_VIEW_BWPPGAME (Packet):
	pass
class CG_QIXISTAR_TEAM_INVITE (Packet):
	pass
class CG_QIXISTAR_TEAM_RESPONSE (Packet):
	pass
class GC_SYNC_QIXISTAR_TEAM_INVITE_LIST (Packet):
	pass
class GC_QIXISTAR_DISMISS (Packet):
	pass
class CG_QIXISTAR_UNLOCK (Packet):
	pass
class CG_QIXISTAR_SAVE_MUSIC (Packet):
	pass
class GC_SYNC_QIXISTAR_STARS_INFO (Packet):
	pass
class CG_QIXISTAR_ASK_REWARD (Packet):
	pass
class GC_SYNC_QIXISTAR_REWARD_STATE (Packet):
	pass
class CG_PICK_FREEDOM_COLOR_ITEM_STORAGE (Packet):
	pass
class GC_SYNC_QIXISTAR_MATE (Packet):
	pass
class CG_QIXISTAR_DISMISS (Packet):
	pass
class CG_GOBACK_BWPP_COPYSCENE (Packet):
	pass
class GC_SYNC_GOBACK_BWPP_COPYSCENE_DATA (Packet):
	pass
class GC_SYNC_NEWPLAYECATCH_DATA (Packet):
	pass
class CG_GET_NEWPLAYERCATCH_REWARD (Packet):
	pass
class GC_SYNC_QIXISTAR_HISTORY_MUSIC (Packet):
	pass
class GC_QL_SYNCDATA (Packet):
	pass
class CG_QL_GETREWARD (Packet):
	pass
class GC_SYNC_SERVERCATCH_DATA (Packet):
	pass
class GC_RET_UNLOCK_PHOTOFRAME (Packet):
	pass
class GC_CHATHISTORY (Packet):
	pass
class GC_SYNC_SERVER_TREASURE_COMPASS_RECORD (Packet):
	pass
class GC_PLAY_SKILLRANGE_EFFECT (Packet):
	pass
class GC_SYNC_ZC_TASK_INFO (Packet):
	pass
class GC_SYNC_ZC_PIECE_INFO (Packet):
	pass
class GC_SYNC_ZC_TICKET_INFO (Packet):
	pass
class CG_ZC_ASK_REWARD (Packet):
	pass
class CG_ZC_PIECE_OP (Packet):
	pass
class GC_ZC_PIECE_OP_RET (Packet):
	pass
class GC_SYNC_ZC_ASKER_LIST (Packet):
	pass
class GC_SYNC_ZC_STAGEREWARD_INFO (Packet):
	pass
class CG_USE_CLIENTDIR_FORSKILL (Packet):
	pass
class CG_FAIRY_SKILL_INHERIT (Packet):
	pass
class GC_SYNC_NEW_FIRST_RECHARGE_DATA (Packet):
	pass
class CG_GET_NEW_FIRST_RECHARGE_REWARD (Packet):
	pass
class GC_SYNC_COLLECTION_SHOP_INFO (Packet):
	pass
class CG_REQ_BUY_COLLECTION_SHOP_ITEM (Packet):
	pass
class GC_NOTICE_NEW_FIRST_RECHARGE_WINDOW (Packet):
	pass
class CG_REQ_CHANGEREMAKENAME_ZJN (Packet):
	pass
class GC_CHANGEREMAKENAME_RET_ZJN (Packet):
	pass
class CG_REQ_CHANGEREMAKENAME (Packet):
	pass
class GC_CHANGEREMAKENAME_RET (Packet):
	pass
class GC_SYNC_LEVELATTRIBUTE (Packet):
	pass
class GC_SYNC_DISCOUNT_LIMIT_DATA (Packet):
	pass
class CG_GET_DISCOUNTLIMIT_ACCUMULATE_REWARD (Packet):
	pass
class CG_GET_DISCOUNTLIMIT_GIFT_REWARD (Packet):
	pass
class GC_NOTICE_DISCOUNTLIMIT_WINDOW (Packet):
	pass
class GC_SYNC_TIANSHUBOX (Packet):
	pass
class GC_RET_UNLOCK_TIANSHUBOX (Packet):
	pass
class CG_TIANSHUBOX_FILL (Packet):
	pass
class GC_RET_TIANSHUBOX_FILL (Packet):
	pass
class CG_TIANSHUBOX_LEVELUP (Packet):
	pass
class GC_RET_TIANSHUBOX_LEVELUP (Packet):
	pass
class CG_ADD_FAIRY_ATTR_POINTS_TEMP (Packet):
	pass
class GC_ADD_FAIRY_ATTR_POINTS_TEMP (Packet):
	pass
class GC_SYNC_BROTHERHOOD_SELF_INFO (Packet):
	pass
class CG_BROTHERHOOD_ASK_REWARD (Packet):
	pass
class CG_BROTHERHOOD_LOG (Packet):
	pass
class GC_BROTHERHOOD_LOG (Packet):
	pass
class GC_SYNC_POJUNQISHA_ENERGY_INFO (Packet):
	pass
class GC_SYNC_FANGONG_HELP_INFO (Packet):
	pass
class CG_REQUEST_SERVANTEQUIP_LASTRECAST_INFO (Packet):
	pass
class GC_RET_SERVANTEQUIP_LASTRECAST_INFO (Packet):
	pass
class CG_GET_ERUDITE_REWARD (Packet):
	pass
class CG_GET_KABINETT_ANECDOTE_TREWARD (Packet):
	pass
class GC_SYNC_KABINETT_INFO (Packet):
	pass
class CG_FV_LOBBY_OPERATE (Packet):
	pass
class GC_XINPO_INFO (Packet):
	pass
class CG_USE_BINGXUEJIE_SNOWBALL (Packet):
	pass
class GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS (Packet):
	pass
class GC_FIXED_CAMERA (Packet):
	pass
class CG_CPS_PICKUP (Packet):
	pass
class CG_REQ_BINGXUEJIE_SNOWMAN_DAILY_AWARD (Packet):
	pass
class CG_REQ_BINGXUEJIE_SNOWMAN_PROGRESS_AWARD (Packet):
	pass
class GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS_AWARD (Packet):
	pass
class GC_SYNC_BINGXUEJIE_QUIZ_RECORD (Packet):
	pass
class CG_TRIGGER_SPECIAL_NPC (Packet):
	pass
class CG_REQ_BINGXUEJIE_QUIZ_DAILY_AWARD (Packet):
	pass
class CG_REQ_BINGXUEJIE_QUIZ_BEST_AWARD (Packet):
	pass
class GC_FV_COPYSCENE_NOTICE (Packet):
	pass
class GC_FV_RESULT (Packet):
	pass
class GC_FV_RANKMINIINFO (Packet):
	pass
class GC_FV_RANK_FULLINFO (Packet):
	pass
class CG_FV_REQ_RANK_FULLINFO (Packet):
	pass
class GC_FV_SKILL_LIST (Packet):
	pass
class CG_FV_USE_SKILL (Packet):
	pass
class GC_FV_CYBYINFO (Packet):
	pass
class CG_SERVANTEQUIP_ITEM (Packet):
	pass
class CG_UNSERVANTEQUIP_ITEM (Packet):
	pass
class CG_UPGRADE_XINPO (Packet):
	pass
class GC_FV_NPCINFO (Packet):
	pass
class GC_BROADCAST_BINGXUEJIE_QUIZ_RESULT (Packet):
	pass
class CG_WUXING_SHORTCUT_AFFIX (Packet):
	pass
class GC_WUXING_SHORTCUT_AFFIX (Packet):
	pass
class CG_WUXING_SHORTCUT_FIGHT (Packet):
	pass
class CG_TREASURE_COMPASS_RESET (Packet):
	pass
class GC_TREASURE_COMPASS_RESET_RET (Packet):
	pass
class CG_REQ_NEWBIEBANK_GET_AWARD (Packet):
	pass
class GC_SYNC_NEWBIEBANK_INFO (Packet):
	pass
class CG_ITEM_SUBSCRIBE_OPERATION (Packet):
	pass
class GC_SYNC_ITEM_SUBSCRIBE (Packet):
	pass
class GC_HONGBAO_COVER (Packet):
	pass
class CG_HONGBAO_COVER_OP (Packet):
	pass
class GC_HONGYUN_INFO (Packet):
	pass
class CG_HONGYUN_RECEIVE (Packet):
	pass
class GC_SYNC_GUILDVAULTDATA_ALL (Packet):
	pass
class GC_SYNC_GUILDVAULTDATA_SIMPLE (Packet):
	pass
class CG_DONATIONGUILDCASHGIFT (Packet):
	pass
class GC_DONATIONGUILDCASHGIFT_RET (Packet):
	pass
class CG_GUILDVAULT_LOTTERY (Packet):
	pass
class CG_GUILDVAULT_LOTTERY_RET (Packet):
	pass
class GC_GUILDVAULT_LOTTERY_RET (Packet):
	pass
class CG_BWGW_FASTCOMMAND (Packet):
	pass
class GC_BWGW_BATTLE_INFO (Packet):
	pass
class CG_BWGW_REQ_PLAYER_DETAIL (Packet):
	pass
class GC_BWGW_BATTLE_DETAIL (Packet):
	pass
class CG_SET_BWGW_MAINSCENE_GUILDROLE (Packet):
	pass
class GC_BWGW_MAINSCENE_GUILDROLE (Packet):
	pass
class CG_GET_BWGW_GUILD_WAR_SCENEINFO (Packet):
	pass
class GC_BWGW_GUILD_WAR_SCENEINFO (Packet):
	pass
class CG_ENTER_BWGW_GUILD_WAR_SCENE (Packet):
	pass
class GC_BWGW_RES_UPDATE (Packet):
	pass
class CG_BWGW_USESKILL (Packet):
	pass
class CG_CBZL_GETEXP (Packet):
	pass
class CG_CBZL_GETLEVELREWARD (Packet):
	pass
class GC_CBZL_ALLINFO (Packet):
	pass
class GC_CBZL_TASKINFO (Packet):
	pass
class GC_BWGW_MATCH_FIGHT_DATA (Packet):
	pass
class CG_BWGW_MATCH_FIGHT_DATA (Packet):
	pass
class CG_REQ_ITEM_SUBSCRIBE_BUY (Packet):
	pass
class GC_Sync_All_TXMQ_Info (Packet):
	pass
class CG_TXMQ_OP (Packet):
	pass
class GC_SYNC_HONGBAO_INFO (Packet):
	pass
class CG_HONGBAO_REQ_INFO (Packet):
	pass
class GC_SYNC_SERVER_ROOKIE_COMPASS_RECORD (Packet):
	pass
class CG_BWGW_GET_MAIN_SCENE_LIMIT_INFO (Packet):
	pass
class GC_SYNC_PERIODBESTSELLER_DATA (Packet):
	pass
class GC_NPC_SHOW_TARGETHEADINFO (Packet):
	pass
class CG_USE_COTCOIN (Packet):
	pass
class GC_SERVANT_DRAW_BOX_CONFIG (Packet):
	pass
class GC_SERVANT_DRAW_SET_CONFIG (Packet):
	pass
class GC_SERVANT_DRAW_SELF_INFO (Packet):
	pass
class CG_SERVANT_DRAW (Packet):
	pass
class GC_SERVANT_DRAW_RESULT (Packet):
	pass
class CG_REQ_SWITCH_TYPE_BATTLE_SCHEME (Packet):
	pass
class CG_REQ_SWITCH_MAIN_BATTLE_SCHEME (Packet):
	pass
class CG_REQ_MODIFY_MAIN_BATTLE_SCHEME (Packet):
	pass
class CG_REQ_CHANGE_BATTLE_SCHEME_NAME (Packet):
	pass
class GC_SYNC_BATTLE_SCHEME (Packet):
	pass
class CG_SERVANT_DRAW_BUY (Packet):
	pass
class GC_SYNC_ONLINEREMINDER (Packet):
	pass
class GC_SYNC_ACTIVITYNIGHTGUIDEINFO (Packet):
	pass
class CG_HAVECLICK_ACTIVITYNIGHTGUIDE (Packet):
	pass
class CG_GETREWARD_ACTIVITYNIGHTGUIDE (Packet):
	pass
class GC_SCENE_TOGGLE_OBJ (Packet):
	pass
class GC_RET_SWITCH_MAIN_BATTLE_SCHEME (Packet):
	pass
class CG_SERVANT_DRAW_SET_PRAY (Packet):
	pass
class GC_SERVANT_DRAW_RSP_SET_PRAY (Packet):
	pass
class CG_HAVECLICK_ACTIVITYNIGHTPAPERTIP (Packet):
	pass
class CG_GET_DOMAIN_SEASON_REWARD (Packet):
	pass
class CG_GET_DOMAIN_SEASON_PLAYER_REWARD (Packet):
	pass
class CG_HUAGUANJIE_SEND_GIFT (Packet):
	pass
class GC_HUAGUANJIE_PLAY_EFFECT (Packet):
	pass
class CG_ASK_GREETING_REWARD (Packet):
	pass
class CG_REQ_GIFT_LIST (Packet):
	pass
class GC_RET_GIFT_LIST (Packet):
	pass
class GC_SYNC_HUAGUANJIE_EXCHANGE_SHOP_INFO (Packet):
	pass
class CG_REQ_BUY_HUAGUANJIE_EXCHANGE_ITEM (Packet):
	pass
class CG_ASK_ANSWERACTIVITY_INFO (Packet):
	pass
class CG_ASK_ANSWERACTIVITY_QUESTION (Packet):
	pass
class GC_SYNC_ANSWERACTIVITY_INFO (Packet):
	pass
class GC_SYNC_ANSWERACTIVITY_QUESTION (Packet):
	pass
class CG_DOMAINWAR_SHOP_BUY (Packet):
	pass
class GC_DOMAINWAR_SHOP_RECORD (Packet):
	pass
class CG_DOMAINWAR_GET_SALARY (Packet):
	pass
class CG_DOMAINWAR_LIMIT_SHOP_BUY (Packet):
	pass
class CG_REQ_UNLOCK_WARPATHBUFF (Packet):
	pass
class CG_REQ_HUANGUANJIE_XINYILEGOU (Packet):
	pass
class GC_SYNC_HUAGUANJIE_XINYILEGOU (Packet):
	pass
class CG_GUILDMERGE_INVITE (Packet):
	pass
class GC_GUILDMERGE_INVITE_LIST (Packet):
	pass
class CG_GUILDMERGE_PREVIEW (Packet):
	pass
class GC_GUILDMERGE_PREVIEW_RET (Packet):
	pass
class CG_GUILDMERGE_OPTION (Packet):
	pass
class GC_GUILDMERGE_OPTION_RESULT (Packet):
	pass
class GC_SYNC_HUAGUANJIE_ACT_INFO (Packet):
	pass
class GC_SYNC_SIGNETNINGLIAN_DATA (Packet):
	pass
class CG_REQ_SIGNETNINGLIAN (Packet):
	pass
class CG_REQ_SIGNETNINGLIAN_REPLACE (Packet):
	pass
class GC_SYNC_WARPATHBUFF_LIST (Packet):
	pass
class GC_DOMAINWAR_INFO_DATA (Packet):
	pass
class GC_DOMAINWAR_SEASON_INFO_DATA (Packet):
	pass
class GC_DOMAINWAR_SERVER_LIMIT_SHOP_DATA (Packet):
	pass
class CG_DOMAINWAR_SERVER_LIMIT_SHOP_DATA (Packet):
	pass
class GC_HUAGUANJIE_SEND_GIFT (Packet):
	pass
class GC_SKILLZHUANJING_OPEN_RET (Packet):
	pass
class CG_ASK_ALL_ROUND_GREETING_REWARD (Packet):
	pass
class GC_SYNC_DAOYI (Packet):
	pass
class CG_REQ_STALL_COUNT (Packet):
	pass
class GC_RET_STALL_COUNT (Packet):
	pass
class CG_LINGSHI_BOARD_INSTALL (Packet):
	pass
class CG_LINGSHI_BOARD_UNINSTALL (Packet):
	pass
class CG_LINGSHI_BOARD_UNINSTALL_ALL (Packet):
	pass
class CG_LINGSHI_BOARD_CHANGEPOS (Packet):
	pass
class CG_LINGSHI_BOARD_LEVELUP (Packet):
	pass
class GC_SYNC_LINGSHIBOARD_INFO (Packet):
	pass
class CG_TEAM_AUTO_FIGHT (Packet):
	pass
class GC_ChronoTriggerSelfInfo (Packet):
	pass
class GC_ChronoTriggerTalentTree (Packet):
	pass
class CG_ChronoTriggerTalentLvlUp (Packet):
	pass
class CG_ChronoTriggerFight (Packet):
	pass
class GC_ChronoTriggerLineInfo (Packet):
	pass
class CG_ChronoTriggerSelectServant (Packet):
	pass
class GC_ChronoTriggerSelectServant (Packet):
	pass
class GC_ChroroTriggerSelectServantInfo (Packet):
	pass
class GC_ChronoTriggerGlobalData (Packet):
	pass
class GC_ChronoTriggerSelectBlessCard (Packet):
	pass
class CG_ChronoTriggerSelectBlessCard (Packet):
	pass
class GC_ChronoTriggerSelectBlessCardInfo (Packet):
	pass
class CG_ChronoTriggerSelectBoss (Packet):
	pass
class GC_ChronoTriggerSelectBossInfo (Packet):
	pass
class GC_ChronoTriggerResult (Packet):
	pass
class CG_ChronoTriggerGetSeasonAward (Packet):
	pass
class CG_LINGSHI_REDUCTION (Packet):
	pass
class GC_ChronoTriggerSeasonAwardGetInfo (Packet):
	pass
class GC_ChronoTriggerServantCall_Sync (Packet):
	pass
class GC_SYNC_BACKGROUNDPHOTO (Packet):
	pass
class CG_REQ_SET_BACKGROUNDPHOTO (Packet):
	pass
class CG_DIMAI_ENTERMIJING (Packet):
	pass
class GC_ChronoTriggerSelectBossPlayersInfo (Packet):
	pass
class GC_ChronoTriggerSelectBossSuccess (Packet):
	pass
class GC_ChronoTriggerCommand (Packet):
	pass
class GC_DIMAIMIJING_FIGHT_TIME (Packet):
	pass
class GC_SYNC_CP_ACT_INFO (Packet):
	pass
class GC_SYNC_CP_SKILLZHUANJINGINFO (Packet):
	pass
class GC_DOMAINWAR_CAR_INFO_SYNC (Packet):
	pass
class LABLE_MAX_PACKET_ID (Packet):
	pass




