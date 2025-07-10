# -*- coding: utf-8 -*-
import struct

from .Packet import Packet
import loadlog


class XX_REQUEST_HEARTBEAT (Packet):
    def handle(self):
        # begin handle [XX_REQUEST_HEARTBEAT] message attrs, auto generate do not change
        self.person['ansi_time'] = self['ansi_time']
        print("received XX_REQUEST_HEARTBEAT")
        # end handle [XX_REQUEST_HEARTBEAT] message attrs, auto generate do not change
        self.person.ActionXX_RESPONSE_HEARTBEAT()


class GC_LOGIN_RET (Packet):
    def handle(self):
        # begin handle [GC_LOGIN_RET] message attrs, auto generate do not change
        self.person['loginresult'] = self['result']

        self.person['validateprocessfailcode'] = self['validateprocessfailcode']
        self.person['validatefailcode'] = self['validatefailcode']
        self.person['validatefailmsg'] = self['validatefailmsg']
        self.person['rapidvalidatecode'] = self['rapidvalidatecode']
        self.person['roleguidlist'] = self['roleguidlist']
        self.person['rolenamelist'] = self['rolenamelist']
        self.person['roleprofessionlist'] = self['roleprofessionlist']
        self.person['rolelevellist'] = self['rolelevellist']
        self.person['rolesexlist'] = self['rolesexlist']
        self.person['rolehairvisuallist'] = self['rolehairvisuallist']
        self.person['rolefacevisuallist'] = self['rolefacevisuallist']
        self.person['roleweaponvisuallist'] = self['roleweaponvisuallist']
        self.person['rolebodyvisuallist'] = self['rolebodyvisuallist']
        self.person['roleweaponrefinevisuallist'] = self['roleweaponrefinevisuallist']
        self.person['createfirstroledependentactivation'] = self['createfirstroledependentactivation']
        self.person['platformrestrictnotice'] = self['platformrestrictnotice']
        self.person['isinbigworld'] = self['isinbigworld']
        self.person['isconnectbigworld'] = self['isconnectbigworld']
        self.person['rolebodycoloreffectvisual'] = self['rolebodycoloreffectvisual']
        self.person['rolenierenlist'] = self['rolenierenlist']
        self.person['rolefashionlist'] = self['rolefashionlist']
        self.person['gemsetid'] = self['gemsetid']
        self.person['skillTransID'] = self['skillTransID']
        self.person['haveprecreateinfo'] = self['haveprecreateinfo']
        self.person['precreatename'] = self['precreatename']
        self.person['precreatevisualid'] = self['precreatevisualid']
        self.person['precreateprofession'] = self['precreateprofession']
        self.person['showhelmet'] = self['showhelmet']
        self.person['precreaterolesex'] = self['precreaterolesex']
        self.person['showtail'] = self['showtail']
        self.person['nxPvpWorldType'] = self['nxPvpWorldType']
        self.person['showear'] = self['showear']
        # end handle [GC_LOGIN_RET] message attrs, auto generate do not change
        loadlog.debug(__class__.__name__ + " [ " + str(self.obj) + "]")


class GC_SESSION (Packet):
    def __init__(self, person):
        super(GC_SESSION, self).__init__(person)
        loadlog.debug(self.obj)

    def handle(self):
        # begin handle [GC_SESSION] message attrs, auto generate do not change
        self.person['session'] = bytes(str(self['session']), 'utf8')
        self.person['realworldid'] = self['realworldid']
        # end handle [GC_SESSION] message attrs, auto generate do not change
        # print("[GC_SESSION]" + str(str(self['session'])))
        pass


class XX_RESPONSE_HEARTBEAT (Packet):
    pass


class CG_REQUEST_PRAYEXP_SYNC (Packet):
    pass


class CG_URGE_MASTER_PUBLISH_MENTOR_TASK (Packet):
    pass


class GC_SYN_FAIRY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYN_FAIRY_INFO] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['curHpRate'] = self['curHpRate']
        self.person['isDie'] = self['isDie']
        self.person['lastDeadTime'] = self['lastDeadTime']
        # end handle [GC_SYN_FAIRY_INFO] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_REQ_INFO (Packet):
    pass


class GC_RET_SIGNININFO_DAYLY (Packet):
    def handle(self):
        # begin handle [GC_RET_SIGNININFO_DAYLY] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        self.person['index'] = self['index']
        self.person['status'] = self['status']
        self.person['reserved'] = self['reserved']
        self.person['Exp'] = self['Exp']
        self.person['Jinbin'] = self['Jinbin']
        self.person['Yinbin'] = self['Yinbin']
        self.person['Yuanbao'] = self['Yuanbao']
        self.person['BindYuanbao'] = self['BindYuanbao']
        self.person['Item1DataID'] = self['Item1DataID']
        self.person['Item1Count'] = self['Item1Count']
        self.person['Item2DataID'] = self['Item2DataID']
        self.person['Item2count'] = self['Item2count']
        self.person['supplySignCost'] = self['supplySignCost']
        self.person['curNaturalIndex'] = self['curNaturalIndex']
        self.person['curMounthIndex'] = self['curMounthIndex']
        self.person['firstCanSignIndex'] = self['firstCanSignIndex']
        self.person['alreadySignedCount'] = self['alreadySignedCount']
        self.person['signedToday'] = self['signedToday']
        self.person['supplySignCount'] = self['supplySignCount']
        self.person['supplySignedToday'] = self['supplySignedToday']
        self.person['allowShow'] = self['allowShow']
        self.person['allowSign'] = self['allowSign']
        self.person['totalSupplyCount'] = self['totalSupplyCount']
        # end handle [GC_RET_SIGNININFO_DAYLY] message attrs, auto generate do not change
        pass


class CG_REQUEST_FIRSTRECHARGE_BONUS (Packet):
    pass


class GC_RES_JIANMUXB_INFO (Packet):
    def handle(self):
        # begin handle [GC_RES_JIANMUXB_INFO] message attrs, auto generate do not change
        self.person['slots'] = self['slots']
        self.person['usedHelpTimes'] = self['usedHelpTimes']
        self.person['getRewardLv'] = self['getRewardLv']
        self.person['openUI'] = self['openUI']
        self.person['addSilvers'] = self['addSilvers']
        self.person['addExps'] = self['addExps']
        self.person['guildContributes'] = self['guildContributes']
        # end handle [GC_RES_JIANMUXB_INFO] message attrs, auto generate do not change
        pass


class GC_MILITARY_SYNC_MILITARYRANK (Packet):
    def handle(self):
        # begin handle [GC_MILITARY_SYNC_MILITARYRANK] message attrs, auto generate do not change
        self.person['getBadge'] = self['getBadge']
        self.person['militaryRank'] = self['militaryRank']
        # end handle [GC_MILITARY_SYNC_MILITARYRANK] message attrs, auto generate do not change
        pass


class GC_RET_MATCH_OP (Packet):
    def handle(self):
        # begin handle [GC_RET_MATCH_OP] message attrs, auto generate do not change
        self.person['activityId'] = self['activityId']
        self.person['optype'] = self['optype']
        self.person['param'] = self['param']
        # end handle [GC_RET_MATCH_OP] message attrs, auto generate do not change
        pass


class GC_REQUEST_INTERACT (Packet):
    def handle(self):
        # begin handle [GC_REQUEST_INTERACT] message attrs, auto generate do not change
        self.person['inviterServerID'] = self['inviterServerID']
        self.person['interactType'] = self['interactType']
        # end handle [GC_REQUEST_INTERACT] message attrs, auto generate do not change
        pass


class GC_GIVESIGN_FORPICDEL (Packet):
    def handle(self):
        # begin handle [GC_GIVESIGN_FORPICDEL] message attrs, auto generate do not change
        self.person['fileId'] = self['fileId']
        self.person['sign'] = self['sign']
        self.person['bucketname'] = self['bucketname']
        self.person['appid'] = self['appid']
        self.person['reqSignType'] = self['reqSignType']
        # end handle [GC_GIVESIGN_FORPICDEL] message attrs, auto generate do not change
        pass


class GC_SYNC_HUANGHUNSHENGDAN_COPY_SCENE_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HUANGHUNSHENGDAN_COPY_SCENE_STATE] message attrs, auto generate do not change
        self.person['copySceneState'] = self['copySceneState']
        # end handle [GC_SYNC_HUANGHUNSHENGDAN_COPY_SCENE_STATE] message attrs, auto generate do not change
        pass


class GC_DOMAIN_SYNC_LINEEVT (Packet):
    def handle(self):
        # begin handle [GC_DOMAIN_SYNC_LINEEVT] message attrs, auto generate do not change
        self.person['syncType'] = self['syncType']
        self.person['evtType'] = self['evtType']
        self.person['evtTime'] = self['evtTime']
        self.person['szParam'] = self['szParam']
        self.person['param1'] = self['param1']
        self.person['guidParam'] = self['guidParam']
        self.person['posParam'] = self['posParam']
        self.person['objId'] = self['objId']
        # end handle [GC_DOMAIN_SYNC_LINEEVT] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_DELETE_ALL_RECRUIT_APPLY (Packet):
    pass


class GC_MISSION_SYNC_LIST (Packet):
    def handle(self):
        # begin handle [GC_MISSION_SYNC_LIST] message attrs, auto generate do not change
        self.person['Missions'] = self['Missions']
        self.person['DoneFlag'] = self['DoneFlag']
        # end handle [GC_MISSION_SYNC_LIST] message attrs, auto generate do not change
        pass


class CG_ACCLOGIN_ASKINFO (Packet):
    pass


class GC_RES_MENTOR_RECURIT (Packet):
    def handle(self):
        # begin handle [GC_RES_MENTOR_RECURIT] message attrs, auto generate do not change
        # end handle [GC_RES_MENTOR_RECURIT] message attrs, auto generate do not change
        pass


class CG_REQ_GUILDCONVOY_FOLLOW (Packet):
    pass


class GC_TONGTIANTREASURE_RETOP (Packet):
    def handle(self):
        # begin handle [GC_TONGTIANTREASURE_RETOP] message attrs, auto generate do not change
        self.person['optype'] = self['optype']
        self.person['mapid'] = self['mapid']
        self.person['param1'] = self['param1']
        # end handle [GC_TONGTIANTREASURE_RETOP] message attrs, auto generate do not change
        pass


class GC_NOTICE_CONST (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_CONST] message attrs, auto generate do not change
        self.person['notice'] = self['notice']
        self.person['bShow'] = self['bShow']
        # end handle [GC_NOTICE_CONST] message attrs, auto generate do not change
        pass


class CG_ASK_TGCFAWARD (Packet):
    pass


class CG_CLIENT_BEHAVIOR (Packet):
    pass


class GC_ISINSELFWILDDUELLIST (Packet):
    def handle(self):
        # begin handle [GC_ISINSELFWILDDUELLIST] message attrs, auto generate do not change
        self.person['tarGuid'] = self['tarGuid']
        self.person['IsInSelfDuelList'] = self['IsInSelfDuelList']
        # end handle [GC_ISINSELFWILDDUELLIST] message attrs, auto generate do not change
        pass


class CG_STALL_REVIEW_DELETE (Packet):
    pass


class CG_SINGLE_INTERACT (Packet):
    pass


class GC_ISINTARGETWILDDUELLIST (Packet):
    def handle(self):
        # begin handle [GC_ISINTARGETWILDDUELLIST] message attrs, auto generate do not change
        self.person['tarGuid'] = self['tarGuid']
        self.person['IsInTargetDuelList'] = self['IsInTargetDuelList']
        # end handle [GC_ISINTARGETWILDDUELLIST] message attrs, auto generate do not change
        pass


class GC_SHOW_ITEMPROMPT (Packet):
    def handle(self):
        # begin handle [GC_SHOW_ITEMPROMPT] message attrs, auto generate do not change
        self.person['Item'] = self['Item']
        self.person['PromptType'] = self['PromptType']
        self.person['DelayShowType'] = self['DelayShowType']
        # end handle [GC_SHOW_ITEMPROMPT] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_RECRUIT_MY (Packet):
    pass


class CG_BROTHERHOOD_RANK_INFO (Packet):
    pass


class GC_PRESTIGE_NEWREWARD (Packet):
    def handle(self):
        # begin handle [GC_PRESTIGE_NEWREWARD] message attrs, auto generate do not change
        self.person['ForceId'] = self['ForceId']
        self.person['RelationId'] = self['RelationId']
        # end handle [GC_PRESTIGE_NEWREWARD] message attrs, auto generate do not change
        pass


class GC_BUFF_REMOVE_INFO (Packet):
    def handle(self):
        # begin handle [GC_BUFF_REMOVE_INFO] message attrs, auto generate do not change
        self.person['charID'] = self['charID']
        self.person['uID'] = self['uID']
        # end handle [GC_BUFF_REMOVE_INFO] message attrs, auto generate do not change
        pass


class GC_RES_PET_SUMMON_OR_CALLBACK (Packet):
    def handle(self):
        # begin handle [GC_RES_PET_SUMMON_OR_CALLBACK] message attrs, auto generate do not change
        self.person['isSummon'] = self['isSummon']
        self.person['petObjID'] = self['petObjID']
        # end handle [GC_RES_PET_SUMMON_OR_CALLBACK] message attrs, auto generate do not change
        pass


class CG_TIANSHU_COMPOSE (Packet):
    pass


class CG_GUILD_DIG_UP_THE_HATCHET (Packet):
    pass


class CG_ASK_FOLLOW (Packet):
    pass


class GC_SYNC_RUBKI_CUBE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RUBKI_CUBE_INFO] message attrs, auto generate do not change
        self.person['cubeInfos'] = self['cubeInfos']
        self.person['curRubkiCubeId'] = self['curRubkiCubeId']
        self.person['teamId'] = self['teamId']
        # end handle [GC_SYNC_RUBKI_CUBE_INFO] message attrs, auto generate do not change
        pass


class GC_MIDAS_REQUEST_BALANCE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_MIDAS_REQUEST_BALANCE_RESULT] message attrs, auto generate do not change
        self.person['result'] = self['result']
        # end handle [GC_MIDAS_REQUEST_BALANCE_RESULT] message attrs, auto generate do not change
        pass


class GC_TIANSHU_MASTER_INFO (Packet):
    def handle(self):
        # begin handle [GC_TIANSHU_MASTER_INFO] message attrs, auto generate do not change
        self.person['tianshuDataId'] = self['tianshuDataId']
        self.person['tianshuLevel'] = self['tianshuLevel']
        # end handle [GC_TIANSHU_MASTER_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_SERVANT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SERVANT] message attrs, auto generate do not change
        self.person['servantInfos'] = self['servantInfos']
        self.person['slotData'] = self['slotData']
        self.person['synctype'] = self['synctype']
        self.person['curSchemeId'] = self['curSchemeId']
        # end handle [GC_SYNC_SERVANT] message attrs, auto generate do not change
        pass


class CG_ASK_AUTOTEAM_QUIT_BW (Packet):
    pass


class GC_RET_FRIEND_USERINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_FRIEND_USERINFO] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['Name'] = self['Name']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['reserved'] = self['reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['ArmyId'] = self['ArmyId']
        self.person['TeamId'] = self['TeamId']
        self.person['TowerFloor'] = self['TowerFloor']
        self.person['TowerTime'] = self['TowerTime']
        self.person['AddDatas'] = self['AddDatas']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['HaveNewPlayerCatch'] = self['HaveNewPlayerCatch']
        # end handle [GC_RET_FRIEND_USERINFO] message attrs, auto generate do not change
        pass


class CG_EXAM_ANSWERQUESTION (Packet):
    pass


class GC_JXGZAWARD_DATA (Packet):
    def handle(self):
        # begin handle [GC_JXGZAWARD_DATA] message attrs, auto generate do not change
        self.person['AwardID'] = self['AwardID']
        self.person['LeftTime'] = self['LeftTime']
        self.person['IsStart'] = self['IsStart']
        # end handle [GC_JXGZAWARD_DATA] message attrs, auto generate do not change
        pass


class CG_GUILD_BINDGROUP_SUCESS (Packet):
    pass


class CG_SWORDTEAM_REQ_LIST (Packet):
    pass


class GC_PLAY_BOSS_PLAYED_PROMPT (Packet):
    def handle(self):
        # begin handle [GC_PLAY_BOSS_PLAYED_PROMPT] message attrs, auto generate do not change
        self.person['BossPlayedPromptId'] = self['BossPlayedPromptId']
        self.person['BossPlayedPromptGroupId'] = self['BossPlayedPromptGroupId']
        # end handle [GC_PLAY_BOSS_PLAYED_PROMPT] message attrs, auto generate do not change
        pass


class CG_REQ_PUBLISH_APPRENTICE_TASK (Packet):
    pass


class GC_RET_YLTXDROP_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_YLTXDROP_INFO] message attrs, auto generate do not change
        self.person['itemIdList'] = self['itemIdList']
        self.person['dropName'] = self['dropName']
        self.person['itemCountList'] = self['itemCountList']
        # end handle [GC_RET_YLTXDROP_INFO] message attrs, auto generate do not change
        pass


class GC_CHAT_REMOVE_GUID (Packet):
    def handle(self):
        # begin handle [GC_CHAT_REMOVE_GUID] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        # end handle [GC_CHAT_REMOVE_GUID] message attrs, auto generate do not change
        pass


class GC_COPYSCENE_INVITEVIEW (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_INVITEVIEW] message attrs, auto generate do not change
        self.person['playerguid'] = self['playerguid']
        self.person['playerstatus'] = self['playerstatus']
        self.person['sceneclass'] = self['sceneclass']
        self.person['grade'] = self['grade']
        self.person['Tier'] = self['Tier']
        self.person['bInit'] = self['bInit']
        self.person['nLayer'] = self['nLayer']
        self.person['nDifficulty'] = self['nDifficulty']
        # end handle [GC_COPYSCENE_INVITEVIEW] message attrs, auto generate do not change
        pass


class GC_GUILD_ALLIANCE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_GUILD_ALLIANCE_RESULT] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        # end handle [GC_GUILD_ALLIANCE_RESULT] message attrs, auto generate do not change
        pass


class CG_REQ_QINGYIVALUE_DAILY_INFO (Packet):
    pass


class GC_RET_RANK (Packet):
    def handle(self):
        # begin handle [GC_RET_RANK] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['curPage'] = self['curPage']
        self.person['totalPage'] = self['totalPage']
        self.person['Reward'] = self['Reward']
        self.person['Guid'] = self['Guid']
        self.person['Name'] = self['Name']
        self.person['Lv'] = self['Lv']
        self.person['Pro'] = self['Pro']
        self.person['Val'] = self['Val']
        self.person['Name2'] = self['Name2']
        self.person['Val2'] = self['Val2']
        self.person['merank'] = self['merank']
        self.person['meReward'] = self['meReward']
        self.person['meName'] = self['meName']
        self.person['meVal'] = self['meVal']
        self.person['meLv'] = self['meLv']
        self.person['mePro'] = self['mePro']
        self.person['meName2'] = self['meName2']
        self.person['meVal2'] = self['meVal2']
        self.person['Guid2'] = self['Guid2']
        self.person['Name3'] = self['Name3']
        self.person['meName3'] = self['meName3']
        self.person['WakeupType'] = self['WakeupType']
        self.person['WakeupBonusTime'] = self['WakeupBonusTime']
        self.person['QQVipType'] = self['QQVipType']
        self.person['QQVipExpireTime'] = self['QQVipExpireTime']
        self.person['meSexType'] = self['meSexType']
        self.person['SexType'] = self['SexType']
        self.person['TeamId'] = self['TeamId']
        self.person['TeamCount'] = self['TeamCount']
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['GuildName'] = self['GuildName']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['FromServerId'] = self['FromServerId']
        # end handle [GC_RET_RANK] message attrs, auto generate do not change
        pass


class GC_TIANSHU_EXCHANGE (Packet):
    def handle(self):
        # begin handle [GC_TIANSHU_EXCHANGE] message attrs, auto generate do not change
        self.person['result'] = self['result']
        # end handle [GC_TIANSHU_EXCHANGE] message attrs, auto generate do not change
        pass


class CG_DW_RETURNHOME (Packet):
    pass


class CG_ASK_SELFROLEVIEWINFO (Packet):
    pass


class CG_TOURNAMENT_OPERATE_MATCH (Packet):
    pass


class GC_ADVENTURE_SYNC_SHOP_OPEN (Packet):
    def handle(self):
        # begin handle [GC_ADVENTURE_SYNC_SHOP_OPEN] message attrs, auto generate do not change
        self.person['time'] = self['time']
        self.person['itemId'] = self['itemId']
        self.person['itemCount'] = self['itemCount']
        # end handle [GC_ADVENTURE_SYNC_SHOP_OPEN] message attrs, auto generate do not change
        pass


class CG_EQUIP_EQUIP_REBIRTH (Packet):
    pass


class CG_LIMITSHOP_BUY (Packet):
    pass


class GC_SYNC_MASK_WORD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MASK_WORD] message attrs, auto generate do not change
        self.person['maskword'] = self['maskword']
        # end handle [GC_SYNC_MASK_WORD] message attrs, auto generate do not change
        pass


class CG_CANCEL_INTERACT (Packet):
    pass


class CG_CDKEY_APPLY (Packet):
    pass


class CG_REQ_GUILDCONVOY_FILL (Packet):
    pass


class GC_SYNC_LIFESKILLCOUNT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_LIFESKILLCOUNT] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['count'] = self['count']
        # end handle [GC_SYNC_LIFESKILLCOUNT] message attrs, auto generate do not change
        pass


class CG_REQ_TEAMMEMBER_APPLY_LEADER (Packet):
    pass


class GC_SYNC_REDPOINT_ONE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_REDPOINT_ONE] message attrs, auto generate do not change
        self.person['redPoint'] = self['redPoint']
        # end handle [GC_SYNC_REDPOINT_ONE] message attrs, auto generate do not change
        pass


class CG_THROW_ITEM (Packet):
    pass


class GC_SYNC_GAMECONFIG (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GAMECONFIG] message attrs, auto generate do not change
        self.person['isgmaccount'] = self['isgmaccount']
        self.person['isopensamsarapre'] = self['isopensamsarapre']
        self.person['mercenarycreateteamtime'] = self['mercenarycreateteamtime']
        self.person['mercenaryrecommendtime'] = self['mercenaryrecommendtime']
        self.person['openmercenary'] = self['openmercenary']
        self.person['realworldid'] = self['realworldid']
        self.person['opencommonrank'] = self['opencommonrank']
        self.person['openvip'] = self['openvip']
        self.person['openfellow'] = self['openfellow']
        self.person['openfellowskill'] = self['openfellowskill']
        self.person['openfellowpoint'] = self['openfellowpoint']
        self.person['openfellowtrain'] = self['openfellowtrain']
        self.person['openfellowstar'] = self['openfellowstar']
        self.person['openfellowkiss'] = self['openfellowkiss']
        self.person['openfellowpicture'] = self['openfellowpicture']
        self.person['forrefineopenscore'] = self['forrefineopenscore']
        self.person['openRefine'] = self['openRefine']
        self.person['openInherit'] = self['openInherit']
        self.person['openEquipLevelUp'] = self['openEquipLevelUp']
        self.person['openLiveSkill'] = self['openLiveSkill']
        self.person['openMonthCardSign'] = self['openMonthCardSign']
        self.person['openFellowStarLevel'] = self['openFellowStarLevel']
        self.person['openworldboss'] = self['openworldboss']
        self.person['OpenCDKEY'] = self['OpenCDKEY']
        self.person['OpenPrayExp'] = self['OpenPrayExp']
        self.person['OpenOldAccountPacket'] = self['OpenOldAccountPacket']
        self.person['OpenZhenMoGuDong'] = self['OpenZhenMoGuDong']
        self.person['OpenFriendPointMileStone'] = self['OpenFriendPointMileStone']
        self.person['openGuild'] = self['openGuild']
        self.person['openGuildCity'] = self['openGuildCity']
        self.person['openFamily'] = self['openFamily']
        self.person['HongBaoRobNeedJoinDay'] = self['HongBaoRobNeedJoinDay']
        self.person['openHongBao'] = self['openHongBao']
        self.person['HongBaoMaxRobGcoinDaily'] = self['HongBaoMaxRobGcoinDaily']
        self.person['HongBaoMaxSendGcoinWeek'] = self['HongBaoMaxSendGcoinWeek']
        self.person['HongBaoMaxRobBindYuanBaoDaily'] = self['HongBaoMaxRobBindYuanBaoDaily']
        self.person['openDailySign'] = self['openDailySign']
        self.person['openFellowSkillLevel'] = self['openFellowSkillLevel']
        self.person['openFellowTrainLevel'] = self['openFellowTrainLevel']
        self.person['openFellowKissLevel'] = self['openFellowKissLevel']
        self.person['openFellowTrainTabPageLevel'] = self['openFellowTrainTabPageLevel']
        self.person['TeamFactorScope'] = self['TeamFactorScope']
        self.person['OpenShouChongWindow'] = self['OpenShouChongWindow']
        self.person['IsOpenAppScore'] = self['IsOpenAppScore']
        self.person['ShowTimeGoods'] = self['ShowTimeGoods']
        self.person['BuyStaminaNeedYuanBao'] = self['BuyStaminaNeedYuanBao']
        self.person['OpenFamilyFriendPointFactor'] = self['OpenFamilyFriendPointFactor']
        self.person['openHuZhu'] = self['openHuZhu']
        self.person['appPushNotification'] = self['appPushNotification']
        self.person['HongBaoMaxChargeSendCountDaily'] = self['HongBaoMaxChargeSendCountDaily']
        self.person['HongBaoMaxChargeOwnCount'] = self['HongBaoMaxChargeOwnCount']
        self.person['HongBaoSendMinGcoinNum'] = self['HongBaoSendMinGcoinNum']
        self.person['HongBaoSendMaxGcoinNum'] = self['HongBaoSendMaxGcoinNum']
        self.person['HongBaoNeedSevenDayActivity'] = self['HongBaoNeedSevenDayActivity']
        self.person['HongBaoNeedSevenDayActivityNum'] = self['HongBaoNeedSevenDayActivityNum']
        self.person['ApprenticeMissionMax'] = self['ApprenticeMissionMax']
        self.person['OrnamentRefineMinLevel'] = self['OrnamentRefineMinLevel']
        self.person['GuildWarWinCon'] = self['GuildWarWinCon']
        self.person['GuildWarLoseCon'] = self['GuildWarLoseCon']
        self.person['OpenSupDrawing'] = self['OpenSupDrawing']
        self.person['IsZhuanSupDraw'] = self['IsZhuanSupDraw']
        self.person['OpenActivityMis'] = self['OpenActivityMis']
        self.person['ActivityMisStartTime'] = self['ActivityMisStartTime']
        self.person['ActivityMisEndTime'] = self['ActivityMisEndTime']
        self.person['ActivityMaxCircleNum'] = self['ActivityMaxCircleNum']
        self.person['OpenAutoAgreeCp'] = self['OpenAutoAgreeCp']
        self.person['OpenRelatFriend'] = self['OpenRelatFriend']
        self.person['ActivityMisStartDay'] = self['ActivityMisStartDay']
        self.person['ActivityMisEndDay'] = self['ActivityMisEndDay']
        self.person['isopendaycard1'] = self['isopendaycard1']
        self.person['isopendaycard2'] = self['isopendaycard2']
        self.person['isopenrefinelucky'] = self['isopenrefinelucky']
        self.person['refineluckytool1'] = self['refineluckytool1']
        self.person['maxrefineluckyval'] = self['maxrefineluckyval']
        self.person['isopenxiaojijoystick'] = self['isopenxiaojijoystick']
        self.person['isopensecpassword'] = self['isopensecpassword']
        self.person['isopenrevertrefine'] = self['isopenrevertrefine']
        self.person['revertrefinecost'] = self['revertrefinecost']
        self.person['moonboxusecd'] = self['moonboxusecd']
        self.person['OpenPullBack'] = self['OpenPullBack']
        self.person['BackActiveDay'] = self['BackActiveDay']
        self.person['BackItemId'] = self['BackItemId']
        self.person['BackLoginDay'] = self['BackLoginDay']
        self.person['BackLogin1_Silver'] = self['BackLogin1_Silver']
        self.person['BackLogin1_BindYB'] = self['BackLogin1_BindYB']
        self.person['BackLogin1_ItemId1'] = self['BackLogin1_ItemId1']
        self.person['BackLogin1_ItemCount1'] = self['BackLogin1_ItemCount1']
        self.person['BackLogin2_Silver'] = self['BackLogin2_Silver']
        self.person['BackLogin2_BindYB'] = self['BackLogin2_BindYB']
        self.person['BackLogin2_ItemId1'] = self['BackLogin2_ItemId1']
        self.person['BackLogin2_ItemCount1'] = self['BackLogin2_ItemCount1']
        self.person['BackLogin3_Silver'] = self['BackLogin3_Silver']
        self.person['BackLogin3_BindYB'] = self['BackLogin3_BindYB']
        self.person['BackLogin3_ItemId1'] = self['BackLogin3_ItemId1']
        self.person['BackLogin3_ItemCount1'] = self['BackLogin3_ItemCount1']
        self.person['BackLogin4_Silver'] = self['BackLogin4_Silver']
        self.person['BackLogin4_BindYB'] = self['BackLogin4_BindYB']
        self.person['BackLogin4_ItemId1'] = self['BackLogin4_ItemId1']
        self.person['BackLogin4_ItemCount1'] = self['BackLogin4_ItemCount1']
        self.person['BackLogin5_Silver'] = self['BackLogin5_Silver']
        self.person['BackLogin5_BindYB'] = self['BackLogin5_BindYB']
        self.person['BackLogin5_ItemId1'] = self['BackLogin5_ItemId1']
        self.person['BackLogin5_ItemCount1'] = self['BackLogin5_ItemCount1']
        self.person['openmanualchangetobigworld'] = self['openmanualchangetobigworld']
        self.person['BackLogin1_ItemId2'] = self['BackLogin1_ItemId2']
        self.person['BackLogin1_ItemCount2'] = self['BackLogin1_ItemCount2']
        self.person['BackLogin2_ItemId2'] = self['BackLogin2_ItemId2']
        self.person['BackLogin2_ItemCount2'] = self['BackLogin2_ItemCount2']
        self.person['BackLogin3_ItemId2'] = self['BackLogin3_ItemId2']
        self.person['BackLogin3_ItemCount2'] = self['BackLogin3_ItemCount2']
        self.person['BackLogin4_ItemId2'] = self['BackLogin4_ItemId2']
        self.person['BackLogin4_ItemCount2'] = self['BackLogin4_ItemCount2']
        self.person['BackLogin5_ItemId2'] = self['BackLogin5_ItemId2']
        self.person['BackLogin5_ItemCount2'] = self['BackLogin5_ItemCount2']
        self.person['OpenMoShenJiangLin'] = self['OpenMoShenJiangLin']
        self.person['ActivityMisLowLevel'] = self['ActivityMisLowLevel']
        self.person['StallReviewGMTime_Review'] = self['StallReviewGMTime_Review']
        self.person['StallReviewGMTime_ReviewFail'] = self['StallReviewGMTime_ReviewFail']
        self.person['StallReviewGMTime_Appeal'] = self['StallReviewGMTime_Appeal']
        self.person['StallReviewGMTime_AppealFail'] = self['StallReviewGMTime_AppealFail']
        self.person['refineluckytool2'] = self['refineluckytool2']
        self.person['refineluckytool3'] = self['refineluckytool3']
        self.person['refineluckytool4'] = self['refineluckytool4']
        self.person['refineluckyval1'] = self['refineluckyval1']
        self.person['refineluckyval2'] = self['refineluckyval2']
        self.person['refineluckyval3'] = self['refineluckyval3']
        self.person['refineluckyequiplv'] = self['refineluckyequiplv']
        self.person['refineluckyplayerlv'] = self['refineluckyplayerlv']
        self.person['refineluckyawardval1'] = self['refineluckyawardval1']
        self.person['refineluckyawardval2'] = self['refineluckyawardval2']
        self.person['refineluckyawardval3'] = self['refineluckyawardval3']
        self.person['refineluckyawardval4'] = self['refineluckyawardval4']
        self.person['OpenFellowReceiveItemReplaceLevel'] = self['OpenFellowReceiveItemReplaceLevel']
        self.person['RechargeScoreStartTime'] = self['RechargeScoreStartTime']
        self.person['RechargeScoreEndTime'] = self['RechargeScoreEndTime']
        self.person['RechargeScoreShopStartTime'] = self['RechargeScoreShopStartTime']
        self.person['RechargeScoreShopEndTime'] = self['RechargeScoreShopEndTime']
        self.person['isopendaycard3'] = self['isopendaycard3']
        self.person['openItemCompensate'] = self['openItemCompensate']
        self.person['ItemCompensateActiveness1'] = self['ItemCompensateActiveness1']
        self.person['ItemCompensateActiveness2'] = self['ItemCompensateActiveness2']
        self.person['OpenForceGuildDigUpTheHatchet'] = self['OpenForceGuildDigUpTheHatchet']
        self.person['OpenGetInfo'] = self['OpenGetInfo']
        self.person['OpenQRFunc'] = self['OpenQRFunc']
        self.person['OpenRechargeScore'] = self['OpenRechargeScore']
        self.person['OpenRechargeScoreShop'] = self['OpenRechargeScoreShop']
        self.person['IsOpenFashionColor'] = self['IsOpenFashionColor']
        self.person['IsOpenCoupleCopyScene'] = self['IsOpenCoupleCopyScene']
        self.person['ItemCompensateOpenLevel'] = self['ItemCompensateOpenLevel']
        self.person['MaxGuildLevel'] = self['MaxGuildLevel']
        self.person['GuildCreateCoin'] = self['GuildCreateCoin']
        self.person['GuildCreateLevel'] = self['GuildCreateLevel']
        self.person['GuildJoinLevel'] = self['GuildJoinLevel']
        self.person['NewGuideReliveLev'] = self['NewGuideReliveLev']
        self.person['OpenGuildBuild'] = self['OpenGuildBuild']
        self.person['EnergyMaxForFastFly'] = self['EnergyMaxForFastFly']
        self.person['ShowHitSignHPPercent'] = self['ShowHitSignHPPercent']
        self.person['AddFriendLevel'] = self['AddFriendLevel']
        self.person['IsOpenMail'] = self['IsOpenMail']
        self.person['IsOpenChatInChannelWorld'] = self['IsOpenChatInChannelWorld']
        self.person['IsOpenChatInChannelProfession'] = self['IsOpenChatInChannelProfession']
        self.person['IsOpenChatInChannelNearby'] = self['IsOpenChatInChannelNearby']
        self.person['IsOpenChatInChannelStation'] = self['IsOpenChatInChannelStation']
        self.person['IsOpenAddFriend'] = self['IsOpenAddFriend']
        self.person['IsOpenCurrencyExchange'] = self['IsOpenCurrencyExchange']
        self.person['IsOpenCurrencyExchange_SilverCoin'] = self['IsOpenCurrencyExchange_SilverCoin']
        self.person['IsOpenCurrencyExchange_GoldCoin'] = self['IsOpenCurrencyExchange_GoldCoin']
        self.person['IsOpenCurrencyExchange_YuanBaoBind'] = self['IsOpenCurrencyExchange_YuanBaoBind']
        self.person['FairyAttrRefix'] = self['FairyAttrRefix']
        self.person['IsOpenRecoverPool'] = self['IsOpenRecoverPool']
        self.person['XiandanOpenLevel'] = self['XiandanOpenLevel']
        self.person['CanShowFashionGoods'] = self['CanShowFashionGoods']
        self.person['FBQuanToYuanbao'] = self['FBQuanToYuanbao']
        self.person['FBAcceptFufeiWeekMax'] = self['FBAcceptFufeiWeekMax']
        self.person['AuraThresholdValue'] = self['AuraThresholdValue']
        self.person['AuraMaxValue'] = self['AuraMaxValue']
        self.person['AuraCdId'] = self['AuraCdId']
        self.person['CraftsmanForgeOpenLevel'] = self['CraftsmanForgeOpenLevel']
        self.person['IsOpenGem'] = self['IsOpenGem']
        self.person['GemOpenLevel'] = self['GemOpenLevel']
        self.person['IsOpenRealTimeVoiceChat'] = self['IsOpenRealTimeVoiceChat']
        self.person['IsShowSecPasswordRedPoint'] = self['IsShowSecPasswordRedPoint']
        self.person['OpenFairy'] = self['OpenFairy']
        self.person['ExpChangeToSkillSoulOpenLevel'] = self['ExpChangeToSkillSoulOpenLevel']
        self.person['GuildWarOpenSinceServerStart'] = self['GuildWarOpenSinceServerStart']
        self.person['IsRecoinOpen'] = self['IsRecoinOpen']
        self.person['FairyLockSkill1Cost'] = self['FairyLockSkill1Cost']
        self.person['FairyLockSkill2Cost'] = self['FairyLockSkill2Cost']
        self.person['FairyLockSkill3Cost'] = self['FairyLockSkill3Cost']
        self.person['IsOpenYuanBaoAndYuanBaoVice'] = self['IsOpenYuanBaoAndYuanBaoVice']
        self.person['GuildSetAddCostGuildMoneyNum'] = self['GuildSetAddCostGuildMoneyNum']
        self.person['IsOpenGuildAddition'] = self['IsOpenGuildAddition']
        self.person['RandomColorItemCost'] = self['RandomColorItemCost']
        self.person['CDkeyServerUrl'] = self['CDkeyServerUrl']
        self.person['IsOpenPhoneBind'] = self['IsOpenPhoneBind']
        self.person['PhoneBindUrl'] = self['PhoneBindUrl']
        self.person['TeamFollowDis'] = self['TeamFollowDis']
        self.person['TeamFollowCheckDis'] = self['TeamFollowCheckDis']
        self.person['MaxLifeSkillGatherCount'] = self['MaxLifeSkillGatherCount']
        self.person['MaxLifeSkillMakeCount'] = self['MaxLifeSkillMakeCount']
        self.person['MaxLifeSkillAlchemyCount'] = self['MaxLifeSkillAlchemyCount']
        self.person['IsOpenChatInChannelHorn'] = self['IsOpenChatInChannelHorn']
        self.person['IsOpenArtifact'] = self['IsOpenArtifact']
        self.person['BFMaxWeeklyScore'] = self['BFMaxWeeklyScore']
        self.person['OpenGuildThiefTime'] = self['OpenGuildThiefTime']
        self.person['CloseGuildThiefTime'] = self['CloseGuildThiefTime']
        self.person['CreateGuildThiefTime'] = self['CreateGuildThiefTime']
        self.person['DelGuildThiefTime'] = self['DelGuildThiefTime']
        self.person['NoticeGuildThiefStartTime'] = self['NoticeGuildThiefStartTime']
        self.person['NoticeGuildRobbersStartTime'] = self['NoticeGuildRobbersStartTime']
        self.person['OpenGuildThiefDay1'] = self['OpenGuildThiefDay1']
        self.person['OpenGuildThiefDay2'] = self['OpenGuildThiefDay2']
        self.person['OpenGuildThiefDay3'] = self['OpenGuildThiefDay3']
        self.person['OpenGuildThiefDay4'] = self['OpenGuildThiefDay4']
        self.person['OpenGuildThiefDay5'] = self['OpenGuildThiefDay5']
        self.person['OpenGuildThiefDay6'] = self['OpenGuildThiefDay6']
        self.person['OpenGuildThiefDay7'] = self['OpenGuildThiefDay7']
        self.person['OpenPAMonthAccrualZulong'] = self['OpenPAMonthAccrualZulong']
        self.person['OpenPAMonthAccrualWanliu'] = self['OpenPAMonthAccrualWanliu']
        self.person['OpenPAForeverAccrual'] = self['OpenPAForeverAccrual']
        self.person['OpenPAGrowUp'] = self['OpenPAGrowUp']
        self.person['OpenImmortality'] = self['OpenImmortality']
        self.person['OpenQQWakeup'] = self['OpenQQWakeup']
        self.person['QQWakeupUrl'] = self['QQWakeupUrl']
        self.person['OpenQQVipPrivilege'] = self['OpenQQVipPrivilege']
        self.person['QQVipUrl'] = self['QQVipUrl']
        self.person['OpenCommunityEntry'] = self['OpenCommunityEntry']
        self.person['TribeAddrQQAndriodUrl'] = self['TribeAddrQQAndriodUrl']
        self.person['TribeAddrQQiOSUrl'] = self['TribeAddrQQiOSUrl']
        self.person['QQGameCentreUrl'] = self['QQGameCentreUrl']
        self.person['ExamOpenWeekDay'] = self['ExamOpenWeekDay']
        self.person['ExamRound3Hour'] = self['ExamRound3Hour']
        self.person['StartWorkDrawLimitPerDay'] = self['StartWorkDrawLimitPerDay']
        self.person['OpenQianKunDai'] = self['OpenQianKunDai']
        self.person['DomainWarRank'] = self['DomainWarRank']
        self.person['DomainWarStartWeek'] = self['DomainWarStartWeek']
        self.person['DomainWarDeclareStartTime'] = self['DomainWarDeclareStartTime']
        self.person['DomainWarDeclareEndTime'] = self['DomainWarDeclareEndTime']
        self.person['DomainWarStartTime'] = self['DomainWarStartTime']
        self.person['DomainWarEndTime'] = self['DomainWarEndTime']
        self.person['OpenDomainWar'] = self['OpenDomainWar']
        self.person['OpenScrollExchange'] = self['OpenScrollExchange']
        self.person['ScrollExchangePreTime'] = self['ScrollExchangePreTime']
        self.person['ScrollExchangeStartTime'] = self['ScrollExchangeStartTime']
        self.person['ScrollExchangeEndTime'] = self['ScrollExchangeEndTime']
        self.person['OpenShareGameGift'] = self['OpenShareGameGift']
        self.person['ShareGamePreTime'] = self['ShareGamePreTime']
        self.person['ShareGameStartTime'] = self['ShareGameStartTime']
        self.person['ShareGameEndTime'] = self['ShareGameEndTime']
        self.person['ShareGameMyExperimenceItemDataId'] = self['ShareGameMyExperimenceItemDataId']
        self.person['ShareGameMyExperimenceItemNum'] = self['ShareGameMyExperimenceItemNum']
        self.person['ShareGameCloseServerItemDataId'] = self['ShareGameCloseServerItemDataId']
        self.person['ShareGameCloseServerItemNum'] = self['ShareGameCloseServerItemNum']
        self.person['ImmortalityOpenDays'] = self['ImmortalityOpenDays']
        self.person['NewbieWishingLevel'] = self['NewbieWishingLevel']
        self.person['BlackMarketBuyCD'] = self['BlackMarketBuyCD']
        self.person['OpenQianzhuang'] = self['OpenQianzhuang']
        self.person['QianzhuangEndtime'] = self['QianzhuangEndtime']
        self.person['OpenBrotherhood'] = self['OpenBrotherhood']
        self.person['RechargeTipAndroidQQ'] = self['RechargeTipAndroidQQ']
        self.person['RechargeTipAndroidWX'] = self['RechargeTipAndroidWX']
        self.person['RechargeTipIOSQQ'] = self['RechargeTipIOSQQ']
        self.person['RechargeTipIOSWX'] = self['RechargeTipIOSWX']
        self.person['OpenPandora'] = self['OpenPandora']
        self.person['OpenGuildFuShuangMiJingDay1'] = self['OpenGuildFuShuangMiJingDay1']
        self.person['OpenGuildFuShuangMiJingDay2'] = self['OpenGuildFuShuangMiJingDay2']
        self.person['OpenGuildFuShuangMiJingDay3'] = self['OpenGuildFuShuangMiJingDay3']
        self.person['OpenGuildFuShuangMiJingDay4'] = self['OpenGuildFuShuangMiJingDay4']
        self.person['OpenGuildFuShuangMiJingDay5'] = self['OpenGuildFuShuangMiJingDay5']
        self.person['OpenGuildFuShuangMiJingDay6'] = self['OpenGuildFuShuangMiJingDay6']
        self.person['OpenGuildFuShuangMiJingDay7'] = self['OpenGuildFuShuangMiJingDay7']
        self.person['GuildFuShuangMiJingLastTime'] = self['GuildFuShuangMiJingLastTime']
        self.person['GuildFuShuangMiJingCostGuildMoney'] = self['GuildFuShuangMiJingCostGuildMoney']
        self.person['SkillZhuanJingOpenLevel'] = self['SkillZhuanJingOpenLevel']
        self.person['WXGameGroupUrl'] = self['WXGameGroupUrl']
        self.person['OpenWXWakeup'] = self['OpenWXWakeup']
        self.person['OpenBroadcastingStation'] = self['OpenBroadcastingStation']
        self.person['OpenOfficialSite'] = self['OpenOfficialSite']
        self.person['OpenQQGiftCenter'] = self['OpenQQGiftCenter']
        self.person['OpenQQInteresting'] = self['OpenQQInteresting']
        self.person['OpenQQGameCenter'] = self['OpenQQGameCenter']
        self.person['OpenWXGameGroup'] = self['OpenWXGameGroup']
        self.person['OpenWXGameCenter'] = self['OpenWXGameCenter']
        self.person['OpenWXPublicAccount'] = self['OpenWXPublicAccount']
        self.person['DailyOnLineAwardTakeMinLevel'] = self['DailyOnLineAwardTakeMinLevel']
        self.person['ActivityOnLineAwardTakeMinLevel'] = self['ActivityOnLineAwardTakeMinLevel']
        self.person['OpenAsura'] = self['OpenAsura']
        self.person['OpenDA'] = self['OpenDA']
        self.person['OpenAchievement'] = self['OpenAchievement']
        self.person['OpenXiuZhen'] = self['OpenXiuZhen']
        self.person['OpenQianKunDaiMaxMake'] = self['OpenQianKunDaiMaxMake']
        self.person['OpenGuildRobberTime'] = self['OpenGuildRobberTime']
        self.person['OpenGuildBindGroup'] = self['OpenGuildBindGroup']
        self.person['OpenXinyueOfCommunity'] = self['OpenXinyueOfCommunity']
        self.person['XinYueVT'] = self['XinYueVT']
        self.person['XinYueCommunityUrl'] = self['XinYueCommunityUrl']
        self.person['XinYueHeadPortraitUrl'] = self['XinYueHeadPortraitUrl']
        self.person['OpenShareRoleBigPhoto'] = self['OpenShareRoleBigPhoto']
        self.person['OpenShareFairyBigPhoto'] = self['OpenShareFairyBigPhoto']
        self.person['OpenShareAchieveBigPhoto'] = self['OpenShareAchieveBigPhoto']
        self.person['OpenShareFashionBigPhoto'] = self['OpenShareFashionBigPhoto']
        self.person['OpenShareGiveGiftBackend'] = self['OpenShareGiveGiftBackend']
        self.person['OpenShareInviteTeamStructure'] = self['OpenShareInviteTeamStructure']
        self.person['OpenShareInviteArmyStructure'] = self['OpenShareInviteArmyStructure']
        self.person['OpenShareInviteFriendStructure'] = self['OpenShareInviteFriendStructure']
        self.person['OpenFireWorks'] = self['OpenFireWorks']
        self.person['FireWorksEffectNum'] = self['FireWorksEffectNum']
        self.person['OpenInscription'] = self['OpenInscription']
        self.person['XinyueSecret'] = self['XinyueSecret']
        self.person['OpenChristmas'] = self['OpenChristmas']
        self.person['OpenTencentXiaoyue'] = self['OpenTencentXiaoyue']
        self.person['XiaoyueRegionId'] = self['XiaoyueRegionId']
        self.person['XiaoyueGameId'] = self['XiaoyueGameId']
        self.person['RechargeIgnoreShow'] = self['RechargeIgnoreShow']
        self.person['OpenRedPacketRain'] = self['OpenRedPacketRain']
        self.person['DigTreasureDistance'] = self['DigTreasureDistance']
        self.person['OpenChristmasTour'] = self['OpenChristmasTour']
        self.person['OpenChristmasMonster'] = self['OpenChristmasMonster']
        self.person['OpenGuildAuction'] = self['OpenGuildAuction']
        self.person['OpenWorldAuction'] = self['OpenWorldAuction']
        self.person['AuctionBidOnceAddPrice'] = self['AuctionBidOnceAddPrice']
        self.person['OpenTencentZone'] = self['OpenTencentZone']
        self.person['TencentZoneMinLevel'] = self['TencentZoneMinLevel']
        self.person['TianshuSlot1OpenLevel'] = self['TianshuSlot1OpenLevel']
        self.person['TianshuSlot2OpenLevel'] = self['TianshuSlot2OpenLevel']
        self.person['TianshuSlot3OpenLevel'] = self['TianshuSlot3OpenLevel']
        self.person['TianshuSlot4OpenLevel'] = self['TianshuSlot4OpenLevel']
        self.person['OpenIOSReviewGuild'] = self['OpenIOSReviewGuild']
        self.person['OpenIOSReviewInnerStyle'] = self['OpenIOSReviewInnerStyle']
        self.person['GuildWarArmyMemberMin'] = self['GuildWarArmyMemberMin']
        self.person['OpenInfiniteDreamland'] = self['OpenInfiniteDreamland']
        self.person['OpenInfiniteDreamlandLevel'] = self['OpenInfiniteDreamlandLevel']
        self.person['InfiniteDreamlandMaxLayer'] = self['InfiniteDreamlandMaxLayer']
        self.person['OpenTower'] = self['OpenTower']
        self.person['OpenTowerSweep'] = self['OpenTowerSweep']
        self.person['OpenTowerShop'] = self['OpenTowerShop']
        self.person['OpenTowerRank'] = self['OpenTowerRank']
        self.person['TowerMaxFloor'] = self['TowerMaxFloor']
        self.person['TowerShopDailyBuyCount'] = self['TowerShopDailyBuyCount']
        self.person['TowerDailyFightCount'] = self['TowerDailyFightCount']
        self.person['TowerDailySweepCount'] = self['TowerDailySweepCount']
        self.person['IsOpenJubao'] = self['IsOpenJubao']
        self.person['CurrentWorldId'] = self['CurrentWorldId']
        self.person['IsOpenAR'] = self['IsOpenAR']
        self.person['IsOpenNierenScore'] = self['IsOpenNierenScore']
        self.person['IsOpenShareAccRechargeBigPhoto'] = self['IsOpenShareAccRechargeBigPhoto']
        self.person['OpenPresent'] = self['OpenPresent']
        self.person['IsOpenStall'] = self['IsOpenStall']
        self.person['IsOpenEquipEngrave'] = self['IsOpenEquipEngrave']
        self.person['IsOpenEquipEngraveAuto'] = self['IsOpenEquipEngraveAuto']
        self.person['EquipEngraveLevelMax'] = self['EquipEngraveLevelMax']
        self.person['NewPlayerProtectedLevel'] = self['NewPlayerProtectedLevel']
        self.person['NewPlayerProtectedLevelDiff'] = self['NewPlayerProtectedLevelDiff']
        self.person['IsOpenNormalQQVip'] = self['IsOpenNormalQQVip']
        self.person['IsOpenSuperQQVip'] = self['IsOpenSuperQQVip']
        self.person['IsOpenInscriptionUpgrade'] = self['IsOpenInscriptionUpgrade']
        self.person['IsOpenInscriptionInaly'] = self['IsOpenInscriptionInaly']
        self.person['IsOpenInscriptionRemove'] = self['IsOpenInscriptionRemove']
        self.person['OpenStallGainWay'] = self['OpenStallGainWay']
        self.person['OpenStallSellWay'] = self['OpenStallSellWay']
        self.person['OpenStallMercyWater'] = self['OpenStallMercyWater']
        self.person['OpenNearbyFriend'] = self['OpenNearbyFriend']
        self.person['OpenContactService'] = self['OpenContactService']
        self.person['OpenLuckyConn'] = self['OpenLuckyConn']
        self.person['OpenSurvey'] = self['OpenSurvey']
        self.person['OpenRanger'] = self['OpenRanger']
        self.person['OpenEquipResonance'] = self['OpenEquipResonance']
        self.person['OpenGuildMonster'] = self['OpenGuildMonster']
        self.person['OpenGuildMonsterNpc'] = self['OpenGuildMonsterNpc']
        self.person['InfiniteDreamlandMaxRewardCount'] = self['InfiniteDreamlandMaxRewardCount']
        self.person['OpenPhotoRandomShare'] = self['OpenPhotoRandomShare']
        self.person['PhotoRandomShareStartTime'] = self['PhotoRandomShareStartTime']
        self.person['PhotoRandomShareEndTime'] = self['PhotoRandomShareEndTime']
        self.person['PhotoRandomShareType'] = self['PhotoRandomShareType']
        self.person['PhotoRandomRewardItemId0'] = self['PhotoRandomRewardItemId0']
        self.person['PhotoRandomRewardItemNum0'] = self['PhotoRandomRewardItemNum0']
        self.person['PhotoRandomRewardItemId1'] = self['PhotoRandomRewardItemId1']
        self.person['PhotoRandomRewardItemNum1'] = self['PhotoRandomRewardItemNum1']
        self.person['PhotoRandomAccDayList'] = self['PhotoRandomAccDayList']
        self.person['PhotoRandomAccItemIdList'] = self['PhotoRandomAccItemIdList']
        self.person['PhotoRandomAccItemNumList'] = self['PhotoRandomAccItemNumList']
        self.person['SameGuildTeamMemberCount'] = self['SameGuildTeamMemberCount']
        self.person['OpenShareDeathAidStructure'] = self['OpenShareDeathAidStructure']
        self.person['OpenYaoshouCreate'] = self['OpenYaoshouCreate']
        self.person['OpenYaojingCreate'] = self['OpenYaojingCreate']
        self.person['OpenYumangMaleCreate'] = self['OpenYumangMaleCreate']
        self.person['OpenYumangFemaleCreate'] = self['OpenYumangFemaleCreate']
        self.person['OpenYulingCreate'] = self['OpenYulingCreate']
        self.person['OpenWuxiaMaleCreate'] = self['OpenWuxiaMaleCreate']
        self.person['OpenWuxiaFemaleCreate'] = self['OpenWuxiaFemaleCreate']
        self.person['OpenFashiMaleCreate'] = self['OpenFashiMaleCreate']
        self.person['OpenFashiFemaleCreate'] = self['OpenFashiFemaleCreate']
        self.person['OpenPlayerBehaviorTlog'] = self['OpenPlayerBehaviorTlog']
        self.person['PlayerBehaviorTlogLevel'] = self['PlayerBehaviorTlogLevel']
        self.person['OpenUnlockAct'] = self['OpenUnlockAct']
        self.person['OpenUnlockEmotion'] = self['OpenUnlockEmotion']
        self.person['OpenRecastInherit'] = self['OpenRecastInherit']
        self.person['OpenFireWorksPlayerRank'] = self['OpenFireWorksPlayerRank']
        self.person['OpenFireWorksGuildRank'] = self['OpenFireWorksGuildRank']
        self.person['OpenPullQQWakeupUrl'] = self['OpenPullQQWakeupUrl']
        self.person['OpenPullQQVipUrl'] = self['OpenPullQQVipUrl']
        self.person['OpenYuanBaoShop'] = self['OpenYuanBaoShop']
        self.person['OpenGuildFlag'] = self['OpenGuildFlag']
        self.person['GuildFlagCDTime'] = self['GuildFlagCDTime']
        self.person['IsOpenMicroBBS'] = self['IsOpenMicroBBS']
        self.person['OpenShareMountBigPhoto'] = self['OpenShareMountBigPhoto']
        self.person['OpenShareAirCraftBigPhoto'] = self['OpenShareAirCraftBigPhoto']
        self.person['OpenSingleInteract'] = self['OpenSingleInteract']
        self.person['ExchangeReputation'] = self['ExchangeReputation']
        self.person['ExchangeMilitaryRank'] = self['ExchangeMilitaryRank']
        self.person['OpenGuildFightWorldBoss'] = self['OpenGuildFightWorldBoss']
        self.person['Dmg2GFWBSoulFactor'] = self['Dmg2GFWBSoulFactor']
        self.person['GFWBRewardGuildNum'] = self['GFWBRewardGuildNum']
        self.person['MisDeliverItemID'] = self['MisDeliverItemID']
        self.person['OpenMisDeliver'] = self['OpenMisDeliver']
        self.person['OpenSweep'] = self['OpenSweep']
        self.person['OpenJingxuan'] = self['OpenJingxuan']
        self.person['OpenZhibo'] = self['OpenZhibo']
        self.person['OpenFriendsMutualHelp'] = self['OpenFriendsMutualHelp']
        self.person['FriendsMutualHelpStartTime'] = self['FriendsMutualHelpStartTime']
        self.person['FriendsMutualHelpEndTime'] = self['FriendsMutualHelpEndTime']
        self.person['IsOpengWeather'] = self['IsOpengWeather']
        self.person['CostEnergyForWorldChat'] = self['CostEnergyForWorldChat']
        self.person['RelatFriendPointAddCountPerDay'] = self['RelatFriendPointAddCountPerDay']
        self.person['OpenShareQRCode'] = self['OpenShareQRCode']
        self.person['IosReviewAppId'] = self['IosReviewAppId']
        self.person['OpenAccRechargeGainWay'] = self['OpenAccRechargeGainWay']
        self.person['OpenAccRechargeTitle'] = self['OpenAccRechargeTitle']
        self.person['AccRechargeTitleType'] = self['AccRechargeTitleType']
        self.person['OpenStallAchievement'] = self['OpenStallAchievement']
        self.person['StallAchievementClass'] = self['StallAchievementClass']
        self.person['OpenStallTitle'] = self['OpenStallTitle']
        self.person['StallTitleType'] = self['StallTitleType']
        self.person['OpenPwdStallDesc'] = self['OpenPwdStallDesc']
        self.person['OpenRechargePlusSign'] = self['OpenRechargePlusSign']
        self.person['OpenRechargeAchievement'] = self['OpenRechargeAchievement']
        self.person['RechargeAchievementClass'] = self['RechargeAchievementClass']
        self.person['OpenLotteryBox'] = self['OpenLotteryBox']
        self.person['LotteryBoxList'] = self['LotteryBoxList']
        self.person['MicroBBSRedDotLevel'] = self['MicroBBSRedDotLevel']
        self.person['FlyRewardLevel'] = self['FlyRewardLevel']
        self.person['OpenYirong'] = self['OpenYirong']
        self.person['BlockTitleClassId'] = self['BlockTitleClassId']
        self.person['BrotherhoodChangeTitleGoldCost'] = self['BrotherhoodChangeTitleGoldCost']
        self.person['bOpenSuperR'] = self['bOpenSuperR']
        self.person['bOpenTssAnti'] = self['bOpenTssAnti']
        self.person['ShowCombatChange'] = self['ShowCombatChange']
        self.person['SystemShopOpen'] = self['SystemShopOpen']
        self.person['FlyMisRewardShow'] = self['FlyMisRewardShow']
        self.person['OpenActivityRoot'] = self['OpenActivityRoot']
        self.person['OpenFuliAndTehuiBtnLevel'] = self['OpenFuliAndTehuiBtnLevel']
        self.person['OpenSiqingRedEnvelope'] = self['OpenSiqingRedEnvelope']
        self.person['OpenYLTXCurInstRemainNpc'] = self['OpenYLTXCurInstRemainNpc']
        self.person['OpenAutoSwitchTeamMissionTabWindow'] = self['OpenAutoSwitchTeamMissionTabWindow']
        self.person['DomainStatueKneelDistance'] = self['DomainStatueKneelDistance']
        self.person['DomainStatueKneelTime'] = self['DomainStatueKneelTime']
        self.person['OpenGuildRealTimeVoice'] = self['OpenGuildRealTimeVoice']
        self.person['OpenHuiliu'] = self['OpenHuiliu']
        self.person['OpenHuiliuGift'] = self['OpenHuiliuGift']
        self.person['OpenHuiliuExpGain'] = self['OpenHuiliuExpGain']
        self.person['OpenHuiliuGoal'] = self['OpenHuiliuGoal']
        self.person['OpenHuiliuRecharge'] = self['OpenHuiliuRecharge']
        self.person['OpenHuiliuIdentity'] = self['OpenHuiliuIdentity']
        self.person['HuiliuTimeSpan'] = self['HuiliuTimeSpan']
        self.person['HuiliuExpGainTimeSpan'] = self['HuiliuExpGainTimeSpan']
        self.person['HuiliuGoalTimeSpan'] = self['HuiliuGoalTimeSpan']
        self.person['OpenARShare'] = self['OpenARShare']
        self.person['OpenShareMarriageContractBigPhoto'] = self['OpenShareMarriageContractBigPhoto']
        self.person['OpenAppointPlayerZone'] = self['OpenAppointPlayerZone']
        self.person['BrotherhoodChangeNameItemDataId'] = self['BrotherhoodChangeNameItemDataId']
        self.person['OpenMentor'] = self['OpenMentor']
        self.person['OpenOBCelebration'] = self['OpenOBCelebration']
        self.person['OpenGroupPhoto'] = self['OpenGroupPhoto']
        self.person['OpenOBCelebrationExchange'] = self['OpenOBCelebrationExchange']
        self.person['OpenOBCelebrationWish'] = self['OpenOBCelebrationWish']
        self.person['OpenLuckyStar'] = self['OpenLuckyStar']
        self.person['LuckyStarMinLevel'] = self['LuckyStarMinLevel']
        self.person['WarpathIncAttrRate'] = self['WarpathIncAttrRate']
        self.person['OpenCustomHeadPic'] = self['OpenCustomHeadPic']
        self.person['PetHungerMidPer'] = self['PetHungerMidPer']
        self.person['PetHungerLowPer'] = self['PetHungerLowPer']
        self.person['PandoraMinLevel'] = self['PandoraMinLevel']
        self.person['PetTameSkillBaseID'] = self['PetTameSkillBaseID']
        self.person['OpenDontNpcDropSet'] = self['OpenDontNpcDropSet']
        self.person['ChildrensDayItemTransformer'] = self['ChildrensDayItemTransformer']
        self.person['ChildrensDayItemBallon'] = self['ChildrensDayItemBallon']
        self.person['OpenChoicenessBtnLevel'] = self['OpenChoicenessBtnLevel']
        self.person['PetSummonSkillBaseID'] = self['PetSummonSkillBaseID']
        self.person['OpenGoddessSelect'] = self['OpenGoddessSelect']
        self.person['GoddessSelectMinLevel'] = self['GoddessSelectMinLevel']
        self.person['OpenLimitShop'] = self['OpenLimitShop']
        self.person['OpenPayTokenCheck'] = self['OpenPayTokenCheck']
        self.person['OpenMentorShop'] = self['OpenMentorShop']
        self.person['OpenOBCelebrationLevel'] = self['OpenOBCelebrationLevel']
        self.person['OpenXiaoK'] = self['OpenXiaoK']
        self.person['XiaoKUrl'] = self['XiaoKUrl']
        self.person['StartWorkAccLoginDay0'] = self['StartWorkAccLoginDay0']
        self.person['StartWorkAccLoginRewardItem0'] = self['StartWorkAccLoginRewardItem0']
        self.person['StartWorkAccLoginRewardNum0'] = self['StartWorkAccLoginRewardNum0']
        self.person['StartWorkAccLoginDay1'] = self['StartWorkAccLoginDay1']
        self.person['StartWorkAccLoginRewardItem1'] = self['StartWorkAccLoginRewardItem1']
        self.person['StartWorkAccLoginRewardNum1'] = self['StartWorkAccLoginRewardNum1']
        self.person['StartWorkAccLoginDay2'] = self['StartWorkAccLoginDay2']
        self.person['StartWorkAccLoginRewardItem2'] = self['StartWorkAccLoginRewardItem2']
        self.person['StartWorkAccLoginRewardNum2'] = self['StartWorkAccLoginRewardNum2']
        self.person['OpenTeachingPointRank'] = self['OpenTeachingPointRank']
        self.person['OpenGFWBGuildRankUI'] = self['OpenGFWBGuildRankUI']
        self.person['ZhiboRedPointLevel'] = self['ZhiboRedPointLevel']
        self.person['CreateArmyLevel'] = self['CreateArmyLevel']
        self.person['XinyueRedDotMinLevel'] = self['XinyueRedDotMinLevel']
        self.person['MidasOpenBigWorldRecharge'] = self['MidasOpenBigWorldRecharge']
        self.person['OpenBigworldFirstRechargeBonus'] = self['OpenBigworldFirstRechargeBonus']
        self.person['OpenBigworldNormalRechargeRebate'] = self['OpenBigworldNormalRechargeRebate']
        self.person['OpenBigworldConsumeStepRebate'] = self['OpenBigworldConsumeStepRebate']
        self.person['OpenBigworldConsumeStepRebateDay'] = self['OpenBigworldConsumeStepRebateDay']
        self.person['OpenBigworldRechargeStepRebate'] = self['OpenBigworldRechargeStepRebate']
        self.person['OpenBigworldRechargeStepRebateDay'] = self['OpenBigworldRechargeStepRebateDay']
        self.person['OpenBigworldAccRechargeBonus'] = self['OpenBigworldAccRechargeBonus']
        self.person['OpenBigworldRechargeScoreShop'] = self['OpenBigworldRechargeScoreShop']
        self.person['OpenBigworldCurrencyExchange'] = self['OpenBigworldCurrencyExchange']
        self.person['OpenBigworldYuanBaoShop'] = self['OpenBigworldYuanBaoShop']
        self.person['OpenBigworldSecretShip'] = self['OpenBigworldSecretShip']
        self.person['OpenBigworldLuckyStar'] = self['OpenBigworldLuckyStar']
        self.person['OpenEngraveResonance'] = self['OpenEngraveResonance']
        self.person['EngraveResonanceAttrCount'] = self['EngraveResonanceAttrCount']
        self.person['PetAutoFeedHungerPer'] = self['PetAutoFeedHungerPer']
        self.person['IsOpenSwordTeam'] = self['IsOpenSwordTeam']
        self.person['IsOpenSwordTeamRecruit'] = self['IsOpenSwordTeamRecruit']
        self.person['IsOpenSwordTeamChangeName'] = self['IsOpenSwordTeamChangeName']
        self.person['IsOpenBigWorldPVP_Final'] = self['IsOpenBigWorldPVP_Final']
        self.person['IsOpenBigWorldPVP_Pre'] = self['IsOpenBigWorldPVP_Pre']
        self.person['IsOpenBigWorldPVP_View'] = self['IsOpenBigWorldPVP_View']
        self.person['IsOpenRollNotice'] = self['IsOpenRollNotice']
        self.person['WorldChatCD'] = self['WorldChatCD']
        self.person['GuildChatCD'] = self['GuildChatCD']
        self.person['TeamChatCD'] = self['TeamChatCD']
        self.person['RaidChatCD'] = self['RaidChatCD']
        self.person['RecruitChatCD'] = self['RecruitChatCD']
        self.person['NormalChatCD'] = self['NormalChatCD']
        self.person['PrivateChatCD'] = self['PrivateChatCD']
        self.person['LoudSpeakChatCD'] = self['LoudSpeakChatCD']
        self.person['IsOpenChineseValentine'] = self['IsOpenChineseValentine']
        self.person['ChineseValentineStartTime'] = self['ChineseValentineStartTime']
        self.person['ChineseValentineEndTime'] = self['ChineseValentineEndTime']
        self.person['IsOpenCValentineFlower'] = self['IsOpenCValentineFlower']
        self.person['CValentineFlowerStartTime'] = self['CValentineFlowerStartTime']
        self.person['CValentineFlowerEndTime'] = self['CValentineFlowerEndTime']
        self.person['CValentineFlowerRankEndTime'] = self['CValentineFlowerRankEndTime']
        self.person['IsOpenCValentineMarriageGift'] = self['IsOpenCValentineMarriageGift']
        self.person['CValentineMarriageGiftStartTime'] = self['CValentineMarriageGiftStartTime']
        self.person['CValentineMarriageGiftEndTime'] = self['CValentineMarriageGiftEndTime']
        self.person['IsOpenCVFireflyWithYou'] = self['IsOpenCVFireflyWithYou']
        self.person['CVFireflyWithYouStartTime'] = self['CVFireflyWithYouStartTime']
        self.person['CVFireflyWithYouEndTime'] = self['CVFireflyWithYouEndTime']
        self.person['ChineseValentineOpenLevel'] = self['ChineseValentineOpenLevel']
        self.person['BountyActiveMinPlayerLevel'] = self['BountyActiveMinPlayerLevel']
        self.person['BountyPickDuration'] = self['BountyPickDuration']
        self.person['BountyPickDistance'] = self['BountyPickDistance']
        self.person['BigWorldPVPRestSceneId'] = self['BigWorldPVPRestSceneId']
        self.person['BigWorldPVPPreSceneId'] = self['BigWorldPVPPreSceneId']
        self.person['BigWorldPVPFinalSceneId'] = self['BigWorldPVPFinalSceneId']
        self.person['BigWorldPVPHelpSceneId'] = self['BigWorldPVPHelpSceneId']
        self.person['BigWorldPVPNeedLevel'] = self['BigWorldPVPNeedLevel']
        self.person['BigWorldPVPOpenDayOfWeek'] = self['BigWorldPVPOpenDayOfWeek']
        self.person['BigWorldPVPPreStartTime'] = self['BigWorldPVPPreStartTime']
        self.person['BigWorldPVPPrePrepareTime'] = self['BigWorldPVPPrePrepareTime']
        self.person['BigWorldPVPPreVerifyTime'] = self['BigWorldPVPPreVerifyTime']
        self.person['BigWorldPVPPreSignUpTime'] = self['BigWorldPVPPreSignUpTime']
        self.person['BigWorldPVPPreMatchTime'] = self['BigWorldPVPPreMatchTime']
        self.person['BigWorldPVPPreAwardTime'] = self['BigWorldPVPPreAwardTime']
        self.person['BigWorldPVPPreEndTime'] = self['BigWorldPVPPreEndTime']
        self.person['BigWorldPVPPreWinHonour'] = self['BigWorldPVPPreWinHonour']
        self.person['BigWorldPVPPreLoseHonour'] = self['BigWorldPVPPreLoseHonour']
        self.person['IsOpenSummerVacation'] = self['IsOpenSummerVacation']
        self.person['IsOpenWatermelonCombat'] = self['IsOpenWatermelonCombat']
        self.person['SummerVacationLevelLimit'] = self['SummerVacationLevelLimit']
        self.person['TickInitTimeRelatedNpcEnabled'] = self['TickInitTimeRelatedNpcEnabled']
        self.person['BountyUIRefreshSpace'] = self['BountyUIRefreshSpace']
        self.person['IsSnowEnvironment'] = self['IsSnowEnvironment']
        self.person['CVFireflyCopySceneStartTime'] = self['CVFireflyCopySceneStartTime']
        self.person['CVFireflyCopySceneEndTime'] = self['CVFireflyCopySceneEndTime']
        self.person['IsOpenNpcGiftExchange'] = self['IsOpenNpcGiftExchange']
        self.person['NpcGiftExchangeLevelLimit'] = self['NpcGiftExchangeLevelLimit']
        self.person['IsOpenGuildConvoy'] = self['IsOpenGuildConvoy']
        self.person['GuildConvoyBrokenBlook'] = self['GuildConvoyBrokenBlook']
        self.person['BountyMaxFightRewardTime'] = self['BountyMaxFightRewardTime']
        self.person['BFMaxDailyGlory'] = self['BFMaxDailyGlory']
        self.person['canTeachingPreachingValue'] = self['canTeachingPreachingValue']
        self.person['OpenFairyNeidan'] = self['OpenFairyNeidan']
        self.person['OpenFairyEvolve'] = self['OpenFairyEvolve']
        self.person['FairyOpenEvolveLevel'] = self['FairyOpenEvolveLevel']
        self.person['OpenPassport'] = self['OpenPassport']
        self.person['PassportWeekExpMax'] = self['PassportWeekExpMax']
        self.person['bOpenEquipEnchanting'] = self['bOpenEquipEnchanting']
        self.person['bOpenCPEnterCountLimit'] = self['bOpenCPEnterCountLimit']
        self.person['OpenTianshuZhenfa'] = self['OpenTianshuZhenfa']
        self.person['OpenTianshuZhenfaYinzhen'] = self['OpenTianshuZhenfaYinzhen']
        self.person['OpenTianshuYinzhenGongming'] = self['OpenTianshuYinzhenGongming']
        self.person['TianshuZhenfaOpenLevel'] = self['TianshuZhenfaOpenLevel']
        self.person['nPassportLevelMax'] = self['nPassportLevelMax']
        self.person['IsOpenFashion'] = self['IsOpenFashion']
        self.person['IsOpenFashionProlon'] = self['IsOpenFashionProlon']
        self.person['IsOpenFashionColorItemPack'] = self['IsOpenFashionColorItemPack']
        self.person['SubscibeProtocolUrl'] = self['SubscibeProtocolUrl']
        self.person['SubscibeStatementUrl'] = self['SubscibeStatementUrl']
        self.person['SwordTeamCreateLevel'] = self['SwordTeamCreateLevel']
        self.person['SwordTeamJoinLevel'] = self['SwordTeamJoinLevel']
        self.person['SwordTeamReserveMemberNum'] = self['SwordTeamReserveMemberNum']
        self.person['IsOpenChangeProfession'] = self['IsOpenChangeProfession']
        self.person['PassportYuanbaoToExp'] = self['PassportYuanbaoToExp']
        self.person['OpenTianshuViewOther'] = self['OpenTianshuViewOther']
        self.person['TianshuMasterLevelMax'] = self['TianshuMasterLevelMax']
        self.person['BountyOpenDay1'] = self['BountyOpenDay1']
        self.person['BountyOpenDay2'] = self['BountyOpenDay2']
        self.person['BountyOpenDay3'] = self['BountyOpenDay3']
        self.person['BountyOpenDay4'] = self['BountyOpenDay4']
        self.person['BountyOpenDay5'] = self['BountyOpenDay5']
        self.person['BountyOpenDay6'] = self['BountyOpenDay6']
        self.person['BountyOpenDay7'] = self['BountyOpenDay7']
        self.person['IsOpenDomainArea'] = self['IsOpenDomainArea']
        self.person['BigWorldPVPFinalStartTime'] = self['BigWorldPVPFinalStartTime']
        self.person['IsOpenChatInChannelGuildHorn'] = self['IsOpenChatInChannelGuildHorn']
        self.person['GuildHornChatCD'] = self['GuildHornChatCD']
        self.person['IsOpenHome'] = self['IsOpenHome']
        self.person['OpenHomeLevel'] = self['OpenHomeLevel']
        self.person['OpenKickPlayerCache'] = self['OpenKickPlayerCache']
        self.person['RubkiBeginTime'] = self['RubkiBeginTime']
        self.person['OpenRubkiCube'] = self['OpenRubkiCube']
        self.person['IsOpenEquipRebirth'] = self['IsOpenEquipRebirth']
        self.person['IsOpenEquipRebirthResonance'] = self['IsOpenEquipRebirthResonance']
        self.person['OpenHomeShowRoom'] = self['OpenHomeShowRoom']
        self.person['OpenHomeProduce'] = self['OpenHomeProduce']
        self.person['HomeGuestNeedFriendPoint'] = self['HomeGuestNeedFriendPoint']
        self.person['ProduceStealHomeHigherLevelMax'] = self['ProduceStealHomeHigherLevelMax']
        self.person['HomeProducePlanterReward'] = self['HomeProducePlanterReward']
        self.person['HomeProduceHavesterReward'] = self['HomeProduceHavesterReward']
        self.person['WarehouseBuildingNumLimit'] = self['WarehouseBuildingNumLimit']
        self.person['IsOpenMidAutumn'] = self['IsOpenMidAutumn']
        self.person['IsOpenMidAutumnLantern'] = self['IsOpenMidAutumnLantern']
        self.person['servantexpitemid1'] = self['servantexpitemid1']
        self.person['servantexpitemid2'] = self['servantexpitemid2']
        self.person['servantexpitemid3'] = self['servantexpitemid3']
        self.person['servantexpitemid4'] = self['servantexpitemid4']
        self.person['servantexpitemidexp1'] = self['servantexpitemidexp1']
        self.person['servantexpitemidexp2'] = self['servantexpitemidexp2']
        self.person['servantexpitemidexp3'] = self['servantexpitemidexp3']
        self.person['servantexpitemidexp4'] = self['servantexpitemidexp4']
        self.person['OpenBuildingDonate'] = self['OpenBuildingDonate']
        self.person['OpenBuildBuilding'] = self['OpenBuildBuilding']
        self.person['OpenChangeHomeName'] = self['OpenChangeHomeName']
        self.person['RubkiCubeSmallCount'] = self['RubkiCubeSmallCount']
        self.person['RubkiCubeBigCount'] = self['RubkiCubeBigCount']
        self.person['OpenNationalDayActivity'] = self['OpenNationalDayActivity']
        self.person['NationalDayPlayerLimitLevel'] = self['NationalDayPlayerLimitLevel']
        self.person['NationalDayStartTime'] = self['NationalDayStartTime']
        self.person['NationalDayEndTime'] = self['NationalDayEndTime']
        self.person['OpenWXSuperRPrivilege'] = self['OpenWXSuperRPrivilege']
        self.person['OpenBigWorldWXSuperRPrivilege'] = self['OpenBigWorldWXSuperRPrivilege']
        self.person['nOpenGrowthUpSamsara'] = self['nOpenGrowthUpSamsara']
        self.person['homeHordeFortuneEquipAtmos'] = self['homeHordeFortuneEquipAtmos']
        self.person['homeHordeFortuneTellingAtmos'] = self['homeHordeFortuneTellingAtmos']
        self.person['OpenShareServantBigPhoto'] = self['OpenShareServantBigPhoto']
        self.person['IsOpenEquipRebirthAuto'] = self['IsOpenEquipRebirthAuto']
        self.person['EquipRebirthLevelMax'] = self['EquipRebirthLevelMax']
        self.person['MidAutumnStartTime'] = self['MidAutumnStartTime']
        self.person['MidAutumnEndTime'] = self['MidAutumnEndTime']
        self.person['ServantSlot0OpenLevel'] = self['ServantSlot0OpenLevel']
        self.person['ServantSlot1OpenLevel'] = self['ServantSlot1OpenLevel']
        self.person['ServantSlot2OpenLevel'] = self['ServantSlot2OpenLevel']
        self.person['ServantSlot3OpenLevel'] = self['ServantSlot3OpenLevel']
        self.person['ServantSlot4OpenLevel'] = self['ServantSlot4OpenLevel']
        self.person['UnlockHomePlan3CostYB'] = self['UnlockHomePlan3CostYB']
        self.person['UnlockHomePlan4CostYB'] = self['UnlockHomePlan4CostYB']
        self.person['NationalDayHomeStartTime'] = self['NationalDayHomeStartTime']
        self.person['NationalDayHomeEndTime'] = self['NationalDayHomeEndTime']
        self.person['ProduceOutputAddOfItemMaxTime'] = self['ProduceOutputAddOfItemMaxTime']
        self.person['OpenEquipMirrorForge'] = self['OpenEquipMirrorForge']
        self.person['MaxEquipMirrorForgeLevel'] = self['MaxEquipMirrorForgeLevel']
        self.person['MaxRefineLevelForForge'] = self['MaxRefineLevelForForge']
        self.person['CurServerMaxLv'] = self['CurServerMaxLv']
        self.person['HomeSettleCD'] = self['HomeSettleCD']
        self.person['FairyBreakLimitLevel'] = self['FairyBreakLimitLevel']
        self.person['SkillRefixMaxLevel'] = self['SkillRefixMaxLevel']
        self.person['OpenShareHomeBigphoto'] = self['OpenShareHomeBigphoto']
        self.person['OpenHomePermission'] = self['OpenHomePermission']
        self.person['OpenHomeGuest'] = self['OpenHomeGuest']
        self.person['MidAutumnSceneStartTime'] = self['MidAutumnSceneStartTime']
        self.person['MidAutumnSceneEndTime'] = self['MidAutumnSceneEndTime']
        self.person['MidAutumnRedPacStartTime'] = self['MidAutumnRedPacStartTime']
        self.person['MidAutumnRedPacEndTime'] = self['MidAutumnRedPacEndTime']
        self.person['HomePrayBuffLastTime'] = self['HomePrayBuffLastTime']
        self.person['HomeHordeLeaderDiscount'] = self['HomeHordeLeaderDiscount']
        self.person['OpenHuiLiuLimitShop'] = self['OpenHuiLiuLimitShop']
        self.person['OpenYirongVip'] = self['OpenYirongVip']
        self.person['YirongCanBuyDay'] = self['YirongCanBuyDay']
        self.person['OpenGrowWay'] = self['OpenGrowWay']
        self.person['OpenHomeGift'] = self['OpenHomeGift']
        self.person['OpenBuyHomeGift'] = self['OpenBuyHomeGift']
        self.person['OpenHomePutGift'] = self['OpenHomePutGift']
        self.person['OpenHomeCollectGift'] = self['OpenHomeCollectGift']
        self.person['OpenHomeHyperlink'] = self['OpenHomeHyperlink']
        self.person['HomeGiftCacheLimit'] = self['HomeGiftCacheLimit']
        self.person['FoodBigBattleLevelLimit'] = self['FoodBigBattleLevelLimit']
        self.person['OpenFoodBigBattleActivity'] = self['OpenFoodBigBattleActivity']
        self.person['HomeOpenBlack'] = self['HomeOpenBlack']
        self.person['HomeBlackCountMax'] = self['HomeBlackCountMax']
        self.person['OpenThankDay'] = self['OpenThankDay']
        self.person['OpenHomeEmploy'] = self['OpenHomeEmploy']
        self.person['LowGiftBoxBuildingId'] = self['LowGiftBoxBuildingId']
        self.person['MidGiftBoxBuildingId'] = self['MidGiftBoxBuildingId']
        self.person['HighGiftBoxBuildingId'] = self['HighGiftBoxBuildingId']
        self.person['LowGiftId'] = self['LowGiftId']
        self.person['MidGiftId'] = self['MidGiftId']
        self.person['HighGiftId'] = self['HighGiftId']
        self.person['HomeEmployeeLifeTime'] = self['HomeEmployeeLifeTime']
        self.person['OpenKitPack'] = self['OpenKitPack']
        self.person['OpenKitPackLevel'] = self['OpenKitPackLevel']
        self.person['OpenTXiaoyueRedDot'] = self['OpenTXiaoyueRedDot']
        self.person['OpenReviewMode'] = self['OpenReviewMode']
        self.person['IsOpenSpokesMan'] = self['IsOpenSpokesMan']
        self.person['IsOpenSpokesManGiveGift'] = self['IsOpenSpokesManGiveGift']
        self.person['IsOpenSpokesManMessage'] = self['IsOpenSpokesManMessage']
        self.person['IsUseMysteryMan'] = self['IsUseMysteryMan']
        self.person['IsOpenGuildAlliance'] = self['IsOpenGuildAlliance']
        self.person['MaxGuildAllianceDays'] = self['MaxGuildAllianceDays']
        self.person['MaxGuildAllianceApplyNum'] = self['MaxGuildAllianceApplyNum']
        self.person['UseClientOpenDeadWatch'] = self['UseClientOpenDeadWatch']
        self.person['EmotionIndexMax'] = self['EmotionIndexMax']
        self.person['EmotionIndexZu'] = self['EmotionIndexZu']
        self.person['OpenBuyAllLimitGift'] = self['OpenBuyAllLimitGift']
        self.person['BuyAllLimitGiftRechargeId'] = self['BuyAllLimitGiftRechargeId']
        self.person['SkillZhuanJingSkillExtendMissionID'] = self['SkillZhuanJingSkillExtendMissionID']
        self.person['ThankDayLevelLimit'] = self['ThankDayLevelLimit']
        self.person['FMutualHelpStartTime4Welfare'] = self['FMutualHelpStartTime4Welfare']
        self.person['FMutualHelpEndTime4Welfare'] = self['FMutualHelpEndTime4Welfare']
        self.person['IsOpenGodWeapon'] = self['IsOpenGodWeapon']
        self.person['OpenYaorenMaleCreate'] = self['OpenYaorenMaleCreate']
        self.person['OpenYaorenFemaleCreate'] = self['OpenYaorenFemaleCreate']
        self.person['OpenSpouseLinkage4HomeAttr'] = self['OpenSpouseLinkage4HomeAttr']
        self.person['SpouseLinkageCoefficient4Honor'] = self['SpouseLinkageCoefficient4Honor']
        self.person['SpouseLinkageCoefficient4Geomancy'] = self['SpouseLinkageCoefficient4Geomancy']
        self.person['HomeOpenEmployLevel'] = self['HomeOpenEmployLevel']
        self.person['HomeOpenGrazeLevel'] = self['HomeOpenGrazeLevel']
        self.person['IsOpenGodWeaponJuYuan'] = self['IsOpenGodWeaponJuYuan']
        self.person['IsOpenGodWeaponEnchant'] = self['IsOpenGodWeaponEnchant']
        self.person['IsOpenGodWeaponFuYuan'] = self['IsOpenGodWeaponFuYuan']
        self.person['IsOpenGodWeaponStunt'] = self['IsOpenGodWeaponStunt']
        self.person['IsOpenGodWeaponCoord'] = self['IsOpenGodWeaponCoord']
        self.person['IsOpenGodWeaponQiLing'] = self['IsOpenGodWeaponQiLing']
        self.person['OpenFairyStar'] = self['OpenFairyStar']
        self.person['IsOpenGodWeaponSkill'] = self['IsOpenGodWeaponSkill']
        self.person['GuildBindGroupAreaId'] = self['GuildBindGroupAreaId']
        self.person['EquipRebirthMinEquipCount'] = self['EquipRebirthMinEquipCount']
        self.person['IsOpenTennagerProtect'] = self['IsOpenTennagerProtect']
        self.person['OpenNewGoodShop'] = self['OpenNewGoodShop']
        self.person['OpenTeamPunish'] = self['OpenTeamPunish']
        self.person['OpenPersonalRebate'] = self['OpenPersonalRebate']
        self.person['IsOpenLimitBestSeller'] = self['IsOpenLimitBestSeller']
        self.person['LimitBestSellerOpenLevel'] = self['LimitBestSellerOpenLevel']
        self.person['LimitBestSellerShowLevel'] = self['LimitBestSellerShowLevel']
        self.person['MinOpenServerShowCount'] = self['MinOpenServerShowCount']
        self.person['OpenSevenDayGift'] = self['OpenSevenDayGift']
        self.person['OpenSevenDayBuy'] = self['OpenSevenDayBuy']
        self.person['OpenSevenDayGet'] = self['OpenSevenDayGet']
        self.person['OpenAdsPicture'] = self['OpenAdsPicture']
        self.person['OpenRealNameCheckAward'] = self['OpenRealNameCheckAward']
        self.person['RealNameCheckAwardID1'] = self['RealNameCheckAwardID1']
        self.person['RealNameCheckAwardNum1'] = self['RealNameCheckAwardNum1']
        self.person['RealNameCheckAwardID2'] = self['RealNameCheckAwardID2']
        self.person['RealNameCheckAwardNum2'] = self['RealNameCheckAwardNum2']
        self.person['RealNameCheckAwardID3'] = self['RealNameCheckAwardID3']
        self.person['RealNameCheckAwardNum3'] = self['RealNameCheckAwardNum3']
        self.person['QianzhuangAcceptTime'] = self['QianzhuangAcceptTime']
        self.person['OpenHistoryRecharge'] = self['OpenHistoryRecharge']
        self.person['OpenHistoryRechargeBindGift'] = self['OpenHistoryRechargeBindGift']
        self.person['OpenHistoryRechargeRepayGift'] = self['OpenHistoryRechargeRepayGift']
        self.person['OpenHVChangeSwitch'] = self['OpenHVChangeSwitch']
        self.person['OpenHistoryRechargeRepayRecharge'] = self['OpenHistoryRechargeRepayRecharge']
        self.person['OpenHistoryRechargeLevelDraw'] = self['OpenHistoryRechargeLevelDraw']
        self.person['OpenBaseAttackGuide'] = self['OpenBaseAttackGuide']
        self.person['OpenBaseAttackMaxLevel'] = self['OpenBaseAttackMaxLevel']
        self.person['IsOpenPosterStar'] = self['IsOpenPosterStar']
        self.person['PosterStarLevelLimit'] = self['PosterStarLevelLimit']
        self.person['OpenCAward'] = self['OpenCAward']
        self.person['CurCAwardVersion'] = self['CurCAwardVersion']
        self.person['CAwardEndTime'] = self['CAwardEndTime']
        self.person['CAwardAcceptTime'] = self['CAwardAcceptTime']
        self.person['OpenSupportClientIpv6'] = self['OpenSupportClientIpv6']
        self.person['HistoryRechargeEndTime'] = self['HistoryRechargeEndTime']
        self.person['OpenHistoryRechargeBind'] = self['OpenHistoryRechargeBind']
        self.person['HistoryRechargeRepayRechargeMax'] = self['HistoryRechargeRepayRechargeMax']
        self.person['OpenNewYearRedPacket'] = self['OpenNewYearRedPacket']
        self.person['NewYearRedPacketLevelLimit'] = self['NewYearRedPacketLevelLimit']
        self.person['IsOpenNewYearLantern'] = self['IsOpenNewYearLantern']
        self.person['OpenSpringFestival'] = self['OpenSpringFestival']
        self.person['SpringFesivalLevelLimit'] = self['SpringFesivalLevelLimit']
        self.person['HistoryRechargeBindGiftRegisterLimitTime'] = self['HistoryRechargeBindGiftRegisterLimitTime']
        self.person['HistoryRechargeBindGiftRechargeLimitTime'] = self['HistoryRechargeBindGiftRechargeLimitTime']
        self.person['DefaultTimeZone'] = self['DefaultTimeZone']
        self.person['OpenServerRandomName'] = self['OpenServerRandomName']
        self.person['IsOpenYaoShouXinShou'] = self['IsOpenYaoShouXinShou']
        self.person['PayCallBackUrl'] = self['PayCallBackUrl']
        self.person['IsSkillBarAutoHideOpen'] = self['IsSkillBarAutoHideOpen']
        self.person['SkillAutoHideOpenLevel'] = self['SkillAutoHideOpenLevel']
        self.person['IsOpenSdkPrice'] = self['IsOpenSdkPrice']
        self.person['IsOpenPlayAndGoLog'] = self['IsOpenPlayAndGoLog']
        self.person['ClientSendLogTime'] = self['ClientSendLogTime']
        self.person['ServerAccpetLogTime'] = self['ServerAccpetLogTime']
        self.person['ErrorMsgSize'] = self['ErrorMsgSize']
        self.person['ClientLogMaxCacheSize'] = self['ClientLogMaxCacheSize']
        self.person['OpenGuildShortName'] = self['OpenGuildShortName']
        self.person['IsOpenDLC'] = self['IsOpenDLC']
        self.person['IsOpenDLCAward'] = self['IsOpenDLCAward']
        self.person['DLCOpenLevel'] = self['DLCOpenLevel']
        self.person['BerforeUpdateDLCVersionDay'] = self['BerforeUpdateDLCVersionDay']
        self.person['AfterUpdateDLCVersionDay'] = self['AfterUpdateDLCVersionDay']
        self.person['ReplaceAcceptRewardActiviness'] = self['ReplaceAcceptRewardActiviness']
        self.person['OpenNoviceShop'] = self['OpenNoviceShop']
        self.person['NoviceShopStartSvrDay'] = self['NoviceShopStartSvrDay']
        self.person['NoviceShopEndSvrDay'] = self['NoviceShopEndSvrDay']
        self.person['IsOpenOneChargeGift'] = self['IsOpenOneChargeGift']
        self.person['BuyCDTime'] = self['BuyCDTime']
        self.person['IsOpenTotalConsume'] = self['IsOpenTotalConsume']
        self.person['OpenFlashSales'] = self['OpenFlashSales']
        self.person['OpenDiscountGift'] = self['OpenDiscountGift']
        self.person['ReadGVoiceConfigFromTimeZoneTable'] = self['ReadGVoiceConfigFromTimeZoneTable']
        self.person['OpenVivoGift'] = self['OpenVivoGift']
        self.person['OpenGuildWorldBoss'] = self['OpenGuildWorldBoss']
        self.person['OpenServerActivityLevel'] = self['OpenServerActivityLevel']
        self.person['IsOpenNewImmortality'] = self['IsOpenNewImmortality']
        self.person['NewImmrotalityOpenDays'] = self['NewImmrotalityOpenDays']
        self.person['OpenNewImmortalityTime'] = self['OpenNewImmortalityTime']
        self.person['MaxPlayerMaxNewCampPrestige'] = self['MaxPlayerMaxNewCampPrestige']
        self.person['IsOpenNewPrestige'] = self['IsOpenNewPrestige']
        self.person['OpenGuildOneKeyJoin'] = self['OpenGuildOneKeyJoin']
        self.person['OpenGuildLabel'] = self['OpenGuildLabel']
        self.person['GuildLabelScoreBase'] = self['GuildLabelScoreBase']
        self.person['GuildLabelRefreshScore'] = self['GuildLabelRefreshScore']
        self.person['GuildLabelParam_CombatRank'] = self['GuildLabelParam_CombatRank']
        self.person['GuildLabelParam_CombatUp'] = self['GuildLabelParam_CombatUp']
        self.person['GuildLabelParam_CombatDown'] = self['GuildLabelParam_CombatDown']
        self.person['GuildLabelParam_ActiveRank'] = self['GuildLabelParam_ActiveRank']
        self.person['GuildLabelParam_ActiveUp'] = self['GuildLabelParam_ActiveUp']
        self.person['GuildLabelParam_ActiveDown'] = self['GuildLabelParam_ActiveDown']
        self.person['OpenAdventure'] = self['OpenAdventure']
        self.person['OpenSevenDayLevel'] = self['OpenSevenDayLevel']
        self.person['OpenPAGrowUpLevel'] = self['OpenPAGrowUpLevel']
        self.person['MaxPrestigeExploits'] = self['MaxPrestigeExploits']
        self.person['UseCentAsRechargePrice'] = self['UseCentAsRechargePrice']
        self.person['OpenNormalRechargeRebate'] = self['OpenNormalRechargeRebate']
        self.person['GuildLeavecdLv'] = self['GuildLeavecdLv']
        self.person['OpenPlayAndGoAward'] = self['OpenPlayAndGoAward']
        self.person['OpenEnterCopySceneOpenAutoFight'] = self['OpenEnterCopySceneOpenAutoFight']
        self.person['EnterCopySceneAutoFightRate'] = self['EnterCopySceneAutoFightRate']
        self.person['EnterCopySceneNotAuoFightRate'] = self['EnterCopySceneNotAuoFightRate']
        self.person['OpenShakeLuckDraw'] = self['OpenShakeLuckDraw']
        self.person['OpenShakeShop'] = self['OpenShakeShop']
        self.person['OpenWarriorsGate'] = self['OpenWarriorsGate']
        self.person['HuaDengChuShangOpen'] = self['HuaDengChuShangOpen']
        self.person['HuaDengChuShangStartTime'] = self['HuaDengChuShangStartTime']
        self.person['HuaDengChuShangEndTime'] = self['HuaDengChuShangEndTime']
        self.person['HuaDengChuShangUseItemAwardDays'] = self['HuaDengChuShangUseItemAwardDays']
        self.person['HuaDengChuShangUseItemAwardItemId'] = self['HuaDengChuShangUseItemAwardItemId']
        self.person['WMKefuTrialItemGetLimitDays'] = self['WMKefuTrialItemGetLimitDays']
        self.person['IsGiveGiftRankOpen'] = self['IsGiveGiftRankOpen']
        self.person['GiftGiveRankStartTime'] = self['GiftGiveRankStartTime']
        self.person['GiftGiveRankSettleTime'] = self['GiftGiveRankSettleTime']
        self.person['GiftGiveRankEndTime'] = self['GiftGiveRankEndTime']
        self.person['GiftRankLikeCount'] = self['GiftRankLikeCount']
        self.person['GiftRankLikeAllRewardId1'] = self['GiftRankLikeAllRewardId1']
        self.person['GiftRankLikeAllRewardNum1'] = self['GiftRankLikeAllRewardNum1']
        self.person['GiftRankLikeAllRewardId2'] = self['GiftRankLikeAllRewardId2']
        self.person['GiftRankLikeAllRewardNum2'] = self['GiftRankLikeAllRewardNum2']
        self.person['GiftRankLikeAllRewardId3'] = self['GiftRankLikeAllRewardId3']
        self.person['GiftRankLikeAllRewardNum3'] = self['GiftRankLikeAllRewardNum3']
        self.person['GiftRankLikeAllRewardId4'] = self['GiftRankLikeAllRewardId4']
        self.person['GiftRankLikeAllRewardNum4'] = self['GiftRankLikeAllRewardNum4']
        self.person['GiftRankLikeAllRewardId5'] = self['GiftRankLikeAllRewardId5']
        self.person['GiftRankLikeAllRewardNum5'] = self['GiftRankLikeAllRewardNum5']
        self.person['GiftRankLikeAllRewardId6'] = self['GiftRankLikeAllRewardId6']
        self.person['GiftRankLikeAllRewardNum6'] = self['GiftRankLikeAllRewardNum6']
        self.person['GiftRankLikeAllCountNum6'] = self['GiftRankLikeAllCountNum6']
        self.person['GiftRankLikeAllCount'] = self['GiftRankLikeAllCount']
        self.person['OpenMonsterNian'] = self['OpenMonsterNian']
        self.person['OpenFestivalLuckyCard'] = self['OpenFestivalLuckyCard']
        self.person['LiuShuiXiNpcId'] = self['LiuShuiXiNpcId']
        self.person['UnforgettablePromiseIsOpen'] = self['UnforgettablePromiseIsOpen']
        self.person['UnforgettablePromiseStartTime'] = self['UnforgettablePromiseStartTime']
        self.person['UPAllPlayerRewardItem1'] = self['UPAllPlayerRewardItem1']
        self.person['UPAllPlayerRewardItem1Count'] = self['UPAllPlayerRewardItem1Count']
        self.person['MonsterNianFirecrackersItem'] = self['MonsterNianFirecrackersItem']
        self.person['LiuShuiXiStartTime'] = self['LiuShuiXiStartTime']
        self.person['LiuShuiXiEndTime'] = self['LiuShuiXiEndTime']
        self.person['LiuShuiXiOpenStartTime'] = self['LiuShuiXiOpenStartTime']
        self.person['LiuShuiXiOpenEndTime'] = self['LiuShuiXiOpenEndTime']
        self.person['WMKefuTrialItemId'] = self['WMKefuTrialItemId']
        self.person['HuaDengChuShangItemStartTime'] = self['HuaDengChuShangItemStartTime']
        self.person['HuaDengChuShangItemEndTime'] = self['HuaDengChuShangItemEndTime']
        self.person['OpenFestivalLoginReward'] = self['OpenFestivalLoginReward']
        self.person['LiuShuiXiItemId'] = self['LiuShuiXiItemId']
        self.person['GiftRankLikeRewardId1'] = self['GiftRankLikeRewardId1']
        self.person['GiftRankLikeRewardNum1'] = self['GiftRankLikeRewardNum1']
        self.person['GiftRankLikeRewardId2'] = self['GiftRankLikeRewardId2']
        self.person['GiftRankLikeRewardNum2'] = self['GiftRankLikeRewardNum2']
        self.person['GiftRankLikeRewardId3'] = self['GiftRankLikeRewardId3']
        self.person['GiftRankLikeRewardNum3'] = self['GiftRankLikeRewardNum3']
        self.person['OpenDiMaiTanXian'] = self['OpenDiMaiTanXian']
        self.person['DiMaiYuanSuNingJuTimesMax'] = self['DiMaiYuanSuNingJuTimesMax']
        self.person['DiMaiBuyHongXiBasePrice'] = self['DiMaiBuyHongXiBasePrice']
        self.person['DiMaiJingCuMaxCountAtSameTime'] = self['DiMaiJingCuMaxCountAtSameTime']
        self.person['DiMaiHongXiRewardTime'] = self['DiMaiHongXiRewardTime']
        self.person['DiMaiJingLingDialogCD'] = self['DiMaiJingLingDialogCD']
        self.person['DiMaiJingLingDialogTimesMax'] = self['DiMaiJingLingDialogTimesMax']
        self.person['DiMaiChallengeOpen'] = self['DiMaiChallengeOpen']
        self.person['DiMaiAutoChallengeRewardTime'] = self['DiMaiAutoChallengeRewardTime']
        self.person['AutoMaxChallengeRewardTime'] = self['AutoMaxChallengeRewardTime']
        self.person['AutoShowSliverItemId'] = self['AutoShowSliverItemId']
        self.person['AutoShowSkillSoulItemId'] = self['AutoShowSkillSoulItemId']
        self.person['OpenDiMaiJingLuo'] = self['OpenDiMaiJingLuo']
        self.person['OpenDiMaiJingLuoOpenLevel'] = self['OpenDiMaiJingLuoOpenLevel']
        self.person['RegressIsOpen'] = self['RegressIsOpen']
        self.person['RegressBuffValid'] = self['RegressBuffValid']
        self.person['RegressGiftCanBuy'] = self['RegressGiftCanBuy']
        self.person['RegressDayBuff'] = self['RegressDayBuff']
        self.person['DiMaiBuyHongXiMaxProgress'] = self['DiMaiBuyHongXiMaxProgress']
        self.person['OpenShiLian'] = self['OpenShiLian']
        self.person['ShiLianMaxLevel'] = self['ShiLianMaxLevel']
        self.person['OpenLiveBroadcast'] = self['OpenLiveBroadcast']
        self.person['LiveBroadcastOpenLevel'] = self['LiveBroadcastOpenLevel']
        self.person['OpenTianShuRecommend'] = self['OpenTianShuRecommend']
        self.person['FashionShowFriendGiftNeedFriendPoint'] = self['FashionShowFriendGiftNeedFriendPoint']
        self.person['ShiLianSettleDayOfWeek'] = self['ShiLianSettleDayOfWeek']
        self.person['ShiLianSettleTime'] = self['ShiLianSettleTime']
        self.person['ShiLianCiZhuiGenDayOfWeek'] = self['ShiLianCiZhuiGenDayOfWeek']
        self.person['ShiLianCiZhuiGenTime'] = self['ShiLianCiZhuiGenTime']
        self.person['OpenChallengeRank'] = self['OpenChallengeRank']
        self.person['OpenHonorCoinsExchange'] = self['OpenHonorCoinsExchange']
        self.person['OpenHonorCoinsExchangeRankLimit'] = self['OpenHonorCoinsExchangeRankLimit']
        self.person['OpenEveryDayBank'] = self['OpenEveryDayBank']
        self.person['OpenGuildTeam'] = self['OpenGuildTeam']
        self.person['OpenGuildTeamServerLevel'] = self['OpenGuildTeamServerLevel']
        self.person['OpenTreasureCompass'] = self['OpenTreasureCompass']
        self.person['OpenJuNengZhuan'] = self['OpenJuNengZhuan']
        self.person['OpenCharm'] = self['OpenCharm']
        self.person['OpenFashionCharm'] = self['OpenFashionCharm']
        self.person['OpenTitleCharm'] = self['OpenTitleCharm']
        self.person['OpenCharmRank'] = self['OpenCharmRank']
        self.person['OpenDyeCharm'] = self['OpenDyeCharm']
        self.person['OpenCharmShop'] = self['OpenCharmShop']
        self.person['OpenFriendCricle'] = self['OpenFriendCricle']
        self.person['OpenBigworldGuildWar'] = self['OpenBigworldGuildWar']
        self.person['BWGWOpenDayOfWeek'] = self['BWGWOpenDayOfWeek']
        self.person['BWGWSignupTime'] = self['BWGWSignupTime']
        self.person['BWGWStartTime1'] = self['BWGWStartTime1']
        self.person['BWGWStartTime2'] = self['BWGWStartTime2']
        self.person['BWGWWinCon'] = self['BWGWWinCon']
        self.person['BWGWLoseCon'] = self['BWGWLoseCon']
        self.person['BWGWMissCon'] = self['BWGWMissCon']
        self.person['BWGWSignupArmyNumLimit'] = self['BWGWSignupArmyNumLimit']
        self.person['BWGWSignupPlayerNumMin'] = self['BWGWSignupPlayerNumMin']
        self.person['BWGWSignupPlayerNumMax'] = self['BWGWSignupPlayerNumMax']
        self.person['BWGWInGuildTimeMin'] = self['BWGWInGuildTimeMin']
        self.person['BWGWPlayerLevelMin'] = self['BWGWPlayerLevelMin']
        self.person['BWGWBlockArmyGuard'] = self['BWGWBlockArmyGuard']
        self.person['BWGWRestSceneId'] = self['BWGWRestSceneId']
        self.person['BWGWBattleSceneId'] = self['BWGWBattleSceneId']
        self.person['BWGWExperienceServerFlag'] = self['BWGWExperienceServerFlag']
        self.person['BWGWExperienceRefrenceTime'] = self['BWGWExperienceRefrenceTime']
        self.person['BWGWExperienceCycle'] = self['BWGWExperienceCycle']
        self.person['BWGWFormalRefrenceTime'] = self['BWGWFormalRefrenceTime']
        self.person['BWGWFormalCycle'] = self['BWGWFormalCycle']
        self.person['BWGWSendRewardTime'] = self['BWGWSendRewardTime']
        self.person['BWGWAutoRewardDayOfWeek'] = self['BWGWAutoRewardDayOfWeek']
        self.person['BWGWAutoRewardTime'] = self['BWGWAutoRewardTime']
        self.person['OpenServantFate'] = self['OpenServantFate']
        self.person['DyeAddCharm'] = self['DyeAddCharm']
        self.person['OpenLiuShuiXi'] = self['OpenLiuShuiXi']
        self.person['OpenPhotoFrame'] = self['OpenPhotoFrame']
        self.person['OpenCOTWarmUp'] = self['OpenCOTWarmUp']
        self.person['COTWarmUpStartTime'] = self['COTWarmUpStartTime']
        self.person['COTWarmUpEndTime'] = self['COTWarmUpEndTime']
        self.person['COTWarmUpRewardItemId'] = self['COTWarmUpRewardItemId']
        self.person['COTWarmUpRewardItemNum'] = self['COTWarmUpRewardItemNum']
        self.person['GlobalPK_Pre_StartTime'] = self['GlobalPK_Pre_StartTime']
        self.person['GlobalPK_Pre_PrepareTime'] = self['GlobalPK_Pre_PrepareTime']
        self.person['GlobalPK_Pre_VerifyTime'] = self['GlobalPK_Pre_VerifyTime']
        self.person['GlobalPK_Pre_SignupTime'] = self['GlobalPK_Pre_SignupTime']
        self.person['GlobalPK_Pre_MatchTime'] = self['GlobalPK_Pre_MatchTime']
        self.person['GlobalPK_Pre_AwardTime'] = self['GlobalPK_Pre_AwardTime']
        self.person['GlobalPK_Pre_EndTime'] = self['GlobalPK_Pre_EndTime']
        self.person['GlobalPK_Pre_CanMatchTime'] = self['GlobalPK_Pre_CanMatchTime']
        self.person['GlobalPK_Final_NoticeTime'] = self['GlobalPK_Final_NoticeTime']
        self.person['GlobalPK_Final_StartTime'] = self['GlobalPK_Final_StartTime']
        self.person['GlobalPK_Final_EndTime'] = self['GlobalPK_Final_EndTime']
        self.person['GlobalPK_Season'] = self['GlobalPK_Season']
        self.person['GlobalPK_RankGrasp'] = self['GlobalPK_RankGrasp']
        self.person['cotviewbegtime'] = self['cotviewbegtime']
        self.person['cotviewendtime'] = self['cotviewendtime']
        self.person['ShowBackFashion'] = self['ShowBackFashion']
        self.person['OpenLXWenDie'] = self['OpenLXWenDie']
        self.person['LXWenDieLevel'] = self['LXWenDieLevel']
        self.person['LXWenDieStartTime'] = self['LXWenDieStartTime']
        self.person['LXWenDieEndTime'] = self['LXWenDieEndTime']
        self.person['LXWenDieBuQianDay'] = self['LXWenDieBuQianDay']
        self.person['OpenQiXiStar'] = self['OpenQiXiStar']
        self.person['QiXiStarCostItemId'] = self['QiXiStarCostItemId']
        self.person['QiXiStarInviteExpirationTime'] = self['QiXiStarInviteExpirationTime']
        self.person['OpenNewPlayerCatch'] = self['OpenNewPlayerCatch']
        self.person['NewPlayerCatchNeedLevel'] = self['NewPlayerCatchNeedLevel']
        self.person['NewPlayerCatchExpValue'] = self['NewPlayerCatchExpValue']
        self.person['NewPlayerCatchDayMax'] = self['NewPlayerCatchDayMax']
        self.person['OpenServerCatch'] = self['OpenServerCatch']
        self.person['CotTotalRewardYuanbaoNum'] = self['CotTotalRewardYuanbaoNum']
        self.person['QiXiStarUnlockColumnCount'] = self['QiXiStarUnlockColumnCount']
        self.person['OpenWishingStep'] = self['OpenWishingStep']
        self.person['OpenDomainWarDargonTreasure'] = self['OpenDomainWarDargonTreasure']
        self.person['DomainWarDargonTreasureServerLevel'] = self['DomainWarDargonTreasureServerLevel']
        self.person['DomainWarDargonTreasureCDTime'] = self['DomainWarDargonTreasureCDTime']
        self.person['DomainWarDargonTreasureBaseTime'] = self['DomainWarDargonTreasureBaseTime']
        self.person['QiXiStarRewardItemId'] = self['QiXiStarRewardItemId']
        self.person['QiXiStarRewardItemCount'] = self['QiXiStarRewardItemCount']
        self.person['GlobalPK_QualificationMatchDate'] = self['GlobalPK_QualificationMatchDate']
        self.person['GlobalPK_CopyUserDate'] = self['GlobalPK_CopyUserDate']
        self.person['GlobalPK_ConfirmDataTime'] = self['GlobalPK_ConfirmDataTime']
        self.person['OpenWishingNewbie'] = self['OpenWishingNewbie']
        self.person['BWPVPSeasonForCOT'] = self['BWPVPSeasonForCOT']
        self.person['OpenZuLongCelebration'] = self['OpenZuLongCelebration']
        self.person['ZCLightPieceCost'] = self['ZCLightPieceCost']
        self.person['ZCLotteryCost'] = self['ZCLotteryCost']
        self.person['ZCMaxReceivedPieceCount'] = self['ZCMaxReceivedPieceCount']
        self.person['OpenNewFirstRecharge'] = self['OpenNewFirstRecharge']
        self.person['OpenShowNewFirstRecharge'] = self['OpenShowNewFirstRecharge']
        self.person['NewFirstRechargeNewId'] = self['NewFirstRechargeNewId']
        self.person['OpenRemakeName'] = self['OpenRemakeName']
        self.person['OpenDiscountLimit'] = self['OpenDiscountLimit']
        self.person['DiscountLimitDays'] = self['DiscountLimitDays']
        self.person['DiscountLimitOpenLevel'] = self['DiscountLimitOpenLevel']
        self.person['OpenTianshuBox'] = self['OpenTianshuBox']
        self.person['OpenTianshuBoxLevel'] = self['OpenTianshuBoxLevel']
        self.person['OpenCollectionShop'] = self['OpenCollectionShop']
        self.person['WMKefuTrialItemNeedAccRecharge'] = self['WMKefuTrialItemNeedAccRecharge']
        self.person['OpenYuLanMaleCreate'] = self['OpenYuLanMaleCreate']
        self.person['OpenYuLanFemaleCreate'] = self['OpenYuLanFemaleCreate']
        self.person['OpenServantEquip'] = self['OpenServantEquip']
        self.person['OpenXinPo'] = self['OpenXinPo']
        self.person['ServantEquipOpenLevel'] = self['ServantEquipOpenLevel']
        self.person['OpenKabinettGarret'] = self['OpenKabinettGarret']
        self.person['OpenAnecdote'] = self['OpenAnecdote']
        self.person['OpenBingXueJie'] = self['OpenBingXueJie']
        self.person['OpenBingXueJieSnowman'] = self['OpenBingXueJieSnowman']
        self.person['BingXueJieSnowmanStartTime'] = self['BingXueJieSnowmanStartTime']
        self.person['BingXueJieSnowmanEndTime'] = self['BingXueJieSnowmanEndTime']
        self.person['BingXueJieSnowmanGetAwardEndTime'] = self['BingXueJieSnowmanGetAwardEndTime']
        self.person['BingXueJieSnowballItemId'] = self['BingXueJieSnowballItemId']
        self.person['BingXueJieQuizStartTime'] = self['BingXueJieQuizStartTime']
        self.person['BingXueJieQuizEndTime'] = self['BingXueJieQuizEndTime']
        self.person['BingXueJieQuizBestAwardId'] = self['BingXueJieQuizBestAwardId']
        self.person['OpenBingXueJieQuiz'] = self['OpenBingXueJieQuiz']
        self.person['OpenFightVolcano'] = self['OpenFightVolcano']
        self.person['FvOpenPlayerLevel'] = self['FvOpenPlayerLevel']
        self.person['FvOpenDayOfWeek'] = self['FvOpenDayOfWeek']
        self.person['FvOpenTime'] = self['FvOpenTime']
        self.person['fvCloseTime'] = self['fvCloseTime']
        self.person['GlobalPK_CotWorldId'] = self['GlobalPK_CotWorldId']
        self.person['FvRelieveCD'] = self['FvRelieveCD']
        self.person['OpenBrotherhoodSkillSystem'] = self['OpenBrotherhoodSkillSystem']
        self.person['OpenNewbieBank'] = self['OpenNewbieBank']
        self.person['OpenRookieCompass'] = self['OpenRookieCompass']
        self.person['GuildAdditionNeedServerOpenDay'] = self['GuildAdditionNeedServerOpenDay']
        self.person['OpenMonsterNianRank'] = self['OpenMonsterNianRank']
        self.person['HongBaoMaxSendYuanBaoNumWeekly'] = self['HongBaoMaxSendYuanBaoNumWeekly']
        self.person['HongBaoMinSendYuanBaoNum'] = self['HongBaoMinSendYuanBaoNum']
        self.person['HongBaoMaxSendYuanBaoNum'] = self['HongBaoMaxSendYuanBaoNum']
        self.person['HongBaoMinSendYuanBaoCount'] = self['HongBaoMinSendYuanBaoCount']
        self.person['HongBaoMaxSendYuanBaoCount'] = self['HongBaoMaxSendYuanBaoCount']
        self.person['HongBaoMaxReceiveYuanBaoNumDaily'] = self['HongBaoMaxReceiveYuanBaoNumDaily']
        self.person['HongBaoMaxTipsReceiveCount'] = self['HongBaoMaxTipsReceiveCount']
        self.person['OpenHongYunLianNian'] = self['OpenHongYunLianNian']
        self.person['HongYunDailyReceiveMax'] = self['HongYunDailyReceiveMax']
        self.person['ReceiveHongBaoGetHongYun'] = self['ReceiveHongBaoGetHongYun']
        self.person['SendHongBaoGetHongYun'] = self['SendHongBaoGetHongYun']
        self.person['OpenItemSubscribe'] = self['OpenItemSubscribe']
        self.person['OpenTianXingMiQi'] = self['OpenTianXingMiQi']
        self.person['OpenCelebrationZL'] = self['OpenCelebrationZL']
        self.person['CelebrationZLStartTime'] = self['CelebrationZLStartTime']
        self.person['CelebrationZLEndTime'] = self['CelebrationZLEndTime']
        self.person['BWGWEndTime1'] = self['BWGWEndTime1']
        self.person['BWGWEndTime2'] = self['BWGWEndTime2']
        self.person['OrangeItemLevel'] = self['OrangeItemLevel']
        self.person['OpenUseFirecrakerRewardItem'] = self['OpenUseFirecrakerRewardItem']
        self.person['TowerRecommendRatio'] = self['TowerRecommendRatio']
        self.person['BWGWBattleSceneMaxNum'] = self['BWGWBattleSceneMaxNum']
        self.person['BWGWBattleSceneMaxNum2'] = self['BWGWBattleSceneMaxNum2']
        self.person['QuickChallengeCombatLessFactor'] = self['QuickChallengeCombatLessFactor']
        self.person['IsOpenPeriodBestSeller'] = self['IsOpenPeriodBestSeller']
        self.person['PeriodBestSellerOpenLevel'] = self['PeriodBestSellerOpenLevel']
        self.person['PeriodBestSellerShowLevel'] = self['PeriodBestSellerShowLevel']
        self.person['OpenBattleScheme'] = self['OpenBattleScheme']
        self.person['OpenBattleSchemeChangeName'] = self['OpenBattleSchemeChangeName']
        self.person['BackpackNewItemExistTime'] = self['BackpackNewItemExistTime']
        self.person['OpenCOTCoin'] = self['OpenCOTCoin']
        self.person['HuaGuanJieHongBaoCoverId'] = self['HuaGuanJieHongBaoCoverId']
        self.person['IsOpenWeeklyFree'] = self['IsOpenWeeklyFree']
        self.person['SmallBigAwardMustGetThreshold'] = self['SmallBigAwardMustGetThreshold']
        self.person['BigAwardMustGetThreshold'] = self['BigAwardMustGetThreshold']
        self.person['NPBigAwardMustGetThreshold'] = self['NPBigAwardMustGetThreshold']
        self.person['QuickChallengeCombatMoreFactor'] = self['QuickChallengeCombatMoreFactor']
        self.person['YuanBaoShopHideItems'] = self['YuanBaoShopHideItems']
        self.person['OpenTianshuBoxStudy'] = self['OpenTianshuBoxStudy']
        self.person['OpenTianshuBoxActive'] = self['OpenTianshuBoxActive']
        self.person['OpenActivityNightGuide'] = self['OpenActivityNightGuide']
        self.person['ActivityNightGuideStartLevel'] = self['ActivityNightGuideStartLevel']
        self.person['ActivityNightGuideDayCnt'] = self['ActivityNightGuideDayCnt']
        self.person['ActivityNightGuideRewardItemId1'] = self['ActivityNightGuideRewardItemId1']
        self.person['ActivityNightGuideRewardItemNum1'] = self['ActivityNightGuideRewardItemNum1']
        self.person['ActivityNightGuideRewardItemId2'] = self['ActivityNightGuideRewardItemId2']
        self.person['ActivityNightGuideRewardItemNum2'] = self['ActivityNightGuideRewardItemNum2']
        self.person['ActivityNightGuideRewardItemId3'] = self['ActivityNightGuideRewardItemId3']
        self.person['ActivityNightGuideRewardItemNum3'] = self['ActivityNightGuideRewardItemNum3']
        self.person['OpenServerActivityCloseRcharegeTime'] = self['OpenServerActivityCloseRcharegeTime']
        self.person['CompressHpPer'] = self['CompressHpPer']
        self.person['OpenHongBaoCustomizeName'] = self['OpenHongBaoCustomizeName']
        self.person['OpenAnswerActivity'] = self['OpenAnswerActivity']
        self.person['AnswerActivityJoinLevel'] = self['AnswerActivityJoinLevel']
        self.person['AnswerActivityStartTime'] = self['AnswerActivityStartTime']
        self.person['AnswerActivityEndTime'] = self['AnswerActivityEndTime']
        self.person['AnswerActivityDayStartTime'] = self['AnswerActivityDayStartTime']
        self.person['AnswerActivityRoundNum'] = self['AnswerActivityRoundNum']
        self.person['AnswerActivityRoundTime'] = self['AnswerActivityRoundTime']
        self.person['AnswerActivityRewardItem'] = self['AnswerActivityRewardItem']
        self.person['AnswerActivityRewardItemNum'] = self['AnswerActivityRewardItemNum']
        self.person['AnswerActivityRewardItemNumForRank'] = self['AnswerActivityRewardItemNumForRank']
        self.person['OpenGuildManualMerge'] = self['OpenGuildManualMerge']
        self.person['OpenSignetNingLian'] = self['OpenSignetNingLian']
        self.person['SignetNingLianOpenLevel'] = self['SignetNingLianOpenLevel']
        self.person['OpenDomainWarSeason'] = self['OpenDomainWarSeason']
        self.person['DomainWarSeasonBaseTime'] = self['DomainWarSeasonBaseTime']
        self.person['DomainWarSeasonCycleDay'] = self['DomainWarSeasonCycleDay']
        self.person['OpenDomainWarSeasonReward'] = self['OpenDomainWarSeasonReward']
        self.person['OpenDomainWarSeasonPlayerReward'] = self['OpenDomainWarSeasonPlayerReward']
        self.person['OpenDomainWarLimitShop'] = self['OpenDomainWarLimitShop']
        self.person['DomainWarLimitShopOpenLevel'] = self['DomainWarLimitShopOpenLevel']
        self.person['OpenDomainWarSalary'] = self['OpenDomainWarSalary']
        self.person['OpenDomainWarGodBear'] = self['OpenDomainWarGodBear']
        self.person['UpAndAdvanceUpDisCountItemId'] = self['UpAndAdvanceUpDisCountItemId']
        self.person['ReportOpenServerDays'] = self['ReportOpenServerDays']
        self.person['HuaGuanJieActivityStartTime'] = self['HuaGuanJieActivityStartTime']
        self.person['HuaGuanJieActivityEndTime'] = self['HuaGuanJieActivityEndTime']
        self.person['HuaGuanJieRankStartTime'] = self['HuaGuanJieRankStartTime']
        self.person['HuaGuanJieRankEndTime'] = self['HuaGuanJieRankEndTime']
        self.person['HuaGuanJieValidRank'] = self['HuaGuanJieValidRank']
        self.person['DomainWarPlayerCountMax'] = self['DomainWarPlayerCountMax']
        self.person['HuaGuanJieFreeGiftCountPerDay'] = self['HuaGuanJieFreeGiftCountPerDay']
        self.person['HuaGuanJieHongBaoMoney'] = self['HuaGuanJieHongBaoMoney']
        self.person['HuaGuanJieHongBaoCount'] = self['HuaGuanJieHongBaoCount']
        self.person['PerfectKoiActivityBeginTime'] = self['PerfectKoiActivityBeginTime']
        self.person['PerfectKoiActivityEndTime'] = self['PerfectKoiActivityEndTime']
        self.person['OpenSignetWarPath'] = self['OpenSignetWarPath']
        self.person['HuaGuanJieXinYiLeGouOpen'] = self['HuaGuanJieXinYiLeGouOpen']
        self.person['DomainLimitShopYuanbaoShare'] = self['DomainLimitShopYuanbaoShare']
        self.person['DomainLimitShopBangYuanShare'] = self['DomainLimitShopBangYuanShare']
        self.person['DomainLimitShopYuanBaoSliverShare'] = self['DomainLimitShopYuanBaoSliverShare']
        self.person['PerfectKoiActivityLevelLimit'] = self['PerfectKoiActivityLevelLimit']
        self.person['OpenArmyLeaderSign'] = self['OpenArmyLeaderSign']
        self.person['BWGWStartTime3'] = self['BWGWStartTime3']
        self.person['BWGWEndTime3'] = self['BWGWEndTime3']
        self.person['OpenDaoChaMaleCreate'] = self['OpenDaoChaMaleCreate']
        self.person['OpenDaoChaFemaleCreate'] = self['OpenDaoChaFemaleCreate']
        self.person['OpenChronoTrigger'] = self['OpenChronoTrigger']
        self.person['OpenChronoTriggerBeginTime'] = self['OpenChronoTriggerBeginTime']
        self.person['OpenChronoTriggerExcShop'] = self['OpenChronoTriggerExcShop']
        self.person['OpenChronoTriggerTalentTree'] = self['OpenChronoTriggerTalentTree']
        self.person['OpenChronoTriggerSeasonAward'] = self['OpenChronoTriggerSeasonAward']
        self.person['OpenChronoTriggerGallary'] = self['OpenChronoTriggerGallary']
        self.person['ChronoTriggerOpenSvrLvl'] = self['ChronoTriggerOpenSvrLvl']
        self.person['ChronoTriggerOpenPlayerLvl'] = self['ChronoTriggerOpenPlayerLvl']
        self.person['ChronoTriggerOpenBeginWeekDay'] = self['ChronoTriggerOpenBeginWeekDay']
        self.person['ChronoTriggerOpenEndWeekDay'] = self['ChronoTriggerOpenEndWeekDay']
        self.person['ChronoTriggerOpenTimeOfDay'] = self['ChronoTriggerOpenTimeOfDay']
        self.person['ChronoTriggerEndTimeOfDay'] = self['ChronoTriggerEndTimeOfDay']
        self.person['ChronoTriggerMaxServantCallValue'] = self['ChronoTriggerMaxServantCallValue']
        self.person['ChronoTriggerSeasonWeekCnt'] = self['ChronoTriggerSeasonWeekCnt']
        self.person['ChronoTriggerTalentPointAddCntPerWeek'] = self['ChronoTriggerTalentPointAddCntPerWeek']
        self.person['ChronoTriggerResetDayOfWeek'] = self['ChronoTriggerResetDayOfWeek']
        self.person['OpenLingShi'] = self['OpenLingShi']
        self.person['OpenTeamAutoFight'] = self['OpenTeamAutoFight']
        self.person['ChronoTriggerSelectServantMaxTime'] = self['ChronoTriggerSelectServantMaxTime']
        self.person['OpenBackGroundPhoto'] = self['OpenBackGroundPhoto']
        self.person['OpenDiMaiPenFa'] = self['OpenDiMaiPenFa']
        self.person['OpenDiMaiMiJing'] = self['OpenDiMaiMiJing']
        self.person['DiMaiMiJingOpenLevel'] = self['DiMaiMiJingOpenLevel']
        self.person['DiMaiMiJingDurationHour'] = self['DiMaiMiJingDurationHour']
        self.person['DiMaiPenFaStartHour1'] = self['DiMaiPenFaStartHour1']
        self.person['DiMaiPenFaStartHour2'] = self['DiMaiPenFaStartHour2']
        self.person['DiMaiMiJingWeekMaxHelpRewardCnt'] = self['DiMaiMiJingWeekMaxHelpRewardCnt']
        self.person['OpenPackNeatenOpearate'] = self['OpenPackNeatenOpearate']
        self.person['OpenEveryDayGift'] = self['OpenEveryDayGift']
        self.person['EveryDayGiftOpenLevel'] = self['EveryDayGiftOpenLevel']
        self.person['EveryDayGiftDuringDayNum'] = self['EveryDayGiftDuringDayNum']
        self.person['OpenMonthCardShop'] = self['OpenMonthCardShop']
        self.person['MonthCardShopXuLongLvForExtraRefreshCnt1'] = self['MonthCardShopXuLongLvForExtraRefreshCnt1']
        self.person['OpenPAMonthAccrualTongTian'] = self['OpenPAMonthAccrualTongTian']
        self.person['FestivalRegressIsOpen'] = self['FestivalRegressIsOpen']
        self.person['OpenCardPhoto'] = self['OpenCardPhoto']
        self.person['FestivalRegressCalculateStartTime'] = self['FestivalRegressCalculateStartTime']
        self.person['OpenLingShiOneKeyInstall'] = self['OpenLingShiOneKeyInstall']
        self.person['OpenDiMaiJingHaiCombateValue'] = self['OpenDiMaiJingHaiCombateValue']
        self.person['IsOpenEquipEnchantTrans'] = self['IsOpenEquipEnchantTrans']
        self.person['BingXueJieMainPagePreTime'] = self['BingXueJieMainPagePreTime']
        self.person['BingXueJieMainPageStartTime'] = self['BingXueJieMainPageStartTime']
        self.person['BingXueJieMainPageEndTime'] = self['BingXueJieMainPageEndTime']
        self.person['BingXueJieFengWuKaoChaStartTime'] = self['BingXueJieFengWuKaoChaStartTime']
        self.person['BingXueJieFengWuKaoChaEndTime'] = self['BingXueJieFengWuKaoChaEndTime']
        #.person['BingXueJieFengWuKaoChaStartMissionId'] = self['BingXueJieFengWuKaoChaStartMissionId']
        self.person['BingXueJieFengWuKaoChaOpen'] = self['BingXueJieFengWuKaoChaOpen']
        self.person['BingXueJieFireworkStartTime1'] = self['BingXueJieFireworkStartTime1']
        self.person['BingXueJieFireworkEndTime1'] = self['BingXueJieFireworkEndTime1']
        self.person['BingXueJieFireworkStartTime2'] = self['BingXueJieFireworkStartTime2']
        self.person['BingXueJieFireworkEndTime2'] = self['BingXueJieFireworkEndTime2']
        self.person['BingXueJieFireworkStartTime3'] = self['BingXueJieFireworkStartTime3']
        self.person['BingXueJieFireworkEndTime3'] = self['BingXueJieFireworkEndTime3']
        self.person['BingXueJieFireworkStartTime4'] = self['BingXueJieFireworkStartTime4']
        self.person['BingXueJieFireworkEndTime4'] = self['BingXueJieFireworkEndTime4']
        self.person['BingXueJieFireworkOpenChestMaxCount'] = self['BingXueJieFireworkOpenChestMaxCount']
        self.person['OpenStudioVerify'] = self['OpenStudioVerify']
        self.person['DiMaiMiJingTriggerWeekMaxCnt'] = self['DiMaiMiJingTriggerWeekMaxCnt']
        self.person['OpenBingXueJieFirework'] = self['OpenBingXueJieFirework']
        self.person['OpenBingXueJieFireworkItem'] = self['OpenBingXueJieFireworkItem']
        self.person['BingXueJieFireworkUseDistance'] = self['BingXueJieFireworkUseDistance']
        self.person['OpenBingXueJiePresent'] = self['OpenBingXueJiePresent']
        self.person['BingXueJiePresentStartTime'] = self['BingXueJiePresentStartTime']
        self.person['BingXueJiePresentEndTime'] = self['BingXueJiePresentEndTime']
        self.person['BingXueJiePresentItemID'] = self['BingXueJiePresentItemID']
        self.person['BingXueJieFireworkChestOpenLevel'] = self['BingXueJieFireworkChestOpenLevel']
        self.person['BingXueJiePresentNeedPlayerLevel'] = self['BingXueJiePresentNeedPlayerLevel']
        self.person['OpenDomainPlunder'] = self['OpenDomainPlunder']
        self.person['OpenDomainPlunderServerLevel'] = self['OpenDomainPlunderServerLevel']
        self.person['BingXueJieFireworkUseRandomShift'] = self['BingXueJieFireworkUseRandomShift']
        self.person['CelebrationZLBuyLevelCost'] = self['CelebrationZLBuyLevelCost']
        self.person['BingXueJieFengWuKaoChaOpenMissionId'] = self['BingXueJieFengWuKaoChaOpenMissionId']
        self.person['FakeGuildChiefName'] = self['FakeGuildChiefName']
        self.person['DomainPlunderDomainWarDebuffRlieveAddTime'] = self['DomainPlunderDomainWarDebuffRlieveAddTime']
        self.person['BingXueJieFireworkChestRefreshTime'] = self['BingXueJieFireworkChestRefreshTime']
        self.person['FakeGuildOpen'] = self['FakeGuildOpen']
        self.person['BingXueJieFengWuKaoChaMission'] = self['BingXueJieFengWuKaoChaMission']
        self.person['IsOpenChangeProfessionAct'] = self['IsOpenChangeProfessionAct']
        self.person['CelebrationZLExtraRewardMaxCnt'] = self['CelebrationZLExtraRewardMaxCnt']
        self.person['GuildFightWorldBossBeginTime'] = self['GuildFightWorldBossBeginTime']
        self.person['GuildFightWorldBossEndTime'] = self['GuildFightWorldBossEndTime']
        self.person['TournamentBeginTime'] = self['TournamentBeginTime']
        self.person['TournamentEndTime'] = self['TournamentEndTime']
        self.person['GuildWarChampionshipOpenTime'] = self['GuildWarChampionshipOpenTime']
        self.person['GuildWarChampionshipCloseTime'] = self['GuildWarChampionshipCloseTime']
        self.person['ShowMisSubTypeLv'] = self['ShowMisSubTypeLv']
        self.person['NewFirstRechargeNoticeMis'] = self['NewFirstRechargeNoticeMis']
        self.person['DiscountLimitNoticeMis'] = self['DiscountLimitNoticeMis']
        self.person['BingXueJiePresentShowStartTime'] = self['BingXueJiePresentShowStartTime']
        self.person['DomainPlunderAttackWinGuildCoinMuti'] = self['DomainPlunderAttackWinGuildCoinMuti']
        self.person['DomainPlunderAttackWinGuildCoin'] = self['DomainPlunderAttackWinGuildCoin']
        self.person['DomainPlunderAttackLoseGuildCoin'] = self['DomainPlunderAttackLoseGuildCoin']
        self.person['ActivityTurnBeginTime'] = self['ActivityTurnBeginTime']
        self.person['CelebrationCakeMaxRewardTimePerDay'] = self['CelebrationCakeMaxRewardTimePerDay']
        self.person['CelebrationCakeOwnerProtectTime'] = self['CelebrationCakeOwnerProtectTime']
        self.person['ReadGetRewarMinPlayerLvl'] = self['ReadGetRewarMinPlayerLvl']
        self.person['OpenBigWorldArena'] = self['OpenBigWorldArena']
        self.person['BigWorldArenaOpenDay'] = self['BigWorldArenaOpenDay']
        self.person['BigWorldArenaOpenTimeBegin'] = self['BigWorldArenaOpenTimeBegin']
        self.person['BigWorldArenaOpenTimeEnd'] = self['BigWorldArenaOpenTimeEnd']
        self.person['BigWorldArenaOpenServerLevel'] = self['BigWorldArenaOpenServerLevel']
        self.person['BigWorldArenaPlayerLevel'] = self['BigWorldArenaPlayerLevel']
        self.person['OpenRefineTimeBox'] = self['OpenRefineTimeBox']
        self.person['RefineTimeFullPower'] = self['RefineTimeFullPower']
        self.person['RefineTimeLevelCondition'] = self['RefineTimeLevelCondition']
        self.person['RefineTimePowerActiveCondition'] = self['RefineTimePowerActiveCondition']
        self.person['RefineTimePowerActiveCount'] = self['RefineTimePowerActiveCount']
        self.person['RefineTimePowerWanLiuActiveCount'] = self['RefineTimePowerWanLiuActiveCount']
        self.person['RefineTimePowerTongTianActiveCount'] = self['RefineTimePowerTongTianActiveCount']
        self.person['OpenGuildProclaimWar'] = self['OpenGuildProclaimWar']
        self.person['OpenGuildProclaimWarDenunciation'] = self['OpenGuildProclaimWarDenunciation']
        self.person['GuildProclaimWarSrcGuildLevel'] = self['GuildProclaimWarSrcGuildLevel']
        self.person['GuildProclaimWarSrcGuildMaxCnt'] = self['GuildProclaimWarSrcGuildMaxCnt']
        self.person['GuildProclaimWarTarMoreThanSrcGuildLevel'] = self['GuildProclaimWarTarMoreThanSrcGuildLevel']
        self.person['GuildProclaimWarTarLessThanSrcGuildLevel'] = self['GuildProclaimWarTarLessThanSrcGuildLevel']
        self.person['GuildProclaimWarTarMoreThanSrcAvgGuildHY'] = self['GuildProclaimWarTarMoreThanSrcAvgGuildHY']
        self.person['GuildProclaimWarTarLessThanSrcAvgGuildHY'] = self['GuildProclaimWarTarLessThanSrcAvgGuildHY']
        self.person['GuildProclaimWarFirstStartHour1'] = self['GuildProclaimWarFirstStartHour1']
        self.person['GuildProclaimWarFirstStartHour2'] = self['GuildProclaimWarFirstStartHour2']
        self.person['GuildProclaimWarSecondStartHour1'] = self['GuildProclaimWarSecondStartHour1']
        self.person['GuildProclaimWarSecondStartHour2'] = self['GuildProclaimWarSecondStartHour2']
        self.person['GuildProclaimWarAdvanceTime'] = self['GuildProclaimWarAdvanceTime']
        self.person['OpenGuildDay'] = self['OpenGuildDay']
        self.person['OpenWuShen'] = self['OpenWuShen']
        self.person['WuShenOpenPlayerLevel'] = self['WuShenOpenPlayerLevel']
        self.person['WuShenOpenWeaponLevel'] = self['WuShenOpenWeaponLevel']
        self.person['WuShenDrillMaxCount'] = self['WuShenDrillMaxCount']
        self.person['WuShenAscendRefineLevel'] = self['WuShenAscendRefineLevel']
        self.person['WuShenAscendUpgradeLevel'] = self['WuShenAscendUpgradeLevel']
        self.person['WuShenAscendDrillCount'] = self['WuShenAscendDrillCount']
        self.person['WuShenAscendItemID1'] = self['WuShenAscendItemID1']
        self.person['WuShenAscendItemCount1'] = self['WuShenAscendItemCount1']
        self.person['WuShenAscendItemID2'] = self['WuShenAscendItemID2']
        self.person['WuShenAscendItemCount2'] = self['WuShenAscendItemCount2']
        self.person['WuShenForgeCostItemID1'] = self['WuShenForgeCostItemID1']
        self.person['WuShenForgeCostItemCount1'] = self['WuShenForgeCostItemCount1']
        self.person['WuShenForgeCostItemID2'] = self['WuShenForgeCostItemID2']
        self.person['WuShenForgeCostItemCount2'] = self['WuShenForgeCostItemCount2']
        self.person['OpenGuessLanternRiddles'] = self['OpenGuessLanternRiddles']
        self.person['WuShenOpenMission'] = self['WuShenOpenMission']
        self.person['WuShenFunctionGuideMission'] = self['WuShenFunctionGuideMission']
        self.person['WuShenPreviewOpenPlayerLevel'] = self['WuShenPreviewOpenPlayerLevel']
        self.person['BigWorldArenaSeasonCycleDay'] = self['BigWorldArenaSeasonCycleDay']
        self.person['BigWorldArenaPlayerJoinTimes'] = self['BigWorldArenaPlayerJoinTimes']
        self.person['BigWorldArenaSeasonStageDec'] = self['BigWorldArenaSeasonStageDec']
        self.person['OpenHuanHuanPaiSong'] = self['OpenHuanHuanPaiSong']
        self.person['HuanHuanPaiSongMinLevel'] = self['HuanHuanPaiSongMinLevel']
        self.person['HuanHuanPaiSongStartSaleTime'] = self['HuanHuanPaiSongStartSaleTime']
        self.person['HuanHuanPaiSongEndSaleTime'] = self['HuanHuanPaiSongEndSaleTime']
        self.person['HuanHuanPaiSongGetBeginTime1'] = self['HuanHuanPaiSongGetBeginTime1']
        self.person['HuanHuanPaiSongGetEndTime1'] = self['HuanHuanPaiSongGetEndTime1']
        self.person['HuanHuanPaiSongGetBeginTime2'] = self['HuanHuanPaiSongGetBeginTime2']
        self.person['HuanHuanPaiSongGetEndTime2'] = self['HuanHuanPaiSongGetEndTime2']
        self.person['HuanHuanPaiSongNeedYuanBao'] = self['HuanHuanPaiSongNeedYuanBao']
        self.person['CheckForceUpdateIntervalTime'] = self['CheckForceUpdateIntervalTime']
        self.person['YuanBaoShopRedPointLevel'] = self['YuanBaoShopRedPointLevel']
        self.person['WuShenForgeMaxNonRareCount'] = self['WuShenForgeMaxNonRareCount']
        self.person['WuShenForgeMultipleCount'] = self['WuShenForgeMultipleCount']
        self.person['BigWorldArenaOpenSpecialTimeBegin'] = self['BigWorldArenaOpenSpecialTimeBegin']
        self.person['BigWorldArenaOpenSpecialTimeEnd'] = self['BigWorldArenaOpenSpecialTimeEnd']
        self.person['BigWorldArenaOpenSpecialTime'] = self['BigWorldArenaOpenSpecialTime']
        self.person['ForceUpdateCancelCD'] = self['ForceUpdateCancelCD']
        self.person['ServantAMaxLevel'] = self['ServantAMaxLevel']
        self.person['ServantBMaxLevel'] = self['ServantBMaxLevel']
        self.person['ServantCMaxLevel'] = self['ServantCMaxLevel']
        self.person['WuShenAscendStartMission'] = self['WuShenAscendStartMission']
        self.person['bwgwwinrewardlimithonorscore'] = self['bwgwwinrewardlimithonorscore']
        self.person['OpenBWRankReward'] = self['OpenBWRankReward']
        self.person['OpenFreeChoice'] = self['OpenFreeChoice']
        self.person['OpenYaoshouFemaleCreate'] = self['OpenYaoshouFemaleCreate']
        self.person['OpenBubbleChat'] = self['OpenBubbleChat']
        self.person['OpenServantRecommend'] = self['OpenServantRecommend']
        self.person['ServantRecommendMinPlayerLvl'] = self['ServantRecommendMinPlayerLvl']
        self.person['OpenExchangeShopServerCatch'] = self['OpenExchangeShopServerCatch']
        self.person['OpenMaterialBag'] = self['OpenMaterialBag']
        self.person['OpenMaterialBagLevel'] = self['OpenMaterialBagLevel']
        self.person['OpenJade'] = self['OpenJade']
        self.person['OpenJadeGemIntensify'] = self['OpenJadeGemIntensify']
        self.person['OpenJadeGemLevelup'] = self['OpenJadeGemLevelup']
        self.person['OpenActivateJade'] = self['OpenActivateJade']
        self.person['OpenQuickIntensify'] = self['OpenQuickIntensify']
        self.person['OpenJadeUI'] = self['OpenJadeUI']
        self.person['OpenHug'] = self['OpenHug']
        self.person['OpenEquipEngraveSmartAuto'] = self['OpenEquipEngraveSmartAuto']
        self.person['AnswerActivityEarlyCloseTime'] = self['AnswerActivityEarlyCloseTime']
        self.person['OpenYuanLingTuXiBrushActivity'] = self['OpenYuanLingTuXiBrushActivity']
        self.person['OpenWildSceneDuel'] = self['OpenWildSceneDuel']
        self.person['OpenBWPP1V1Mode'] = self['OpenBWPP1V1Mode']
        self.person['BWPP1V1ModeNeedLevel'] = self['BWPP1V1ModeNeedLevel']
        self.person['BWPP1V1OpenTime'] = self['BWPP1V1OpenTime']
        self.person['BWPP1V1CloseTime'] = self['BWPP1V1CloseTime']
        self.person['AfterReliveIgnoreCombatMountDuration'] = self['AfterReliveIgnoreCombatMountDuration']
        self.person['OpenPoYuSwitch'] = self['OpenPoYuSwitch']
        self.person['OpenYueXianMaleCreate'] = self['OpenYueXianMaleCreate']
        self.person['OpenYueXianFemaleCreate'] = self['OpenYueXianFemaleCreate']
        self.person['IsOpenChatInChannelSwordTeam'] = self['IsOpenChatInChannelSwordTeam']
        self.person['SwordTeamChatCD'] = self['SwordTeamChatCD']
        self.person['ActiveBrotherhoodWeeklyLoyaltyVal'] = self['ActiveBrotherhoodWeeklyLoyaltyVal']
        self.person['OpenTurnTable'] = self['OpenTurnTable']
        self.person['OpenQuickTargetSelect'] = self['OpenQuickTargetSelect']
        self.person['QuickTargetSelectTimeInterval'] = self['QuickTargetSelectTimeInterval']
        self.person['RiderTigerSceneId'] = self['RiderTigerSceneId']
        self.person['RiderTigerScenePosX'] = self['RiderTigerScenePosX']
        self.person['RiderTigerScenePosY'] = self['RiderTigerScenePosY']
        self.person['RiderTigerScenePosZ'] = self['RiderTigerScenePosZ']
        self.person['RiderTigerCanGetRewardTimes1'] = self['RiderTigerCanGetRewardTimes1']
        self.person['RiderTigerCanGetRewardTimes2'] = self['RiderTigerCanGetRewardTimes2']
        self.person['RiderTigerCanGetRewardTimes3'] = self['RiderTigerCanGetRewardTimes3']
        self.person['RiderTigerRewardItemId1'] = self['RiderTigerRewardItemId1']
        self.person['RiderTigerRewardItemId2'] = self['RiderTigerRewardItemId2']
        self.person['RiderTigerRewardItemId3'] = self['RiderTigerRewardItemId3']
        self.person['OpenBrotherhoodRecruitDeclaration'] = self['OpenBrotherhoodRecruitDeclaration']
        self.person['RiderTigerRewardItemCount1'] = self['RiderTigerRewardItemCount1']
        self.person['RiderTigerRewardItemCount2'] = self['RiderTigerRewardItemCount2']
        self.person['RiderTigerRewardItemCount3'] = self['RiderTigerRewardItemCount3']
        # end handle [GC_SYNC_GAMECONFIG] message attrs, auto generate do not change
        pass


class GC_RET_CHANNELINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_CHANNELINFO] message attrs, auto generate do not change
        self.person['sceneinstcount'] = self['sceneinstcount']
        self.person['sceneactivation'] = self['sceneactivation']
        self.person['sceneplayercount'] = self['sceneplayercount']
        # end handle [GC_RET_CHANNELINFO] message attrs, auto generate do not change
        pass


class GC_GUILDMONSTER_STATE (Packet):
    def handle(self):
        # begin handle [GC_GUILDMONSTER_STATE] message attrs, auto generate do not change
        self.person['GuildMonsterState'] = self['GuildMonsterState']
        self.person['NextActiveTime'] = self['NextActiveTime']
        # end handle [GC_GUILDMONSTER_STATE] message attrs, auto generate do not change
        pass


class GC_TEAM_CALLMEMBER (Packet):
    def handle(self):
        # begin handle [GC_TEAM_CALLMEMBER] message attrs, auto generate do not change
        self.person['inviterName'] = self['inviterName']
        self.person['sceneID'] = self['sceneID']
        self.person['barmy'] = self['barmy']
        # end handle [GC_TEAM_CALLMEMBER] message attrs, auto generate do not change
        pass


class GC_CHANGENAME_RET (Packet):
    def handle(self):
        # begin handle [GC_CHANGENAME_RET] message attrs, auto generate do not change
        self.person['changeType'] = self['changeType']
        self.person['ret'] = self['ret']
        # end handle [GC_CHANGENAME_RET] message attrs, auto generate do not change
        pass


class GC_NPCGIFTEXCHANGE_SYNC_STATUE (Packet):
    def handle(self):
        # begin handle [GC_NPCGIFTEXCHANGE_SYNC_STATUE] message attrs, auto generate do not change
        self.person['npcId'] = self['npcId']
        self.person['awardIndex'] = self['awardIndex']
        self.person['FPValue'] = self['FPValue']
        # end handle [GC_NPCGIFTEXCHANGE_SYNC_STATUE] message attrs, auto generate do not change
        pass


class CG_DW_REQCAR (Packet):
    pass


class GC_SYNC_NPC_TITLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NPC_TITLE] message attrs, auto generate do not change
        self.person['ObjId'] = self['ObjId']
        self.person['NpcTitle'] = self['NpcTitle']
        # end handle [GC_SYNC_NPC_TITLE] message attrs, auto generate do not change
        pass


class GC_SWORDTEAM_RET_INFO (Packet):
    def handle(self):
        # begin handle [GC_SWORDTEAM_RET_INFO] message attrs, auto generate do not change
        self.person['swordteamGuid'] = self['swordteamGuid']
        self.person['swordteamName'] = self['swordteamName']
        self.person['swordteamChiefGuid'] = self['swordteamChiefGuid']
        self.person['creatDay'] = self['creatDay']
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberVIP'] = self['memberVIP']
        self.person['memberProf'] = self['memberProf']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberLastLogout'] = self['memberLastLogout']
        self.person['memberState'] = self['memberState']
        self.person['memberJob'] = self['memberJob']
        self.person['combatval'] = self['combatval']
        self.person['BodyId'] = self['BodyId']
        self.person['FaceId'] = self['FaceId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairId'] = self['HairId']
        self.person['swordteamScore'] = self['swordteamScore']
        self.person['nGroup'] = self['nGroup']
        self.person['nPlaceInGroup'] = self['nPlaceInGroup']
        self.person['BodyColorEffectVisual'] = self['BodyColorEffectVisual']
        self.person['hairColorIndex'] = self['hairColorIndex']
        self.person['openRecuit'] = self['openRecuit']
        self.person['recuitCombat'] = self['recuitCombat']
        self.person['recuitProfession'] = self['recuitProfession']
        self.person['BodyColorVisual'] = self['BodyColorVisual']
        self.person['BodyFashionId'] = self['BodyFashionId']
        self.person['BodyColorIndex'] = self['BodyColorIndex']
        self.person['HairFashionId'] = self['HairFashionId']
        self.person['WeaponFashionId'] = self['WeaponFashionId']
        self.person['WeaponColorIndex'] = self['WeaponColorIndex']
        self.person['rolenierenlist'] = self['rolenierenlist']
        self.person['UseBodyFreeDyeSlotIds'] = self['UseBodyFreeDyeSlotIds']
        self.person['UseHairFreeDyeSlotIds'] = self['UseHairFreeDyeSlotIds']
        self.person['BodyFreeDyeColorInfos'] = self['BodyFreeDyeColorInfos']
        self.person['HairFreeDyeColorInfos'] = self['HairFreeDyeColorInfos']
        self.person['BackFashionId'] = self['BackFashionId']
        self.person['BackColorIndex'] = self['BackColorIndex']
        self.person['bCotQualified'] = self['bCotQualified']
        # end handle [GC_SWORDTEAM_RET_INFO] message attrs, auto generate do not change
        pass


class GC_CHALLENGE_REWARD (Packet):
    def handle(self):
        # begin handle [GC_CHALLENGE_REWARD] message attrs, auto generate do not change
        self.person['HonorCoins'] = self['HonorCoins']
        self.person['isLose'] = self['isLose']
        self.person['newPos'] = self['newPos']
        self.person['upPos'] = self['upPos']
        self.person['exp'] = self['exp']
        self.person['yuanbao'] = self['yuanbao']
        self.person['soul'] = self['soul']
        self.person['challengeLevel'] = self['challengeLevel']
        self.person['challengeProfession'] = self['challengeProfession']
        self.person['challengeCombatNum'] = self['challengeCombatNum']
        self.person['challengeName'] = self['challengeName']
        self.person['challengePlayerGuid'] = self['challengePlayerGuid']
        self.person['challengeSex'] = self['challengeSex']
        self.person['challengeCustomHeadPic'] = self['challengeCustomHeadPic']
        self.person['oldPos'] = self['oldPos']
        self.person['quickMode'] = self['quickMode']
        # end handle [GC_CHALLENGE_REWARD] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_ABDICANT (Packet):
    pass


class CG_BWPVPFINAL_ASKGOTOBIGWORLD (Packet):
    pass


class CG_SWORDTEAM_APPROVE_RESERVE (Packet):
    pass


class GC_CANCEL_INTERACT (Packet):
    def handle(self):
        # begin handle [GC_CANCEL_INTERACT] message attrs, auto generate do not change
        self.person['memberIDList'] = self['memberIDList']
        # end handle [GC_CANCEL_INTERACT] message attrs, auto generate do not change
        pass


class GC_FLIGHT (Packet):
    def handle(self):
        # begin handle [GC_FLIGHT] message attrs, auto generate do not change
        self.person['objid'] = self['objid']
        self.person['hight'] = self['hight']
        self.person['time'] = self['time']
        # end handle [GC_FLIGHT] message attrs, auto generate do not change
        pass


class CG_DONATE_BUILDING (Packet):
    pass


class GC_SYNC_SPECIAL_POISON_TIME (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SPECIAL_POISON_TIME] message attrs, auto generate do not change
        self.person['skillStdCanUseRemainTime'] = self['skillStdCanUseRemainTime']
        self.person['skillCanUseRemainTime'] = self['skillCanUseRemainTime']
        self.person['poisonMaxNum'] = self['poisonMaxNum']
        self.person['poisonNowNum'] = self['poisonNowNum']
        # end handle [GC_SYNC_SPECIAL_POISON_TIME] message attrs, auto generate do not change
        pass


class GC_BWPVPFINAL_RETGROUPINFO (Packet):
    def handle(self):
        # begin handle [GC_BWPVPFINAL_RETGROUPINFO] message attrs, auto generate do not change
        self.person['MemAGuid'] = self['MemAGuid']
        self.person['MemAName'] = self['MemAName']
        self.person['MemAWorldName'] = self['MemAWorldName']
        self.person['MemAIsSameWorld'] = self['MemAIsSameWorld']
        self.person['MemBGuid'] = self['MemBGuid']
        self.person['MemBName'] = self['MemBName']
        self.person['MemBWorldName'] = self['MemBWorldName']
        self.person['MemBIsSameWorld'] = self['MemBIsSameWorld']
        self.person['WinType'] = self['WinType']
        self.person['selfGroupIndex'] = self['selfGroupIndex']
        self.person['remainTime'] = self['remainTime']
        self.person['bIsLastRound'] = self['bIsLastRound']
        self.person['QingLongScore'] = self['QingLongScore']
        self.person['BaiHuScore'] = self['BaiHuScore']
        self.person['ZhuQueScore'] = self['ZhuQueScore']
        self.person['XuanWuScore'] = self['XuanWuScore']
        self.person['helpCounts'] = self['helpCounts']
        self.person['CurRound'] = self['CurRound']
        self.person['TotalRound'] = self['TotalRound']
        self.person['WinGuid4Round'] = self['WinGuid4Round']
        # end handle [GC_BWPVPFINAL_RETGROUPINFO] message attrs, auto generate do not change
        pass


class GC_RES_JIANMUXB_HELP (Packet):
    def handle(self):
        # begin handle [GC_RES_JIANMUXB_HELP] message attrs, auto generate do not change
        self.person['usedHelpTimes'] = self['usedHelpTimes']
        # end handle [GC_RES_JIANMUXB_HELP] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_FASHION_CHANGE] message attrs, auto generate do not change
        self.person['FashionPart'] = self['FashionPart']
        self.person['FashionId'] = self['FashionId']
        # end handle [GC_FASHION_CHANGE] message attrs, auto generate do not change
        pass


class CG_CANCEL_MFLY (Packet):
    pass


class CG_MULPVP_ANSWER (Packet):
    pass


class GC_SYNC_SUPER_R_TIPS (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SUPER_R_TIPS] message attrs, auto generate do not change
        self.person['bNewTips'] = self['bNewTips']
        # end handle [GC_SYNC_SUPER_R_TIPS] message attrs, auto generate do not change
        pass


class GC_RET_EQUIP_REBIRTH_RECASE (Packet):
    def handle(self):
        # begin handle [GC_RET_EQUIP_REBIRTH_RECASE] message attrs, auto generate do not change
        self.person['nResult'] = self['nResult']
        # end handle [GC_RET_EQUIP_REBIRTH_RECASE] message attrs, auto generate do not change
        pass


class GC_ADD_LOUDSPEAKER (Packet):
    def handle(self):
        # begin handle [GC_ADD_LOUDSPEAKER] message attrs, auto generate do not change
        # end handle [GC_ADD_LOUDSPEAKER] message attrs, auto generate do not change
        pass


class CG_GUILDFIGHT_WORLDBOSS_PURIFY (Packet):
    pass


class GC_RET_FAIRY_LASTRECAST_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_FAIRY_LASTRECAST_INFO] message attrs, auto generate do not change
        self.person['fairyGuid'] = self['fairyGuid']
        self.person['growthRate'] = self['growthRate']
        self.person['aptitudeBaseSTR'] = self['aptitudeBaseSTR']
        self.person['aptitudeBaseAGI'] = self['aptitudeBaseAGI']
        self.person['aptitudeBaseVIT'] = self['aptitudeBaseVIT']
        self.person['aptitudeBaseSPI'] = self['aptitudeBaseSPI']
        self.person['skillList'] = self['skillList']
        self.person['combatValue'] = self['combatValue']
        # end handle [GC_RET_FAIRY_LASTRECAST_INFO] message attrs, auto generate do not change
        pass


class GC_CHANGE_MAJORCITY_RET (Packet):
    def handle(self):
        # begin handle [GC_CHANGE_MAJORCITY_RET] message attrs, auto generate do not change
        self.person['LastOpSucceedTime'] = self['LastOpSucceedTime']
        # end handle [GC_CHANGE_MAJORCITY_RET] message attrs, auto generate do not change
        pass


class GC_BWPVP_ROUND_RESULT (Packet):
    def handle(self):
        # begin handle [GC_BWPVP_ROUND_RESULT] message attrs, auto generate do not change
        self.person['CurRound'] = self['CurRound']
        self.person['TotalRound'] = self['TotalRound']
        self.person['WinGuid4Round'] = self['WinGuid4Round']
        # end handle [GC_BWPVP_ROUND_RESULT] message attrs, auto generate do not change
        pass


class GC_GUILD_NEW_TISHI (Packet):
    def handle(self):
        # begin handle [GC_GUILD_NEW_TISHI] message attrs, auto generate do not change
        self.person['index'] = self['index']
        self.person['value'] = self['value']
        # end handle [GC_GUILD_NEW_TISHI] message attrs, auto generate do not change
        pass


class CG_REQ_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM (Packet):
    pass


class GC_AUCTION_RETRECORD (Packet):
    def handle(self):
        # begin handle [GC_AUCTION_RETRECORD] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['targetguid'] = self['targetguid']
        self.person['targetname'] = self['targetname']
        self.person['price'] = self['price']
        self.person['itemid'] = self['itemid']
        self.person['reserved'] = self['reserved']
        self.person['recordtime'] = self['recordtime']
        # end handle [GC_AUCTION_RETRECORD] message attrs, auto generate do not change
        pass


class CG_GUILD_CREATE (Packet):
    pass


class CG_TEAM_CALLMEMBER (Packet):
    pass


class GC_GIVESIGN_FORPIC (Packet):
    def handle(self):
        # begin handle [GC_GIVESIGN_FORPIC] message attrs, auto generate do not change
        self.person['fileId'] = self['fileId']
        self.person['sign'] = self['sign']
        self.person['filePath'] = self['filePath']
        self.person['bucketname'] = self['bucketname']
        self.person['appid'] = self['appid']
        self.person['reqSignType'] = self['reqSignType']
        # end handle [GC_GIVESIGN_FORPIC] message attrs, auto generate do not change
        pass


class CG_FAIRY_RECAST_REPLACEATTR (Packet):
    pass


class GC_RET_USE_SKILL_XML (Packet):
    def handle(self):
        # begin handle [GC_RET_USE_SKILL_XML] message attrs, auto generate do not change
        self.person['skillId'] = self['skillId']
        self.person['senderId'] = self['senderId']
        self.person['TargetId'] = self['TargetId']
        self.person['vDirectionX'] = self['vDirectionX']
        self.person['vDirectionY'] = self['vDirectionY']
        self.person['vDirectionZ'] = self['vDirectionZ']
        self.person['vTargetPosX'] = self['vTargetPosX']
        self.person['vTargetPosY'] = self['vTargetPosY']
        self.person['vTargetPosZ'] = self['vTargetPosZ']
        self.person['startByServer'] = self['startByServer']
        # end handle [GC_RET_USE_SKILL_XML] message attrs, auto generate do not change
        loadlog.debug(__class__.__name__)
        loadlog.debug(self.obj)
        pass


class CG_UPDATE_AUTOCOMBAT (Packet):
    pass


class GC_FORCE_SETPOS (Packet):
    def handle(self):
        # begin handle [GC_FORCE_SETPOS] message attrs, auto generate do not change
        self.person['ServerID'] = self['ServerID']
        self.person['PosX'] = self['PosX']
        self.person['PosY'] = self['PosY']
        self.person['PosZ'] = self['PosZ']
        self.person['isShowTrans'] = self['isShowTrans']
        self.person['skillBaseId'] = self['skillBaseId']
        # end handle [GC_FORCE_SETPOS] message attrs, auto generate do not change
        pass


class GC_TEAM_LEAVE (Packet):
    def handle(self):
        # begin handle [GC_TEAM_LEAVE] message attrs, auto generate do not change
        self.person['teamID'] = self['teamID']
        # end handle [GC_TEAM_LEAVE] message attrs, auto generate do not change
        pass


class GC_SYN_SKILLCOUNT (Packet):
    def handle(self):
        # begin handle [GC_SYN_SKILLCOUNT] message attrs, auto generate do not change
        self.person['skillid'] = self['skillid']
        self.person['useCount'] = self['useCount']
        # end handle [GC_SYN_SKILLCOUNT] message attrs, auto generate do not change
        pass


class CG_TOURNAMENT_REQ_INFO (Packet):
    pass


class GC_PLAY_SNARE_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_PLAY_SNARE_EFFECT] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['effectId'] = self['effectId']
        # end handle [GC_PLAY_SNARE_EFFECT] message attrs, auto generate do not change
        pass


class CG_CHANGE_ARMY_MEMBER_POSITION (Packet):
    pass


class GC_NOTICE_ADDED_FRIEND (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_ADDED_FRIEND] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['name'] = self['name']
        # end handle [GC_NOTICE_ADDED_FRIEND] message attrs, auto generate do not change
        pass


class GC_PRESTIGE_TODAYEXPLOITMAX (Packet):
    def handle(self):
        # begin handle [GC_PRESTIGE_TODAYEXPLOITMAX] message attrs, auto generate do not change
        self.person['todayexlpoitmax'] = self['todayexlpoitmax']
        # end handle [GC_PRESTIGE_TODAYEXPLOITMAX] message attrs, auto generate do not change
        pass


class GC_SYNC_PET_ATTR (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PET_ATTR] message attrs, auto generate do not change
        self.person['petAttr'] = self['petAttr']
        # end handle [GC_SYNC_PET_ATTR] message attrs, auto generate do not change
        pass


class CG_MILITARY_REQ_EQUIPDONATE (Packet):
    pass


class GC_GUILD_RET_INFO (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_INFO] message attrs, auto generate do not change
        self.person['guildGuid'] = self['guildGuid']
        self.person['guildName'] = self['guildName']
        self.person['guildChiefGuid'] = self['guildChiefGuid']
        self.person['guildLevel'] = self['guildLevel']
        self.person['guildVitality'] = self['guildVitality']
        self.person['guildContribute'] = self['guildContribute']
        self.person['guildScene'] = self['guildScene']
        self.person['guildNotice'] = self['guildNotice']
        self.person['acceptQuickJoin'] = self['acceptQuickJoin']
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['reserved'] = self['reserved']
        self.person['memberProf'] = self['memberProf']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberContirbute'] = self['memberContirbute']
        self.person['memberHisContirbute'] = self['memberHisContirbute']
        self.person['memberLastLogout'] = self['memberLastLogout']
        self.person['memberState'] = self['memberState']
        self.person['memberJob'] = self['memberJob']
        self.person['combatval'] = self['combatval']
        self.person['sex'] = self['sex']
        self.person['guildwarjoin'] = self['guildwarjoin']
        self.person['guildAuthority'] = self['guildAuthority']
        self.person['demiseTime'] = self['demiseTime']
        self.person['demiseMemberGuid'] = self['demiseMemberGuid']
        self.person['guildActivityNotice'] = self['guildActivityNotice']
        self.person['guildjobName'] = self['guildjobName']
        self.person['fullacceptapply'] = self['fullacceptapply']
        self.person['guildShortName'] = self['guildShortName']
        self.person['guildShortNameColor'] = self['guildShortNameColor']
        self.person['guildNvShenTitle'] = self['guildNvShenTitle']
        self.person['guildChangeNSTitleTime'] = self['guildChangeNSTitleTime']
        self.person['guildCangKuLevel'] = self['guildCangKuLevel']
        self.person['guildGongFangLevel'] = self['guildGongFangLevel']
        self.person['guildBuildingLeftTime'] = self['guildBuildingLeftTime']
        self.person['guildBuildingType'] = self['guildBuildingType']
        self.person['guildChiefModelLevel'] = self['guildChiefModelLevel']
        self.person['memberJoinTime'] = self['memberJoinTime']
        self.person['ArmyId'] = self['ArmyId']
        self.person['TeamId'] = self['TeamId']
        self.person['isBanghuaActive'] = self['isBanghuaActive']
        self.person['guildMoney'] = self['guildMoney']
        self.person['guildPoMoTangLevel'] = self['guildPoMoTangLevel']
        self.person['guildXiuLianFangLevel'] = self['guildXiuLianFangLevel']
        self.person['guildTianYuanBaoKuLevel'] = self['guildTianYuanBaoKuLevel']
        self.person['guildOpenAddition'] = self['guildOpenAddition']
        self.person['guildAttrAdditionLevel'] = self['guildAttrAdditionLevel']
        self.person['guildAttrAdditionExp'] = self['guildAttrAdditionExp']
        self.person['guildAutoJoinLevel'] = self['guildAutoJoinLevel']
        self.person['guildAutoJoinCombatVal'] = self['guildAutoJoinCombatVal']
        self.person['occupyDomainIdList'] = self['occupyDomainIdList']
        self.person['guildActivityOpenTime'] = self['guildActivityOpenTime']
        self.person['guildCreateGroupMoney'] = self['guildCreateGroupMoney']
        self.person['guildBindGroupState'] = self['guildBindGroupState']
        self.person['guildBindGroupId'] = self['guildBindGroupId']
        self.person['memberJoinGuildWarCount'] = self['memberJoinGuildWarCount']
        self.person['memberGuildMisCompletedCount'] = self['memberGuildMisCompletedCount']
        self.person['memberGuildActivityDropCount'] = self['memberGuildActivityDropCount']
        self.person['guildWildScene'] = self['guildWildScene']
        self.person['guildMonsterScore'] = self['guildMonsterScore']
        self.person['guildMonsterState'] = self['guildMonsterState']
        self.person['guildFlagLevel'] = self['guildFlagLevel']
        self.person['lastGuildFlagUseTime'] = self['lastGuildFlagUseTime']
        self.person['todayAddGuildMoney'] = self['todayAddGuildMoney']
        self.person['isAutoRejectNonEligible'] = self['isAutoRejectNonEligible']
        self.person['AllianceGuildGuid'] = self['AllianceGuildGuid']
        self.person['AllianceEndTime'] = self['AllianceEndTime']
        self.person['AllianceGuildName'] = self['AllianceGuildName']
        self.person['guildTeamInfo'] = self['guildTeamInfo']
        self.person['guildTeamActivityInfo'] = self['guildTeamActivityInfo']
        self.person['memberBWGWRankRewardState'] = self['memberBWGWRankRewardState']
        self.person['bwgwranknum'] = self['bwgwranknum']
        self.person['job'] = self['job']
        self.person['guildHealthRate'] = self['guildHealthRate']
        self.person['guildType'] = self['guildType']
        self.person['guildproclaimwarguid'] = self['guildproclaimwarguid']
        self.person['proclaimwarcnt'] = self['proclaimwarcnt']
        # end handle [GC_GUILD_RET_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_EYESSTAR_TEN_TIMES (Packet):
    pass


class GC_ATTACKFLY (Packet):
    def handle(self):
        # begin handle [GC_ATTACKFLY] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['Dis'] = self['Dis']
        self.person['isXp'] = self['isXp']
        self.person['FlyTime'] = self['FlyTime']
        self.person['dirX'] = self['dirX']
        self.person['dirY'] = self['dirY']
        self.person['dirZ'] = self['dirZ']
        # end handle [GC_ATTACKFLY] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_HUILIU_STATE] message attrs, auto generate do not change
        self.person['roleType'] = self['roleType']
        self.person['currentDay'] = self['currentDay']
        self.person['goalType'] = self['goalType']
        self.person['goalDone'] = self['goalDone']
        self.person['goalAwardGot'] = self['goalAwardGot']
        self.person['recharged'] = self['recharged']
        self.person['haveIdentity'] = self['haveIdentity']
        self.person['expGainLeft'] = self['expGainLeft']
        # end handle [GC_HUILIU_STATE] message attrs, auto generate do not change
        pass


class GC_SYNC_HOME_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HOME_DATA] message attrs, auto generate do not change
        self.person['DataType'] = self['DataType']
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['MasterGuid'] = self['MasterGuid']
        self.person['MasterName'] = self['MasterName']
        self.person['MasterLevel'] = self['MasterLevel']
        self.person['MasterCombat'] = self['MasterCombat']
        self.person['CreateTime'] = self['CreateTime']
        self.person['HomeLevel'] = self['HomeLevel']
        self.person['PlantValue'] = self['PlantValue']
        self.person['TameValue'] = self['TameValue']
        self.person['MiningValue'] = self['MiningValue']
        self.person['Honor'] = self['Honor']
        self.person['Geomancy'] = self['Geomancy']
        self.person['TribeContribute'] = self['TribeContribute']
        self.person['ZoneList'] = self['ZoneList']
        self.person['PermissionList'] = self['PermissionList']
        self.person['LandLoad'] = self['LandLoad']
        self.person['Guest'] = self['Guest']
        self.person['ElementList'] = self['ElementList']
        self.person['HomeLog'] = self['HomeLog']
        self.person['ProduceLog'] = self['ProduceLog']
        self.person['GuestLog'] = self['GuestLog']
        self.person['GeomancyLog'] = self['GeomancyLog']
        self.person['PlantValueLimit'] = self['PlantValueLimit']
        self.person['TameValueLimit'] = self['TameValueLimit']
        self.person['MiningValueLimit'] = self['MiningValueLimit']
        self.person['HonorLimit'] = self['HonorLimit']
        self.person['GeomancyLimit'] = self['GeomancyLimit']
        self.person['nTakecareCountToday'] = self['nTakecareCountToday']
        self.person['nBeenAidCountToday'] = self['nBeenAidCountToday']
        self.person['nAidOtherCountToday'] = self['nAidOtherCountToday']
        self.person['nStealCountToday'] = self['nStealCountToday']
        self.person['ProduceData'] = self['ProduceData']
        self.person['HomeName'] = self['HomeName']
        self.person['HomeSettleTime'] = self['HomeSettleTime']
        self.person['WeekTribeContribute'] = self['WeekTribeContribute']
        self.person['HordeLeaderName'] = self['HordeLeaderName']
        self.person['HomeHordeData'] = self['HomeHordeData']
        self.person['AtmosphereVal'] = self['AtmosphereVal']
        self.person['bProduceDataChanged'] = self['bProduceDataChanged']
        self.person['bGuestDataChanged'] = self['bGuestDataChanged']
        self.person['bZoneListChanged'] = self['bZoneListChanged']
        self.person['bPermissionChanged'] = self['bPermissionChanged']
        self.person['bElementListChanged'] = self['bElementListChanged']
        self.person['bHomeLogChanged'] = self['bHomeLogChanged']
        self.person['bProduceLogChanged'] = self['bProduceLogChanged']
        self.person['bGuestLogChanged'] = self['bGuestLogChanged']
        self.person['bGeomancyLogChanged'] = self['bGeomancyLogChanged']
        self.person['StewardName'] = self['StewardName']
        self.person['CurPlanIndex'] = self['CurPlanIndex']
        self.person['Plan1Unlock'] = self['Plan1Unlock']
        self.person['Plan2Unlock'] = self['Plan2Unlock']
        self.person['Plan3Unlock'] = self['Plan3Unlock']
        self.person['Plan4Unlock'] = self['Plan4Unlock']
        self.person['HordeName'] = self['HordeName']
        self.person['PlantAddedOfItem'] = self['PlantAddedOfItem']
        self.person['TameAddedOfItem'] = self['TameAddedOfItem']
        self.person['MiningAddedOfItem'] = self['MiningAddedOfItem']
        self.person['FunctionList'] = self['FunctionList']
        self.person['FurnitureList'] = self['FurnitureList']
        self.person['bFunctionListChanged'] = self['bFunctionListChanged']
        self.person['bFurnitureListChanged'] = self['bFurnitureListChanged']
        self.person['homeAttrId'] = self['homeAttrId']
        self.person['homeAttrValue'] = self['homeAttrValue']
        self.person['bHomeAttrChanged'] = self['bHomeAttrChanged']
        self.person['EmployeeList'] = self['EmployeeList']
        self.person['bEmployeeChanged'] = self['bEmployeeChanged']
        self.person['IsGainGiftBox'] = self['IsGainGiftBox']
        self.person['AlreadyPutGiftNum'] = self['AlreadyPutGiftNum']
        self.person['HomeGiftArray'] = self['HomeGiftArray']
        self.person['bHomeGiftChanged'] = self['bHomeGiftChanged']
        self.person['PopularValue'] = self['PopularValue']
        self.person['BlackList'] = self['BlackList']
        self.person['bHomeBlackChanged'] = self['bHomeBlackChanged']
        self.person['CurExteriorId'] = self['CurExteriorId']
        self.person['bHomeExteriorChanged'] = self['bHomeExteriorChanged']
        self.person['ExteriorList'] = self['ExteriorList']
        self.person['SpouseHonor'] = self['SpouseHonor']
        self.person['SpouseGeomancy'] = self['SpouseGeomancy']
        # end handle [GC_SYNC_HOME_DATA] message attrs, auto generate do not change
        pass


class CG_AUCTION_CANCELSELL (Packet):
    pass


class CG_AID_PUBLISH (Packet):
    pass


class CG_HOME_DEL_BLACK (Packet):
    pass


class GC_RET_HOME_FITMENT (Packet):
    def handle(self):
        # begin handle [GC_RET_HOME_FITMENT] message attrs, auto generate do not change
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['Success'] = self['Success']
        self.person['BeginOrEnd'] = self['BeginOrEnd']
        # end handle [GC_RET_HOME_FITMENT] message attrs, auto generate do not change
        pass


class GC_START_CAMERA_RESET (Packet):
    def handle(self):
        # begin handle [GC_START_CAMERA_RESET] message attrs, auto generate do not change
        self.person['resetOnce'] = self['resetOnce']
        self.person['isForward'] = self['isForward']
        self.person['isVertical'] = self['isVertical']
        self.person['isScale'] = self['isScale']
        self.person['forwardx'] = self['forwardx']
        self.person['forwardy'] = self['forwardy']
        self.person['vertical'] = self['vertical']
        self.person['scale'] = self['scale']
        # end handle [GC_START_CAMERA_RESET] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_RET_GUILD_THIEF_ISACTIVE] message attrs, auto generate do not change
        self.person['isShow'] = self['isShow']
        # end handle [GC_RET_GUILD_THIEF_ISACTIVE] message attrs, auto generate do not change
        pass


class CG_OPEN_RUBKI_CUBE_ACTIVITY (Packet):
    pass


class CG_FIRE_MERCENARY (Packet):
    pass


class CG_READ_XIAOYUE_TIPS (Packet):
    pass


class GC_MAKE_MFLY (Packet):
    def handle(self):
        # begin handle [GC_MAKE_MFLY] message attrs, auto generate do not change
        self.person['masterServerID'] = self['masterServerID']
        self.person['guestServerID'] = self['guestServerID']
        # end handle [GC_MAKE_MFLY] message attrs, auto generate do not change
        pass


class CG_MENTOR_BUY_ITEM (Packet):
    pass


class GC_PGL_RESPONSE_DAN_AWARD (Packet):
    def handle(self):
        # begin handle [GC_PGL_RESPONSE_DAN_AWARD] message attrs, auto generate do not change
        self.person['nOperateResult'] = self['nOperateResult']
        # end handle [GC_PGL_RESPONSE_DAN_AWARD] message attrs, auto generate do not change
        pass


class GC_COPYSCENE_HIDINGBOSS_SHOW_SELECT_OPEN_WINDOW (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_HIDINGBOSS_SHOW_SELECT_OPEN_WINDOW] message attrs, auto generate do not change
        self.person['teamLeaderItemids'] = self['teamLeaderItemids']
        self.person['teamMemberItemids'] = self['teamMemberItemids']
        # end handle [GC_COPYSCENE_HIDINGBOSS_SHOW_SELECT_OPEN_WINDOW] message attrs, auto generate do not change
        pass


class GC_NOTICE_MESSAGE (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_MESSAGE] message attrs, auto generate do not change
        self.person['sceneid'] = self['sceneid']
        self.person['eventid'] = self['eventid']
        self.person['reasult'] = self['reasult']
        self.person['results'] = self['results']
        self.person['param1'] = self['param1']
        self.person['param2'] = self['param2']
        # end handle [GC_NOTICE_MESSAGE] message attrs, auto generate do not change
        pass


class GC_GM_PRINT_DEBUG (Packet):
    def handle(self):
        # begin handle [GC_GM_PRINT_DEBUG] message attrs, auto generate do not change
        self.person['fileName'] = self['fileName']
        self.person['info'] = self['info']
        # end handle [GC_GM_PRINT_DEBUG] message attrs, auto generate do not change
        pass


class CG_MOUNT_MOUNT (Packet):
    pass


class CG_UNLOCK_HOME_ZONE (Packet):
    pass


class GC_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF] message attrs, auto generate do not change
        self.person['chiefGuid'] = self['chiefGuid']
        self.person['chiefName'] = self['chiefName']
        # end handle [GC_BROTHERHOOD_RECRUIT_NOTICE_TRY_CONTACT_CHIEF] message attrs, auto generate do not change
        pass


class GC_START_RUBKICUBE_PLAY (Packet):
    def handle(self):
        # begin handle [GC_START_RUBKICUBE_PLAY] message attrs, auto generate do not change
        self.person['rubkiCubePlayId'] = self['rubkiCubePlayId']
        self.person['endTime'] = self['endTime']
        self.person['serverTime'] = self['serverTime']
        # end handle [GC_START_RUBKICUBE_PLAY] message attrs, auto generate do not change
        pass


class CG_MPFOODLIST_CHANGED (Packet):
    pass


class CG_AUCTION_ASKRECORD (Packet):
    pass


class CG_REQ_AUTO_DECOMPOSE (Packet):
    pass


class GC_GUILDFIGHT_WORLDBOSS_STATE (Packet):
    def handle(self):
        # begin handle [GC_GUILDFIGHT_WORLDBOSS_STATE] message attrs, auto generate do not change
        self.person['CurState'] = self['CurState']
        # end handle [GC_GUILDFIGHT_WORLDBOSS_STATE] message attrs, auto generate do not change
        pass


class GC_START_CAMERA_MOVE (Packet):
    def handle(self):
        # begin handle [GC_START_CAMERA_MOVE] message attrs, auto generate do not change
        self.person['PathId'] = self['PathId']
        # end handle [GC_START_CAMERA_MOVE] message attrs, auto generate do not change
        pass


class GC_PGL_SYNC_GROUP_INFO (Packet):
    def handle(self):
        # begin handle [GC_PGL_SYNC_GROUP_INFO] message attrs, auto generate do not change
        self.person['remainTime'] = self['remainTime']
        self.person['sideId'] = self['sideId']
        self.person['memName'] = self['memName']
        self.person['memGuid'] = self['memGuid']
        self.person['memLev'] = self['memLev']
        self.person['memproId'] = self['memproId']
        self.person['memSex'] = self['memSex']
        self.person['memSideId'] = self['memSideId']
        self.person['memDan'] = self['memDan']
        # end handle [GC_PGL_SYNC_GROUP_INFO] message attrs, auto generate do not change
        pass


class GC_TODAY_FIRST_LOGIN (Packet):
    def handle(self):
        # begin handle [GC_TODAY_FIRST_LOGIN] message attrs, auto generate do not change
        # end handle [GC_TODAY_FIRST_LOGIN] message attrs, auto generate do not change
        pass


class CG_BWPVPFINAL_ASKHELPMEMINFO (Packet):
    pass


class CG_REQ_WORLDBOSS_NUM (Packet):
    pass


class GC_PRESENT_DEL (Packet):
    def handle(self):
        # begin handle [GC_PRESENT_DEL] message attrs, auto generate do not change
        self.person['BillGuid'] = self['BillGuid']
        # end handle [GC_PRESENT_DEL] message attrs, auto generate do not change
        pass


class CG_ASKTRACKPLAYER (Packet):
    pass


class CG_COPYSCENE_INVITE_RET (Packet):
    pass


class CG_UPDATE_COMMUNITY_REDDOT (Packet):
    pass


class GC_CREATE_PET (Packet):
    def handle(self):
        # begin handle [GC_CREATE_PET] message attrs, auto generate do not change
        self.person['charBaseAttr'] = self['charBaseAttr']
        self.person['ownerID'] = self['ownerID']
        self.person['ownerName'] = self['ownerName']
        # end handle [GC_CREATE_PET] message attrs, auto generate do not change
        pass


class CG_ASKFOR_FRIENDMAXNUM (Packet):
    pass


class GC_COPYSCENE_BOSSTIME (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_BOSSTIME] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['time'] = self['time']
        # end handle [GC_COPYSCENE_BOSSTIME] message attrs, auto generate do not change
        pass


class CG_HONGBAO_ROB (Packet):
    pass


class GC_TELEMOVE (Packet):
    def handle(self):
        # begin handle [GC_TELEMOVE] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['targetPosX'] = self['targetPosX']
        self.person['targetPosY'] = self['targetPosY']
        self.person['targetPosZ'] = self['targetPosZ']
        self.person['needChangeFaceto'] = self['needChangeFaceto']
        self.person['animaId'] = self['animaId']
        self.person['skillBaseId'] = self['skillBaseId']
        # end handle [GC_TELEMOVE] message attrs, auto generate do not change
        pass


class CG_REQ_ACCEPT_RECRUIT (Packet):
    pass


class CG_REQ_SYNC_HOME_COLLECTION (Packet):
    pass


class CG_REQ_CHANNELINFO (Packet):
    pass


class GC_MIDAS_RESPONSE_BUYGOODS (Packet):
    def handle(self):
        # begin handle [GC_MIDAS_RESPONSE_BUYGOODS] message attrs, auto generate do not change
        self.person['Ret'] = self['Ret']
        self.person['Message'] = self['Message']
        self.person['UrlParams'] = self['UrlParams']
        # end handle [GC_MIDAS_RESPONSE_BUYGOODS] message attrs, auto generate do not change
        pass


class GC_PRESTIGE_TODAYWILDNUM (Packet):
    def handle(self):
        # begin handle [GC_PRESTIGE_TODAYWILDNUM] message attrs, auto generate do not change
        self.person['todaywildnum'] = self['todaywildnum']
        self.person['exploitnum'] = self['exploitnum']
        # end handle [GC_PRESTIGE_TODAYWILDNUM] message attrs, auto generate do not change
        pass


class GC_SYNC_GODWEAPON_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GODWEAPON_DATA] message attrs, auto generate do not change
        self.person['Elems'] = self['Elems']
        self.person['OpType'] = self['OpType']
        # end handle [GC_SYNC_GODWEAPON_DATA] message attrs, auto generate do not change
        pass


class GC_DEATH_LETHAL_DAMAGE_LIST_INFO (Packet):
    def handle(self):
        # begin handle [GC_DEATH_LETHAL_DAMAGE_LIST_INFO] message attrs, auto generate do not change
        self.person['casterName'] = self['casterName']
        self.person['skillId'] = self['skillId']
        self.person['damageVal'] = self['damageVal']
        self.person['ratio'] = self['ratio']
        # end handle [GC_DEATH_LETHAL_DAMAGE_LIST_INFO] message attrs, auto generate do not change
        pass


class CG_RESET_FAIRY_ATTR_POINTS (Packet):
    pass


class CG_SYNC_BOUNTY_ITEM_POS_LIST (Packet):
    pass


class CG_EQUIPMIRROR_PURIFY (Packet):
    pass


class GC_PRESTIGE_SYNCINFO (Packet):
    def handle(self):
        # begin handle [GC_PRESTIGE_SYNCINFO] message attrs, auto generate do not change
        self.person['PlayerPrestigeInfo'] = self['PlayerPrestigeInfo']
        # end handle [GC_PRESTIGE_SYNCINFO] message attrs, auto generate do not change
        pass


class CG_REQ_ENTER_GUILD_WAR (Packet):
    pass


class GC_MILITARY_SYNC_LIMITINFO (Packet):
    def handle(self):
        # begin handle [GC_MILITARY_SYNC_LIMITINFO] message attrs, auto generate do not change
        self.person['nSaveIndex'] = self['nSaveIndex']
        self.person['nCanBuyCount'] = self['nCanBuyCount']
        # end handle [GC_MILITARY_SYNC_LIMITINFO] message attrs, auto generate do not change
        pass


class GC_GET_GUILD_CONTRIBUTE (Packet):
    def handle(self):
        # begin handle [GC_GET_GUILD_CONTRIBUTE] message attrs, auto generate do not change
        self.person['count'] = self['count']
        # end handle [GC_GET_GUILD_CONTRIBUTE] message attrs, auto generate do not change
        pass


class GC_RET_USE_SKILL (Packet):
    def handle(self):
        # begin handle [GC_RET_USE_SKILL] message attrs, auto generate do not change
        self.person['skillId'] = self['skillId']
        self.person['senderId'] = self['senderId']
        self.person['TargetId'] = self['TargetId']
        self.person['isClientPlayed'] = self['isClientPlayed']
        self.person['skillname'] = self['skillname']
        self.person['itemDataId'] = self['itemDataId']
        self.person['isFailed'] = self['isFailed']
        self.person['vDirectionX'] = self['vDirectionX']
        self.person['vDirectionY'] = self['vDirectionY']
        self.person['vDirectionZ'] = self['vDirectionZ']
        self.person['vTargetPosX'] = self['vTargetPosX']
        self.person['vTargetPosY'] = self['vTargetPosY']
        self.person['vTargetPosZ'] = self['vTargetPosZ']
        # end handle [GC_RET_USE_SKILL] message attrs, auto generate do not change
        pass


class GC_REQ_APPRENTICE_CONFIGM_RECRUIT (Packet):
    def handle(self):
        # begin handle [GC_REQ_APPRENTICE_CONFIGM_RECRUIT] message attrs, auto generate do not change
        self.person['masterGuid'] = self['masterGuid']
        self.person['masterName'] = self['masterName']
        # end handle [GC_REQ_APPRENTICE_CONFIGM_RECRUIT] message attrs, auto generate do not change
        pass


class CG_BWPVPVIEW_SETPOS (Packet):
    pass


class GC_RET_QQ_UNREG_FRIENDS (Packet):
    def handle(self):
        # begin handle [GC_RET_QQ_UNREG_FRIENDS] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['errorMsg'] = self['errorMsg']
        self.person['friendList'] = self['friendList']
        # end handle [GC_RET_QQ_UNREG_FRIENDS] message attrs, auto generate do not change
        pass


class CG_FASHION_COLOR (Packet):
    pass


class GC_SYNC_BOUNTY_ITEM_POS_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BOUNTY_ITEM_POS_LIST] message attrs, auto generate do not change
        self.person['playerPosX'] = self['playerPosX']
        self.person['playerPosY'] = self['playerPosY']
        self.person['playerPosZ'] = self['playerPosZ']
        self.person['npcPosX'] = self['npcPosX']
        self.person['npcPosY'] = self['npcPosY']
        self.person['npcPosZ'] = self['npcPosZ']
        # end handle [GC_SYNC_BOUNTY_ITEM_POS_LIST] message attrs, auto generate do not change
        pass


class GC_FRIENDPOINTVALUE_REWARDSTATUS_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_FRIENDPOINTVALUE_REWARDSTATUS_UPDATE] message attrs, auto generate do not change
        self.person['friendGuid'] = self['friendGuid']
        self.person['rewardstatus'] = self['rewardstatus']
        # end handle [GC_FRIENDPOINTVALUE_REWARDSTATUS_UPDATE] message attrs, auto generate do not change
        pass


class GC_ISOPEN_SIGNINANDOLDLOGIN (Packet):
    def handle(self):
        # begin handle [GC_ISOPEN_SIGNINANDOLDLOGIN] message attrs, auto generate do not change
        self.person['isopensignin'] = self['isopensignin']
        # end handle [GC_ISOPEN_SIGNINANDOLDLOGIN] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_REACHEDSCENE] message attrs, auto generate do not change
        self.person['reachedSceneID'] = self['reachedSceneID']
        # end handle [GC_SYNC_REACHEDSCENE] message attrs, auto generate do not change
        pass


class GC_QIANKUNDAI_MAKE (Packet):
    def handle(self):
        # begin handle [GC_QIANKUNDAI_MAKE] message attrs, auto generate do not change
        self.person['makeItem'] = self['makeItem']
        # end handle [GC_QIANKUNDAI_MAKE] message attrs, auto generate do not change
        pass


class CG_WAITPAY_REFUSE (Packet):
    pass


class GC_SYN_SKILLINFO (Packet):
    def handle(self):
        # begin handle [GC_SYN_SKILLINFO] message attrs, auto generate do not change
        self.person['skillid'] = self['skillid']
        self.person['skillindex'] = self['skillindex']
        self.person['CDId'] = self['CDId']
        self.person['CDTime'] = self['CDTime']
        self.person['isSkillLevelUp'] = self['isSkillLevelUp']
        self.person['skillLayer'] = self['skillLayer']
        self.person['skillLevel'] = self['skillLevel']
        self.person['useCount'] = self['useCount']
        self.person['chargeCount'] = self['chargeCount']
        self.person['cooldownLayer'] = self['cooldownLayer']
        self.person['skillRealLevel'] = self['skillRealLevel']
        self.person['bUnlockSkill'] = self['bUnlockSkill']
        self.person['bActiveSkill'] = self['bActiveSkill']
        self.person['skillcombat'] = self['skillcombat']
        # end handle [GC_SYN_SKILLINFO] message attrs, auto generate do not change
        pass


class GC_CRAFTMAN_FORGE_RET (Packet):
    def handle(self):
        # begin handle [GC_CRAFTMAN_FORGE_RET] message attrs, auto generate do not change
        self.person['itemGuid'] = self['itemGuid']
        self.person['retCode'] = self['retCode']
        # end handle [GC_CRAFTMAN_FORGE_RET] message attrs, auto generate do not change
        pass


class CG_SET_SOCIALUI_IS_NEEDTO_UPDATE (Packet):
    pass


class GC_PLAYCG (Packet):
    def handle(self):
        # begin handle [GC_PLAYCG] message attrs, auto generate do not change
        self.person['CGName'] = self['CGName']
        # end handle [GC_PLAYCG] message attrs, auto generate do not change
        pass


class GC_RET_MIRROR_QUICKCOMPOND_RESULT (Packet):
    def handle(self):
        # begin handle [GC_RET_MIRROR_QUICKCOMPOND_RESULT] message attrs, auto generate do not change
        self.person['mirrorguidlist'] = self['mirrorguidlist']
        # end handle [GC_RET_MIRROR_QUICKCOMPOND_RESULT] message attrs, auto generate do not change
        pass


class GC_UPDATE_TITLE (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_TITLE] message attrs, auto generate do not change
        self.person['TitleClass'] = self['TitleClass']
        self.person['TitleIndex'] = self['TitleIndex']
        self.person['TitleId'] = self['TitleId']
        self.person['CreateTime'] = self['CreateTime']
        self.person['OpType'] = self['OpType']
        self.person['FirstUserDefContent'] = self['FirstUserDefContent']
        self.person['SecondUserDefContent'] = self['SecondUserDefContent']
        self.person['ExtraLifeTime'] = self['ExtraLifeTime']
        # end handle [GC_UPDATE_TITLE] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_REQ_OTHERINFO (Packet):
    pass


class GC_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE (Packet):
    def handle(self):
        # begin handle [GC_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE] message attrs, auto generate do not change
        self.person['RealTimeRole'] = self['RealTimeRole']
        self.person['GRTVRoomId'] = self['GRTVRoomId']
        self.person['managerGuid'] = self['managerGuid']
        # end handle [GC_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE] message attrs, auto generate do not change
        pass


class GC_DOMAIN_SYNC_DECLAREINFO (Packet):
    def handle(self):
        # begin handle [GC_DOMAIN_SYNC_DECLAREINFO] message attrs, auto generate do not change
        self.person['declareDomainIdList'] = self['declareDomainIdList']
        self.person['declareDomainIdPriceList'] = self['declareDomainIdPriceList']
        self.person['declareDomainCnt'] = self['declareDomainCnt']
        # end handle [GC_DOMAIN_SYNC_DECLAREINFO] message attrs, auto generate do not change
        pass


class GC_GUILD_INVITE_CONFIRM (Packet):
    def handle(self):
        # begin handle [GC_GUILD_INVITE_CONFIRM] message attrs, auto generate do not change
        self.person['inviterGuid'] = self['inviterGuid']
        self.person['inviterGuildGuid'] = self['inviterGuildGuid']
        self.person['inviterName'] = self['inviterName']
        self.person['inviterGuidName'] = self['inviterGuidName']
        # end handle [GC_GUILD_INVITE_CONFIRM] message attrs, auto generate do not change
        pass


class CG_HONGBAO_FESTIVAL_SEND (Packet):
    pass


class GC_GUILD_RET_CANCELBUILD (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_CANCELBUILD] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['guildMoney'] = self['guildMoney']
        # end handle [GC_GUILD_RET_CANCELBUILD] message attrs, auto generate do not change
        pass


class GC_RET_LASTRECAST_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_LASTRECAST_INFO] message attrs, auto generate do not change
        self.person['equipguid'] = self['equipguid']
        self.person['AttrId'] = self['AttrId']
        self.person['AttrVal'] = self['AttrVal']
        self.person['AttrType'] = self['AttrType']
        # end handle [GC_RET_LASTRECAST_INFO] message attrs, auto generate do not change
        pass


class CG_MERCENARY_REQ (Packet):
    pass


class GC_UPDATE_PART_COMBATVAL (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_PART_COMBATVAL] message attrs, auto generate do not change
        self.person['skill'] = self['skill']
        self.person['guildAddition'] = self['guildAddition']
        self.person['equip'] = self['equip']
        self.person['refine'] = self['refine']
        self.person['gem'] = self['gem']
        self.person['fairy'] = self['fairy']
        self.person['tianshu'] = self['tianshu']
        self.person['engrave'] = self['engrave']
        self.person['servant'] = self['servant']
        self.person['rebirth'] = self['rebirth']
        self.person['home'] = self['home']
        self.person['godweapon'] = self['godweapon']
        self.person['jade'] = self['jade']
        # end handle [GC_UPDATE_PART_COMBATVAL] message attrs, auto generate do not change
        pass


class GC_GUILD_RET_SET_QUICKJOIN (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_SET_QUICKJOIN] message attrs, auto generate do not change
        self.person['flag'] = self['flag']
        # end handle [GC_GUILD_RET_SET_QUICKJOIN] message attrs, auto generate do not change
        pass


class GC_SYNC_EQUIP_REBIRTH_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_EQUIP_REBIRTH_DATA] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['syncType'] = self['syncType']
        self.person['rebirthDatas'] = self['rebirthDatas']
        # end handle [GC_SYNC_EQUIP_REBIRTH_DATA] message attrs, auto generate do not change
        pass


class GC_MOUNT_MARK_RET (Packet):
    def handle(self):
        # begin handle [GC_MOUNT_MARK_RET] message attrs, auto generate do not change
        self.person['MountID'] = self['MountID']
        self.person['Ret'] = self['Ret']
        # end handle [GC_MOUNT_MARK_RET] message attrs, auto generate do not change
        pass


class GC_RESIZE_FAIRY_PACK (Packet):
    def handle(self):
        # begin handle [GC_RESIZE_FAIRY_PACK] message attrs, auto generate do not change
        self.person['size'] = self['size']
        # end handle [GC_RESIZE_FAIRY_PACK] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILDCONVOY_CONVOY (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILDCONVOY_CONVOY] message attrs, auto generate do not change
        self.person['leftTime'] = self['leftTime']
        self.person['carriageObjId'] = self['carriageObjId']
        self.person['carriageSceneClassId'] = self['carriageSceneClassId']
        self.person['carriageSceneInstId'] = self['carriageSceneInstId']
        # end handle [GC_SYNC_GUILDCONVOY_CONVOY] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_MOVE] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['poscount'] = self['poscount']
        self.person['posserial'] = self['posserial']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        self.person['exState'] = self['exState']
        # end handle [GC_MOVE] message attrs, auto generate do not change
        pass


class CG_HUILIU_GOAL_GET_AWARD (Packet):
    pass


class GC_GUILDMONSTER_DANGERFISH (Packet):
    def handle(self):
        # begin handle [GC_GUILDMONSTER_DANGERFISH] message attrs, auto generate do not change
        self.person['NpcDataId'] = self['NpcDataId']
        self.person['PosX'] = self['PosX']
        self.person['PosY'] = self['PosY']
        self.person['PosZ'] = self['PosZ']
        self.person['OpType'] = self['OpType']
        # end handle [GC_GUILDMONSTER_DANGERFISH] message attrs, auto generate do not change
        pass


class CG_REQ_HOME_HORDE_RENAME (Packet):
    pass


class GC_TOWER_BUY_RESULT (Packet):
    def handle(self):
        # begin handle [GC_TOWER_BUY_RESULT] message attrs, auto generate do not change
        self.person['TowerShopID'] = self['TowerShopID']
        self.person['BuyCount'] = self['BuyCount']
        self.person['FutuCoin'] = self['FutuCoin']
        # end handle [GC_TOWER_BUY_RESULT] message attrs, auto generate do not change
        pass


class CG_ASK_LEVELREWARD (Packet):
    pass


class GC_GUILDCHECK_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_GUILDCHECK_UPDATE] message attrs, auto generate do not change
        self.person['ObjId'] = self['ObjId']
        self.person['TitleId'] = self['TitleId']
        self.person['FirstUserDef'] = self['FirstUserDef']
        self.person['SecondUserDef'] = self['SecondUserDef']
        # end handle [GC_GUILDCHECK_UPDATE] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_UPDATE_SKILLZHUANJING_ACTIVE_INFO] message attrs, auto generate do not change
        self.person['nSkillZhuanJingId'] = self['nSkillZhuanJingId']
        self.person['bActiveFlag'] = self['bActiveFlag']
        self.person['bIsAuto'] = self['bIsAuto']
        self.person['bNewActive'] = self['bNewActive']
        # end handle [GC_UPDATE_SKILLZHUANJING_ACTIVE_INFO] message attrs, auto generate do not change
        pass


class CG_JOIN_TEAM_INVITE_RESULT (Packet):
    pass


class CG_SWITCH_HOME_PLAN (Packet):
    pass


class CG_ASKCOLORCORRECTIONMAIL (Packet):
    pass


class GC_REMOVEEFFECT (Packet):
    def handle(self):
        # begin handle [GC_REMOVEEFFECT] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['effectId'] = self['effectId']
        self.person['isForEffectCamera'] = self['isForEffectCamera']
        self.person['senderID'] = self['senderID']
        # end handle [GC_REMOVEEFFECT] message attrs, auto generate do not change
        pass


class CG_SHOW_HELMET (Packet):
    pass


class GC_CANCEL_MFLY (Packet):
    def handle(self):
        # begin handle [GC_CANCEL_MFLY] message attrs, auto generate do not change
        # end handle [GC_CANCEL_MFLY] message attrs, auto generate do not change
        pass


class CG_ASKTRACKCHANGE (Packet):
    pass


class GC_PGL_RESPONSE_INFO (Packet):
    def handle(self):
        # begin handle [GC_PGL_RESPONSE_INFO] message attrs, auto generate do not change
        self.person['nDan'] = self['nDan']
        self.person['bDanAwardFlag'] = self['bDanAwardFlag']
        self.person['nRank'] = self['nRank']
        self.person['nTotalNumber'] = self['nTotalNumber']
        self.person['nCurrentNumber'] = self['nCurrentNumber']
        self.person['nMatchStatus'] = self['nMatchStatus']
        # end handle [GC_PGL_RESPONSE_INFO] message attrs, auto generate do not change
        pass


class CG_ASK_CHRISTMASMONSTERLIST_DATA (Packet):
    pass


class CG_BROTHERHOOD_INVITE_BIRTHDAY (Packet):
    pass


class CG_DOMAIN_REQ_ENTERLINE (Packet):
    pass


class GC_PRESENT_NEW (Packet):
    def handle(self):
        # begin handle [GC_PRESENT_NEW] message attrs, auto generate do not change
        self.person['NewBill'] = self['NewBill']
        # end handle [GC_PRESENT_NEW] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_CHANGE_TITLE (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_CHANGE_TITLE] message attrs, auto generate do not change
        self.person['title'] = self['title']
        # end handle [GC_BROTHERHOOD_CHANGE_TITLE] message attrs, auto generate do not change
        pass


class GC_RET_ATTR_ADD_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_RET_ATTR_ADD_NOTICE] message attrs, auto generate do not change
        self.person['nType'] = self['nType']
        self.person['nNum'] = self['nNum']
        # end handle [GC_RET_ATTR_ADD_NOTICE] message attrs, auto generate do not change
        pass


class GC_SCENE_SPECIAL_OPERATE (Packet):
    def handle(self):
        # begin handle [GC_SCENE_SPECIAL_OPERATE] message attrs, auto generate do not change
        self.person['sceneId'] = self['sceneId']
        self.person['operateId'] = self['operateId']
        self.person['isOpen'] = self['isOpen']
        self.person['Param'] = self['Param']
        # end handle [GC_SCENE_SPECIAL_OPERATE] message attrs, auto generate do not change
        pass


class CG_COMBATLIMITSHOP_BUY (Packet):
    pass


class CG_PRESENT_ADD (Packet):
    pass


class GC_BROTHERHOOD_INVITE_CONFIRM (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_INVITE_CONFIRM] message attrs, auto generate do not change
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberProf'] = self['memberProf']
        self.person['memberSex'] = self['memberSex']
        self.person['confirmed'] = self['confirmed']
        self.person['inviterGuid'] = self['inviterGuid']
        # end handle [GC_BROTHERHOOD_INVITE_CONFIRM] message attrs, auto generate do not change
        pass


class GC_RET_GUILD_MONSTER_LASTTIME (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILD_MONSTER_LASTTIME] message attrs, auto generate do not change
        self.person['lastTime'] = self['lastTime']
        # end handle [GC_RET_GUILD_MONSTER_LASTTIME] message attrs, auto generate do not change
        pass


class CG_UPGRADE_PRACTICE_REQUEST (Packet):
    pass


class CG_MULPVP_INVITE (Packet):
    pass


class CG_BIGBATTLE_ENROLL (Packet):
    pass


class GC_WATERMELON_SYNC_COMBAT_STATUS (Packet):
    def handle(self):
        # begin handle [GC_WATERMELON_SYNC_COMBAT_STATUS] message attrs, auto generate do not change
        self.person['playerName'] = self['playerName']
        self.person['playerGuid'] = self['playerGuid']
        self.person['playerId'] = self['playerId']
        self.person['playerScore'] = self['playerScore']
        self.person['rewardItemId'] = self['rewardItemId']
        self.person['rewardItemCount'] = self['rewardItemCount']
        self.person['syncMode'] = self['syncMode']
        self.person['killerX'] = self['killerX']
        self.person['killerY'] = self['killerY']
        self.person['killerZ'] = self['killerZ']
        # end handle [GC_WATERMELON_SYNC_COMBAT_STATUS] message attrs, auto generate do not change
        pass


class CG_REQ_FAIRY_NEIDAN_INLAY (Packet):
    pass


class GC_QTE_PLAY (Packet):
    def handle(self):
        # begin handle [GC_QTE_PLAY] message attrs, auto generate do not change
        self.person['QTEID'] = self['QTEID']
        # end handle [GC_QTE_PLAY] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_RECRUIT_APPLY_BY_PLAYERGUID (Packet):
    pass


class GC_SHEDAOSAIMA_GETDAOJU (Packet):
    def handle(self):
        # begin handle [GC_SHEDAOSAIMA_GETDAOJU] message attrs, auto generate do not change
        self.person['DaoJuId'] = self['DaoJuId']
        # end handle [GC_SHEDAOSAIMA_GETDAOJU] message attrs, auto generate do not change
        pass


class CG_TIANSHUBOARD_INFO_SYNC (Packet):
    pass


class GC_PRESENT_RECEIVE (Packet):
    def handle(self):
        # begin handle [GC_PRESENT_RECEIVE] message attrs, auto generate do not change
        self.person['BillGuid'] = self['BillGuid']
        # end handle [GC_PRESENT_RECEIVE] message attrs, auto generate do not change
        pass


class GC_SYNC_DAY_CARD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DAY_CARD] message attrs, auto generate do not change
        self.person['isopen'] = self['isopen']
        self.person['getaward'] = self['getaward']
        self.person['is2open'] = self['is2open']
        self.person['is2get'] = self['is2get']
        self.person['neednum'] = self['neednum']
        self.person['is3open'] = self['is3open']
        self.person['is3get'] = self['is3get']
        self.person['need3num'] = self['need3num']
        self.person['todaynum'] = self['todaynum']
        # end handle [GC_SYNC_DAY_CARD] message attrs, auto generate do not change
        pass


class CG_MIDAS_REQUEST_BUYGOODS (Packet):
    pass


class CG_REQ_BOUNTY_CHANGE_SCENE (Packet):
    pass


class GC_ROLE_ONLINE (Packet):
    def handle(self):
        # begin handle [GC_ROLE_ONLINE] message attrs, auto generate do not change
        self.person['palyerGuid'] = self['palyerGuid']
        self.person['isOnline'] = self['isOnline']
        # end handle [GC_ROLE_ONLINE] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_RECRUIT_SETUP (Packet):
    pass


class GC_AUCTION_RETSELLLIST (Packet):
    def handle(self):
        # begin handle [GC_AUCTION_RETSELLLIST] message attrs, auto generate do not change
        self.person['auctionitems'] = self['auctionitems']
        # end handle [GC_AUCTION_RETSELLLIST] message attrs, auto generate do not change
        pass


class GC_DISCONNECT_NOTIFY (Packet):
    def handle(self):
        # begin handle [GC_DISCONNECT_NOTIFY] message attrs, auto generate do not change
        self.person['reason'] = self['reason']
        self.person['attachmsg'] = self['attachmsg']
        # end handle [GC_DISCONNECT_NOTIFY] message attrs, auto generate do not change
        pass


class CG_DOMAINWAR_REQ_DECLAREINFO (Packet):
    pass


class CG_SET_OR_MODIFY_SECPASSWORD (Packet):
    pass


class CG_TIANSHU_MASTER_LEVELUP (Packet):
    pass


class GC_FASHION_ADD (Packet):
    def handle(self):
        # begin handle [GC_FASHION_ADD] message attrs, auto generate do not change
        self.person['Fashion'] = self['Fashion']
        self.person['HideRed'] = self['HideRed']
        # end handle [GC_FASHION_ADD] message attrs, auto generate do not change
        pass


class GC_EYECATCHING_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_EYECATCHING_NOTICE] message attrs, auto generate do not change
        self.person['notice'] = self['notice']
        self.person['param'] = self['param']
        # end handle [GC_EYECATCHING_NOTICE] message attrs, auto generate do not change
        pass


class GC_SCREDITSCORE_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_SCREDITSCORE_NOTICE] message attrs, auto generate do not change
        self.person['noticetype'] = self['noticetype']
        self.person['noticeparam'] = self['noticeparam']
        self.person['noticeGuidparam'] = self['noticeGuidparam']
        self.person['targetName'] = self['targetName']
        # end handle [GC_SCREDITSCORE_NOTICE] message attrs, auto generate do not change
        pass


class GC_CVFIREFLY_SYNC_MEMBER_DATA (Packet):
    def handle(self):
        # begin handle [GC_CVFIREFLY_SYNC_MEMBER_DATA] message attrs, auto generate do not change
        self.person['teamId'] = self['teamId']
        self.person['teamName'] = self['teamName']
        self.person['playerName'] = self['playerName']
        self.person['playerGuid'] = self['playerGuid']
        self.person['profession'] = self['profession']
        self.person['sex'] = self['sex']
        # end handle [GC_CVFIREFLY_SYNC_MEMBER_DATA] message attrs, auto generate do not change
        pass


class GC_BUFF_CLEAR (Packet):
    def handle(self):
        # begin handle [GC_BUFF_CLEAR] message attrs, auto generate do not change
        # end handle [GC_BUFF_CLEAR] message attrs, auto generate do not change
        pass


class CG_REQ_PAYACT_CONFIG_DATA (Packet):
    pass


class GC_GUILDWAR_MEMBER_BATTLE_INFO (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_MEMBER_BATTLE_INFO] message attrs, auto generate do not change
        self.person['memberObjId'] = self['memberObjId']
        self.person['killcount'] = self['killcount']
        self.person['deathcount'] = self['deathcount']
        self.person['pointcount'] = self['pointcount']
        self.person['runepoint'] = self['runepoint']
        self.person['memberProfession'] = self['memberProfession']
        self.person['memberName'] = self['memberName']
        self.person['armyId'] = self['armyId']
        self.person['isMvp'] = self['isMvp']
        self.person['memberSex'] = self['memberSex']
        # end handle [GC_GUILDWAR_MEMBER_BATTLE_INFO] message attrs, auto generate do not change
        pass


class GC_BWPVPFINAL_SHOWICON (Packet):
    def handle(self):
        # begin handle [GC_BWPVPFINAL_SHOWICON] message attrs, auto generate do not change
        self.person['isShow'] = self['isShow']
        # end handle [GC_BWPVPFINAL_SHOWICON] message attrs, auto generate do not change
        pass


class GC_SYNC_RECENT_FINISH_ALL_ACHIEVEMENT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RECENT_FINISH_ALL_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        self.person['recordID'] = self['recordID']
        # end handle [GC_SYNC_RECENT_FINISH_ALL_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        pass


class CG_RECEIVE_ACHIEVEMENT_REWARD (Packet):
    pass


class GC_SYC_FULL_APPLY_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYC_FULL_APPLY_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['ReportCount'] = self['ReportCount']
        # end handle [GC_SYC_FULL_APPLY_LIST] message attrs, auto generate do not change
        pass


class GC_RES_PET_RENAME (Packet):
    def handle(self):
        # begin handle [GC_RES_PET_RENAME] message attrs, auto generate do not change
        self.person['petGuid'] = self['petGuid']
        self.person['name'] = self['name']
        # end handle [GC_RES_PET_RENAME] message attrs, auto generate do not change
        pass


class GC_SYNC_FIREWORKS_RANK_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FIREWORKS_RANK_CONFIG] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['posMin'] = self['posMin']
        self.person['posMax'] = self['posMax']
        self.person['awardIdA'] = self['awardIdA']
        self.person['awardNumA'] = self['awardNumA']
        self.person['awardIdB'] = self['awardIdB']
        self.person['awardNumB'] = self['awardNumB']
        self.person['awardIdC'] = self['awardIdC']
        self.person['awardNumC'] = self['awardNumC']
        # end handle [GC_SYNC_FIREWORKS_RANK_CONFIG] message attrs, auto generate do not change
        pass


class GC_SYNC_GEM_SLOT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GEM_SLOT] message attrs, auto generate do not change
        self.person['gemSlotList'] = self['gemSlotList']
        # end handle [GC_SYNC_GEM_SLOT] message attrs, auto generate do not change
        pass


class GC_SAVE_HOME_PLAN (Packet):
    def handle(self):
        # begin handle [GC_SAVE_HOME_PLAN] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        # end handle [GC_SAVE_HOME_PLAN] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_RET_APPLY_LEADER_VOTE] message attrs, auto generate do not change
        # end handle [GC_RET_APPLY_LEADER_VOTE] message attrs, auto generate do not change
        pass


class CG_HOME_PRODUCE_EMPLOY (Packet):
    pass


class GC_SYNC_TEAM_MERCENARY (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TEAM_MERCENARY] message attrs, auto generate do not change
        self.person['mercenaryList'] = self['mercenaryList']
        # end handle [GC_SYNC_TEAM_MERCENARY] message attrs, auto generate do not change
        pass


class GC_IDIP_SYNC_BAN_CHAT_REASON (Packet):
    def handle(self):
        # begin handle [GC_IDIP_SYNC_BAN_CHAT_REASON] message attrs, auto generate do not change
        self.person['reason'] = self['reason']
        self.person['endTime'] = self['endTime']
        # end handle [GC_IDIP_SYNC_BAN_CHAT_REASON] message attrs, auto generate do not change
        pass


class CG_ENTER_HOME (Packet):
    pass


class GC_SYNC_NATIONALDAY_TRIBUTE_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NATIONALDAY_TRIBUTE_CONFIG] message attrs, auto generate do not change
        self.person['startTime'] = self['startTime']
        self.person['endTime'] = self['endTime']
        self.person['maxTributeTime'] = self['maxTributeTime']
        self.person['costItemID'] = self['costItemID']
        self.person['costItemCount'] = self['costItemCount']
        self.person['rewardItemID'] = self['rewardItemID']
        self.person['rewardItemCount'] = self['rewardItemCount']
        self.person['progRewardItemID'] = self['progRewardItemID']
        self.person['progRewardItemCount'] = self['progRewardItemCount']
        self.person['progValue'] = self['progValue']
        self.person['maxTributeProgValue'] = self['maxTributeProgValue']
        # end handle [GC_SYNC_NATIONALDAY_TRIBUTE_CONFIG] message attrs, auto generate do not change
        pass


class GC_EXAM_UPDATESTATE (Packet):
    def handle(self):
        # begin handle [GC_EXAM_UPDATESTATE] message attrs, auto generate do not change
        self.person['state'] = self['state']
        self.person['questionIndex'] = self['questionIndex']
        self.person['timeLeft'] = self['timeLeft']
        self.person['question'] = self['question']
        self.person['answers'] = self['answers']
        self.person['category'] = self['category']
        self.person['rewards'] = self['rewards']
        self.person['questionCount'] = self['questionCount']
        self.person['openLevel'] = self['openLevel']
        self.person['examType'] = self['examType']
        # end handle [GC_EXAM_UPDATESTATE] message attrs, auto generate do not change
        pass


class GC_SET_ISINPKATTACKLIST (Packet):
    def handle(self):
        # begin handle [GC_SET_ISINPKATTACKLIST] message attrs, auto generate do not change
        self.person['targetGuid'] = self['targetGuid']
        self.person['IsInAttackList'] = self['IsInAttackList']
        # end handle [GC_SET_ISINPKATTACKLIST] message attrs, auto generate do not change
        pass


class GC_PRESTIGE_TODAYEXPLOIT (Packet):
    def handle(self):
        # begin handle [GC_PRESTIGE_TODAYEXPLOIT] message attrs, auto generate do not change
        self.person['todayexlpoit'] = self['todayexlpoit']
        # end handle [GC_PRESTIGE_TODAYEXPLOIT] message attrs, auto generate do not change
        pass


class GC_ASK_COMMONFLAG_RET (Packet):
    def handle(self):
        # begin handle [GC_ASK_COMMONFLAG_RET] message attrs, auto generate do not change
        self.person['nBits'] = self['nBits']
        self.person['bFlag'] = self['bFlag']
        # end handle [GC_ASK_COMMONFLAG_RET] message attrs, auto generate do not change
        pass


class GC_RET_MARRIAGE_DIVORCE (Packet):
    def handle(self):
        # begin handle [GC_RET_MARRIAGE_DIVORCE] message attrs, auto generate do not change
        self.person['loverLastOnlineTime'] = self['loverLastOnlineTime']
        # end handle [GC_RET_MARRIAGE_DIVORCE] message attrs, auto generate do not change
        pass


class GC_CHAT_SYNC_BUBBLESTYLE (Packet):
    def handle(self):
        # begin handle [GC_CHAT_SYNC_BUBBLESTYLE] message attrs, auto generate do not change
        self.person['unlock'] = self['unlock']
        self.person['HornStyle'] = self['HornStyle']
        self.person['PaoPaoStyle'] = self['PaoPaoStyle']
        # end handle [GC_CHAT_SYNC_BUBBLESTYLE] message attrs, auto generate do not change
        pass


class CG_ADD_FAIRY_PACK_SIZE (Packet):
    pass


class GC_SYNC_WAKEUP_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_WAKEUP_DATA] message attrs, auto generate do not change
        self.person['time'] = self['time']
        self.person['type'] = self['type']
        # end handle [GC_SYNC_WAKEUP_DATA] message attrs, auto generate do not change
        pass


class GC_SHEDAOSAIMA_RET_USEDAOJU (Packet):
    def handle(self):
        # begin handle [GC_SHEDAOSAIMA_RET_USEDAOJU] message attrs, auto generate do not change
        self.person['DaoJuId'] = self['DaoJuId']
        self.person['IsUsed'] = self['IsUsed']
        # end handle [GC_SHEDAOSAIMA_RET_USEDAOJU] message attrs, auto generate do not change
        pass


class GC_SYNC_EQUIP_SLOT_OPEN (Packet):
    def handle(self):
        # begin handle [GC_SYNC_EQUIP_SLOT_OPEN] message attrs, auto generate do not change
        self.person['openMirror'] = self['openMirror']
        self.person['openSignet'] = self['openSignet']
        self.person['noticeMirror'] = self['noticeMirror']
        self.person['noticeSignet'] = self['noticeSignet']
        # end handle [GC_SYNC_EQUIP_SLOT_OPEN] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_RECRUIT_MY (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_RECRUIT_MY] message attrs, auto generate do not change
        self.person['comvatVal'] = self['comvatVal']
        self.person['needProf'] = self['needProf']
        self.person['openRecruit'] = self['openRecruit']
        self.person['tags'] = self['tags']
        self.person['declaration'] = self['declaration']
        # end handle [GC_BROTHERHOOD_RECRUIT_MY] message attrs, auto generate do not change
        pass


class CG_DRAW_PHOTORANDOM_SHARE_GIFT (Packet):
    pass


class CG_SET_SELECT_PET (Packet):
    pass


class GC_RES_MIDSENDLANTERN (Packet):
    def handle(self):
        # begin handle [GC_RES_MIDSENDLANTERN] message attrs, auto generate do not change
        self.person['receiverGuid'] = self['receiverGuid']
        self.person['itemDataId'] = self['itemDataId']
        self.person['count'] = self['count']
        # end handle [GC_RES_MIDSENDLANTERN] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_INVITE_TITLE (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_INVITE_TITLE] message attrs, auto generate do not change
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberProf'] = self['memberProf']
        self.person['memberSex'] = self['memberSex']
        self.person['confirmed'] = self['confirmed']
        self.person['memberTitle'] = self['memberTitle']
        self.person['inviterGuid'] = self['inviterGuid']
        self.person['brotherhoodName'] = self['brotherhoodName']
        # end handle [GC_BROTHERHOOD_INVITE_TITLE] message attrs, auto generate do not change
        pass


class GC_SYNC_PVPZOMBIE_MEMBERINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PVPZOMBIE_MEMBERINFO] message attrs, auto generate do not change
        self.person['index'] = self['index']
        self.person['name'] = self['name']
        self.person['guid'] = self['guid']
        self.person['level'] = self['level']
        self.person['profession'] = self['profession']
        self.person['sex'] = self['sex']
        self.person['bodyId'] = self['bodyId']
        self.person['faceId'] = self['faceId']
        self.person['weaponId'] = self['weaponId']
        self.person['hairId'] = self['hairId']
        self.person['weaponRefineVisual'] = self['weaponRefineVisual']
        self.person['bodyColorVisual'] = self['bodyColorVisual']
        self.person['hp'] = self['hp']
        self.person['maxHp'] = self['maxHp']
        self.person['mp'] = self['mp']
        self.person['maxMp'] = self['maxMp']
        # end handle [GC_SYNC_PVPZOMBIE_MEMBERINFO] message attrs, auto generate do not change
        pass


class GC_GUILD_RET_SET_FULLACCEPT (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_SET_FULLACCEPT] message attrs, auto generate do not change
        self.person['flag'] = self['flag']
        # end handle [GC_GUILD_RET_SET_FULLACCEPT] message attrs, auto generate do not change
        pass


class GC_SYNC_SPECIAL_CIRTICAL_TIME (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SPECIAL_CIRTICAL_TIME] message attrs, auto generate do not change
        self.person['leftCriticalTime'] = self['leftCriticalTime']
        self.person['criticalTimes'] = self['criticalTimes']
        self.person['leftCanUseSpecialSkillTime'] = self['leftCanUseSpecialSkillTime']
        self.person['maxCriticalTimes'] = self['maxCriticalTimes']
        self.person['criticalTime'] = self['criticalTime']
        self.person['canUseSpecialSkillTime'] = self['canUseSpecialSkillTime']
        # end handle [GC_SYNC_SPECIAL_CIRTICAL_TIME] message attrs, auto generate do not change
        pass


class GC_UPDATE_FRIENDMAXNUM (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_FRIENDMAXNUM] message attrs, auto generate do not change
        self.person['friendMaxNum'] = self['friendMaxNum']
        self.person['optioncode'] = self['optioncode']
        # end handle [GC_UPDATE_FRIENDMAXNUM] message attrs, auto generate do not change
        pass


class GC_LOGIN_QUEUE_STATUS (Packet):
    def handle(self):
        # begin handle [GC_LOGIN_QUEUE_STATUS] message attrs, auto generate do not change
        self.person['status'] = self['status']
        self.person['index'] = self['index']
        self.person['xinYueLevel'] = self['xinYueLevel']
        # end handle [GC_LOGIN_QUEUE_STATUS] message attrs, auto generate do not change
        pass


class CG_REQ_CANCEL_APPLICANT_TEAM (Packet):
    pass


class GC_PGL_FIGHT_RESULT (Packet):
    def handle(self):
        # begin handle [GC_PGL_FIGHT_RESULT] message attrs, auto generate do not change
        self.person['myWinType'] = self['myWinType']
        self.person['myOldElo'] = self['myOldElo']
        self.person['myNewElo'] = self['myNewElo']
        self.person['myOldDan'] = self['myOldDan']
        self.person['myNewDan'] = self['myNewDan']
        self.person['memName'] = self['memName']
        self.person['memGuid'] = self['memGuid']
        self.person['memLev'] = self['memLev']
        self.person['memproId'] = self['memproId']
        self.person['memSideId'] = self['memSideId']
        self.person['memKillNum'] = self['memKillNum']
        self.person['memIsMVP'] = self['memIsMVP']
        self.person['nShowMoney1'] = self['nShowMoney1']
        self.person['nShowMoney2'] = self['nShowMoney2']
        # end handle [GC_PGL_FIGHT_RESULT] message attrs, auto generate do not change
        pass


class CG_ASK_RECOVER (Packet):
    pass


class CG_DEVICECLASSFY (Packet):
    pass


class GC_REQUEST_MFLY (Packet):
    def handle(self):
        # begin handle [GC_REQUEST_MFLY] message attrs, auto generate do not change
        self.person['sourceServerID'] = self['sourceServerID']
        self.person['inviteType'] = self['inviteType']
        # end handle [GC_REQUEST_MFLY] message attrs, auto generate do not change
        pass


class GC_REFINE_RET_REFINEMETER (Packet):
    def handle(self):
        # begin handle [GC_REFINE_RET_REFINEMETER] message attrs, auto generate do not change
        self.person['weapon'] = self['weapon']
        self.person['glove'] = self['glove']
        self.person['ring'] = self['ring']
        self.person['necklace'] = self['necklace']
        self.person['cloak'] = self['cloak']
        self.person['shoes'] = self['shoes']
        self.person['pants'] = self['pants']
        self.person['belt'] = self['belt']
        self.person['clothes'] = self['clothes']
        self.person['helmet'] = self['helmet']
        self.person['tome'] = self['tome']
        self.person['mirror'] = self['mirror']
        self.person['signet'] = self['signet']
        self.person['convo'] = self['convo']
        # end handle [GC_REFINE_RET_REFINEMETER] message attrs, auto generate do not change
        pass


class GC_MENTOR_SHOP_INFO (Packet):
    def handle(self):
        # begin handle [GC_MENTOR_SHOP_INFO] message attrs, auto generate do not change
        self.person['MentorShopItemId'] = self['MentorShopItemId']
        self.person['MentorShopItemBuyCount'] = self['MentorShopItemBuyCount']
        # end handle [GC_MENTOR_SHOP_INFO] message attrs, auto generate do not change
        pass


class GC_RET_RANDOMNAMES (Packet):
    def handle(self):
        # begin handle [GC_RET_RANDOMNAMES] message attrs, auto generate do not change
        self.person['malenames'] = self['malenames']
        self.person['femalenames'] = self['femalenames']
        self.person['openRandomName'] = self['openRandomName']
        self.person['openServerRandomName'] = self['openServerRandomName']
        # end handle [GC_RET_RANDOMNAMES] message attrs, auto generate do not change
        pass


class CG_AUCTION_SELL (Packet):
    pass


class GC_ASURA_SHOW_KILLINFO (Packet):
    def handle(self):
        # begin handle [GC_ASURA_SHOW_KILLINFO] message attrs, auto generate do not change
        self.person['killerName'] = self['killerName']
        self.person['victimName'] = self['victimName']
        self.person['killerProf'] = self['killerProf']
        self.person['victimProf'] = self['victimProf']
        self.person['killerSex'] = self['killerSex']
        self.person['victimSex'] = self['victimSex']
        self.person['itemDataId'] = self['itemDataId']
        # end handle [GC_ASURA_SHOW_KILLINFO] message attrs, auto generate do not change
        pass


class GC_COPYSCENE_STATISTICS (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_STATISTICS] message attrs, auto generate do not change
        self.person['charguid'] = self['charguid']
        self.person['charname'] = self['charname']
        self.person['charcure'] = self['charcure']
        self.person['charatk'] = self['charatk']
        self.person['chardmg'] = self['chardmg']
        self.person['deathcount'] = self['deathcount']
        self.person['profession'] = self['profession']
        self.person['sex'] = self['sex']
        # end handle [GC_COPYSCENE_STATISTICS] message attrs, auto generate do not change
        pass


class GC_SYNC_MERCENARY_HP (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MERCENARY_HP] message attrs, auto generate do not change
        self.person['teamid'] = self['teamid']
        self.person['merguid'] = self['merguid']
        self.person['nowhp'] = self['nowhp']
        self.person['maxhp'] = self['maxhp']
        # end handle [GC_SYNC_MERCENARY_HP] message attrs, auto generate do not change
        pass


class GC_HOLIDAY_REDPOINT (Packet):
    def handle(self):
        # begin handle [GC_HOLIDAY_REDPOINT] message attrs, auto generate do not change
        self.person['HolidaySmallType'] = self['HolidaySmallType']
        self.person['bRedPoint'] = self['bRedPoint']
        # end handle [GC_HOLIDAY_REDPOINT] message attrs, auto generate do not change
        pass


class GC_WAITPAY_NEW (Packet):
    def handle(self):
        # begin handle [GC_WAITPAY_NEW] message attrs, auto generate do not change
        self.person['NewBill'] = self['NewBill']
        # end handle [GC_WAITPAY_NEW] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILD_THITF_AWARD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_THITF_AWARD] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['silverCoin'] = self['silverCoin']
        self.person['exp'] = self['exp']
        self.person['ItemList'] = self['ItemList']
        self.person['ItemNumList'] = self['ItemNumList']
        # end handle [GC_SYNC_GUILD_THITF_AWARD] message attrs, auto generate do not change
        pass


class CG_WISHING_REQUEST_DATA (Packet):
    pass


class GC_DOWNLOAD_VOICECHAT (Packet):
    def handle(self):
        # begin handle [GC_DOWNLOAD_VOICECHAT] message attrs, auto generate do not change
        self.person['VoiceIndex'] = self['VoiceIndex']
        self.person['VoiceFile'] = self['VoiceFile']
        self.person['PlayVoice'] = self['PlayVoice']
        # end handle [GC_DOWNLOAD_VOICECHAT] message attrs, auto generate do not change
        pass


class GC_ASK_CONTINUE_CATCHGHOST (Packet):
    def handle(self):
        # begin handle [GC_ASK_CONTINUE_CATCHGHOST] message attrs, auto generate do not change
        # end handle [GC_ASK_CONTINUE_CATCHGHOST] message attrs, auto generate do not change
        pass


class GC_RES_PET_LOCK (Packet):
    def handle(self):
        # begin handle [GC_RES_PET_LOCK] message attrs, auto generate do not change
        self.person['petGuid'] = self['petGuid']
        self.person['bLock'] = self['bLock']
        # end handle [GC_RES_PET_LOCK] message attrs, auto generate do not change
        pass


class CG_EQUIP_RECASTINHERIT (Packet):
    pass


class GC_RET_ACTIVENESSINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_ACTIVENESSINFO] message attrs, auto generate do not change
        self.person['activenessValue'] = self['activenessValue']
        self.person['activeAwardFlag'] = self['activeAwardFlag']
        # end handle [GC_RET_ACTIVENESSINFO] message attrs, auto generate do not change
        pass


class CG_BUY_BLACKMARKETITEM (Packet):
    pass


class CG_ASK_BOUNTY_REFREST_STATE (Packet):
    pass


class GC_PLAY_WORLD_DARKNESS (Packet):
    def handle(self):
        # begin handle [GC_PLAY_WORLD_DARKNESS] message attrs, auto generate do not change
        self.person['dataID'] = self['dataID']
        # end handle [GC_PLAY_WORLD_DARKNESS] message attrs, auto generate do not change
        pass


class CG_REQ_RANDOMNAMES (Packet):
    pass


class GC_UPDATE_XIUZHEN_COPYSCENE_DATA (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_XIUZHEN_COPYSCENE_DATA] message attrs, auto generate do not change
        self.person['xiuZhenCopySceneData'] = self['xiuZhenCopySceneData']
        # end handle [GC_UPDATE_XIUZHEN_COPYSCENE_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_FORTUNE_LEVEL_EXP (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FORTUNE_LEVEL_EXP] message attrs, auto generate do not change
        self.person['level'] = self['level']
        self.person['exp'] = self['exp']
        # end handle [GC_SYNC_FORTUNE_LEVEL_EXP] message attrs, auto generate do not change
        pass


class CG_ASK_WORLD_BOSS_STATE (Packet):
    pass


class CG_HONGBAO_CHARGE_SEND (Packet):
    pass


class CG_REQ_EYESSTAR (Packet):
    pass


class GC_RET_ADVENTURE_COMPLETED (Packet):
    def handle(self):
        # begin handle [GC_RET_ADVENTURE_COMPLETED] message attrs, auto generate do not change
        self.person['misHistory'] = self['misHistory']
        # end handle [GC_RET_ADVENTURE_COMPLETED] message attrs, auto generate do not change
        pass


class CG_CHAT (Packet):
    pass


class GC_START_CATCHGHOST (Packet):
    def handle(self):
        # begin handle [GC_START_CATCHGHOST] message attrs, auto generate do not change
        # end handle [GC_START_CATCHGHOST] message attrs, auto generate do not change
        pass


class GC_SYNC_PLAYER_HOMEGIFT_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PLAYER_HOMEGIFT_DATA] message attrs, auto generate do not change
        self.person['AlreadyGetGiftNum'] = self['AlreadyGetGiftNum']
        # end handle [GC_SYNC_PLAYER_HOMEGIFT_DATA] message attrs, auto generate do not change
        pass


class GC_SET_BLOCK_FRIENDAPPLY (Packet):
    def handle(self):
        # begin handle [GC_SET_BLOCK_FRIENDAPPLY] message attrs, auto generate do not change
        self.person['enableBlock'] = self['enableBlock']
        # end handle [GC_SET_BLOCK_FRIENDAPPLY] message attrs, auto generate do not change
        pass


class CG_TAKE_ITEM_STORAGEPACK (Packet):
    pass


class CG_ASK_BACK_LOGIN_AWARD (Packet):
    pass


class GC_FRIENDSENDFLOWER (Packet):
    def handle(self):
        # begin handle [GC_FRIENDSENDFLOWER] message attrs, auto generate do not change
        self.person['friendGuid'] = self['friendGuid']
        self.person['flowerDataid'] = self['flowerDataid']
        self.person['addedfrdpoint'] = self['addedfrdpoint']
        # end handle [GC_FRIENDSENDFLOWER] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_CHANGE_TITLE (Packet):
    pass


class GC_SYNC_XIUZHEN_LEVEL_REWARD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_XIUZHEN_LEVEL_REWARD] message attrs, auto generate do not change
        self.person['xiuZhenRewardData'] = self['xiuZhenRewardData']
        # end handle [GC_SYNC_XIUZHEN_LEVEL_REWARD] message attrs, auto generate do not change
        pass


class GC_RELATION_OPTIONPANELINFO_RET (Packet):
    def handle(self):
        # begin handle [GC_RELATION_OPTIONPANELINFO_RET] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['returnRet'] = self['returnRet']
        self.person['TeamMemberNum'] = self['TeamMemberNum']
        self.person['IsTeamLeader'] = self['IsTeamLeader']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['optiontype'] = self['optiontype']
        self.person['guildguid'] = self['guildguid']
        self.person['sceneclassid'] = self['sceneclassid']
        self.person['sceneinstid'] = self['sceneinstid']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        self.person['IsArmyLeader'] = self['IsArmyLeader']
        self.person['ArmyID'] = self['ArmyID']
        self.person['TeamID'] = self['TeamID']
        self.person['ServerID'] = self['ServerID']
        self.person['BrotherhoodGuid'] = self['BrotherhoodGuid']
        self.person['SwordTeamGuid'] = self['SwordTeamGuid']
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['GuildType'] = self['GuildType']
        # end handle [GC_RELATION_OPTIONPANELINFO_RET] message attrs, auto generate do not change
        pass


class GC_BATTLEFIELD_LEAVE_BF (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_LEAVE_BF] message attrs, auto generate do not change
        # end handle [GC_BATTLEFIELD_LEAVE_BF] message attrs, auto generate do not change
        pass


class CG_SERVANT_REQOP (Packet):
    pass


class CG_REQ_TEAM_LEAVE (Packet):
    pass


class CG_RELATFRIEND_RECV_GIFT (Packet):
    pass


class GC_COPYSCENE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_RESULT] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['SceneID'] = self['SceneID']
        self.person['Mode'] = self['Mode']
        self.person['Grade'] = self['Grade']
        self.person['Star'] = self['Star']
        self.person['Score'] = self['Score']
        self.person['Time'] = self['Time']
        self.person['DeathCount'] = self['DeathCount']
        self.person['ExtraRule'] = self['ExtraRule']
        self.person['Profit'] = self['Profit']
        self.person['LeftTime'] = self['LeftTime']
        self.person['BestPlayer'] = self['BestPlayer']
        self.person['BestPlayerGuid'] = self['BestPlayerGuid']
        self.person['ResultType'] = self['ResultType']
        self.person['RewardItemIsBind'] = self['RewardItemIsBind']
        self.person['LastBossDropInfo'] = self['LastBossDropInfo']
        self.person['BestPlayerInfo'] = self['BestPlayerInfo']
        # end handle [GC_COPYSCENE_RESULT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_TOWER_FIGHT_RESULT] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['FightType'] = self['FightType']
        self.person['UseTime'] = self['UseTime']
        self.person['FightLeftCount'] = self['FightLeftCount']
        self.person['SweepLeftCount'] = self['SweepLeftCount']
        self.person['CurFloor'] = self['CurFloor']
        self.person['RewardItem'] = self['RewardItem']
        # end handle [GC_TOWER_FIGHT_RESULT] message attrs, auto generate do not change
        pass


class CG_QUIT_GAME (Packet):
    pass


class CG_GUILD_REQ_CHANGE_ACTIVITY_NOTICE (Packet):
    pass


class GC_RETTRACKPLAYER (Packet):
    def handle(self):
        # begin handle [GC_RETTRACKPLAYER] message attrs, auto generate do not change
        self.person['tarname'] = self['tarname']
        self.person['sceneclassid'] = self['sceneclassid']
        self.person['sceneinstid'] = self['sceneinstid']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        self.person['retType'] = self['retType']
        # end handle [GC_RETTRACKPLAYER] message attrs, auto generate do not change
        pass


class CG_REQ_YLTXINST_DES_REMAIN_NUM (Packet):
    pass


class GC_CLEAR_ITEMPACK_NEWLIST (Packet):
    def handle(self):
        # begin handle [GC_CLEAR_ITEMPACK_NEWLIST] message attrs, auto generate do not change
        self.person['PackType'] = self['PackType']
        self.person['ClearAll'] = self['ClearAll']
        self.person['ClearGuid'] = self['ClearGuid']
        # end handle [GC_CLEAR_ITEMPACK_NEWLIST] message attrs, auto generate do not change
        pass


class GC_STOP_RUBKICUBE_SUB_PLAY (Packet):
    def handle(self):
        # begin handle [GC_STOP_RUBKICUBE_SUB_PLAY] message attrs, auto generate do not change
        self.person['subRubkiCubePlayId'] = self['subRubkiCubePlayId']
        self.person['serverTime'] = self['serverTime']
        # end handle [GC_STOP_RUBKICUBE_SUB_PLAY] message attrs, auto generate do not change
        pass


class CG_SKILLZHUANJING_LEVEL_UP (Packet):
    pass


class CG_ASKFOR_RELATION_OPTIONPANELINFO (Packet):
    pass


class GC_COMBATLIMITSHOP_SYNC (Packet):
    def handle(self):
        # begin handle [GC_COMBATLIMITSHOP_SYNC] message attrs, auto generate do not change
        self.person['ItemId'] = self['ItemId']
        self.person['Stack'] = self['Stack']
        self.person['MoneyType'] = self['MoneyType']
        self.person['Price'] = self['Price']
        self.person['Discount'] = self['Discount']
        self.person['PlayerRemain'] = self['PlayerRemain']
        self.person['GoodsIndex'] = self['GoodsIndex']
        self.person['ShowSort'] = self['ShowSort']
        self.person['RemainTime'] = self['RemainTime']
        self.person['LimitType'] = self['LimitType']
        self.person['IsInSale'] = self['IsInSale']
        self.person['Version'] = self['Version']
        self.person['buyitem'] = self['buyitem']
        self.person['playerMaxNum'] = self['playerMaxNum']
        self.person['EndTime'] = self['EndTime']
        # end handle [GC_COMBATLIMITSHOP_SYNC] message attrs, auto generate do not change
        pass


class GC_MISSION_STATE (Packet):
    def handle(self):
        # begin handle [GC_MISSION_STATE] message attrs, auto generate do not change
        self.person['nMisID'] = self['nMisID']
        self.person['nTargetIndex'] = self['nTargetIndex']
        self.person['State'] = self['State']
        # end handle [GC_MISSION_STATE] message attrs, auto generate do not change
        pass


class CG_GUILD_APPROVE_RESERVE (Packet):
    pass


class GC_AUTO_TEAMFOLLOW_AFTER_KILLTARGET (Packet):
    def handle(self):
        # begin handle [GC_AUTO_TEAMFOLLOW_AFTER_KILLTARGET] message attrs, auto generate do not change
        self.person['targetId'] = self['targetId']
        # end handle [GC_AUTO_TEAMFOLLOW_AFTER_KILLTARGET] message attrs, auto generate do not change
        pass


class GC_LOCK_CURTITLE (Packet):
    def handle(self):
        # begin handle [GC_LOCK_CURTITLE] message attrs, auto generate do not change
        self.person['IsLock'] = self['IsLock']
        # end handle [GC_LOCK_CURTITLE] message attrs, auto generate do not change
        pass


class GC_UPDATEITEM (Packet):
    def handle(self):
        # begin handle [GC_UPDATEITEM] message attrs, auto generate do not change
        self.person['packtype'] = self['packtype']
        self.person['packindex'] = self['packindex']
        self.person['item'] = self['item']
        self.person['packdirty'] = self['packdirty']
        # end handle [GC_UPDATEITEM] message attrs, auto generate do not change
        pass


class CG_REQ_WILDSCENEDUEL (Packet):
    pass


class GC_CHANGE_FAIRY_NAME_RET (Packet):
    def handle(self):
        # begin handle [GC_CHANGE_FAIRY_NAME_RET] message attrs, auto generate do not change
        self.person['bRet'] = self['bRet']
        # end handle [GC_CHANGE_FAIRY_NAME_RET] message attrs, auto generate do not change
        pass


class CG_EQUIP_ENGRAVE (Packet):
    pass


class GC_SYNC_OTHERTEAMINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_OTHERTEAMINFO] message attrs, auto generate do not change
        self.person['sceneid'] = self['sceneid']
        self.person['sceneinst'] = self['sceneinst']
        self.person['otherteamid'] = self['otherteamid']
        self.person['syncop'] = self['syncop']
        self.person['meminfos'] = self['meminfos']
        # end handle [GC_SYNC_OTHERTEAMINFO] message attrs, auto generate do not change
        pass


class GC_NOTICE_PET_TAME (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_PET_TAME] message attrs, auto generate do not change
        self.person['petDataID'] = self['petDataID']
        # end handle [GC_NOTICE_PET_TAME] message attrs, auto generate do not change
        pass


class GC_REQUEST_SECOND_INTERACT (Packet):
    def handle(self):
        # begin handle [GC_REQUEST_SECOND_INTERACT] message attrs, auto generate do not change
        self.person['inviterServerID'] = self['inviterServerID']
        self.person['interactType'] = self['interactType']
        # end handle [GC_REQUEST_SECOND_INTERACT] message attrs, auto generate do not change
        pass


class CG_ASURA_ENROLL (Packet):
    pass


class GC_RET_CHRISTMASMONSTERLIST_DATA (Packet):
    def handle(self):
        # begin handle [GC_RET_CHRISTMASMONSTERLIST_DATA] message attrs, auto generate do not change
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        # end handle [GC_RET_CHRISTMASMONSTERLIST_DATA] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_RECRUIT_SYNC_APPLICANTS (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_RECRUIT_SYNC_APPLICANTS] message attrs, auto generate do not change
        self.person['applicantGuid'] = self['applicantGuid']
        self.person['applicantName'] = self['applicantName']
        self.person['applicantSex'] = self['applicantSex']
        self.person['applicantProf'] = self['applicantProf']
        self.person['applicantLevel'] = self['applicantLevel']
        # end handle [GC_BROTHERHOOD_RECRUIT_SYNC_APPLICANTS] message attrs, auto generate do not change
        pass


class GC_BATTLEFIELD_TOTAL_INFO (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_TOTAL_INFO] message attrs, auto generate do not change
        self.person['CreateTime'] = self['CreateTime']
        self.person['CopySceneID'] = self['CopySceneID']
        self.person['Players'] = self['Players']
        self.person['ResPoint'] = self['ResPoint']
        self.person['Flag'] = self['Flag']
        # end handle [GC_BATTLEFIELD_TOTAL_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_GROWTHUP_MARASARA_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GROWTHUP_MARASARA_DATA] message attrs, auto generate do not change
        self.person['m_GrowthUpActiveData'] = self['m_GrowthUpActiveData']
        self.person['m_DrawnLevelData'] = self['m_DrawnLevelData']
        self.person['tableData'] = self['tableData']
        # end handle [GC_SYNC_GROWTHUP_MARASARA_DATA] message attrs, auto generate do not change
        pass


class CG_GUILD_WAR_AGREE_SIGN_UP (Packet):
    pass


class CG_SET_MARRIAGE_PERSONAL_IDENTIFICATIONID (Packet):
    pass


class CG_ASK_COUPLE_BPCP_OPEN (Packet):
    pass


class GC_SYNC_EQUIP_ENGRAVE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_EQUIP_ENGRAVE_DATA] message attrs, auto generate do not change
        self.person['SlotList'] = self['SlotList']
        # end handle [GC_SYNC_EQUIP_ENGRAVE_DATA] message attrs, auto generate do not change
        pass


class CG_REQ_SCROLL_EXCHANGE (Packet):
    pass


class GC_RECOVERYFOODINFO_SYNC (Packet):
    def handle(self):
        # begin handle [GC_RECOVERYFOODINFO_SYNC] message attrs, auto generate do not change
        self.person['HPFoodlist'] = self['HPFoodlist']
        self.person['MPFoodlist'] = self['MPFoodlist']
        self.person['HPAutoValue'] = self['HPAutoValue']
        self.person['MPAutoValue'] = self['MPAutoValue']
        self.person['HPAutoSwitch'] = self['HPAutoSwitch']
        self.person['MPAutoSwitch'] = self['MPAutoSwitch']
        # end handle [GC_RECOVERYFOODINFO_SYNC] message attrs, auto generate do not change
        pass


class CG_ADD_MIS_COUNT (Packet):
    pass


class CG_DELIVER_SCENE_POSITION (Packet):
    pass


class GC_GUILDWAR_POINT_INFO (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_POINT_INFO] message attrs, auto generate do not change
        self.person['pointlist'] = self['pointlist']
        self.person['statelist'] = self['statelist']
        self.person['belongarmy'] = self['belongarmy']
        self.person['occupytime'] = self['occupytime']
        self.person['fposX'] = self['fposX']
        self.person['fposY'] = self['fposY']
        self.person['fposZ'] = self['fposZ']
        # end handle [GC_GUILDWAR_POINT_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_SET_GUILD_ADDITION (Packet):
    pass


class CG_ASK_COMMUNICATEWITHNPC (Packet):
    pass


class CG_FASHION_CHANGE (Packet):
    pass


class GC_OPEN_TIANSHUCHEST (Packet):
    def handle(self):
        # begin handle [GC_OPEN_TIANSHUCHEST] message attrs, auto generate do not change
        self.person['tianshuDataId'] = self['tianshuDataId']
        self.person['tianshuCount'] = self['tianshuCount']
        self.person['bind'] = self['bind']
        # end handle [GC_OPEN_TIANSHUCHEST] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_RES_JIANMUXB_CLICKLINK] message attrs, auto generate do not change
        self.person['targetGuid'] = self['targetGuid']
        self.person['slotId'] = self['slotId']
        self.person['itemId'] = self['itemId']
        self.person['itemNum'] = self['itemNum']
        self.person['helpCount'] = self['helpCount']
        self.person['guildContribute'] = self['guildContribute']
        self.person['silver'] = self['silver']
        self.person['exp'] = self['exp']
        # end handle [GC_RES_JIANMUXB_CLICKLINK] message attrs, auto generate do not change
        pass


class GC_MILITARY_SYNC_PINGMO (Packet):
    def handle(self):
        # begin handle [GC_MILITARY_SYNC_PINGMO] message attrs, auto generate do not change
        self.person['pingmoAcptTime'] = self['pingmoAcptTime']
        # end handle [GC_MILITARY_SYNC_PINGMO] message attrs, auto generate do not change
        pass


class CG_SAVE_HOME_PLAN (Packet):
    pass


class GC_CREATE_CHRISTMAS_COLLECT_BOX (Packet):
    def handle(self):
        # begin handle [GC_CREATE_CHRISTMAS_COLLECT_BOX] message attrs, auto generate do not change
        # end handle [GC_CREATE_CHRISTMAS_COLLECT_BOX] message attrs, auto generate do not change
        pass


class GC_SYNC_ARTIFACT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ARTIFACT_INFO] message attrs, auto generate do not change
        self.person['IsArtifactExc'] = self['IsArtifactExc']
        self.person['ProveState'] = self['ProveState']
        # end handle [GC_SYNC_ARTIFACT_INFO] message attrs, auto generate do not change
        pass


class GC_FASHION_SHOW (Packet):
    def handle(self):
        # begin handle [GC_FASHION_SHOW] message attrs, auto generate do not change
        self.person['FashionPart'] = self['FashionPart']
        self.person['ShowFashion'] = self['ShowFashion']
        # end handle [GC_FASHION_SHOW] message attrs, auto generate do not change
        pass


class GC_UPDATE_SKILL_LEVELUP_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_SKILL_LEVELUP_INFO] message attrs, auto generate do not change
        self.person['nSkillClassId'] = self['nSkillClassId']
        # end handle [GC_UPDATE_SKILL_LEVELUP_INFO] message attrs, auto generate do not change
        pass


class CG_ASK_GETREWARDFORSIGNIN_DAILY (Packet):
    pass


class GC_SYNC_ADD_DA_VALUE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ADD_DA_VALUE] message attrs, auto generate do not change
        self.person['dicId'] = self['dicId']
        self.person['diffValue'] = self['diffValue']
        # end handle [GC_SYNC_ADD_DA_VALUE] message attrs, auto generate do not change
        pass


class GC_SYNC_FIRSTCHARGEFLAG (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FIRSTCHARGEFLAG] message attrs, auto generate do not change
        self.person['isopen'] = self['isopen']
        self.person['firstget'] = self['firstget']
        self.person['weaponid'] = self['weaponid']
        self.person['toolid'] = self['toolid']
        self.person['toolcount'] = self['toolcount']
        self.person['silver'] = self['silver']
        # end handle [GC_SYNC_FIRSTCHARGEFLAG] message attrs, auto generate do not change
        pass


class GC_MULPVP_INVITE_MEM (Packet):
    def handle(self):
        # begin handle [GC_MULPVP_INVITE_MEM] message attrs, auto generate do not change
        self.person['inviterPlayerGuid'] = self['inviterPlayerGuid']
        self.person['isAskMem'] = self['isAskMem']
        self.person['inviterName'] = self['inviterName']
        self.person['inviterIsTeam'] = self['inviterIsTeam']
        self.person['answerName'] = self['answerName']
        self.person['answerIsTeam'] = self['answerIsTeam']
        # end handle [GC_MULPVP_INVITE_MEM] message attrs, auto generate do not change
        pass


class GC_SYNC_CHINESE_VALENTINE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CHINESE_VALENTINE_DATA] message attrs, auto generate do not change
        self.person['bMarriageGiftDrawn'] = self['bMarriageGiftDrawn']
        self.person['nCVFireflyChallengeCt'] = self['nCVFireflyChallengeCt']
        # end handle [GC_SYNC_CHINESE_VALENTINE_DATA] message attrs, auto generate do not change
        pass


class GC_AUCTION_RETFAVORITE (Packet):
    def handle(self):
        # begin handle [GC_AUCTION_RETFAVORITE] message attrs, auto generate do not change
        self.person['auctionguid'] = self['auctionguid']
        self.person['optype'] = self['optype']
        self.person['type'] = self['type']
        # end handle [GC_AUCTION_RETFAVORITE] message attrs, auto generate do not change
        pass


class GC_SYNC_PAYACT_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PAYACT_DATA] message attrs, auto generate do not change
        self.person['monthAccrualList'] = self['monthAccrualList']
        self.person['bGrowUp'] = self['bGrowUp']
        self.person['nGrowUpAlreadyLevel'] = self['nGrowUpAlreadyLevel']
        self.person['nGrowUpBuyLevel'] = self['nGrowUpBuyLevel']
        self.person['bDailyLimitedGiftFree'] = self['bDailyLimitedGiftFree']
        self.person['bDailyLimitedGift1'] = self['bDailyLimitedGift1']
        self.person['bDailyLimitedGift6'] = self['bDailyLimitedGift6']
        self.person['bDailyLimitedGift12'] = self['bDailyLimitedGift12']
        self.person['nStartWorkActivenes'] = self['nStartWorkActivenes']
        self.person['drawnItemList'] = self['drawnItemList']
        self.person['nDrawnCountToday'] = self['nDrawnCountToday']
        self.person['nStartWorkDrawnGiftLevel'] = self['nStartWorkDrawnGiftLevel']
        self.person['nStartWorkAccLoginCount'] = self['nStartWorkAccLoginCount']
        self.person['nStartWorkAccLoginDrawList'] = self['nStartWorkAccLoginDrawList']
        # end handle [GC_SYNC_PAYACT_DATA] message attrs, auto generate do not change
        pass


class CG_DOMAINSTATUE_REQ_KNEEL (Packet):
    pass


class CG_TIANSHU_MASTER_UNLOCK (Packet):
    pass


class GC_TIANSHU_COMPOSE (Packet):
    def handle(self):
        # begin handle [GC_TIANSHU_COMPOSE] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['decomposedTianshuId'] = self['decomposedTianshuId']
        self.person['debrisCount'] = self['debrisCount']
        # end handle [GC_TIANSHU_COMPOSE] message attrs, auto generate do not change
        pass


class CG_ASK_BLACKMARKETITEMINFO (Packet):
    pass


class CG_REQ_NATIONALDAY_TRIBUTE_STATE (Packet):
    pass


class GC_HUILIULIMITSHOP_SYNC (Packet):
    def handle(self):
        # begin handle [GC_HUILIULIMITSHOP_SYNC] message attrs, auto generate do not change
        self.person['ItemId'] = self['ItemId']
        self.person['Stack'] = self['Stack']
        self.person['MoneyType'] = self['MoneyType']
        self.person['Price'] = self['Price']
        self.person['Discount'] = self['Discount']
        self.person['PlayerRemain'] = self['PlayerRemain']
        self.person['GoodsIndex'] = self['GoodsIndex']
        self.person['ShowSort'] = self['ShowSort']
        self.person['RemainTime'] = self['RemainTime']
        self.person['LimitType'] = self['LimitType']
        self.person['IsInSale'] = self['IsInSale']
        self.person['GoodsVersion'] = self['GoodsVersion']
        self.person['ShopVersion'] = self['ShopVersion']
        self.person['ShopRemainTime'] = self['ShopRemainTime']
        self.person['buyitem'] = self['buyitem']
        # end handle [GC_HUILIULIMITSHOP_SYNC] message attrs, auto generate do not change
        pass


class GC_PLAYER_MOVETO (Packet):
    def handle(self):
        # begin handle [GC_PLAYER_MOVETO] message attrs, auto generate do not change
        self.person['scene'] = self['scene']
        self.person['dirX'] = self['dirX']
        self.person['dirY'] = self['dirY']
        self.person['dirZ'] = self['dirZ']
        self.person['isFly'] = self['isFly']
        # end handle [GC_PLAYER_MOVETO] message attrs, auto generate do not change
        pass


class GC_SYNC_JIAZHEN_RUBKICUBE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_JIAZHEN_RUBKICUBE_INFO] message attrs, auto generate do not change
        self.person['curJiaZhenCount'] = self['curJiaZhenCount']
        self.person['maxJiaZhenCount'] = self['maxJiaZhenCount']
        # end handle [GC_SYNC_JIAZHEN_RUBKICUBE_INFO] message attrs, auto generate do not change
        pass


class GC_MISSION_PARAM (Packet):
    def handle(self):
        # begin handle [GC_MISSION_PARAM] message attrs, auto generate do not change
        self.person['nMisID'] = self['nMisID']
        self.person['nTargetIndex'] = self['nTargetIndex']
        self.person['nParamIndex'] = self['nParamIndex']
        self.person['nVal'] = self['nVal']
        # end handle [GC_MISSION_PARAM] message attrs, auto generate do not change
        pass


class CG_PGL_REQUEST_INFO (Packet):
    pass


class GC_SyncShangGuEMoEnergy (Packet):
    def handle(self):
        # begin handle [GC_SyncShangGuEMoEnergy] message attrs, auto generate do not change
        self.person['curEnergyLayers'] = self['curEnergyLayers']
        self.person['maxEnergyLayers'] = self['maxEnergyLayers']
        # end handle [GC_SyncShangGuEMoEnergy] message attrs, auto generate do not change
        pass


class GC_DROPITEM_INFO (Packet):
    def handle(self):
        # begin handle [GC_DROPITEM_INFO] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['ownerGuid'] = self['ownerGuid']
        self.person['dropItemId'] = self['dropItemId']
        self.person['pos_x'] = self['pos_x']
        self.person['pos_y'] = self['pos_y']
        self.person['pos_z'] = self['pos_z']
        self.person['type'] = self['type']
        self.person['count'] = self['count']
        self.person['npc_posx'] = self['npc_posx']
        self.person['npc_posy'] = self['npc_posy']
        self.person['npc_posz'] = self['npc_posz']
        # end handle [GC_DROPITEM_INFO] message attrs, auto generate do not change
        pass


class CG_JUMP_REPORT (Packet):
    pass


class GC_SYNC_COMBATVALUE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COMBATVALUE] message attrs, auto generate do not change
        self.person['CombatValueList'] = self['CombatValueList']
        # end handle [GC_SYNC_COMBATVALUE] message attrs, auto generate do not change
        pass


class GC_GUILDWAR_RESULT (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_RESULT] message attrs, auto generate do not change
        self.person['result'] = self['result']
        # end handle [GC_GUILDWAR_RESULT] message attrs, auto generate do not change
        pass


class GC_PGL_NOTICE_TEAM_JOIN (Packet):
    def handle(self):
        # begin handle [GC_PGL_NOTICE_TEAM_JOIN] message attrs, auto generate do not change
        self.person['noticeType'] = self['noticeType']
        self.person['remainTimes'] = self['remainTimes']
        self.person['memStatus'] = self['memStatus']
        self.person['memName'] = self['memName']
        self.person['memGuid'] = self['memGuid']
        self.person['memLev'] = self['memLev']
        self.person['memProId'] = self['memProId']
        self.person['memNumber'] = self['memNumber']
        # end handle [GC_PGL_NOTICE_TEAM_JOIN] message attrs, auto generate do not change
        pass


class CG_DELE_HATEPEOPLEINFO (Packet):
    pass


class GC_BWPP_CONFIRMMATCH (Packet):
    def handle(self):
        # begin handle [GC_BWPP_CONFIRMMATCH] message attrs, auto generate do not change
        self.person['confimTip'] = self['confimTip']
        # end handle [GC_BWPP_CONFIRMMATCH] message attrs, auto generate do not change
        pass


class GC_MISSION_ABANDON_RET (Packet):
    def handle(self):
        # begin handle [GC_MISSION_ABANDON_RET] message attrs, auto generate do not change
        self.person['nMisID'] = self['nMisID']
        self.person['bRet'] = self['bRet']
        # end handle [GC_MISSION_ABANDON_RET] message attrs, auto generate do not change
        pass


class CG_NPCGIFTEXCHANGE_SEND_GIFT (Packet):
    pass


class GC_CHAT_PERSONAL (Packet):
    def handle(self):
        # begin handle [GC_CHAT_PERSONAL] message attrs, auto generate do not change
        self.person['Content'] = self['Content']
        self.person['SenderGuid'] = self['SenderGuid']
        self.person['SenderName'] = self['SenderName']
        self.person['SenderProfession'] = self['SenderProfession']
        self.person['SenderSex'] = self['SenderSex']
        self.person['reserved1'] = self['reserved1']
        self.person['Link'] = self['Link']
        self.person['LinkData'] = self['LinkData']
        self.person['ReciverGuid'] = self['ReciverGuid']
        self.person['ReciverName'] = self['ReciverName']
        self.person['ReciverProfession'] = self['ReciverProfession']
        self.person['ReciverSex'] = self['ReciverSex']
        self.person['reserved2'] = self['reserved2']
        self.person['SendTime'] = self['SendTime']
        self.person['VoiceFile'] = self['VoiceFile']
        self.person['VoiceDuration'] = self['VoiceDuration']
        self.person['SenderTeamId'] = self['SenderTeamId']
        self.person['LinkDownloadIndex'] = self['LinkDownloadIndex']
        self.person['LinkColorParam'] = self['LinkColorParam']
        self.person['emotionInfo'] = self['emotionInfo']
        self.person['VoiceLanguage'] = self['VoiceLanguage']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['BubbleChatId'] = self['BubbleChatId']
        # end handle [GC_CHAT_PERSONAL] message attrs, auto generate do not change
        packet = tasks.actions.net_packets.PACKETS.CG_CHAT_PERSONAL
        packet['Content'] = str(self['Content']) + " recved"
        packet['ReciverGuid'] = self['SenderGuid']
        tasks.actions.Functions.send_packet(packet)
        pass


class CG_WAITPAY_ADD (Packet):
    pass


class GC_COPYSCENE_DEATHNOTICE (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_DEATHNOTICE] message attrs, auto generate do not change
        self.person['id'] = self['id']
        # end handle [GC_COPYSCENE_DEATHNOTICE] message attrs, auto generate do not change
        pass


class GC_BUFF_SYNC_INFO (Packet):
    def handle(self):
        # begin handle [GC_BUFF_SYNC_INFO] message attrs, auto generate do not change
        self.person['charID'] = self['charID']
        self.person['id'] = self['id']
        self.person['uID'] = self['uID']
        self.person['layer'] = self['layer']
        self.person['totalTime'] = self['totalTime']
        self.person['remainTime'] = self['remainTime']
        self.person['isDisableMove'] = self['isDisableMove']
        self.person['isDisableSkill'] = self['isDisableSkill']
        self.person['parentSkillID'] = self['parentSkillID']
        self.person['isBorn'] = self['isBorn']
        self.person['stateIndex'] = self['stateIndex']
        self.person['isStopMove'] = self['isStopMove']
        self.person['senderID'] = self['senderID']
        # end handle [GC_BUFF_SYNC_INFO] message attrs, auto generate do not change
        pass


class GC_RET_LIFESKILL_LEVELUP (Packet):
    def handle(self):
        # begin handle [GC_RET_LIFESKILL_LEVELUP] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['level'] = self['level']
        self.person['guildContribute'] = self['guildContribute']
        # end handle [GC_RET_LIFESKILL_LEVELUP] message attrs, auto generate do not change
        pass


class GC_BATTLEFIELD_ACHIEVEMENT_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_ACHIEVEMENT_UPDATE] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['BFAchievementID'] = self['BFAchievementID']
        self.person['ObjId'] = self['ObjId']
        # end handle [GC_BATTLEFIELD_ACHIEVEMENT_UPDATE] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_INVITE_JOIN (Packet):
    pass


class GC_UPDATE_ACHIEVEMENT_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        self.person['recordID'] = self['recordID']
        self.person['bFinish'] = self['bFinish']
        self.person['bHaveReward'] = self['bHaveReward']
        # end handle [GC_UPDATE_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        pass


class GC_CVFIREFLY_UPDATE_SCORE (Packet):
    def handle(self):
        # begin handle [GC_CVFIREFLY_UPDATE_SCORE] message attrs, auto generate do not change
        self.person['teamId'] = self['teamId']
        self.person['score'] = self['score']
        self.person['nLastScoreTime'] = self['nLastScoreTime']
        # end handle [GC_CVFIREFLY_UPDATE_SCORE] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_PLAYER_LEVELUP_MANUAL_RET] message attrs, auto generate do not change
        self.person['optype'] = self['optype']
        self.person['opparam'] = self['opparam']
        # end handle [GC_PLAYER_LEVELUP_MANUAL_RET] message attrs, auto generate do not change
        pass


class GC_RET_AUTOTEAM (Packet):
    def handle(self):
        # begin handle [GC_RET_AUTOTEAM] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['targetID'] = self['targetID']
        self.person['sceneClassID'] = self['sceneClassID']
        self.person['difficulty'] = self['difficulty']
        # end handle [GC_RET_AUTOTEAM] message attrs, auto generate do not change
        pass


class GC_SEARCH_ACTOR (Packet):
    def handle(self):
        # begin handle [GC_SEARCH_ACTOR] message attrs, auto generate do not change
        self.person['SearchResult'] = self['SearchResult']
        self.person['ActorInfo'] = self['ActorInfo']
        # end handle [GC_SEARCH_ACTOR] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_BROTHERHOOD_INVITE_JOIN] message attrs, auto generate do not change
        self.person['inviterGuid'] = self['inviterGuid']
        self.person['brotherhoodName'] = self['brotherhoodName']
        self.person['inviterName'] = self['inviterName']
        # end handle [GC_BROTHERHOOD_INVITE_JOIN] message attrs, auto generate do not change
        pass


class GC_GROUPPHOTO_REPONSE (Packet):
    def handle(self):
        # begin handle [GC_GROUPPHOTO_REPONSE] message attrs, auto generate do not change
        self.person['function'] = self['function']
        self.person['optor'] = self['optor']
        self.person['opresult'] = self['opresult']
        # end handle [GC_GROUPPHOTO_REPONSE] message attrs, auto generate do not change
        pass


class CG_REQ_SKILLSOUL_GET (Packet):
    pass


class GC_RECENT_FINISH_ACHIEVEMENT_INFO (Packet):
    def handle(self):
        # begin handle [GC_RECENT_FINISH_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        self.person['achievementID'] = self['achievementID']
        # end handle [GC_RECENT_FINISH_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        pass


class GC_REFINETRANS_CONFIRM_RET (Packet):
    def handle(self):
        # begin handle [GC_REFINETRANS_CONFIRM_RET] message attrs, auto generate do not change
        self.person['state'] = self['state']
        self.person['srcguid'] = self['srcguid']
        self.person['targuid'] = self['targuid']
        # end handle [GC_REFINETRANS_CONFIRM_RET] message attrs, auto generate do not change
        pass


class GC_FASHION_RANDOM_COLOR_RET (Packet):
    def handle(self):
        # begin handle [GC_FASHION_RANDOM_COLOR_RET] message attrs, auto generate do not change
        self.person['SoltIndex'] = self['SoltIndex']
        self.person['FashionId'] = self['FashionId']
        self.person['ColorIndex'] = self['ColorIndex']
        # end handle [GC_FASHION_RANDOM_COLOR_RET] message attrs, auto generate do not change
        pass


class GC_AUCTION_RETBUY (Packet):
    def handle(self):
        # begin handle [GC_AUCTION_RETBUY] message attrs, auto generate do not change
        self.person['auctionguid'] = self['auctionguid']
        # end handle [GC_AUCTION_RETBUY] message attrs, auto generate do not change
        pass


class GC_MERCENARY_EMPLOYLIST (Packet):
    def handle(self):
        # begin handle [GC_MERCENARY_EMPLOYLIST] message attrs, auto generate do not change
        # end handle [GC_MERCENARY_EMPLOYLIST] message attrs, auto generate do not change
        pass


class CG_SEND_FLOWER (Packet):
    pass


class CG_ASK_MERGE_INSCRP0TION (Packet):
    pass


class CG_REQ_ARMY_CHANGE_RTROLE_NOTICE_LEADER (Packet):
    pass


class GC_RECHARGESCORESHOP_SYNC (Packet):
    def handle(self):
        # begin handle [GC_RECHARGESCORESHOP_SYNC] message attrs, auto generate do not change
        self.person['GoodsIndex'] = self['GoodsIndex']
        self.person['ItemId'] = self['ItemId']
        self.person['BuyVipLevel'] = self['BuyVipLevel']
        self.person['BuyAmt'] = self['BuyAmt']
        self.person['Price'] = self['Price']
        self.person['Discount'] = self['Discount']
        self.person['MaxCount'] = self['MaxCount']
        self.person['BuyCount'] = self['BuyCount']
        self.person['ShowSort'] = self['ShowSort']
        self.person['IsShowInMainPage'] = self['IsShowInMainPage']
        self.person['BadgeBuyLimit'] = self['BadgeBuyLimit']
        self.person['BadgeHotSell'] = self['BadgeHotSell']
        self.person['BadgeTimeLimit'] = self['BadgeTimeLimit']
        self.person['SellStartTime'] = self['SellStartTime']
        self.person['SellEndTime'] = self['SellEndTime']
        self.person['IsBuySucceed'] = self['IsBuySucceed']
        self.person['BadgeDayBuyLimit'] = self['BadgeDayBuyLimit']
        self.person['PageId'] = self['PageId']
        self.person['RechargeScoreShopStartTime'] = self['RechargeScoreShopStartTime']
        self.person['RechargeScoreShopEndTime'] = self['RechargeScoreShopEndTime']
        # end handle [GC_RECHARGESCORESHOP_SYNC] message attrs, auto generate do not change
        pass


class GC_SYNC_SCROLL_EXCHANGE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SCROLL_EXCHANGE_DATA] message attrs, auto generate do not change
        self.person['ConfigList'] = self['ConfigList']
        self.person['ExchangedItemList'] = self['ExchangedItemList']
        self.person['ExchangedItemNumList'] = self['ExchangedItemNumList']
        self.person['PreTimeList'] = self['PreTimeList']
        self.person['StartTimeList'] = self['StartTimeList']
        self.person['EndTimeList'] = self['EndTimeList']
        self.person['IsNewVersion'] = self['IsNewVersion']
        # end handle [GC_SYNC_SCROLL_EXCHANGE_DATA] message attrs, auto generate do not change
        pass


class CG_HOME_PRODUCE_OPERA (Packet):
    pass


class GC_SWORDTEAM_RET_OTHERINFO (Packet):
    def handle(self):
        # begin handle [GC_SWORDTEAM_RET_OTHERINFO] message attrs, auto generate do not change
        self.person['swordteamGuid'] = self['swordteamGuid']
        self.person['swordteamName'] = self['swordteamName']
        self.person['swordteamChiefGuid'] = self['swordteamChiefGuid']
        self.person['creatDay'] = self['creatDay']
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberVIP'] = self['memberVIP']
        self.person['memberProf'] = self['memberProf']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberLastLogout'] = self['memberLastLogout']
        self.person['memberState'] = self['memberState']
        self.person['memberJob'] = self['memberJob']
        self.person['combatval'] = self['combatval']
        self.person['BodyId'] = self['BodyId']
        self.person['FaceId'] = self['FaceId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairId'] = self['HairId']
        self.person['swordteamScore'] = self['swordteamScore']
        self.person['nGroup'] = self['nGroup']
        self.person['nPlaceInGroup'] = self['nPlaceInGroup']
        self.person['WeaponPolishVisual'] = self['WeaponPolishVisual']
        self.person['BodyColorEffectVisual'] = self['BodyColorEffectVisual']
        self.person['hairColorIndex'] = self['hairColorIndex']
        self.person['BodyColorVisual'] = self['BodyColorVisual']
        self.person['BodyFashionId'] = self['BodyFashionId']
        self.person['BodyColorIndex'] = self['BodyColorIndex']
        self.person['HairFashionId'] = self['HairFashionId']
        self.person['WeaponFashionId'] = self['WeaponFashionId']
        self.person['WeaponColorIndex'] = self['WeaponColorIndex']
        self.person['rolenierenlist'] = self['rolenierenlist']
        self.person['UseBodyFreeDyeSlotIds'] = self['UseBodyFreeDyeSlotIds']
        self.person['UseHairFreeDyeSlotIds'] = self['UseHairFreeDyeSlotIds']
        self.person['BodyFreeDyeColorInfos'] = self['BodyFreeDyeColorInfos']
        self.person['HairFreeDyeColorInfos'] = self['HairFreeDyeColorInfos']
        self.person['BackFashionId'] = self['BackFashionId']
        self.person['BackColorIndex'] = self['BackColorIndex']
        # end handle [GC_SWORDTEAM_RET_OTHERINFO] message attrs, auto generate do not change
        pass


class GC_YINZHEN_LEVELUP (Packet):
    def handle(self):
        # begin handle [GC_YINZHEN_LEVELUP] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        # end handle [GC_YINZHEN_LEVELUP] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_CREATE (Packet):
    pass


class GC_SWORDTEAM_JOIN (Packet):
    def handle(self):
        # begin handle [GC_SWORDTEAM_JOIN] message attrs, auto generate do not change
        self.person['swordteamGuid'] = self['swordteamGuid']
        # end handle [GC_SWORDTEAM_JOIN] message attrs, auto generate do not change
        pass


class GC_DOMAINWAR_DECLAREINFO (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_DECLAREINFO] message attrs, auto generate do not change
        self.person['declareInfo'] = self['declareInfo']
        self.person['clientVersion'] = self['clientVersion']
        # end handle [GC_DOMAINWAR_DECLAREINFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SHEDAISAIMA_RET_PLAYERAPPLYMATCH] message attrs, auto generate do not change
        self.person['playerlist'] = self['playerlist']
        # end handle [GC_SHEDAISAIMA_RET_PLAYERAPPLYMATCH] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILDCONVOY_FILL (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILDCONVOY_FILL] message attrs, auto generate do not change
        self.person['memberGuid'] = self['memberGuid']
        self.person['fillId'] = self['fillId']
        self.person['randomCount'] = self['randomCount']
        self.person['leftTime'] = self['leftTime']
        self.person['pathId'] = self['pathId']
        self.person['socialAddition'] = self['socialAddition']
        self.person['hasRewardCount'] = self['hasRewardCount']
        self.person['comfirmState'] = self['comfirmState']
        self.person['syncOp'] = self['syncOp']
        self.person['guildmoney'] = self['guildmoney']
        self.person['count'] = self['count']
        # end handle [GC_SYNC_GUILDCONVOY_FILL] message attrs, auto generate do not change
        pass


class GC_JUBAOPLAYER_RET (Packet):
    def handle(self):
        # begin handle [GC_JUBAOPLAYER_RET] message attrs, auto generate do not change
        # end handle [GC_JUBAOPLAYER_RET] message attrs, auto generate do not change
        pass


class CG_GUILD_SEND_GROUP_MSG (Packet):
    pass


class GC_RET_RELATFRIEND_SEND_GIFT (Packet):
    def handle(self):
        # begin handle [GC_RET_RELATFRIEND_SEND_GIFT] message attrs, auto generate do not change
        self.person['account'] = self['account']
        # end handle [GC_RET_RELATFRIEND_SEND_GIFT] message attrs, auto generate do not change
        pass


class GC_CHALLENGE_HISTORY (Packet):
    def handle(self):
        # begin handle [GC_CHALLENGE_HISTORY] message attrs, auto generate do not change
        self.person['playerGuid'] = self['playerGuid']
        self.person['name'] = self['name']
        self.person['isLose'] = self['isLose']
        self.person['occurTime'] = self['occurTime']
        self.person['isActive'] = self['isActive']
        self.person['rankPos'] = self['rankPos']
        self.person['combatNum'] = self['combatNum']
        self.person['level'] = self['level']
        self.person['profession'] = self['profession']
        self.person['selflevel'] = self['selflevel']
        self.person['selfcombatNum'] = self['selfcombatNum']
        self.person['selfRankPosChangeNum'] = self['selfRankPosChangeNum']
        self.person['sex'] = self['sex']
        self.person['customHeadPic'] = self['customHeadPic']
        # end handle [GC_CHALLENGE_HISTORY] message attrs, auto generate do not change
        pass


class CG_CHANGE_TO_NEXT_RUBKI_CUBE (Packet):
    pass


class CG_SWORDTEAM_KICK (Packet):
    pass


class GC_DAMAGEBOARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_DAMAGEBOARD_INFO] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['type'] = self['type']
        self.person['value'] = self['value']
        self.person['addanimstate'] = self['addanimstate']
        self.person['convoDamageType'] = self['convoDamageType']
        self.person['convoUsePlayerGuid'] = self['convoUsePlayerGuid']
        # end handle [GC_DAMAGEBOARD_INFO] message attrs, auto generate do not change
        pass


class GC_COMPOUND_GEM_RET (Packet):
    def handle(self):
        # begin handle [GC_COMPOUND_GEM_RET] message attrs, auto generate do not change
        self.person['operateType'] = self['operateType']
        self.person['shopConsumeIds'] = self['shopConsumeIds']
        self.person['shopConsumeNums'] = self['shopConsumeNums']
        # end handle [GC_COMPOUND_GEM_RET] message attrs, auto generate do not change
        pass


class GC_PLAY_BULLET_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_PLAY_BULLET_EFFECT] message attrs, auto generate do not change
        self.person['SenderObjID'] = self['SenderObjID']
        self.person['EffectID'] = self['EffectID']
        self.person['BulletSpeed'] = self['BulletSpeed']
        self.person['isBulletReverse'] = self['isBulletReverse']
        self.person['ArriveEffectID'] = self['ArriveEffectID']
        self.person['TargetType'] = self['TargetType']
        self.person['TargetObjID'] = self['TargetObjID']
        self.person['PosX'] = self['PosX']
        self.person['PosY'] = self['PosY']
        self.person['PosZ'] = self['PosZ']
        self.person['ArriveColorID'] = self['ArriveColorID']
        # end handle [GC_PLAY_BULLET_EFFECT] message attrs, auto generate do not change
        pass


class CG_BATTLEFIELD_CANCEL_SIGNUP (Packet):
    pass


class CG_FLY_LAND (Packet):
    pass


class GC_PUSH_RECOMMOND_FRIEND_LIST (Packet):
    def handle(self):
        # begin handle [GC_PUSH_RECOMMOND_FRIEND_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['SpaceSex'] = self['SpaceSex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['recommondtype'] = self['recommondtype']
        self.person['RealSex'] = self['RealSex']
        # end handle [GC_PUSH_RECOMMOND_FRIEND_LIST] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_LEAVE (Packet):
    pass


class CG_REQ_COMBATVALUE (Packet):
    pass


class CG_MAIL_OPERATION (Packet):
    pass


class GC_COPYSCENE_LEFTIME (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_LEFTIME] message attrs, auto generate do not change
        self.person['ntime'] = self['ntime']
        self.person['nLayer'] = self['nLayer']
        # end handle [GC_COPYSCENE_LEFTIME] message attrs, auto generate do not change
        pass


class CG_EQUIP_LEVELUP (Packet):
    pass


class CG_NOTIFY_SHARE_EVENT (Packet):
    pass


class GC_SET_SELECT_PET (Packet):
    def handle(self):
        # begin handle [GC_SET_SELECT_PET] message attrs, auto generate do not change
        self.person['petGuid'] = self['petGuid']
        # end handle [GC_SET_SELECT_PET] message attrs, auto generate do not change
        pass


class GC_FLY_AIRCRAFT_MARK_RET (Packet):
    def handle(self):
        # begin handle [GC_FLY_AIRCRAFT_MARK_RET] message attrs, auto generate do not change
        self.person['AircraftID'] = self['AircraftID']
        self.person['Ret'] = self['Ret']
        # end handle [GC_FLY_AIRCRAFT_MARK_RET] message attrs, auto generate do not change
        pass


class CG_REQ_CANCEL_CUTOF_MENTOR (Packet):
    pass


class GC_MERGE_INSCRP0TION_RESEPONSE (Packet):
    def handle(self):
        # begin handle [GC_MERGE_INSCRP0TION_RESEPONSE] message attrs, auto generate do not change
        self.person['sucessItem'] = self['sucessItem']
        # end handle [GC_MERGE_INSCRP0TION_RESEPONSE] message attrs, auto generate do not change
        pass


class CG_REQ_GUILDMONSTER_DANGERFISH (Packet):
    pass


class GC_BATTLEFIELD_PLAYER_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_PLAYER_UPDATE] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['KillNum'] = self['KillNum']
        self.person['FlagNum'] = self['FlagNum']
        self.person['Score'] = self['Score']
        # end handle [GC_BATTLEFIELD_PLAYER_UPDATE] message attrs, auto generate do not change
        pass


class GC_SYNC_COUNTRESETINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COUNTRESETINFO] message attrs, auto generate do not change
        self.person['nResetID'] = self['nResetID']
        self.person['nResetCount'] = self['nResetCount']
        self.person['nResetExtraCount'] = self['nResetExtraCount']
        self.person['nResetUsedCount'] = self['nResetUsedCount']
        # end handle [GC_SYNC_COUNTRESETINFO] message attrs, auto generate do not change
        pass


class CG_ASK_PASSPORT_REWARD (Packet):
    pass


class GC_UPDATE_GUILD_BINGGROUP_STATE (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_GUILD_BINGGROUP_STATE] message attrs, auto generate do not change
        self.person['guildBindGroupState'] = self['guildBindGroupState']
        self.person['guildBindGroupId'] = self['guildBindGroupId']
        # end handle [GC_UPDATE_GUILD_BINGGROUP_STATE] message attrs, auto generate do not change
        pass


class CG_GUILD_REQ_INFO (Packet):
    pass


class GC_AUTO_COMMIT_GUILD_MONSTER_ITEM (Packet):
    def handle(self):
        # begin handle [GC_AUTO_COMMIT_GUILD_MONSTER_ITEM] message attrs, auto generate do not change
        # end handle [GC_AUTO_COMMIT_GUILD_MONSTER_ITEM] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_JOIN (Packet):
    pass


class GC_FINDPLAYER (Packet):
    def handle(self):
        # begin handle [GC_FINDPLAYER] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['RealSex'] = self['RealSex']
        self.person['Birthday'] = self['Birthday']
        self.person['Address'] = self['Address']
        self.person['Ret'] = self['Ret']
        self.person['SpaceSex'] = self['SpaceSex']
        self.person['headPicname'] = self['headPicname']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrame'] = self['PhotoFrame']
        # end handle [GC_FINDPLAYER] message attrs, auto generate do not change
        pass


class CG_ASK_USE_SWEEP_ITEM (Packet):
    pass


class CG_REQ_SYNC_HOME (Packet):
    pass


class CG_GUILD_KICK (Packet):
    pass


class GC_GUILD_BUILDING_CD (Packet):
    def handle(self):
        # begin handle [GC_GUILD_BUILDING_CD] message attrs, auto generate do not change
        self.person['buildingCD'] = self['buildingCD']
        self.person['buildingType'] = self['buildingType']
        self.person['guildMoney'] = self['guildMoney']
        # end handle [GC_GUILD_BUILDING_CD] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_INVITE_TITLE (Packet):
    pass


class CG_GUILD_REQ_THIEF_FIGHT (Packet):
    pass


class GC_RES_AUCTION_FAVORITE_LOOK (Packet):
    def handle(self):
        # begin handle [GC_RES_AUCTION_FAVORITE_LOOK] message attrs, auto generate do not change
        self.person['auctionitems'] = self['auctionitems']
        self.person['type'] = self['type']
        # end handle [GC_RES_AUCTION_FAVORITE_LOOK] message attrs, auto generate do not change
        pass


class CG_REQ_GUILDCONVOY_MAP_POS (Packet):
    pass


class CG_GUILD_REQ_LEVELUP (Packet):
    pass


class GC_SYN_DIRTY_MENTOR_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYN_DIRTY_MENTOR_INFO] message attrs, auto generate do not change
        self.person['dirtyMentorInfo'] = self['dirtyMentorInfo']
        self.person['teachingLevel'] = self['teachingLevel']
        self.person['teachingExp'] = self['teachingExp']
        self.person['teachingPoint'] = self['teachingPoint']
        self.person['lastPulisTime'] = self['lastPulisTime']
        # end handle [GC_SYN_DIRTY_MENTOR_INFO] message attrs, auto generate do not change
        pass


class CG_DOMAINWAR_REQ_LINEINFO (Packet):
    pass


class GC_SYNC_PHONE_BIND_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PHONE_BIND_DATA] message attrs, auto generate do not change
        self.person['bIsBindPhone'] = self['bIsBindPhone']
        # end handle [GC_SYNC_PHONE_BIND_DATA] message attrs, auto generate do not change
        pass


class CG_EQUIPMIRROR_QUICK_COMPOUND (Packet):
    pass


class GC_EMOTION_LOCKINFO (Packet):
    def handle(self):
        # begin handle [GC_EMOTION_LOCKINFO] message attrs, auto generate do not change
        self.person['unlock'] = self['unlock']
        self.person['emotionlockflg'] = self['emotionlockflg']
        # end handle [GC_EMOTION_LOCKINFO] message attrs, auto generate do not change
        pass


class GC_STALL_RETSELLLIST (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETSELLLIST] message attrs, auto generate do not change
        self.person['stallitems'] = self['stallitems']
        # end handle [GC_STALL_RETSELLLIST] message attrs, auto generate do not change
        pass


class GC_CUTSCENE_PLAY (Packet):
    def handle(self):
        # begin handle [GC_CUTSCENE_PLAY] message attrs, auto generate do not change
        self.person['cutSceneID'] = self['cutSceneID']
        # end handle [GC_CUTSCENE_PLAY] message attrs, auto generate do not change
        pass


class CG_STALL_BUY (Packet):
    pass


class GC_PGL_SYNC_TEAM_MEM_INFO (Packet):
    def handle(self):
        # begin handle [GC_PGL_SYNC_TEAM_MEM_INFO] message attrs, auto generate do not change
        self.person['teamId'] = self['teamId']
        self.person['memGuid'] = self['memGuid']
        self.person['memMmr'] = self['memMmr']
        self.person['memRemainTimes'] = self['memRemainTimes']
        # end handle [GC_PGL_SYNC_TEAM_MEM_INFO] message attrs, auto generate do not change
        pass


class GC_RET_TEAMMEMBER_APPLY_LEADER (Packet):
    def handle(self):
        # begin handle [GC_RET_TEAMMEMBER_APPLY_LEADER] message attrs, auto generate do not change
        self.person['playerName'] = self['playerName']
        self.person['nAgreeNum'] = self['nAgreeNum']
        self.person['nDisAgreeNum'] = self['nDisAgreeNum']
        self.person['nLeftTime'] = self['nLeftTime']
        self.person['nTotalNum'] = self['nTotalNum']
        # end handle [GC_RET_TEAMMEMBER_APPLY_LEADER] message attrs, auto generate do not change
        pass


class CG_OPEN_RUBKI_CUBE_PLAY (Packet):
    pass


class GC_SYC_FRIEND_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYC_FRIEND_INFO] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['BodyId'] = self['BodyId']
        self.person['HeadId'] = self['HeadId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        # end handle [GC_SYC_FRIEND_INFO] message attrs, auto generate do not change
        pass


class CG_BEGIN_AIRBUS (Packet):
    pass


class CG_PUT_COLOR_ITEM_STORAGE (Packet):
    pass


class GC_WEDDING_SYNC_INFO (Packet):
    def handle(self):
        # begin handle [GC_WEDDING_SYNC_INFO] message attrs, auto generate do not change
        self.person['weddingType'] = self['weddingType']
        self.person['weddingProcess'] = self['weddingProcess']
        self.person['weddingTotalBless'] = self['weddingTotalBless']
        self.person['weddingGuestBless'] = self['weddingGuestBless']
        self.person['weddingLeftTime'] = self['weddingLeftTime']
        self.person['groomGuid'] = self['groomGuid']
        self.person['groomName'] = self['groomName']
        self.person['brideGuid'] = self['brideGuid']
        self.person['brideName'] = self['brideName']
        self.person['customBoatIdx'] = self['customBoatIdx']
        self.person['bridgeBuildProcess'] = self['bridgeBuildProcess']
        self.person['bridgeMaxProcess'] = self['bridgeMaxProcess']
        self.person['weddingActId'] = self['weddingActId']
        self.person['weddingActEndTime'] = self['weddingActEndTime']
        # end handle [GC_WEDDING_SYNC_INFO] message attrs, auto generate do not change
        pass


class GC_BWPPCOMBAT_RESULT (Packet):
    def handle(self):
        # begin handle [GC_BWPPCOMBAT_RESULT] message attrs, auto generate do not change
        self.person['isWin'] = self['isWin']
        self.person['nScore'] = self['nScore']
        self.person['nAdd'] = self['nAdd']
        self.person['nExp'] = self['nExp']
        self.person['nHonour'] = self['nHonour']
        self.person['nSilver'] = self['nSilver']
        # end handle [GC_BWPPCOMBAT_RESULT] message attrs, auto generate do not change
        pass


class CG_REQUEST_ARMYLEADER_POSITION (Packet):
    pass


class CG_ARTIFACT_PROVE_REWARD (Packet):
    pass


class GC_RET_PK_KILLINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_PK_KILLINFO] message attrs, auto generate do not change
        self.person['isBeKilled'] = self['isBeKilled']
        self.person['targetGuid'] = self['targetGuid']
        self.person['targetName'] = self['targetName']
        self.person['killTime'] = self['killTime']
        self.person['sceneclassId'] = self['sceneclassId']
        self.person['sceneinstId'] = self['sceneinstId']
        self.person['targetGuildName'] = self['targetGuildName']
        self.person['Lev'] = self['Lev']
        self.person['Pro'] = self['Pro']
        self.person['SexType'] = self['SexType']
        self.person['isGPW'] = self['isGPW']
        self.person['costSoul'] = self['costSoul']
        self.person['CostType'] = self['CostType']
        self.person['killType'] = self['killType']
        # end handle [GC_RET_PK_KILLINFO] message attrs, auto generate do not change
        pass


class CG_SYSTEMTRADE_BUY (Packet):
    pass


class GC_RES_MARRAY_RECURIT (Packet):
    def handle(self):
        # begin handle [GC_RES_MARRAY_RECURIT] message attrs, auto generate do not change
        # end handle [GC_RES_MARRAY_RECURIT] message attrs, auto generate do not change
        pass


class GC_EQUIPMIRROR_RET_RESULT (Packet):
    def handle(self):
        # begin handle [GC_EQUIPMIRROR_RET_RESULT] message attrs, auto generate do not change
        self.person['resultItem'] = self['resultItem']
        # end handle [GC_EQUIPMIRROR_RET_RESULT] message attrs, auto generate do not change
        pass


class GC_UPDATE_ANIMATION_STATE (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_ANIMATION_STATE] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['AnimationState'] = self['AnimationState']
        self.person['SourceSkillId'] = self['SourceSkillId']
        self.person['SourceObjId'] = self['SourceObjId']
        # end handle [GC_UPDATE_ANIMATION_STATE] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_MARRIAGE_SYNC] message attrs, auto generate do not change
        self.person['loverguid'] = self['loverguid']
        self.person['lovername'] = self['lovername']
        self.person['marrytime'] = self['marrytime']
        self.person['marryindex'] = self['marryindex']
        self.person['marrydaily'] = self['marrydaily']
        self.person['marrydailyfinish'] = self['marrydailyfinish']
        self.person['chineseweddingtime'] = self['chineseweddingtime']
        self.person['loverNieRenValue'] = self['loverNieRenValue']
        self.person['loverProf'] = self['loverProf']
        self.person['marryAdvancedMissionIndex'] = self['marryAdvancedMissionIndex']
        self.person['marryAdvancedMissionStatus'] = self['marryAdvancedMissionStatus']
        self.person['loverhomeguid'] = self['loverhomeguid']
        # end handle [GC_MARRIAGE_SYNC] message attrs, auto generate do not change
        pass


class GC_ANSWER_WORLD_BOSS_STATE (Packet):
    def handle(self):
        # begin handle [GC_ANSWER_WORLD_BOSS_STATE] message attrs, auto generate do not change
        self.person['NpcServerID'] = self['NpcServerID']
        self.person['BossState'] = self['BossState']
        self.person['MemberBossFight'] = self['MemberBossFight']
        # end handle [GC_ANSWER_WORLD_BOSS_STATE] message attrs, auto generate do not change
        pass


class CG_USE_CHILDRENSDAY_BALLON (Packet):
    pass


class GC_FASHION_PAIR_SAVE_RET (Packet):
    def handle(self):
        # begin handle [GC_FASHION_PAIR_SAVE_RET] message attrs, auto generate do not change
        self.person['FashionPairList'] = self['FashionPairList']
        # end handle [GC_FASHION_PAIR_SAVE_RET] message attrs, auto generate do not change
        pass


class GC_REQ_APPRENTICE_CONFIGM_TEACHER (Packet):
    def handle(self):
        # begin handle [GC_REQ_APPRENTICE_CONFIGM_TEACHER] message attrs, auto generate do not change
        self.person['masterGuid'] = self['masterGuid']
        self.person['masterName'] = self['masterName']
        # end handle [GC_REQ_APPRENTICE_CONFIGM_TEACHER] message attrs, auto generate do not change
        pass


class GC_STALL_RETSEARCH (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETSEARCH] message attrs, auto generate do not change
        self.person['ispublic'] = self['ispublic']
        self.person['curpage'] = self['curpage']
        self.person['stallitems'] = self['stallitems']
        self.person['maxcount'] = self['maxcount']
        self.person['order'] = self['order']
        # end handle [GC_STALL_RETSEARCH] message attrs, auto generate do not change
        pass


class CG_REQ_GUILD_THIEF_ISACTIVE (Packet):
    pass


class GC_SHOW_KILLINFO_VIEW (Packet):
    def handle(self):
        # begin handle [GC_SHOW_KILLINFO_VIEW] message attrs, auto generate do not change
        self.person['IsFriend'] = self['IsFriend']
        self.person['KillerObjId'] = self['KillerObjId']
        self.person['KilledObjId'] = self['KilledObjId']
        self.person['szKillerName'] = self['szKillerName']
        self.person['szKilledName'] = self['szKilledName']
        self.person['killerProf'] = self['killerProf']
        self.person['killedProf'] = self['killedProf']
        self.person['killerSex'] = self['killerSex']
        self.person['killedSex'] = self['killedSex']
        # end handle [GC_SHOW_KILLINFO_VIEW] message attrs, auto generate do not change
        pass


class CG_ACCLOGIN_GETAWARD (Packet):
    pass


class CG_GUILD_REQ_ENTER_GUILD_WILD (Packet):
    pass


class CG_MERCENARY_LIST_REQ (Packet):
    pass


class GC_MARRIAGE_PROCESS (Packet):
    def handle(self):
        # begin handle [GC_MARRIAGE_PROCESS] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['targetguid'] = self['targetguid']
        self.person['targetname'] = self['targetname']
        # end handle [GC_MARRIAGE_PROCESS] message attrs, auto generate do not change
        pass


class CG_REQ_MATCH_OP (Packet):
    pass


class GC_NOTICE_CATCHGHOST_NEED_ASSEMBLE (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_CATCHGHOST_NEED_ASSEMBLE] message attrs, auto generate do not change
        # end handle [GC_NOTICE_CATCHGHOST_NEED_ASSEMBLE] message attrs, auto generate do not change
        pass


class GC_SWORDTEAM_CREATE (Packet):
    def handle(self):
        # begin handle [GC_SWORDTEAM_CREATE] message attrs, auto generate do not change
        self.person['swordteamGuid'] = self['swordteamGuid']
        self.person['swordteamName'] = self['swordteamName']
        self.person['showRecuitBox'] = self['showRecuitBox']
        # end handle [GC_SWORDTEAM_CREATE] message attrs, auto generate do not change
        pass


class CG_REQ_ARMY_INVITE (Packet):
    pass


class CG_REQ_EXCHANGE_CHOOSEREWARDBOX (Packet):
    pass


class CG_SWORDTEAM_INVITE (Packet):
    pass


class GC_SYNC_ADVENTURE_EVENT_HISTORY (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ADVENTURE_EVENT_HISTORY] message attrs, auto generate do not change
        self.person['eventId'] = self['eventId']
        self.person['time'] = self['time']
        self.person['state'] = self['state']
        # end handle [GC_SYNC_ADVENTURE_EVENT_HISTORY] message attrs, auto generate do not change
        pass


class GC_TIANSHU_BACKPACK_INFO (Packet):
    def handle(self):
        # begin handle [GC_TIANSHU_BACKPACK_INFO] message attrs, auto generate do not change
        self.person['tianshuDataId'] = self['tianshuDataId']
        self.person['tianshuCount'] = self['tianshuCount']
        self.person['bind'] = self['bind']
        self.person['nextTradeTime'] = self['nextTradeTime']
        self.person['tianshuDebris'] = self['tianshuDebris']
        # end handle [GC_TIANSHU_BACKPACK_INFO] message attrs, auto generate do not change
        pass


class CG_DELRECENTCONTACTLIST (Packet):
    pass


class GC_LOUDSPEAKER_USE (Packet):
    def handle(self):
        # begin handle [GC_LOUDSPEAKER_USE] message attrs, auto generate do not change
        # end handle [GC_LOUDSPEAKER_USE] message attrs, auto generate do not change
        pass


class GC_ITEMCOMPENSATE_SYNCINFO (Packet):
    def handle(self):
        # begin handle [GC_ITEMCOMPENSATE_SYNCINFO] message attrs, auto generate do not change
        self.person['bGetItem1'] = self['bGetItem1']
        self.person['bGetItem2'] = self['bGetItem2']
        self.person['totalDay'] = self['totalDay']
        self.person['itemFree1'] = self['itemFree1']
        self.person['itemFree2'] = self['itemFree2']
        self.person['itemPay1'] = self['itemPay1']
        self.person['itemPay2'] = self['itemPay2']
        self.person['itemCost1'] = self['itemCost1']
        self.person['itemCost2'] = self['itemCost2']
        # end handle [GC_ITEMCOMPENSATE_SYNCINFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_PGL_TEAM_REQ_FAILED] message attrs, auto generate do not change
        self.person['faile_type'] = self['faile_type']
        self.person['sArg'] = self['sArg']
        # end handle [GC_PGL_TEAM_REQ_FAILED] message attrs, auto generate do not change
        pass


class GC_SYNC_FORTUNE_EQUIP (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FORTUNE_EQUIP] message attrs, auto generate do not change
        self.person['packIndex'] = self['packIndex']
        self.person['index'] = self['index']
        self.person['dataId'] = self['dataId']
        self.person['level'] = self['level']
        self.person['exp'] = self['exp']
        # end handle [GC_SYNC_FORTUNE_EQUIP] message attrs, auto generate do not change
        pass


class CG_ITEM_MERGE (Packet):
    pass


class CG_ASK_SYN_FAIRY_PACK (Packet):
    pass


class CG_SKILL_USE (Packet):
    pass


class GC_ASK_PAYACT_RET (Packet):
    def handle(self):
        # begin handle [GC_ASK_PAYACT_RET] message attrs, auto generate do not change
        self.person['prizeType'] = self['prizeType']
        self.person['prizeParam1'] = self['prizeParam1']
        self.person['prizeParam2'] = self['prizeParam2']
        self.person['result'] = self['result']
        # end handle [GC_ASK_PAYACT_RET] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_NOTICE] message attrs, auto generate do not change
        self.person['notice'] = self['notice']
        self.person['filterRepeat'] = self['filterRepeat']
        # end handle [GC_NOTICE] message attrs, auto generate do not change
        pass


class CG_UNBIND_GUILDGROUP (Packet):
    pass


class GC_SYNC_WXSUPERR_PRIVILEGE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_WXSUPERR_PRIVILEGE] message attrs, auto generate do not change
        self.person['m_nIsWXSuperR'] = self['m_nIsWXSuperR']
        # end handle [GC_SYNC_WXSUPERR_PRIVILEGE] message attrs, auto generate do not change
        pass


class CG_ASK_FIREWORKS_AWARD (Packet):
    pass


class CG_ASKOTHEROLE_VIEWINFO (Packet):
    pass


class GC_TOWER_INFO (Packet):
    def handle(self):
        # begin handle [GC_TOWER_INFO] message attrs, auto generate do not change
        self.person['CurFloor'] = self['CurFloor']
        self.person['FightLeftCount'] = self['FightLeftCount']
        self.person['SweepLeftCount'] = self['SweepLeftCount']
        self.person['TowerShopItemBuyCount'] = self['TowerShopItemBuyCount']
        self.person['CurSweepFloor'] = self['CurSweepFloor']
        self.person['LastFloorTime'] = self['LastFloorTime']
        # end handle [GC_TOWER_INFO] message attrs, auto generate do not change
        pass


class CG_BATTLEFIELD_LEAVE (Packet):
    pass


class GC_TRIGGER (Packet):
    def handle(self):
        # begin handle [GC_TRIGGER] message attrs, auto generate do not change
        self.person['trigger_type'] = self['trigger_type']
        self.person['trigger_id'] = self['trigger_id']
        # end handle [GC_TRIGGER] message attrs, auto generate do not change
        pass


class GC_PRESTIGE_RET_GETREWARD (Packet):
    def handle(self):
        # begin handle [GC_PRESTIGE_RET_GETREWARD] message attrs, auto generate do not change
        self.person['ForceId'] = self['ForceId']
        self.person['RelationRewardId'] = self['RelationRewardId']
        self.person['bSuccess'] = self['bSuccess']
        # end handle [GC_PRESTIGE_RET_GETREWARD] message attrs, auto generate do not change
        pass


class GC_ASURA_RESULT_UI (Packet):
    def handle(self):
        # begin handle [GC_ASURA_RESULT_UI] message attrs, auto generate do not change
        self.person['floorId'] = self['floorId']
        self.person['result'] = self['result']
        self.person['playerCount'] = self['playerCount']
        self.person['winnerCount'] = self['winnerCount']
        self.person['boxCollected'] = self['boxCollected']
        self.person['gainExp'] = self['gainExp']
        self.person['gainSkillSoul'] = self['gainSkillSoul']
        self.person['gainSilver'] = self['gainSilver']
        self.person['time'] = self['time']
        self.person['uiCloseCountDown'] = self['uiCloseCountDown']
        self.person['itemId'] = self['itemId']
        self.person['itemCount'] = self['itemCount']
        self.person['itemBind'] = self['itemBind']
        # end handle [GC_ASURA_RESULT_UI] message attrs, auto generate do not change
        pass


class GC_CAMERA_COLORMASK_OPERATE (Packet):
    def handle(self):
        # begin handle [GC_CAMERA_COLORMASK_OPERATE] message attrs, auto generate do not change
        self.person['OPERATETYPE'] = self['OPERATETYPE']
        self.person['nParam'] = self['nParam']
        # end handle [GC_CAMERA_COLORMASK_OPERATE] message attrs, auto generate do not change
        pass


class CG_REQ_FORTURE_EQUIP_GENERATE (Packet):
    pass


class CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_TYPE (Packet):
    pass


class GC_SYNC_HOME_ATTRIBUTE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HOME_ATTRIBUTE] message attrs, auto generate do not change
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['Honor'] = self['Honor']
        self.person['Geomancy'] = self['Geomancy']
        self.person['PlantValueLimit'] = self['PlantValueLimit']
        self.person['TameValueLimit'] = self['TameValueLimit']
        self.person['MiningValueLimit'] = self['MiningValueLimit']
        self.person['HonorLimit'] = self['HonorLimit']
        self.person['GeomancyLimit'] = self['GeomancyLimit']
        self.person['Atmosphere'] = self['Atmosphere']
        self.person['SpouseHonor'] = self['SpouseHonor']
        self.person['SpouseGeomancy'] = self['SpouseGeomancy']
        # end handle [GC_SYNC_HOME_ATTRIBUTE] message attrs, auto generate do not change
        pass


class CG_GETFLYMISREWARD (Packet):
    pass


class GC_BWPVPFINAL_UPDATEFINALSTATE (Packet):
    def handle(self):
        # begin handle [GC_BWPVPFINAL_UPDATEFINALSTATE] message attrs, auto generate do not change
        self.person['isPvPFinal'] = self['isPvPFinal']
        # end handle [GC_BWPVPFINAL_UPDATEFINALSTATE] message attrs, auto generate do not change
        pass


class GC_SWORDTEAM_RET_LIST (Packet):
    def handle(self):
        # begin handle [GC_SWORDTEAM_RET_LIST] message attrs, auto generate do not change
        self.person['preserveswordteamGuid'] = self['preserveswordteamGuid']
        self.person['swordteamGuid'] = self['swordteamGuid']
        self.person['swordteamName'] = self['swordteamName']
        self.person['swordteamChiefName'] = self['swordteamChiefName']
        self.person['swordteamMemberNum'] = self['swordteamMemberNum']
        self.person['swordteamCombat'] = self['swordteamCombat']
        self.person['openRecuit'] = self['openRecuit']
        self.person['recuitCombat'] = self['recuitCombat']
        self.person['needPros'] = self['needPros']
        # end handle [GC_SWORDTEAM_RET_LIST] message attrs, auto generate do not change
        pass


class GC_RET_APPOINT_OPEN_PLAYER_GZONE (Packet):
    def handle(self):
        # begin handle [GC_RET_APPOINT_OPEN_PLAYER_GZONE] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['openType'] = self['openType']
        self.person['roleId'] = self['roleId']
        self.person['openId'] = self['openId']
        self.person['platId'] = self['platId']
        self.person['areaId'] = self['areaId']
        self.person['partitionId'] = self['partitionId']
        # end handle [GC_RET_APPOINT_OPEN_PLAYER_GZONE] message attrs, auto generate do not change
        pass


class CG_ASK_COLLECT (Packet):
    pass


class GC_OPERATE_AIRWALL (Packet):
    def handle(self):
        # begin handle [GC_OPERATE_AIRWALL] message attrs, auto generate do not change
        self.person['operate_type'] = self['operate_type']
        self.person['air_wall_id'] = self['air_wall_id']
        # end handle [GC_OPERATE_AIRWALL] message attrs, auto generate do not change
        pass


class GC_START_AUTOCOMBAT (Packet):
    def handle(self):
        # begin handle [GC_START_AUTOCOMBAT] message attrs, auto generate do not change
        # end handle [GC_START_AUTOCOMBAT] message attrs, auto generate do not change
        pass


class GC_OPTUI (Packet):
    def handle(self):
        # begin handle [GC_OPTUI] message attrs, auto generate do not change
        self.person['nIndex'] = self['nIndex']
        self.person['optType'] = self['optType']
        self.person['param'] = self['param']
        # end handle [GC_OPTUI] message attrs, auto generate do not change
        pass


class GC_UI_NEWGUIDE (Packet):
    def handle(self):
        # begin handle [GC_UI_NEWGUIDE] message attrs, auto generate do not change
        self.person['guidType'] = self['guidType']
        # end handle [GC_UI_NEWGUIDE] message attrs, auto generate do not change
        pass


class GC_TEAM_TARGET (Packet):
    def handle(self):
        # begin handle [GC_TEAM_TARGET] message attrs, auto generate do not change
        self.person['teamID'] = self['teamID']
        self.person['targetId'] = self['targetId']
        self.person['minLevel'] = self['minLevel']
        self.person['maxLevel'] = self['maxLevel']
        self.person['armyID'] = self['armyID']
        # end handle [GC_TEAM_TARGET] message attrs, auto generate do not change
        pass


class CG_RELATFRIEND_SEND_GIFT (Packet):
    pass


class CG_ENTER_SCENE_OK (Packet):
    pass


class CG_COPYSCENE_NAVIGATION (Packet):
    pass


class GC_REBATE_RANKCONFIG (Packet):
    def handle(self):
        # begin handle [GC_REBATE_RANKCONFIG] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['open'] = self['open']
        self.person['begint'] = self['begint']
        self.person['endt'] = self['endt']
        self.person['showt'] = self['showt']
        self.person['rankh'] = self['rankh']
        self.person['rankl'] = self['rankl']
        self.person['ida'] = self['ida']
        self.person['numa'] = self['numa']
        self.person['idb'] = self['idb']
        self.person['numb'] = self['numb']
        self.person['idc'] = self['idc']
        self.person['numc'] = self['numc']
        # end handle [GC_REBATE_RANKCONFIG] message attrs, auto generate do not change
        pass


class CG_REQ_CHANGEPROFESSION (Packet):
    pass


class GC_GUILDCONVOY_GMCMD (Packet):
    def handle(self):
        # begin handle [GC_GUILDCONVOY_GMCMD] message attrs, auto generate do not change
        self.person['isgmopen'] = self['isgmopen']
        # end handle [GC_GUILDCONVOY_GMCMD] message attrs, auto generate do not change
        pass


class CG_GODWEAPON_COORDINATION (Packet):
    pass


class GC_CREATE_SKILL_ENTITY (Packet):
    def handle(self):
        # begin handle [GC_CREATE_SKILL_ENTITY] message attrs, auto generate do not change
        self.person['charBaseAttr'] = self['charBaseAttr']
        self.person['ownerID'] = self['ownerID']
        self.person['isBorn'] = self['isBorn']
        # end handle [GC_CREATE_SKILL_ENTITY] message attrs, auto generate do not change
        pass


class GC_BATTLEFIELD_GROUPSCORE_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_GROUPSCORE_UPDATE] message attrs, auto generate do not change
        self.person['GroupID'] = self['GroupID']
        self.person['GroupScore'] = self['GroupScore']
        # end handle [GC_BATTLEFIELD_GROUPSCORE_UPDATE] message attrs, auto generate do not change
        pass


class CG_ASK_JXGZAWARD (Packet):
    pass


class CG_FASHION_SHOW (Packet):
    pass


class GC_RES_UPDATE_AUCTION_ONE (Packet):
    def handle(self):
        # begin handle [GC_RES_UPDATE_AUCTION_ONE] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['item'] = self['item']
        # end handle [GC_RES_UPDATE_AUCTION_ONE] message attrs, auto generate do not change
        pass


class GC_BWPVPFINAL_MEMINFOINVIEW (Packet):
    def handle(self):
        # begin handle [GC_BWPVPFINAL_MEMINFOINVIEW] message attrs, auto generate do not change
        self.person['bwName'] = self['bwName']
        self.person['curRound'] = self['curRound']
        self.person['MemAObj'] = self['MemAObj']
        self.person['MemAName'] = self['MemAName']
        self.person['MemALev'] = self['MemALev']
        self.person['MemAPro'] = self['MemAPro']
        self.person['MemAMaxHP'] = self['MemAMaxHP']
        self.person['MemACurHp'] = self['MemACurHp']
        self.person['MemAVipLev'] = self['MemAVipLev']
        self.person['MemBObj'] = self['MemBObj']
        self.person['MemBName'] = self['MemBName']
        self.person['MemBLev'] = self['MemBLev']
        self.person['MemBPro'] = self['MemBPro']
        self.person['MemBMaxHP'] = self['MemBMaxHP']
        self.person['MemBCurHp'] = self['MemBCurHp']
        self.person['MemBVipLev'] = self['MemBVipLev']
        self.person['IsMemAWin'] = self['IsMemAWin']
        self.person['TeamAName'] = self['TeamAName']
        self.person['TeamBName'] = self['TeamBName']
        self.person['SwordTeamAGuid'] = self['SwordTeamAGuid']
        self.person['SwordTeamBGuid'] = self['SwordTeamBGuid']
        # end handle [GC_BWPVPFINAL_MEMINFOINVIEW] message attrs, auto generate do not change
        pass


class CG_SKILLZHUANJING_WASH (Packet):
    pass


class GC_CREATE_CUTSCENE_TRIGGER (Packet):
    def handle(self):
        # begin handle [GC_CREATE_CUTSCENE_TRIGGER] message attrs, auto generate do not change
        self.person['DynamicAreaId'] = self['DynamicAreaId']
        self.person['CutsceneId'] = self['CutsceneId']
        self.person['TriggerType'] = self['TriggerType']
        # end handle [GC_CREATE_CUTSCENE_TRIGGER] message attrs, auto generate do not change
        pass


class GC_SYNC_EQUIP_ENCHANTING_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_EQUIP_ENCHANTING_DATA] message attrs, auto generate do not change
        self.person['EnchantingData'] = self['EnchantingData']
        self.person['ResultData'] = self['ResultData']
        # end handle [GC_SYNC_EQUIP_ENCHANTING_DATA] message attrs, auto generate do not change
        pass


class GC_STOP_SOUND (Packet):
    def handle(self):
        # begin handle [GC_STOP_SOUND] message attrs, auto generate do not change
        self.person['SoundID'] = self['SoundID']
        # end handle [GC_STOP_SOUND] message attrs, auto generate do not change
        pass


class CG_ENTER_CATCHGHOST (Packet):
    pass


class GC_BROTHERHOOD_MY (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_MY] message attrs, auto generate do not change
        self.person['brotherhoodGuid'] = self['brotherhoodGuid']
        self.person['brotherhoodName'] = self['brotherhoodName']
        self.person['chiefGuid'] = self['chiefGuid']
        self.person['combatVal'] = self['combatVal']
        self.person['createDay'] = self['createDay']
        self.person['buffLevel'] = self['buffLevel']
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberProf'] = self['memberProf']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberState'] = self['memberState']
        self.person['memberPos'] = self['memberPos']
        self.person['memberCombatVal'] = self['memberCombatVal']
        self.person['memberSex'] = self['memberSex']
        self.person['memberTitle'] = self['memberTitle']
        self.person['applicantGuid'] = self['applicantGuid']
        self.person['applicantName'] = self['applicantName']
        self.person['applicantProf'] = self['applicantProf']
        self.person['applicantSex'] = self['applicantSex']
        self.person['applicantLevel'] = self['applicantLevel']
        self.person['memberCustomHeadPic'] = self['memberCustomHeadPic']
        self.person['memberPhotoFrameId'] = self['memberPhotoFrameId']
        self.person['memberWeeklyContribution'] = self['memberWeeklyContribution']
        self.person['memberTotalContribution'] = self['memberTotalContribution']
        self.person['brotherhoodLevel'] = self['brotherhoodLevel']
        self.person['loyaltyVal'] = self['loyaltyVal']
        self.person['weeklyloyaltyVal'] = self['weeklyloyaltyVal']
        self.person['weeklyloyaltyValLimit'] = self['weeklyloyaltyValLimit']
        self.person['memberLifeSkillLevel'] = self['memberLifeSkillLevel']
        self.person['applicantCustomHeadPic'] = self['applicantCustomHeadPic']
        self.person['applicantPhotoFrameId'] = self['applicantPhotoFrameId']
        self.person['applicantCombatVal'] = self['applicantCombatVal']
        # end handle [GC_BROTHERHOOD_MY] message attrs, auto generate do not change
        pass


class GC_RELEASE_FAIRY_RET (Packet):
    def handle(self):
        # begin handle [GC_RELEASE_FAIRY_RET] message attrs, auto generate do not change
        self.person['result'] = self['result']
        # end handle [GC_RELEASE_FAIRY_RET] message attrs, auto generate do not change
        pass


class GC_TOURNAMENT_SYNC_MATCH_RESULT (Packet):
    def handle(self):
        # begin handle [GC_TOURNAMENT_SYNC_MATCH_RESULT] message attrs, auto generate do not change
        self.person['remainTime'] = self['remainTime']
        self.person['memberInfo'] = self['memberInfo']
        # end handle [GC_TOURNAMENT_SYNC_MATCH_RESULT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_COUPLEBP_SUCCESSCOUNT_SYNC] message attrs, auto generate do not change
        self.person['successcount'] = self['successcount']
        self.person['isbossTime'] = self['isbossTime']
        # end handle [GC_COUPLEBP_SUCCESSCOUNT_SYNC] message attrs, auto generate do not change
        pass


class GC_APIFIXACTIONSTR_FORQCLOUDPIC (Packet):
    def handle(self):
        # begin handle [GC_APIFIXACTIONSTR_FORQCLOUDPIC] message attrs, auto generate do not change
        self.person['apiFixActionStr'] = self['apiFixActionStr']
        self.person['apiCgiUrlStr'] = self['apiCgiUrlStr']
        self.person['apiDetectionCgiUrlStr'] = self['apiDetectionCgiUrlStr']
        # end handle [GC_APIFIXACTIONSTR_FORQCLOUDPIC] message attrs, auto generate do not change
        pass


class CG_CACHELOG (Packet):
    pass


class CG_REQ_SWITCH_PET_FIGHT_STATE (Packet):
    pass


class GC_SYNC_DAMAGE_SHOW_HP (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DAMAGE_SHOW_HP] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['nCurHp'] = self['nCurHp']
        # end handle [GC_SYNC_DAMAGE_SHOW_HP] message attrs, auto generate do not change
        pass


class GC_DIRECTIVE_INFO (Packet):
    def handle(self):
        # begin handle [GC_DIRECTIVE_INFO] message attrs, auto generate do not change
        self.person['HitTargetserverId'] = self['HitTargetserverId']
        self.person['sceneId'] = self['sceneId']
        self.person['sceneinst'] = self['sceneinst']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        # end handle [GC_DIRECTIVE_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_RECOMMEND_MEMBER_INFO (Packet):
    pass


class GC_BOSSDIE_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_BOSSDIE_NOTICE] message attrs, auto generate do not change
        self.person['notice'] = self['notice']
        # end handle [GC_BOSSDIE_NOTICE] message attrs, auto generate do not change
        pass


class GC_RES_GUILD_JIANMUXB_LIST (Packet):
    def handle(self):
        # begin handle [GC_RES_GUILD_JIANMUXB_LIST] message attrs, auto generate do not change
        self.person['seekHelpName'] = self['seekHelpName']
        self.person['itemId'] = self['itemId']
        self.person['bFinished'] = self['bFinished']
        self.person['helperName'] = self['helperName']
        self.person['playerGuid'] = self['playerGuid']
        self.person['slotId'] = self['slotId']
        self.person['needNum'] = self['needNum']
        self.person['guildContribute'] = self['guildContribute']
        # end handle [GC_RES_GUILD_JIANMUXB_LIST] message attrs, auto generate do not change
        pass


class CG_SKILLLEVUP_RECOMMEND (Packet):
    pass


class GC_SYC_FRIEND_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYC_FRIEND_STATE] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['State'] = self['State']
        # end handle [GC_SYC_FRIEND_STATE] message attrs, auto generate do not change
        pass


class GC_SYN_SKILLZHUANJINGINFO (Packet):
    def handle(self):
        # begin handle [GC_SYN_SKILLZHUANJINGINFO] message attrs, auto generate do not change
        self.person['bOpenLine'] = self['bOpenLine']
        self.person['SkillZhuanJingShengXianPointCost'] = self['SkillZhuanJingShengXianPointCost']
        self.person['SkillZhuanJingRuMoPointCost'] = self['SkillZhuanJingRuMoPointCost']
        self.person['SkillZhuanjingLine'] = self['SkillZhuanjingLine']
        self.person['SkillZhuanjingid'] = self['SkillZhuanjingid']
        self.person['SkillZhuanjingLevel'] = self['SkillZhuanjingLevel']
        self.person['bUnlockSkillZhuanjing'] = self['bUnlockSkillZhuanjing']
        self.person['bActiveSkillZhuanjing'] = self['bActiveSkillZhuanjing']
        self.person['skillCombatValue'] = self['skillCombatValue']
        # end handle [GC_SYN_SKILLZHUANJINGINFO] message attrs, auto generate do not change
        pass


class GC_SYNC_AUTOTEAM_BW (Packet):
    def handle(self):
        # begin handle [GC_SYNC_AUTOTEAM_BW] message attrs, auto generate do not change
        self.person['flag'] = self['flag']
        self.person['timeoutFlag'] = self['timeoutFlag']
        # end handle [GC_SYNC_AUTOTEAM_BW] message attrs, auto generate do not change
        pass


class GC_AUCTION_RETSELLINFO (Packet):
    def handle(self):
        # begin handle [GC_AUCTION_RETSELLINFO] message attrs, auto generate do not change
        self.person['itemid'] = self['itemid']
        self.person['taxrate'] = self['taxrate']
        self.person['othersames'] = self['othersames']
        self.person['stepPercent'] = self['stepPercent']
        self.person['baseMin'] = self['baseMin']
        self.person['baseMax'] = self['baseMax']
        self.person['oneMin'] = self['oneMin']
        self.person['oneMax'] = self['oneMax']
        self.person['maxTax'] = self['maxTax']
        self.person['timeMin'] = self['timeMin']
        self.person['timeMax'] = self['timeMax']
        self.person['checktime'] = self['checktime']
        # end handle [GC_AUCTION_RETSELLINFO] message attrs, auto generate do not change
        pass


class GC_WISHING_RESPONSE_DATA (Packet):
    def handle(self):
        # begin handle [GC_WISHING_RESPONSE_DATA] message attrs, auto generate do not change
        self.person['opt'] = self['opt']
        self.person['open'] = self['open']
        self.person['begint'] = self['begint']
        self.person['lotteryt'] = self['lotteryt']
        self.person['endt'] = self['endt']
        self.person['costitemid'] = self['costitemid']
        self.person['costitemnum'] = self['costitemnum']
        self.person['name1'] = self['name1']
        self.person['unlockt1'] = self['unlockt1']
        self.person['pool1'] = self['pool1']
        self.person['soltnum1'] = self['soltnum1']
        self.person['name2'] = self['name2']
        self.person['unlockt2'] = self['unlockt2']
        self.person['pool2'] = self['pool2']
        self.person['soltnum2'] = self['soltnum2']
        self.person['name3'] = self['name3']
        self.person['unlockt3'] = self['unlockt3']
        self.person['pool3'] = self['pool3']
        self.person['soltnum3'] = self['soltnum3']
        self.person['bg0'] = self['bg0']
        self.person['bg1'] = self['bg1']
        self.person['bg2'] = self['bg2']
        self.person['bg3'] = self['bg3']
        self.person['bg4'] = self['bg4']
        # end handle [GC_WISHING_RESPONSE_DATA] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_MY (Packet):
    pass


class GC_CVFIREFLY_SYNC_RESULT (Packet):
    def handle(self):
        # begin handle [GC_CVFIREFLY_SYNC_RESULT] message attrs, auto generate do not change
        self.person['normalRewardId'] = self['normalRewardId']
        self.person['coupleRewardId'] = self['coupleRewardId']
        self.person['guildRewardId'] = self['guildRewardId']
        self.person['bAnotherIsCouple'] = self['bAnotherIsCouple']
        # end handle [GC_CVFIREFLY_SYNC_RESULT] message attrs, auto generate do not change
        pass


class GC_SERVANT_SYNC_KIZUNA (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_SYNC_KIZUNA] message attrs, auto generate do not change
        self.person['m_activekizuna'] = self['m_activekizuna']
        self.person['m_addkizuna'] = self['m_addkizuna']
        # end handle [GC_SERVANT_SYNC_KIZUNA] message attrs, auto generate do not change
        pass


class CG_AUCTION_REVIEW_ASK (Packet):
    pass


class GC_RES_GUILDCONVOY_MAP_POS (Packet):
    def handle(self):
        # begin handle [GC_RES_GUILDCONVOY_MAP_POS] message attrs, auto generate do not change
        self.person['sceneClassID'] = self['sceneClassID']
        self.person['sceneInstID'] = self['sceneInstID']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        # end handle [GC_RES_GUILDCONVOY_MAP_POS] message attrs, auto generate do not change
        pass


class GC_FLY_DATA (Packet):
    def handle(self):
        # begin handle [GC_FLY_DATA] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['flystat'] = self['flystat']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        self.person['aircraftid'] = self['aircraftid']
        self.person['AircraftFashoinId'] = self['AircraftFashoinId']
        self.person['AircraftColorIndex'] = self['AircraftColorIndex']
        # end handle [GC_FLY_DATA] message attrs, auto generate do not change
        pass


class CG_RECHARGESCORESHOP_REQ (Packet):
    pass


class GC_UPDATE_IMMORTAILTY_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_IMMORTAILTY_INFO] message attrs, auto generate do not change
        self.person['wayData'] = self['wayData']
        self.person['activityData'] = self['activityData']
        self.person['immortalityActivityState'] = self['immortalityActivityState']
        self.person['immortalityActiveDays'] = self['immortalityActiveDays']
        self.person['immortalityFinalRewardState'] = self['immortalityFinalRewardState']
        # end handle [GC_UPDATE_IMMORTAILTY_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_GET_SIQINGREDENVELOPE (Packet):
    pass


class GC_TOURNAMENT_TEAM_REQ_FAILED (Packet):
    def handle(self):
        # begin handle [GC_TOURNAMENT_TEAM_REQ_FAILED] message attrs, auto generate do not change
        self.person['failType'] = self['failType']
        self.person['sArg'] = self['sArg']
        # end handle [GC_TOURNAMENT_TEAM_REQ_FAILED] message attrs, auto generate do not change
        pass


class GC_CDTIME_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_CDTIME_UPDATE] message attrs, auto generate do not change
        self.person['CDTimeId'] = self['CDTimeId']
        self.person['CDTime'] = self['CDTime']
        # end handle [GC_CDTIME_UPDATE] message attrs, auto generate do not change
        pass


class CG_REQ_DEL_HOME_HORDE_COLLECTION (Packet):
    pass


class CG_GUILD_CHANGETITLE (Packet):
    pass


class GC_ADD_GUILDLOUDSPEAKER (Packet):
    def handle(self):
        # begin handle [GC_ADD_GUILDLOUDSPEAKER] message attrs, auto generate do not change
        # end handle [GC_ADD_GUILDLOUDSPEAKER] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_DOMAIN_HISTORYLIST] message attrs, auto generate do not change
        self.person['version'] = self['version']
        self.person['domainHistoryList'] = self['domainHistoryList']
        # end handle [GC_DOMAIN_HISTORYLIST] message attrs, auto generate do not change
        pass


class GC_NEAR_PLAYERLIST (Packet):
    def handle(self):
        # begin handle [GC_NEAR_PLAYERLIST] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Com'] = self['Com']
        self.person['Sex'] = self['Sex']
        self.person['ProfCamp'] = self['ProfCamp']
        # end handle [GC_NEAR_PLAYERLIST] message attrs, auto generate do not change
        pass


class GC_SYNC_QQVIP_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_QQVIP_DATA] message attrs, auto generate do not change
        self.person['type'] = self['type']
        # end handle [GC_SYNC_QQVIP_DATA] message attrs, auto generate do not change
        pass


class CG_STATICSYSTEMSHOP_SELL (Packet):
    pass


class GC_SYNC_DANCE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DANCE_INFO] message attrs, auto generate do not change
        self.person['nDanceState'] = self['nDanceState']
        self.person['nCurrAuraValue'] = self['nCurrAuraValue']
        self.person['nAuraCdId'] = self['nAuraCdId']
        self.person['nCdTime'] = self['nCdTime']
        self.person['nCurrPosition'] = self['nCurrPosition']
        # end handle [GC_SYNC_DANCE_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_REGION_HOME_NUM] message attrs, auto generate do not change
        self.person['homeNum'] = self['homeNum']
        # end handle [GC_SYNC_REGION_HOME_NUM] message attrs, auto generate do not change
        pass


class CG_QIANKUNDAI_MAKE (Packet):
    pass


class CG_REQ_GUILDCONVOY_FILLINFO (Packet):
    pass


class CG_REBATE_ASKFORBONUS (Packet):
    pass


class GC_NIEREN_CHANGE (Packet):
    def handle(self):
        # begin handle [GC_NIEREN_CHANGE] message attrs, auto generate do not change
        self.person['nierenvalue'] = self['nierenvalue']
        self.person['objid'] = self['objid']
        # end handle [GC_NIEREN_CHANGE] message attrs, auto generate do not change
        pass


class GC_BWPP_GROUP_CHANGED (Packet):
    def handle(self):
        # begin handle [GC_BWPP_GROUP_CHANGED] message attrs, auto generate do not change
        self.person['IsRise'] = self['IsRise']
        self.person['OldGroup'] = self['OldGroup']
        self.person['NewGroup'] = self['NewGroup']
        # end handle [GC_BWPP_GROUP_CHANGED] message attrs, auto generate do not change
        pass


class GC_ADDFRIEND (Packet):
    def handle(self):
        # begin handle [GC_ADDFRIEND] message attrs, auto generate do not change
        suffix = str(self['guid'] % 10000)
        recv_friend_key = 'recv_friend_' + suffix
        self.person[recv_friend_key] = {}

        self.person[recv_friend_key]['guid'] = self['guid']
        self.person[recv_friend_key]['Name'] = self['Name']
        self.person[recv_friend_key]['Level'] = self['Level']
        self.person[recv_friend_key]['Prof'] = self['Prof']
        self.person[recv_friend_key]['Combat'] = self['Combat']
        self.person[recv_friend_key]['State'] = self['State']
        self.person[recv_friend_key]['TimeInfo'] = self['TimeInfo']
        self.person[recv_friend_key]['RelationPoint'] = self['RelationPoint']
        self.person[recv_friend_key]['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person[recv_friend_key]['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person[recv_friend_key]['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person[recv_friend_key]['VoiceSignName'] = self['VoiceSignName']
        self.person[recv_friend_key]['TextSign'] = self['TextSign']
        self.person[recv_friend_key]['Sex'] = self['Sex']
        self.person[recv_friend_key]['Birthday'] = self['Birthday']
        self.person[recv_friend_key]['PersonalLocation'] = self['PersonalLocation']
        self.person[recv_friend_key]['reserved'] = self['reserved']
        self.person[recv_friend_key]['DelFriendTime'] = self['DelFriendTime']
        self.person[recv_friend_key]['addType'] = self['addType']
        self.person[recv_friend_key]['BodyId'] = self['BodyId']
        self.person[recv_friend_key]['FaceId'] = self['FaceId']
        self.person[recv_friend_key]['WeaponId'] = self['WeaponId']
        self.person[recv_friend_key]['PlayerSex'] = self['PlayerSex']
        self.person[recv_friend_key]['guildname'] = self['guildname']
        self.person[recv_friend_key]['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person[recv_friend_key]['checkSignCode'] = self['checkSignCode']
        self.person[recv_friend_key]['HairId'] = self['HairId']
        self.person[recv_friend_key]['addfriendmsg'] = self['addfriendmsg']
        self.person[recv_friend_key]['loverName'] = self['loverName']
        self.person[recv_friend_key]['loverGuid'] = self['loverGuid']
        self.person[recv_friend_key]['homeGuid'] = self['homeGuid']
        self.person[recv_friend_key]['PhotoFrameId'] = self['PhotoFrameId']
        if not self.person['friends']:
            self.person['friends'] = []
        self.person['friends'].append(self.person[recv_friend_key])

        # end handle [GC_ADDFRIEND] message attrs, auto generate do not change)
        pass


class GC_SYNC_SUBSCIBE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SUBSCIBE_INFO] message attrs, auto generate do not change
        self.person['IsSubscibe'] = self['IsSubscibe']
        self.person['BeginTime'] = self['BeginTime']
        self.person['EndTime'] = self['EndTime']
        self.person['LastGainBonusTime'] = self['LastGainBonusTime']
        # end handle [GC_SYNC_SUBSCIBE_INFO] message attrs, auto generate do not change
        pass


class GC_ADDRECENTCONTACTLIST (Packet):
    def handle(self):
        # begin handle [GC_ADDRECENTCONTACTLIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['BodyId'] = self['BodyId']
        self.person['FaceId'] = self['FaceId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairId'] = self['HairId']
        self.person['loverName'] = self['loverName']
        self.person['loverGuid'] = self['loverGuid']
        self.person['homeGuid'] = self['homeGuid']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['remakeName'] = self['remakeName']
        # end handle [GC_ADDRECENTCONTACTLIST] message attrs, auto generate do not change
        pass


class CG_REQ_GUILDAUCTION_INFO (Packet):
    pass


class GC_HONGBAO_ROB (Packet):
    def handle(self):
        # begin handle [GC_HONGBAO_ROB] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['SenderGuid'] = self['SenderGuid']
        self.person['strSenderName'] = self['strSenderName']
        self.person['nSenderProfession'] = self['nSenderProfession']
        self.person['strDesc'] = self['strDesc']
        self.person['nType'] = self['nType']
        self.person['nChannel'] = self['nChannel']
        self.person['nMaxCount'] = self['nMaxCount']
        self.person['nMoneyType'] = self['nMoneyType']
        self.person['nMoney'] = self['nMoney']
        self.person['RobberData'] = self['RobberData']
        self.person['nSenderSex'] = self['nSenderSex']
        self.person['isRob'] = self['isRob']
        self.person['nCoverId'] = self['nCoverId']
        # end handle [GC_HONGBAO_ROB] message attrs, auto generate do not change
        pass


class GC_RECEIVEFLOWER_PLAYEFFECT (Packet):
    def handle(self):
        # begin handle [GC_RECEIVEFLOWER_PLAYEFFECT] message attrs, auto generate do not change
        self.person['effectid'] = self['effectid']
        self.person['fromname'] = self['fromname']
        # end handle [GC_RECEIVEFLOWER_PLAYEFFECT] message attrs, auto generate do not change
        pass


class CG_ASK_FIREWORKS_DATA (Packet):
    pass


class CG_ARMY_LEADER_CALL_MEMBER (Packet):
    pass


class CG_WEDDING_ASKINFO (Packet):
    pass


class GC_KEEP_ROTATE (Packet):
    def handle(self):
        # begin handle [GC_KEEP_ROTATE] message attrs, auto generate do not change
        self.person['objID'] = self['objID']
        self.person['targetDir'] = self['targetDir']
        self.person['speed'] = self['speed']
        self.person['isStop'] = self['isStop']
        self.person['isAimDir'] = self['isAimDir']
        # end handle [GC_KEEP_ROTATE] message attrs, auto generate do not change
        pass


class GC_LIMITSHOP_SYNC (Packet):
    def handle(self):
        # begin handle [GC_LIMITSHOP_SYNC] message attrs, auto generate do not change
        self.person['Version'] = self['Version']
        self.person['ItemId'] = self['ItemId']
        self.person['Stack'] = self['Stack']
        self.person['MoneyType'] = self['MoneyType']
        self.person['Price'] = self['Price']
        self.person['Discount'] = self['Discount']
        self.person['PlayerRemain'] = self['PlayerRemain']
        self.person['ServerRemain'] = self['ServerRemain']
        self.person['GoodsIndex'] = self['GoodsIndex']
        self.person['ShowSort'] = self['ShowSort']
        self.person['RemainTime'] = self['RemainTime']
        self.person['LimitType'] = self['LimitType']
        self.person['buyitem'] = self['buyitem']
        self.person['ShowInNewGood'] = self['ShowInNewGood']
        self.person['ShopType'] = self['ShopType']
        self.person['MaxLevelRequired'] = self['MaxLevelRequired']
        self.person['PlayerMax'] = self['PlayerMax']
        self.person['IsNew'] = self['IsNew']
        self.person['SubTitle'] = self['SubTitle']
        self.person['RecommendTabIndex'] = self['RecommendTabIndex']
        self.person['RecommendTabSort'] = self['RecommendTabSort']
        self.person['EndTime'] = self['EndTime']
        # end handle [GC_LIMITSHOP_SYNC] message attrs, auto generate do not change
        pass


class GC_USE_DIRECTSENDGIDT (Packet):
    def handle(self):
        # begin handle [GC_USE_DIRECTSENDGIDT] message attrs, auto generate do not change
        self.person['success'] = self['success']
        self.person['receiverGuid'] = self['receiverGuid']
        self.person['itemDataId'] = self['itemDataId']
        self.person['count'] = self['count']
        self.person['retCode'] = self['retCode']
        # end handle [GC_USE_DIRECTSENDGIDT] message attrs, auto generate do not change
        pass


class GC_NPCGIFTEXCHANGE_GET_AWARD (Packet):
    def handle(self):
        # begin handle [GC_NPCGIFTEXCHANGE_GET_AWARD] message attrs, auto generate do not change
        self.person['targetNPC'] = self['targetNPC']
        # end handle [GC_NPCGIFTEXCHANGE_GET_AWARD] message attrs, auto generate do not change
        pass


class CG_SET_GUILD_ACTIVITY_OPEN_TIME (Packet):
    pass


class CG_REPLACE_ENCHANT_RESULT (Packet):
    pass


class GC_ISINSELFHATEPEOPLELIST (Packet):
    def handle(self):
        # begin handle [GC_ISINSELFHATEPEOPLELIST] message attrs, auto generate do not change
        self.person['tarGuid'] = self['tarGuid']
        self.person['IsInSelfDuelList'] = self['IsInSelfDuelList']
        # end handle [GC_ISINSELFHATEPEOPLELIST] message attrs, auto generate do not change
        pass


class CG_FASHION_RANDOM_COLOR_COMFIRM (Packet):
    pass


class GC_TONGTIANTREASURE_SYNC (Packet):
    def handle(self):
        # begin handle [GC_TONGTIANTREASURE_SYNC] message attrs, auto generate do not change
        self.person['synctype'] = self['synctype']
        self.person['starttime'] = self['starttime']
        self.person['endtime'] = self['endtime']
        self.person['showreddot'] = self['showreddot']
        self.person['isopen'] = self['isopen']
        self.person['mapinfo'] = self['mapinfo']
        self.person['versionNo'] = self['versionNo']
        # end handle [GC_TONGTIANTREASURE_SYNC] message attrs, auto generate do not change
        pass


class CG_REQ_CUTOF_MENTOR (Packet):
    pass


class GC_BROADCAST_YLTX (Packet):
    def handle(self):
        # begin handle [GC_BROADCAST_YLTX] message attrs, auto generate do not change
        self.person['isYLTXNotOver'] = self['isYLTXNotOver']
        # end handle [GC_BROADCAST_YLTX] message attrs, auto generate do not change
        pass


class GC_RESET_FAIRY_ATTR_POINTS_RET (Packet):
    def handle(self):
        # begin handle [GC_RESET_FAIRY_ATTR_POINTS_RET] message attrs, auto generate do not change
        self.person['bRet'] = self['bRet']
        # end handle [GC_RESET_FAIRY_ATTR_POINTS_RET] message attrs, auto generate do not change
        pass


class CG_BREAKCURSKILL (Packet):
    pass


class GC_MILITARY_SYNC_REPUTATION (Packet):
    def handle(self):
        # begin handle [GC_MILITARY_SYNC_REPUTATION] message attrs, auto generate do not change
        self.person['reputation'] = self['reputation']
        self.person['dailyReputation'] = self['dailyReputation']
        self.person['weeklyDonationReputation'] = self['weeklyDonationReputation']
        self.person['dailyItemReputation'] = self['dailyItemReputation']
        self.person['servercatchDonationReputation'] = self['servercatchDonationReputation']
        # end handle [GC_MILITARY_SYNC_REPUTATION] message attrs, auto generate do not change
        pass


class CG_GUILD_REQ_WORSHIP_CHIEFMODEL (Packet):
    pass


class GC_SYN_MENTOR_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYN_MENTOR_INFO] message attrs, auto generate do not change
        self.person['mentorInfo'] = self['mentorInfo']
        self.person['teaachingLevel'] = self['teaachingLevel']
        self.person['teachingExp'] = self['teachingExp']
        self.person['teachingPoint'] = self['teachingPoint']
        self.person['lastMentorMasterInfo'] = self['lastMentorMasterInfo']
        self.person['lasterMentorGuid'] = self['lasterMentorGuid']
        self.person['lastPulisTime'] = self['lastPulisTime']
        self.person['syncType'] = self['syncType']
        # end handle [GC_SYN_MENTOR_INFO] message attrs, auto generate do not change
        pass


class GC_XIANDAN_EQUIP_RET (Packet):
    def handle(self):
        # begin handle [GC_XIANDAN_EQUIP_RET] message attrs, auto generate do not change
        self.person['xiandanGuid'] = self['xiandanGuid']
        # end handle [GC_XIANDAN_EQUIP_RET] message attrs, auto generate do not change
        pass


class GC_PET_FLY_STATE (Packet):
    def handle(self):
        # begin handle [GC_PET_FLY_STATE] message attrs, auto generate do not change
        self.person['serverID'] = self['serverID']
        self.person['state'] = self['state']
        # end handle [GC_PET_FLY_STATE] message attrs, auto generate do not change
        pass


class CG_ASKFORPIC_SIGN (Packet):
    pass


class GC_RET_GUILDLOG (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILDLOG] message attrs, auto generate do not change
        self.person['logType'] = self['logType']
        self.person['recordTime'] = self['recordTime']
        self.person['param1'] = self['param1']
        self.person['param2'] = self['param2']
        self.person['param3'] = self['param3']
        self.person['param4'] = self['param4']
        self.person['param5'] = self['param5']
        # end handle [GC_RET_GUILDLOG] message attrs, auto generate do not change
        pass


class CG_DEATH_ASKFOR_LETHAL_DAMAGE_LIST (Packet):
    pass


class GC_SYNC_ENERMYPOS (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ENERMYPOS] message attrs, auto generate do not change
        self.person['objIdList'] = self['objIdList']
        self.person['posList'] = self['posList']
        self.person['teaminfo'] = self['teaminfo']
        self.person['playerguid'] = self['playerguid']
        self.person['armyteamindex'] = self['armyteamindex']
        # end handle [GC_SYNC_ENERMYPOS] message attrs, auto generate do not change
        pass


class CG_QUEST_CHANGETOBIGWORLD (Packet):
    pass


class GC_BATTLEFIELD_FLAG_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_FLAG_UPDATE] message attrs, auto generate do not change
        self.person['Flag'] = self['Flag']
        # end handle [GC_BATTLEFIELD_FLAG_UPDATE] message attrs, auto generate do not change
        pass


class GC_PGL_SYNC_RANK (Packet):
    def handle(self):
        # begin handle [GC_PGL_SYNC_RANK] message attrs, auto generate do not change
        self.person['rankidx'] = self['rankidx']
        # end handle [GC_PGL_SYNC_RANK] message attrs, auto generate do not change
        pass


class CG_REQ_HOME_PRAY_CHANGE_ATTR (Packet):
    pass


class GC_PLAY_ANIMATION (Packet):
    def handle(self):
        # begin handle [GC_PLAY_ANIMATION] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['animationid'] = self['animationid']
        self.person['facetargetid'] = self['facetargetid']
        # end handle [GC_PLAY_ANIMATION] message attrs, auto generate do not change
        pass


class CG_ASK_SETCOMMONFLAG (Packet):
    pass


class CG_STALL_ASKRECORD (Packet):
    pass


class GC_SYNC_PERSONALREBATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PERSONALREBATE] message attrs, auto generate do not change
        self.person['overtime'] = self['overtime']
        self.person['nowcount'] = self['nowcount']
        self.person['needcount'] = self['needcount']
        self.person['state'] = self['state']
        self.person['bonus'] = self['bonus']
        # end handle [GC_SYNC_PERSONALREBATE] message attrs, auto generate do not change
        pass


class CG_GUILD_APPROVE_ALLRESERVE (Packet):
    pass


class CG_NEATEN_ITEMPACK (Packet):
    pass


class GC_REPLY_PASSPORT_DATA (Packet):
    def handle(self):
        # begin handle [GC_REPLY_PASSPORT_DATA] message attrs, auto generate do not change
        self.person['isvip'] = self['isvip']
        self.person['passexp'] = self['passexp']
        self.person['passlevel'] = self['passlevel']
        self.person['misid'] = self['misid']
        self.person['miscount'] = self['miscount']
        self.person['totalcount'] = self['totalcount']
        self.person['rewardsigned'] = self['rewardsigned']
        self.person['passopenid'] = self['passopenid']
        self.person['signcount'] = self['signcount']
        self.person['weekexp'] = self['weekexp']
        # end handle [GC_REPLY_PASSPORT_DATA] message attrs, auto generate do not change
        pass


class CG_CHANGE_ARMY_MEMBER_BIAOJI (Packet):
    pass


class GC_SYN_COLOR_ITEM_STORAGE (Packet):
    def handle(self):
        # begin handle [GC_SYN_COLOR_ITEM_STORAGE] message attrs, auto generate do not change
        self.person['count'] = self['count']
        self.person['random_count'] = self['random_count']
        self.person['freedomCount'] = self['freedomCount']
        # end handle [GC_SYN_COLOR_ITEM_STORAGE] message attrs, auto generate do not change
        pass


class GC_RET_CHAT_PLAYERINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_CHAT_PLAYERINFO] message attrs, auto generate do not change
        self.person['senderGuid'] = self['senderGuid']
        self.person['senderTeamId'] = self['senderTeamId']
        self.person['senderArmyId'] = self['senderArmyId']
        self.person['senderLevel'] = self['senderLevel']
        self.person['senderGuildName'] = self['senderGuildName']
        self.person['senderBrotherhood'] = self['senderBrotherhood']
        self.person['haveHuiliuIdentity'] = self['haveHuiliuIdentity']
        self.person['senderSwordTeamGuid'] = self['senderSwordTeamGuid']
        self.person['senderHomeGuid'] = self['senderHomeGuid']
        # end handle [GC_RET_CHAT_PLAYERINFO] message attrs, auto generate do not change
        pass


class CG_BWPVPFINAL_ASKMEMINFOINVIEW (Packet):
    pass


class GC_SYNC_DIRTY_KIT_PACK (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DIRTY_KIT_PACK] message attrs, auto generate do not change
        self.person['validCount'] = self['validCount']
        self.person['items'] = self['items']
        self.person['dirtyItemIndex'] = self['dirtyItemIndex']
        self.person['itemUnlockState'] = self['itemUnlockState']
        self.person['dirtyUnlockIndex'] = self['dirtyUnlockIndex']
        # end handle [GC_SYNC_DIRTY_KIT_PACK] message attrs, auto generate do not change
        pass


class GC_ACTIVITYNOTICE (Packet):
    def handle(self):
        # begin handle [GC_ACTIVITYNOTICE] message attrs, auto generate do not change
        self.person['strNotice'] = self['strNotice']
        self.person['priority'] = self['priority']
        self.person['LinkType'] = self['LinkType']
        self.person['LinkData'] = self['LinkData']
        self.person['LinkDownloadIndex'] = self['LinkDownloadIndex']
        self.person['LinkColorParam'] = self['LinkColorParam']
        self.person['Pos'] = self['Pos']
        # end handle [GC_ACTIVITYNOTICE] message attrs, auto generate do not change
        pass


class CG_DOMAINWARSHOP_BUY (Packet):
    pass


class GC_WAITPAY_PAY (Packet):
    def handle(self):
        # begin handle [GC_WAITPAY_PAY] message attrs, auto generate do not change
        self.person['BillGuid'] = self['BillGuid']
        # end handle [GC_WAITPAY_PAY] message attrs, auto generate do not change
        pass


class CG_STALL_ASKITEM_SELLINFO (Packet):
    pass


class CG_TOWER_FIGHT (Packet):
    pass


class CG_RANDOM_OPPONENT (Packet):
    pass


class GC_SWEEP_REWARD (Packet):
    def handle(self):
        # begin handle [GC_SWEEP_REWARD] message attrs, auto generate do not change
        self.person['exp'] = self['exp']
        self.person['guildContri'] = self['guildContri']
        self.person['itemId'] = self['itemId']
        self.person['itemCount'] = self['itemCount']
        self.person['itemBind'] = self['itemBind']
        self.person['sweepID'] = self['sweepID']
        self.person['dropSoul'] = self['dropSoul']
        # end handle [GC_SWEEP_REWARD] message attrs, auto generate do not change
        pass


class CG_GUILD_DISMISS (Packet):
    pass


class CG_REQ_HOME_SETTLE (Packet):
    pass


class GC_BWPVPFINAL_HELPMEMINFO (Packet):
    def handle(self):
        # begin handle [GC_BWPVPFINAL_HELPMEMINFO] message attrs, auto generate do not change
        self.person['MemAGuid'] = self['MemAGuid']
        self.person['MemAName'] = self['MemAName']
        self.person['MemAQingLongScore'] = self['MemAQingLongScore']
        self.person['MemABaiHuScore'] = self['MemABaiHuScore']
        self.person['MemAZhuQueScore'] = self['MemAZhuQueScore']
        self.person['MemAXuanWuScore'] = self['MemAXuanWuScore']
        self.person['MemAIsHelp'] = self['MemAIsHelp']
        self.person['MemAWorldName'] = self['MemAWorldName']
        self.person['MemBGuid'] = self['MemBGuid']
        self.person['MemBName'] = self['MemBName']
        self.person['MemBQingLongScore'] = self['MemBQingLongScore']
        self.person['MemBBaiHuScore'] = self['MemBBaiHuScore']
        self.person['MemBZhuQueScore'] = self['MemBZhuQueScore']
        self.person['MemBXuanWuScore'] = self['MemBXuanWuScore']
        self.person['MemBIsHelp'] = self['MemBIsHelp']
        self.person['MemBWorldName'] = self['MemBWorldName']
        self.person['remainTime'] = self['remainTime']
        self.person['myHelpScore'] = self['myHelpScore']
        self.person['nextStartTime'] = self['nextStartTime']
        # end handle [GC_BWPVPFINAL_HELPMEMINFO] message attrs, auto generate do not change
        pass


class CG_DOMAINWAR_OP (Packet):
    pass


class CG_BOUNTY_PICK_ITEM_NPC (Packet):
    pass


class GC_PA_OPERATE_REQUEST (Packet):
    def handle(self):
        # begin handle [GC_PA_OPERATE_REQUEST] message attrs, auto generate do not change
        self.person['OperateCode'] = self['OperateCode']
        self.person['IsAdult'] = self['IsAdult']
        self.person['Content'] = self['Content']
        # end handle [GC_PA_OPERATE_REQUEST] message attrs, auto generate do not change
        pass


class CG_REQ_FAIRY_NEIDAN_FORGET (Packet):
    pass


class GC_INFINITEDREAMLAND_INFO (Packet):
    def handle(self):
        # begin handle [GC_INFINITEDREAMLAND_INFO] message attrs, auto generate do not change
        self.person['ActivityID'] = self['ActivityID']
        self.person['AffixID'] = self['AffixID']
        self.person['RankShowNewIcon'] = self['RankShowNewIcon']
        # end handle [GC_INFINITEDREAMLAND_INFO] message attrs, auto generate do not change
        pass


class GC_BATTLEFIELD_CANCEL_SIGNUP (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_CANCEL_SIGNUP] message attrs, auto generate do not change
        self.person['SignupID'] = self['SignupID']
        self.person['IsCanceled'] = self['IsCanceled']
        self.person['SignupPlayerNum'] = self['SignupPlayerNum']
        # end handle [GC_BATTLEFIELD_CANCEL_SIGNUP] message attrs, auto generate do not change
        pass


class GC_SYC_FULL_FRIEND_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYC_FULL_FRIEND_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['BodyId'] = self['BodyId']
        self.person['FaceId'] = self['FaceId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairId'] = self['HairId']
        self.person['rewardstatus'] = self['rewardstatus']
        self.person['loverName'] = self['loverName']
        self.person['loverGuid'] = self['loverGuid']
        self.person['ArmyId'] = self['ArmyId']
        self.person['TeamId'] = self['TeamId']
        self.person['haveHuiliuIdentity'] = self['haveHuiliuIdentity']
        self.person['TowerFloor'] = self['TowerFloor']
        self.person['TowerTime'] = self['TowerTime']
        self.person['AddDatas'] = self['AddDatas']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['RmName'] = self['RmName']
        self.person['haveFestivalHuiliuIdentity'] = self['haveFestivalHuiliuIdentity']
        self.person['FriendGroupIndx'] = self['FriendGroupIndx']
        self.person['HaveNewPlayerCatch'] = self['HaveNewPlayerCatch']
        # end handle [GC_SYC_FULL_FRIEND_LIST] message attrs, auto generate do not change
        pass


class CG_ASK_ZHUGUO_INFO (Packet):
    pass


class GC_SYNC_EQUIP_REBIRTH_RECASE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_EQUIP_REBIRTH_RECASE_INFO] message attrs, auto generate do not change
        self.person['nEquipGuid'] = self['nEquipGuid']
        self.person['nTrickGroupId'] = self['nTrickGroupId']
        # end handle [GC_SYNC_EQUIP_REBIRTH_RECASE_INFO] message attrs, auto generate do not change
        pass


class GC_JOIN_TEAM_INVITE (Packet):
    def handle(self):
        # begin handle [GC_JOIN_TEAM_INVITE] message attrs, auto generate do not change
        self.person['inviterGuid'] = self['inviterGuid']
        self.person['inviterName'] = self['inviterName']
        self.person['inviterSignCode'] = self['inviterSignCode']
        self.person['sceneId'] = self['sceneId']
        self.person['sceneinst'] = self['sceneinst']
        self.person['invitetype'] = self['invitetype']
        self.person['targetID'] = self['targetID']
        self.person['teamLeaderGuid'] = self['teamLeaderGuid']
        self.person['teamLeaderName'] = self['teamLeaderName']
        self.person['armyID'] = self['armyID']
        self.person['bFullTeamInvite'] = self['bFullTeamInvite']
        self.person['isBrotherhoodTeam'] = self['isBrotherhoodTeam']
        self.person['inviterIsNewCatchPlayer'] = self['inviterIsNewCatchPlayer']
        self.person['inviterSex'] = self['inviterSex']
        self.person['inviterProf'] = self['inviterProf']
        self.person['inviterLevel'] = self['inviterLevel']
        # end handle [GC_JOIN_TEAM_INVITE] message attrs, auto generate do not change
        pass


class GC_BANGHUA_CAGE_INFO (Packet):
    def handle(self):
        # begin handle [GC_BANGHUA_CAGE_INFO] message attrs, auto generate do not change
        self.person['optype'] = self['optype']
        self.person['guids'] = self['guids']
        # end handle [GC_BANGHUA_CAGE_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_ARMY_COPYSCENE_INVITEVIEW] message attrs, auto generate do not change
        self.person['sceneID'] = self['sceneID']
        self.person['bPopMessageBox'] = self['bPopMessageBox']
        self.person['bIsBossInFight'] = self['bIsBossInFight']
        # end handle [GC_ARMY_COPYSCENE_INVITEVIEW] message attrs, auto generate do not change
        pass


class GC_IDIP_ROLL_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_IDIP_ROLL_NOTICE] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['content'] = self['content']
        self.person['priority'] = self['priority']
        self.person['startTime'] = self['startTime']
        self.person['endTime'] = self['endTime']
        self.person['intervalTime'] = self['intervalTime']
        # end handle [GC_IDIP_ROLL_NOTICE] message attrs, auto generate do not change
        pass


class GC_RESPONSE_RECHARGE (Packet):
    def handle(self):
        # begin handle [GC_RESPONSE_RECHARGE] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['producttype'] = self['producttype']
        self.person['productid'] = self['productid']
        self.person['productnum'] = self['productnum']
        self.person['param'] = self['param']
        # end handle [GC_RESPONSE_RECHARGE] message attrs, auto generate do not change
        pass


class GC_SYNC_RECHARGE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RECHARGE_DATA] message attrs, auto generate do not change
        self.person['openfrb'] = self['openfrb']
        self.person['openfrd'] = self['openfrd']
        self.person['baseyuan1'] = self['baseyuan1']
        self.person['baseyuan6'] = self['baseyuan6']
        self.person['baseyuan30'] = self['baseyuan30']
        self.person['baseyuan50'] = self['baseyuan50']
        self.person['baseyuan98'] = self['baseyuan98']
        self.person['baseyuan198'] = self['baseyuan198']
        self.person['baseyuan328'] = self['baseyuan328']
        self.person['baseyuan648'] = self['baseyuan648']
        self.person['opensrd'] = self['opensrd']
        self.person['isinact'] = self['isinact']
        self.person['begint'] = self['begint']
        self.person['endt'] = self['endt']
        self.person['actyuan1'] = self['actyuan1']
        self.person['actyuan6'] = self['actyuan6']
        self.person['actyuan30'] = self['actyuan30']
        self.person['actyuan50'] = self['actyuan50']
        self.person['actyuan98'] = self['actyuan98']
        self.person['actyuan198'] = self['actyuan198']
        self.person['actyuan328'] = self['actyuan328']
        self.person['actyuan648'] = self['actyuan648']
        self.person['baselimit'] = self['baselimit']
        self.person['actyuan1limit'] = self['actyuan1limit']
        self.person['actyuan6limit'] = self['actyuan6limit']
        self.person['actyuan30limit'] = self['actyuan30limit']
        self.person['actyuan50limit'] = self['actyuan50limit']
        self.person['actyuan98limit'] = self['actyuan98limit']
        self.person['actyuan198limit'] = self['actyuan198limit']
        self.person['actyuan328limit'] = self['actyuan328limit']
        self.person['actyuan648limit'] = self['actyuan648limit']
        self.person['openrecharge'] = self['openrecharge']
        self.person['firstChargeData'] = self['firstChargeData']
        self.person['accumt'] = self['accumt']
        # end handle [GC_SYNC_RECHARGE_DATA] message attrs, auto generate do not change
        pass


class CG_REQ_GUILDCONVOY_NEXT_POINT (Packet):
    pass


class GC_SNARESTATE_BROADCAST (Packet):
    def handle(self):
        # begin handle [GC_SNARESTATE_BROADCAST] message attrs, auto generate do not change
        self.person['snareObjId'] = self['snareObjId']
        self.person['snarestate'] = self['snarestate']
        # end handle [GC_SNARESTATE_BROADCAST] message attrs, auto generate do not change
        pass


class GC_RET_RELIVE (Packet):
    def handle(self):
        # begin handle [GC_RET_RELIVE] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['pos_x'] = self['pos_x']
        self.person['pos_y'] = self['pos_y']
        self.person['pos_z'] = self['pos_z']
        self.person['facedir'] = self['facedir']
        self.person['reviveTime'] = self['reviveTime']
        # end handle [GC_RET_RELIVE] message attrs, auto generate do not change
        pass


class CG_HONGBAO_ASK_UPDATE (Packet):
    pass


class CG_GUILD_GRANTTITLE (Packet):
    pass


class GC_RESPONSE_ZHUGUO_INFO (Packet):
    def handle(self):
        # begin handle [GC_RESPONSE_ZHUGUO_INFO] message attrs, auto generate do not change
        self.person['zhuGuoCombat'] = self['zhuGuoCombat']
        self.person['zhuGuoAttrId'] = self['zhuGuoAttrId']
        self.person['zhuGuoAttrCount'] = self['zhuGuoAttrCount']
        # end handle [GC_RESPONSE_ZHUGUO_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_GROWWAY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GROWWAY_INFO] message attrs, auto generate do not change
        self.person['WayData'] = self['WayData']
        self.person['ActivityData'] = self['ActivityData']
        self.person['GrowWayActivityState'] = self['GrowWayActivityState']
        self.person['GrowWayActiveDays'] = self['GrowWayActiveDays']
        self.person['StageOpenDay'] = self['StageOpenDay']
        # end handle [GC_SYNC_GROWWAY_INFO] message attrs, auto generate do not change
        pass


class GC_FLY_LANDING (Packet):
    def handle(self):
        # begin handle [GC_FLY_LANDING] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['opType'] = self['opType']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        # end handle [GC_FLY_LANDING] message attrs, auto generate do not change
        pass


class GC_HOME_SYNC_PERMISSION_DATA (Packet):
    def handle(self):
        # begin handle [GC_HOME_SYNC_PERMISSION_DATA] message attrs, auto generate do not change
        self.person['RelationList'] = self['RelationList']
        self.person['PermissionList'] = self['PermissionList']
        # end handle [GC_HOME_SYNC_PERMISSION_DATA] message attrs, auto generate do not change
        pass


class CG_GUILDFIGHT_WORLDBOSS_ASK_SOULS (Packet):
    pass


class GC_NOTIF_WORLDBOSS_STRIVE (Packet):
    def handle(self):
        # begin handle [GC_NOTIF_WORLDBOSS_STRIVE] message attrs, auto generate do not change
        self.person['Inst'] = self['Inst']
        self.person['LeaderName'] = self['LeaderName']
        # end handle [GC_NOTIF_WORLDBOSS_STRIVE] message attrs, auto generate do not change
        pass


class GC_UPDATE_BATTLE_FAIRY (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_BATTLE_FAIRY] message attrs, auto generate do not change
        self.person['battleFairy'] = self['battleFairy']
        self.person['curHpRate'] = self['curHpRate']
        self.person['level'] = self['level']
        self.person['schemeId'] = self['schemeId']
        # end handle [GC_UPDATE_BATTLE_FAIRY] message attrs, auto generate do not change
        pass


class GC_SYNC_KXJFAWARDTABLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_KXJFAWARDTABLE] message attrs, auto generate do not change
        self.person['IsShow'] = self['IsShow']
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['NeedLv'] = self['NeedLv']
        self.person['AwardID'] = self['AwardID']
        self.person['LeftTime'] = self['LeftTime']
        self.person['Awards'] = self['Awards']
        # end handle [GC_SYNC_KXJFAWARDTABLE] message attrs, auto generate do not change
        pass


class CG_BUY_CHALLENGE_TIMES (Packet):
    pass


class GC_TIANSHUBOARD_SETUP (Packet):
    def handle(self):
        # begin handle [GC_TIANSHUBOARD_SETUP] message attrs, auto generate do not change
        self.person['boardInfo'] = self['boardInfo']
        self.person['zhenfaDataId'] = self['zhenfaDataId']
        self.person['zhenfaLevel'] = self['zhenfaLevel']
        self.person['yinzhenId'] = self['yinzhenId']
        self.person['yinzhenLevel'] = self['yinzhenLevel']
        self.person['curSchemeId'] = self['curSchemeId']
        # end handle [GC_TIANSHUBOARD_SETUP] message attrs, auto generate do not change
        pass


class CG_SEARCH_ACTOR (Packet):
    pass


class GC_ACCLOGIN_SYNCSTATUS (Packet):
    def handle(self):
        # begin handle [GC_ACCLOGIN_SYNCSTATUS] message attrs, auto generate do not change
        self.person['version'] = self['version']
        self.person['playerIndex'] = self['playerIndex']
        self.person['canGetAward'] = self['canGetAward']
        self.person['action'] = self['action']
        # end handle [GC_ACCLOGIN_SYNCSTATUS] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_CHANGE_STEWARD_NAME] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['HomeGuid'] = self['HomeGuid']
        # end handle [GC_CHANGE_STEWARD_NAME] message attrs, auto generate do not change
        pass


class CG_SYNC_PLAYER_AREA_INFO (Packet):
    pass


class GC_SYN_CHARGE_COUNT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYN_CHARGE_COUNT_INFO] message attrs, auto generate do not change
        self.person['nSkillBaseId'] = self['nSkillBaseId']
        self.person['nSkillChargeCount'] = self['nSkillChargeCount']
        # end handle [GC_SYN_CHARGE_COUNT_INFO] message attrs, auto generate do not change
        pass


class GC_FAIRY_RAISE_SYNC_FEED_TIME (Packet):
    def handle(self):
        # begin handle [GC_FAIRY_RAISE_SYNC_FEED_TIME] message attrs, auto generate do not change
        self.person['feedTimeLeft'] = self['feedTimeLeft']
        self.person['feedTimeCanBuy'] = self['feedTimeCanBuy']
        # end handle [GC_FAIRY_RAISE_SYNC_FEED_TIME] message attrs, auto generate do not change
        pass


class CG_ASK_AUTOTEAM_BW (Packet):
    pass


class CG_CHANGE_MAJORCITY (Packet):
    pass


class CG_STOP_KIT_PACK (Packet):
    pass


class GC_ADDBLACKLIST (Packet):
    def handle(self):
        # begin handle [GC_ADDBLACKLIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        # end handle [GC_ADDBLACKLIST] message attrs, auto generate do not change
        pass


class CG_ASK_ELITENPCCREATECD (Packet):
    pass


class GC_STOP_RUBKICUBE_PLAY (Packet):
    def handle(self):
        # begin handle [GC_STOP_RUBKICUBE_PLAY] message attrs, auto generate do not change
        self.person['rubkiCubePlayId'] = self['rubkiCubePlayId']
        self.person['serverTime'] = self['serverTime']
        # end handle [GC_STOP_RUBKICUBE_PLAY] message attrs, auto generate do not change
        pass


class GC_STALL_RETINFO (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETINFO] message attrs, auto generate do not change
        self.person['stallitems'] = self['stallitems']
        self.person['type'] = self['type']
        # end handle [GC_STALL_RETINFO] message attrs, auto generate do not change
        pass


class GC_DOMAINWAR_UPDATECAR (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_UPDATECAR] message attrs, auto generate do not change
        self.person['carObjId'] = self['carObjId']
        self.person['newTitle'] = self['newTitle']
        # end handle [GC_DOMAINWAR_UPDATECAR] message attrs, auto generate do not change
        pass


class GC_RETENEMYMEMINFO (Packet):
    def handle(self):
        # begin handle [GC_RETENEMYMEMINFO] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['pro'] = self['pro']
        self.person['lev'] = self['lev']
        self.person['curhp'] = self['curhp']
        self.person['maxhp'] = self['maxhp']
        self.person['name'] = self['name']
        self.person['vipLev'] = self['vipLev']
        self.person['guid'] = self['guid']
        # end handle [GC_RETENEMYMEMINFO] message attrs, auto generate do not change
        pass


class CG_REQ_GUILDCONVOY_CALL_LINE (Packet):
    pass


class CG_PK_DIE_HELP_FOR_GUILD (Packet):
    pass


class CG_LUCKY_CONNECT_DRAW (Packet):
    pass


class GC_SWORDTEAM_INVITE_CONFIRM (Packet):
    def handle(self):
        # begin handle [GC_SWORDTEAM_INVITE_CONFIRM] message attrs, auto generate do not change
        self.person['inviterGuid'] = self['inviterGuid']
        self.person['inviterswordteamGuid'] = self['inviterswordteamGuid']
        self.person['inviterName'] = self['inviterName']
        self.person['inviterswordteamName'] = self['inviterswordteamName']
        self.person['job'] = self['job']
        self.person['inviterSignCode'] = self['inviterSignCode']
        # end handle [GC_SWORDTEAM_INVITE_CONFIRM] message attrs, auto generate do not change
        pass


class GC_SELECT_ROLE_RET (Packet):
    def handle(self):
        # begin handle [GC_SELECT_ROLE_RET] message attrs, auto generate do not change
        self.person['selectresult'] = self['result']
        self.person['guid'] = self['playerGuid']
        self.person['freezeminute'] = self['freezeminute']
        self.person['freezeStartTime'] = self['freezeStartTime']
        self.person['freezeOverTime'] = self['freezeOverTime']
        self.person['freezeReason'] = self['freezeReason']
        # end handle [GC_SELECT_ROLE_RET] message attrs, auto generate do not change

        pass


class GC_RET_YLTX_POS (Packet):
    def handle(self):
        # begin handle [GC_RET_YLTX_POS] message attrs, auto generate do not change
        self.person['sceneid'] = self['sceneid']
        # end handle [GC_RET_YLTX_POS] message attrs, auto generate do not change
        pass


class GC_STALL_SYNC (Packet):
    def handle(self):
        # begin handle [GC_STALL_SYNC] message attrs, auto generate do not change
        self.person['cursellcount'] = self['cursellcount']
        self.person['maxsellcount'] = self['maxsellcount']
        self.person['curbuycount'] = self['curbuycount']
        self.person['maxbuycount'] = self['maxbuycount']
        self.person['maxsellshelves'] = self['maxsellshelves']
        # end handle [GC_STALL_SYNC] message attrs, auto generate do not change
        pass


class CG_REQ_QUIT_GUILD_REALTIME_VOICE_ROOM (Packet):
    pass


class GC_AID_PUBLISH_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_AID_PUBLISH_CONFIG] message attrs, auto generate do not change
        self.person['name'] = self['name']
        self.person['guid'] = self['guid']
        self.person['misID'] = self['misID']
        self.person['misName'] = self['misName']
        # end handle [GC_AID_PUBLISH_CONFIG] message attrs, auto generate do not change
        pass


class CG_BWPVPFINAL_ASKGROUPINFO (Packet):
    pass


class CG_ASK_PERSONALREBATE (Packet):
    pass


class GC_ACHIEVEMENT_REWARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_ACHIEVEMENT_REWARD_INFO] message attrs, auto generate do not change
        self.person['rewardIDs'] = self['rewardIDs']
        # end handle [GC_ACHIEVEMENT_REWARD_INFO] message attrs, auto generate do not change
        pass


class GC_MULPVP_ANSWERLISTINFO (Packet):
    def handle(self):
        # begin handle [GC_MULPVP_ANSWERLISTINFO] message attrs, auto generate do not change
        self.person['inviterPlayerGuid'] = self['inviterPlayerGuid']
        self.person['remainTime'] = self['remainTime']
        self.person['thisIsLeader'] = self['thisIsLeader']
        self.person['memName'] = self['memName']
        self.person['memLev'] = self['memLev']
        self.person['proId'] = self['proId']
        self.person['answerState'] = self['answerState']
        self.person['isSelfMem'] = self['isSelfMem']
        self.person['memGuid'] = self['memGuid']
        self.person['sex'] = self['sex']
        # end handle [GC_MULPVP_ANSWERLISTINFO] message attrs, auto generate do not change
        pass


class GC_TEAM_RET_ACCEPT (Packet):
    def handle(self):
        # begin handle [GC_TEAM_RET_ACCEPT] message attrs, auto generate do not change
        self.person['memberGuid'] = self['memberGuid']
        self.person['teamID'] = self['teamID']
        # end handle [GC_TEAM_RET_ACCEPT] message attrs, auto generate do not change
        pass


class CG_PUBLISH_MENTOR_MESSAGE (Packet):
    pass


class CG_REQ_SCROLL_EXCHANGE_DATA (Packet):
    pass


class CG_TOWER_FIGHT_NEXT (Packet):
    pass


class GC_FASHION_PROLONG_RET (Packet):
    def handle(self):
        # begin handle [GC_FASHION_PROLONG_RET] message attrs, auto generate do not change
        self.person['FashionList'] = self['FashionList']
        # end handle [GC_FASHION_PROLONG_RET] message attrs, auto generate do not change
        pass


class CG_REQ_JIANMUXB_HELP (Packet):
    pass


class GC_GUILD_UPDATE_AUTHORITY (Packet):
    def handle(self):
        # begin handle [GC_GUILD_UPDATE_AUTHORITY] message attrs, auto generate do not change
        self.person['guildGuid'] = self['guildGuid']
        self.person['authority'] = self['authority']
        # end handle [GC_GUILD_UPDATE_AUTHORITY] message attrs, auto generate do not change
        pass


class CG_ITEMCOMPENSATE_GET (Packet):
    pass


class GC_SYC_FULL_RECENTCONTACT_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYC_FULL_RECENTCONTACT_LIST] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['BodyId'] = self['BodyId']
        self.person['FaceId'] = self['FaceId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairId'] = self['HairId']
        self.person['loverName'] = self['loverName']
        self.person['loverGuid'] = self['loverGuid']
        self.person['haveHuiliuIdentity'] = self['haveHuiliuIdentity']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['RmName'] = self['RmName']
        self.person['haveFestivalHuiliuIdentity'] = self['haveFestivalHuiliuIdentity']
        self.person['haveNewPlayerCatch'] = self['haveNewPlayerCatch']
        # end handle [GC_SYC_FULL_RECENTCONTACT_LIST] message attrs, auto generate do not change
        pass


class GC_GUILD_JOIN (Packet):
    def handle(self):
        # begin handle [GC_GUILD_JOIN] message attrs, auto generate do not change
        self.person['guildGuid'] = self['guildGuid']
        # end handle [GC_GUILD_JOIN] message attrs, auto generate do not change
        pass


class GC_RET_WORLDBOSS (Packet):
    def handle(self):
        # begin handle [GC_RET_WORLDBOSS] message attrs, auto generate do not change
        self.person['waitSec'] = self['waitSec']
        self.person['strMsg'] = self['strMsg']
        # end handle [GC_RET_WORLDBOSS] message attrs, auto generate do not change
        pass


class CG_REQ_QINYOU_FRIEND (Packet):
    pass


class CG_REQ_ACCEPT_TEACHER (Packet):
    pass


class CG_GODWEAPON_EQUIP (Packet):
    pass


class GC_ZHENFA_LEVELUP (Packet):
    def handle(self):
        # begin handle [GC_ZHENFA_LEVELUP] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        # end handle [GC_ZHENFA_LEVELUP] message attrs, auto generate do not change
        pass


class CG_LOGIN (Packet):
    pass


class GC_RET_RECEIVE_GUILD_GIFTPACKAGE (Packet):
    def handle(self):
        # begin handle [GC_RET_RECEIVE_GUILD_GIFTPACKAGE] message attrs, auto generate do not change
        self.person['result'] = self['result']
        # end handle [GC_RET_RECEIVE_GUILD_GIFTPACKAGE] message attrs, auto generate do not change
        pass


class GC_EQUIP_ENGRAVE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_EQUIP_ENGRAVE_RESULT] message attrs, auto generate do not change
        self.person['nResult'] = self['nResult']
        self.person['nEquipSlot'] = self['nEquipSlot']
        self.person['nAttrId'] = self['nAttrId']
        self.person['nCurExp'] = self['nCurExp']
        self.person['nCurLevel'] = self['nCurLevel']
        self.person['nCurResonanceLv'] = self['nCurResonanceLv']
        # end handle [GC_EQUIP_ENGRAVE_RESULT] message attrs, auto generate do not change
        pass


class GC_SPOKESMAN_SYNC_INFO (Packet):
    def handle(self):
        # begin handle [GC_SPOKESMAN_SYNC_INFO] message attrs, auto generate do not change
        self.person['FavorPoint'] = self['FavorPoint']
        self.person['FavorLevel'] = self['FavorLevel']
        self.person['EncounterDays'] = self['EncounterDays']
        # end handle [GC_SPOKESMAN_SYNC_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_LUCKY_CONNECT_SYNC (Packet):
    pass


class CG_ARMY_LEADER_RESET_COPYSCENE (Packet):
    pass


class CG_ASK_BUY_EXCITEM (Packet):
    pass


class GC_ORIENTATION_CHANGE (Packet):
    def handle(self):
        # begin handle [GC_ORIENTATION_CHANGE] message attrs, auto generate do not change
        self.person['professionOrientationParentID'] = self['professionOrientationParentID']
        self.person['professionOrientationChildID'] = self['professionOrientationChildID']
        self.person['armyid'] = self['armyid']
        self.person['teamindex'] = self['teamindex']
        # end handle [GC_ORIENTATION_CHANGE] message attrs, auto generate do not change
        pass


class CG_REQ_FRIEND_USERINFO (Packet):
    pass


class CG_REQ_CHAT_PLAYERINFO (Packet):
    pass


class GC_COPYSCENE_NAVIGATION (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_NAVIGATION] message attrs, auto generate do not change
        self.person['nType'] = self['nType']
        self.person['nSceneID'] = self['nSceneID']
        self.person['nPosx'] = self['nPosx']
        self.person['nPosy'] = self['nPosy']
        self.person['nPosz'] = self['nPosz']
        # end handle [GC_COPYSCENE_NAVIGATION] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_LEAVE (Packet):
    pass


class GC_STOP (Packet):
    def handle(self):
        # begin handle [GC_STOP] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['posserial'] = self['posserial']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        # end handle [GC_STOP] message attrs, auto generate do not change
        pass


class GC_UPDATE_CIRCLEDATA (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_CIRCLEDATA] message attrs, auto generate do not change
        self.person['nForceID'] = self['nForceID']
        self.person['nCurMisID'] = self['nCurMisID']
        self.person['nCircleID'] = self['nCircleID']
        self.person['nCurForceID'] = self['nCurForceID']
        self.person['nMisType'] = self['nMisType']
        self.person['nMisSubType'] = self['nMisSubType']
        # end handle [GC_UPDATE_CIRCLEDATA] message attrs, auto generate do not change
        pass


class GC_ACHIEVEMENT_VALUE_INFO (Packet):
    def handle(self):
        # begin handle [GC_ACHIEVEMENT_VALUE_INFO] message attrs, auto generate do not change
        self.person['achievementTypeIDs'] = self['achievementTypeIDs']
        self.person['value'] = self['value']
        # end handle [GC_ACHIEVEMENT_VALUE_INFO] message attrs, auto generate do not change
        pass


class GC_ADD_FAIRY_ATTR_POINTS_RET (Packet):
    def handle(self):
        # begin handle [GC_ADD_FAIRY_ATTR_POINTS_RET] message attrs, auto generate do not change
        self.person['bRet'] = self['bRet']
        # end handle [GC_ADD_FAIRY_ATTR_POINTS_RET] message attrs, auto generate do not change
        pass


class GC_PRESENT_ADD (Packet):
    def handle(self):
        # begin handle [GC_PRESENT_ADD] message attrs, auto generate do not change
        self.person['FriendGuid'] = self['FriendGuid']
        self.person['GoodsId'] = self['GoodsId']
        self.person['GoodsCount'] = self['GoodsCount']
        self.person['IsAnonymous'] = self['IsAnonymous']
        # end handle [GC_PRESENT_ADD] message attrs, auto generate do not change
        pass


class CG_HOME_MANAGER_GUSET (Packet):
    pass


class GC_PLAYERTIPSCHANGE (Packet):
    def handle(self):
        # begin handle [GC_PLAYERTIPSCHANGE] message attrs, auto generate do not change
        self.person['showattrchange'] = self['showattrchange']
        self.person['attrlist'] = self['attrlist']
        # end handle [GC_PLAYERTIPSCHANGE] message attrs, auto generate do not change
        pass


class CG_STALL_SELLINFO (Packet):
    pass


class GC_EXAM_ANSWERRESULT (Packet):
    def handle(self):
        # begin handle [GC_EXAM_ANSWERRESULT] message attrs, auto generate do not change
        self.person['reward'] = self['reward']
        self.person['rightAnswers'] = self['rightAnswers']
        self.person['errorAnswers'] = self['errorAnswers']
        self.person['timeInfo'] = self['timeInfo']
        self.person['question'] = self['question']
        self.person['answers'] = self['answers']
        self.person['questionIndex'] = self['questionIndex']
        self.person['examType'] = self['examType']
        # end handle [GC_EXAM_ANSWERRESULT] message attrs, auto generate do not change
        pass


class CG_WEDDING_CLOSE (Packet):
    pass


class GC_GWSKILL_SHOWHELP (Packet):
    def handle(self):
        # begin handle [GC_GWSKILL_SHOWHELP] message attrs, auto generate do not change
        self.person['Num'] = self['Num']
        # end handle [GC_GWSKILL_SHOWHELP] message attrs, auto generate do not change
        pass


class CG_WISHING_REQUEST_LOTTERY (Packet):
    pass


class GC_FLY_FASTSPEED_RET (Packet):
    def handle(self):
        # begin handle [GC_FLY_FASTSPEED_RET] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        self.person['openAutoFly'] = self['openAutoFly']
        # end handle [GC_FLY_FASTSPEED_RET] message attrs, auto generate do not change
        pass


class CG_REQ_GUILD_CHANGE_AUTOJOINSET (Packet):
    pass


class CG_ASK_CDTIME (Packet):
    pass


class GC_REBATE_STEPCONFIG (Packet):
    def handle(self):
        # begin handle [GC_REBATE_STEPCONFIG] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['open'] = self['open']
        self.person['preheatt'] = self['preheatt']
        self.person['begint'] = self['begint']
        self.person['endt'] = self['endt']
        self.person['step'] = self['step']
        self.person['ida'] = self['ida']
        self.person['numa'] = self['numa']
        self.person['idb'] = self['idb']
        self.person['numb'] = self['numb']
        self.person['idc'] = self['idc']
        self.person['numc'] = self['numc']
        self.person['idd'] = self['idd']
        self.person['numd'] = self['numd']
        self.person['ide'] = self['ide']
        self.person['nume'] = self['nume']
        self.person['rate'] = self['rate']
        self.person['introduction'] = self['introduction']
        self.person['icon'] = self['icon']
        self.person['HelpTitleId'] = self['HelpTitleId']
        self.person['HelpContentId'] = self['HelpContentId']
        # end handle [GC_REBATE_STEPCONFIG] message attrs, auto generate do not change
        pass


class GC_UPDATE_FAIRY_FORMATION (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_FAIRY_FORMATION] message attrs, auto generate do not change
        self.person['curFairyFormation'] = self['curFairyFormation']
        self.person['fairyGuid'] = self['fairyGuid']
        self.person['fairyFormationCollect'] = self['fairyFormationCollect']
        # end handle [GC_UPDATE_FAIRY_FORMATION] message attrs, auto generate do not change
        pass


class CG_REQ_CHANGE_FAIRY_VISUAL (Packet):
    pass


class GC_ASURA_TIME_SYNC (Packet):
    def handle(self):
        # begin handle [GC_ASURA_TIME_SYNC] message attrs, auto generate do not change
        self.person['enrollStart'] = self['enrollStart']
        self.person['enrollEnd'] = self['enrollEnd']
        self.person['level1Start'] = self['level1Start']
        self.person['level2Start'] = self['level2Start']
        self.person['level3Start'] = self['level3Start']
        self.person['level1End'] = self['level1End']
        self.person['level2End'] = self['level2End']
        self.person['level3End'] = self['level3End']
        # end handle [GC_ASURA_TIME_SYNC] message attrs, auto generate do not change
        pass


class GC_WAITPAY_DEL (Packet):
    def handle(self):
        # begin handle [GC_WAITPAY_DEL] message attrs, auto generate do not change
        self.person['BillGuid'] = self['BillGuid']
        # end handle [GC_WAITPAY_DEL] message attrs, auto generate do not change
        pass


class GC_SYNC_JXGZAWARDTABLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_JXGZAWARDTABLE] message attrs, auto generate do not change
        self.person['IsShow'] = self['IsShow']
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['NeedLv'] = self['NeedLv']
        self.person['AwardID'] = self['AwardID']
        self.person['LeftTime'] = self['LeftTime']
        self.person['Awards'] = self['Awards']
        # end handle [GC_SYNC_JXGZAWARDTABLE] message attrs, auto generate do not change
        pass


class GC_CHANGESCENE_DYNAMICLEVEL (Packet):
    def handle(self):
        # begin handle [GC_CHANGESCENE_DYNAMICLEVEL] message attrs, auto generate do not change
        self.person['opendynamiclevel'] = self['opendynamiclevel']
        # end handle [GC_CHANGESCENE_DYNAMICLEVEL] message attrs, auto generate do not change
        pass


class GC_SYNC_PAYACT_CONFIG_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PAYACT_CONFIG_DATA] message attrs, auto generate do not change
        self.person['m_PA_MonthAccrual_RebuyDays'] = self['m_PA_MonthAccrual_RebuyDays']
        self.person['m_MonthCardList'] = self['m_MonthCardList']
        self.person['m_GrowUpBoundaryLevel'] = self['m_GrowUpBoundaryLevel']
        self.person['m_GrowUpReturnYuanBaoList'] = self['m_GrowUpReturnYuanBaoList']
        self.person['m_GrowUpReturnYuanBaoExList'] = self['m_GrowUpReturnYuanBaoExList']
        self.person['m_DailyLimitedGiftConfigList'] = self['m_DailyLimitedGiftConfigList']
        self.person['nStartWorkNeedActivitiness'] = self['nStartWorkNeedActivitiness']
        self.person['m_StartWorkGiftConfigList'] = self['m_StartWorkGiftConfigList']
        self.person['m_GrowUpLevelList'] = self['m_GrowUpLevelList']
        self.person['m_DailyLimitedGiftFreeAwardList'] = self['m_DailyLimitedGiftFreeAwardList']
        # end handle [GC_SYNC_PAYACT_CONFIG_DATA] message attrs, auto generate do not change
        pass


class CG_SHEDAOSAIMA_ASK_USEDAOJU (Packet):
    pass


class CG_SKILL_SWITCH_TYPE_SKILL (Packet):
    pass


class CG_AUCTION_ASKSELLLIST (Packet):
    pass


class GC_RET_RELATFRIEND_STATUS (Packet):
    def handle(self):
        # begin handle [GC_RET_RELATFRIEND_STATUS] message attrs, auto generate do not change
        self.person['friendaccount'] = self['account']
        self.person['fgsend'] = self['fgsend']
        self.person['fgrecv'] = self['fgrecv']
        self.person['loginsync'] = self['loginsync']
        self.person['maxsend'] = self['maxsend']
        self.person['maxrecv'] = self['maxrecv']
        self.person['remainsend'] = self['remainsend']
        self.person['remainrecv'] = self['remainrecv']
        # end handle [GC_RET_RELATFRIEND_STATUS] message attrs, auto generate do not change
        pass


class CG_ASK_CHRISTMAS_DATA (Packet):
    pass


class CG_UPLOAD_CUSTOMHEAD_SUCCESS (Packet):
    pass


class GC_SYNC_LEVELUP_RED_POINT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_LEVELUP_RED_POINT] message attrs, auto generate do not change
        self.person['levelupRedPoint'] = self['levelupRedPoint']
        # end handle [GC_SYNC_LEVELUP_RED_POINT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_UPDATE_FAIRY] message attrs, auto generate do not change
        self.person['packindex'] = self['packindex']
        self.person['fairy'] = self['fairy']
        # end handle [GC_UPDATE_FAIRY] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_INVITE_BIRTHDAY (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_INVITE_BIRTHDAY] message attrs, auto generate do not change
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberProf'] = self['memberProf']
        self.person['memberSex'] = self['memberSex']
        self.person['confirmed'] = self['confirmed']
        self.person['inviterGuid'] = self['inviterGuid']
        # end handle [GC_BROTHERHOOD_INVITE_BIRTHDAY] message attrs, auto generate do not change
        pass


class GC_READY_CONFIRM_RET (Packet):
    def handle(self):
        # begin handle [GC_READY_CONFIRM_RET] message attrs, auto generate do not change
        self.person['state'] = self['state']
        # end handle [GC_READY_CONFIRM_RET] message attrs, auto generate do not change
        pass


class CG_EQUIPMIRROR_PURIFY_REPLACEATTR (Packet):
    pass


class GC_USE_SKILL_XML_MainPlayer (Packet):
    def handle(self):
        # begin handle [GC_USE_SKILL_XML_MainPlayer] message attrs, auto generate do not change
        self.person['skillId'] = self['skillId']
        self.person['TargetId'] = self['TargetId']
        # end handle [GC_USE_SKILL_XML_MainPlayer] message attrs, auto generate do not change
        loadlog.debug(__class__.__name__)
        loadlog.debug(self.obj)
        pass


class GC_BATTLEFIELD_RES_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_RES_UPDATE] message attrs, auto generate do not change
        self.person['Index'] = self['Index']
        self.person['OwnerGroupID'] = self['OwnerGroupID']
        self.person['State'] = self['State']
        self.person['GroupAPlayerNum'] = self['GroupAPlayerNum']
        self.person['GroupBPlayerNum'] = self['GroupBPlayerNum']
        self.person['Progress'] = self['Progress']
        self.person['PosX'] = self['PosX']
        self.person['PosY'] = self['PosY']
        self.person['PosZ'] = self['PosZ']
        self.person['ResObjID'] = self['ResObjID']
        # end handle [GC_BATTLEFIELD_RES_UPDATE] message attrs, auto generate do not change
        pass


class GC_SYNC_HOME_PRAY_ATTR (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HOME_PRAY_ATTR] message attrs, auto generate do not change
        self.person['prayAttrID'] = self['prayAttrID']
        self.person['prayAttrVal'] = self['prayAttrVal']
        self.person['altAttrID'] = self['altAttrID']
        self.person['altAttrVal'] = self['altAttrVal']
        self.person['prayTime'] = self['prayTime']
        self.person['dailyPrayCount'] = self['dailyPrayCount']
        # end handle [GC_SYNC_HOME_PRAY_ATTR] message attrs, auto generate do not change
        pass


class CG_TONGTIANTREASURE_REQOP (Packet):
    pass


class CG_FASHION_RANDOM_COLOR (Packet):
    pass


class GC_FAIRY_USE_SKILL (Packet):
    def handle(self):
        # begin handle [GC_FAIRY_USE_SKILL] message attrs, auto generate do not change
        self.person['skillId'] = self['skillId']
        self.person['senderId'] = self['senderId']
        self.person['TargetId'] = self['TargetId']
        # end handle [GC_FAIRY_USE_SKILL] message attrs, auto generate do not change
        pass


class CG_HUILIU_STATE (Packet):
    pass


class CG_GUILDMONSTER_UNLOCK (Packet):
    pass


class GC_SUCCESS_BP_COUPLE (Packet):
    def handle(self):
        # begin handle [GC_SUCCESS_BP_COUPLE] message attrs, auto generate do not change
        self.person['nOrderId'] = self['nOrderId']
        self.person['nWorkCoupleResult'] = self['nWorkCoupleResult']
        # end handle [GC_SUCCESS_BP_COUPLE] message attrs, auto generate do not change
        pass


class GC_SYNC_XCTJAWARDTABLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_XCTJAWARDTABLE] message attrs, auto generate do not change
        self.person['IsShow'] = self['IsShow']
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['NeedLv'] = self['NeedLv']
        self.person['AwardDay'] = self['AwardDay']
        self.person['id'] = self['id']
        self.person['lefttime'] = self['lefttime']
        self.person['bindYB'] = self['bindYB']
        self.person['BindGold'] = self['BindGold']
        self.person['BindSilver'] = self['BindSilver']
        self.person['itemdataid1'] = self['itemdataid1']
        self.person['itemcount1'] = self['itemcount1']
        self.person['itemRefineLv1'] = self['itemRefineLv1']
        self.person['itemdataid2'] = self['itemdataid2']
        self.person['itemcount2'] = self['itemcount2']
        self.person['itemRefineLv2'] = self['itemRefineLv2']
        self.person['ShowLv'] = self['ShowLv']
        self.person['Model1'] = self['Model1']
        self.person['Model2'] = self['Model2']
        # end handle [GC_SYNC_XCTJAWARDTABLE] message attrs, auto generate do not change
        pass


class GC_UPDATE_SKILLZHUANJING_UNLOCK_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_SKILLZHUANJING_UNLOCK_INFO] message attrs, auto generate do not change
        self.person['nSkillZhuanjingId'] = self['nSkillZhuanjingId']
        self.person['bUnlockFlag'] = self['bUnlockFlag']
        self.person['bIsAuto'] = self['bIsAuto']
        self.person['bNewUnlock'] = self['bNewUnlock']
        # end handle [GC_UPDATE_SKILLZHUANJING_UNLOCK_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_HOME_HORDE_COLLECTION (Packet):
    pass


class GC_RET_WORLD_GROUPINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_WORLD_GROUPINFO] message attrs, auto generate do not change
        self.person['bigworldid'] = self['bigworldid']
        self.person['bigworldname'] = self['bigworldname']
        self.person['originworldid'] = self['originworldid']
        self.person['originworldname'] = self['originworldname']
        # end handle [GC_RET_WORLD_GROUPINFO] message attrs, auto generate do not change
        pass


class GC_GUILD_RET_SETADDITION_TIME (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_SETADDITION_TIME] message attrs, auto generate do not change
        self.person['changeGuildAdditionTime'] = self['changeGuildAdditionTime']
        self.person['guildOpenAddition'] = self['guildOpenAddition']
        # end handle [GC_GUILD_RET_SETADDITION_TIME] message attrs, auto generate do not change
        pass


class CG_REQ_USE_GUILD_FLAG (Packet):
    pass


class CG_MOVE (Packet):
    pass


class CG_NOTIFY_ARMY_CHANGE_RTMEMBERINFO (Packet):
    pass


class GC_RET_ADVENTURE_ACCEPT (Packet):
    def handle(self):
        # begin handle [GC_RET_ADVENTURE_ACCEPT] message attrs, auto generate do not change
        self.person['awardId'] = self['awardId']
        # end handle [GC_RET_ADVENTURE_ACCEPT] message attrs, auto generate do not change
        pass


class GC_MERCENARY_LIST_RES (Packet):
    def handle(self):
        # begin handle [GC_MERCENARY_LIST_RES] message attrs, auto generate do not change
        # end handle [GC_MERCENARY_LIST_RES] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_INVITE_CONFIRM (Packet):
    pass


class GC_CANCEL_AUTOCOMBAT (Packet):
    def handle(self):
        # begin handle [GC_CANCEL_AUTOCOMBAT] message attrs, auto generate do not change
        # end handle [GC_CANCEL_AUTOCOMBAT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_RET_SHOWRECHARGE] message attrs, auto generate do not change
        self.person['bShow'] = self['bShow']
        # end handle [GC_RET_SHOWRECHARGE] message attrs, auto generate do not change
        pass


class GC_ADDAPPLYLIST (Packet):
    def handle(self):
        # begin handle [GC_ADDAPPLYLIST] message attrs, auto generate do not change
        suffix = str(self['guid'] % 10000)
        recv_apply_key = 'recv_apply_' + suffix
        self.person[recv_apply_key] = {}
        self.person[recv_apply_key]['guid'] = self['guid']
        self.person[recv_apply_key]['Name'] = self['Name']
        self.person[recv_apply_key]['Level'] = self['Level']
        self.person[recv_apply_key]['Prof'] = self['Prof']
        self.person[recv_apply_key]['Combat'] = self['Combat']
        self.person[recv_apply_key]['State'] = self['State']
        self.person[recv_apply_key]['TimeInfo'] = self['TimeInfo']
        self.person[recv_apply_key]['RelationPoint'] = self['RelationPoint']
        self.person[recv_apply_key]['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person[recv_apply_key]['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person[recv_apply_key]['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person[recv_apply_key]['VoiceSignName'] = self['VoiceSignName']
        self.person[recv_apply_key]['TextSign'] = self['TextSign']
        self.person[recv_apply_key]['Sex'] = self['Sex']
        self.person[recv_apply_key]['Birthday'] = self['Birthday']
        self.person[recv_apply_key]['PersonalLocation'] = self['PersonalLocation']
        self.person[recv_apply_key]['Reserved'] = self['Reserved']
        self.person[recv_apply_key]['DelFriendTime'] = self['DelFriendTime']
        self.person[recv_apply_key]['ReportFlag'] = self['ReportFlag']
        self.person[recv_apply_key]['PhotoFrameId'] = self['PhotoFrameId']
        self.person[recv_apply_key]['ReportCount'] = self['ReportCount']
        if not self.person['applylist']:
            self.person['applylist'] = []
        self.person['applylist'].append(self.person[recv_apply_key])
        # end handle [GC_ADDAPPLYLIST] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_GUILD_LEAVE] message attrs, auto generate do not change
        self.person['guildGuid'] = self['guildGuid']
        # end handle [GC_GUILD_LEAVE] message attrs, auto generate do not change
        pass


class GC_STALL_REVIEW_ADD (Packet):
    def handle(self):
        # begin handle [GC_STALL_REVIEW_ADD] message attrs, auto generate do not change
        self.person['StallGuid'] = self['StallGuid']
        self.person['StallState'] = self['StallState']
        self.person['SellItemId'] = self['SellItemId']
        self.person['SellFellowId'] = self['SellFellowId']
        self.person['SellCount'] = self['SellCount']
        self.person['ReviewMoney'] = self['ReviewMoney']
        self.person['StallTime'] = self['StallTime']
        self.person['IsGold'] = self['IsGold']
        # end handle [GC_STALL_REVIEW_ADD] message attrs, auto generate do not change
        pass


class GC_SHEDAISAIMA_PLAYERRACEHLINE (Packet):
    def handle(self):
        # begin handle [GC_SHEDAISAIMA_PLAYERRACEHLINE] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['mingci'] = self['mingci']
        # end handle [GC_SHEDAISAIMA_PLAYERRACEHLINE] message attrs, auto generate do not change
        pass


class GC_SYNC_GODWEAPON_PACK (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GODWEAPON_PACK] message attrs, auto generate do not change
        self.person['Elems'] = self['Elems']
        self.person['OpType'] = self['OpType']
        self.person['CurEquipPos'] = self['CurEquipPos']
        self.person['MaxPackSize'] = self['MaxPackSize']
        self.person['SchemeId'] = self['SchemeId']
        # end handle [GC_SYNC_GODWEAPON_PACK] message attrs, auto generate do not change
        pass


class GC_RET_EXCHANGE_GUILD_MONSTER_BUFF (Packet):
    def handle(self):
        # begin handle [GC_RET_EXCHANGE_GUILD_MONSTER_BUFF] message attrs, auto generate do not change
        self.person['pakSource'] = self['pakSource']
        self.person['selfMonsterScore'] = self['selfMonsterScore']
        self.person['oldBuffId'] = self['oldBuffId']
        self.person['newBuffId'] = self['newBuffId']
        # end handle [GC_RET_EXCHANGE_GUILD_MONSTER_BUFF] message attrs, auto generate do not change
        pass


class GC_SYNC_IOS_REVIEW_EVENT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_IOS_REVIEW_EVENT] message attrs, auto generate do not change
        self.person['nEventId'] = self['nEventId']
        # end handle [GC_SYNC_IOS_REVIEW_EVENT] message attrs, auto generate do not change
        pass


class CG_NPCGIFTEXCHANGE_SYNC_STATUE (Packet):
    pass


class GC_SYNC_INSCRIPTION_SLOT_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_INSCRIPTION_SLOT_DATA] message attrs, auto generate do not change
        self.person['slotDatas'] = self['slotDatas']
        # end handle [GC_SYNC_INSCRIPTION_SLOT_DATA] message attrs, auto generate do not change
        pass


class CG_GUILD_JOIN (Packet):
    pass


class GC_PLAY_SOUND (Packet):
    def handle(self):
        # begin handle [GC_PLAY_SOUND] message attrs, auto generate do not change
        self.person['SoundID'] = self['SoundID']
        self.person['SoundType'] = self['SoundType']
        # end handle [GC_PLAY_SOUND] message attrs, auto generate do not change
        pass


class CG_REQ_NEAR_LIST (Packet):
    pass


class GC_BATTLEFIELD_STATE (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_STATE] message attrs, auto generate do not change
        self.person['CurState'] = self['CurState']
        self.person['CurStateLeftTime'] = self['CurStateLeftTime']
        self.person['EndTime'] = self['EndTime']
        # end handle [GC_BATTLEFIELD_STATE] message attrs, auto generate do not change
        pass


class CG_PICK_COLOR_ITEM_STORAGE (Packet):
    pass


class CG_UPDATE_XIAOK_REDDOT (Packet):
    pass


class GC_SYNC_GUILD_REAMTIME_VOICEROOM_MEMBERINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_REAMTIME_VOICEROOM_MEMBERINFO] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['syncType'] = self['syncType']
        self.person['roomType'] = self['roomType']
        self.person['roomId'] = self['roomId']
        self.person['roomMemeberInfo'] = self['roomMemeberInfo']
        # end handle [GC_SYNC_GUILD_REAMTIME_VOICEROOM_MEMBERINFO] message attrs, auto generate do not change
        pass


class CG_REQ_EQUIP_ENCHANT (Packet):
    pass


class CG_PUT_CONVO (Packet):
    pass


class GC_NOTIFY_CHANGETOBIGWORLD (Packet):
    def handle(self):
        # begin handle [GC_NOTIFY_CHANGETOBIGWORLD] message attrs, auto generate do not change
        # end handle [GC_NOTIFY_CHANGETOBIGWORLD] message attrs, auto generate do not change
        pass


class GC_SYNC_IDIP_REDDOT_TIPS (Packet):
    def handle(self):
        # begin handle [GC_SYNC_IDIP_REDDOT_TIPS] message attrs, auto generate do not change
        self.person['bCommunityTips'] = self['bCommunityTips']
        self.person['bChaoYueTips'] = self['bChaoYueTips']
        self.person['bWuLinDaHuiTips'] = self['bWuLinDaHuiTips']
        # end handle [GC_SYNC_IDIP_REDDOT_TIPS] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_CREATE_TRY (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_CREATE_TRY] message attrs, auto generate do not change
        self.person['code'] = self['code']
        # end handle [GC_BROTHERHOOD_CREATE_TRY] message attrs, auto generate do not change
        pass


class GC_SYNC_RUBKICUE_ENERGY_COUNT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RUBKICUE_ENERGY_COUNT] message attrs, auto generate do not change
        self.person['curEnergyCount'] = self['curEnergyCount']
        self.person['maxEnergyCount'] = self['maxEnergyCount']
        # end handle [GC_SYNC_RUBKICUE_ENERGY_COUNT] message attrs, auto generate do not change
        pass


class GC_GUILD_RET_LIST (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_LIST] message attrs, auto generate do not change
        self.person['preserveGuildGuid'] = self['preserveGuildGuid']
        self.person['guildGuid'] = self['guildGuid']
        self.person['guildName'] = self['guildName']
        self.person['guildChiefName'] = self['guildChiefName']
        self.person['guildChiefGuid'] = self['guildChiefGuid']
        self.person['guildChiefProf'] = self['guildChiefProf']
        self.person['guildLevel'] = self['guildLevel']
        self.person['guildMemberNum'] = self['guildMemberNum']
        self.person['guildCombat'] = self['guildCombat']
        self.person['isEnemyGuild'] = self['isEnemyGuild']
        self.person['guildApplyNum'] = self['guildApplyNum']
        self.person['guildApplyMaxNum'] = self['guildApplyMaxNum']
        self.person['guildVitality'] = self['guildVitality']
        self.person['guildShortName'] = self['guildShortName']
        self.person['guildShortNameColor'] = self['guildShortNameColor']
        self.person['guildNotice'] = self['guildNotice']
        self.person['guildIsStudio'] = self['guildIsStudio']
        self.person['guildLabelType'] = self['guildLabelType']
        self.person['guildLabelValue'] = self['guildLabelValue']
        self.person['guildLabelScore'] = self['guildLabelScore']
        self.person['guildTotalVitality'] = self['guildTotalVitality']
        self.person['guildHealthRate'] = self['guildHealthRate']
        self.person['customHeadPic'] = self['customHeadPic']
        # end handle [GC_GUILD_RET_LIST] message attrs, auto generate do not change
        pass


class GC_LEVELUP_BUILDING (Packet):
    def handle(self):
        # begin handle [GC_LEVELUP_BUILDING] message attrs, auto generate do not change
        self.person['m_Result'] = self['m_Result']
        self.person['m_HomeGuid'] = self['m_HomeGuid']
        self.person['m_OldFunctionGuid'] = self['m_OldFunctionGuid']
        self.person['m_NewFunctionGuid'] = self['m_NewFunctionGuid']
        # end handle [GC_LEVELUP_BUILDING] message attrs, auto generate do not change
        pass


class CG_REQ_MARRAY_RECURIT (Packet):
    pass


class GC_SKILL_FINISH (Packet):
    def handle(self):
        # begin handle [GC_SKILL_FINISH] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['FinishType'] = self['FinishType']
        self.person['FinishSkillId'] = self['FinishSkillId']
        self.person['ErrorIndex'] = self['ErrorIndex']
        # end handle [GC_SKILL_FINISH] message attrs, auto generate do not change
        loadlog.debug(__class__.__name__)
        loadlog.debug(self.obj)
        pass


class GC_DOMAINWAR_SCENENINFO (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_SCENENINFO] message attrs, auto generate do not change
        self.person['domaininfo'] = self['domaininfo']
        # end handle [GC_DOMAINWAR_SCENENINFO] message attrs, auto generate do not change
        pass


class CG_PGL_REQ_MATCH (Packet):
    pass


class CG_ZHENFA_UNLOCK (Packet):
    pass


class CG_RET_ROLE_SHARE_DATA (Packet):
    pass


class GC_PRESTIGE_TODAYWILDNUMMAX (Packet):
    def handle(self):
        # begin handle [GC_PRESTIGE_TODAYWILDNUMMAX] message attrs, auto generate do not change
        self.person['todaywildnummax'] = self['todaywildnummax']
        # end handle [GC_PRESTIGE_TODAYWILDNUMMAX] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_FREE_HOME_SETTLE] message attrs, auto generate do not change
        self.person['HasFreeSettle'] = self['HasFreeSettle']
        # end handle [GC_SYNC_FREE_HOME_SETTLE] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SEND_FAIRY_EGG_RESULT] message attrs, auto generate do not change
        self.person['fairy'] = self['fairy']
        # end handle [GC_SEND_FAIRY_EGG_RESULT] message attrs, auto generate do not change
        pass


class CG_PUBLISH_HOME_LINK (Packet):
    pass


class GC_RES_JIANMUXB_REWARD (Packet):
    def handle(self):
        # begin handle [GC_RES_JIANMUXB_REWARD] message attrs, auto generate do not change
        self.person['getRewardLv'] = self['getRewardLv']
        # end handle [GC_RES_JIANMUXB_REWARD] message attrs, auto generate do not change
        pass


class CG_ASK_COMMIT_GUILD_MONSTER_ITEM (Packet):
    pass


class GC_AIRBUS_DATA (Packet):
    def handle(self):
        # begin handle [GC_AIRBUS_DATA] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['airbusstat'] = self['airbusstat']
        self.person['airlineid'] = self['airlineid']
        self.person['nextairpathidx'] = self['nextairpathidx']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        # end handle [GC_AIRBUS_DATA] message attrs, auto generate do not change
        pass


class GC_RET_MIRRORLASTPURIFY_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_MIRRORLASTPURIFY_INFO] message attrs, auto generate do not change
        self.person['Equipguid'] = self['Equipguid']
        self.person['AttrId'] = self['AttrId']
        self.person['AttrVal'] = self['AttrVal']
        self.person['AttrType'] = self['AttrType']
        self.person['BuffId'] = self['BuffId']
        # end handle [GC_RET_MIRRORLASTPURIFY_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_RET_FAIRY_EVOLVE] message attrs, auto generate do not change
        self.person['fairyGuid'] = self['fairyGuid']
        self.person['success'] = self['success']
        # end handle [GC_RET_FAIRY_EVOLVE] message attrs, auto generate do not change
        pass


class GC_MAIL_DELETE (Packet):
    def handle(self):
        # begin handle [GC_MAIL_DELETE] message attrs, auto generate do not change
        self.person['MailGuid'] = self['MailGuid']
        # end handle [GC_MAIL_DELETE] message attrs, auto generate do not change
        pass


class GC_CLIENT_RELIVE (Packet):
    def handle(self):
        # begin handle [GC_CLIENT_RELIVE] message attrs, auto generate do not change
        self.person['reliveType'] = self['reliveType']
        # end handle [GC_CLIENT_RELIVE] message attrs, auto generate do not change
        pass


class GC_GODWEAPON_SYNC_CD (Packet):
    def handle(self):
        # begin handle [GC_GODWEAPON_SYNC_CD] message attrs, auto generate do not change
        self.person['StartTime'] = self['StartTime']
        self.person['CurState'] = self['CurState']
        self.person['SecStartTime'] = self['SecStartTime']
        self.person['TargetSkillId'] = self['TargetSkillId']
        # end handle [GC_GODWEAPON_SYNC_CD] message attrs, auto generate do not change
        pass


class CG_GET_WORDREDPACKETRAIN_AWARD (Packet):
    pass


class GC_SECPASSWORD_CLIENTINFO (Packet):
    def handle(self):
        # begin handle [GC_SECPASSWORD_CLIENTINFO] message attrs, auto generate do not change
        self.person['redpoint'] = self['redpoint']
        self.person['canclepasswordtime'] = self['canclepasswordtime']
        self.person['issetsecpassword'] = self['issetsecpassword']
        # end handle [GC_SECPASSWORD_CLIENTINFO] message attrs, auto generate do not change
        pass


class GC_GUILD_ASK_DIG_UP_THE_HATCHET (Packet):
    def handle(self):
        # begin handle [GC_GUILD_ASK_DIG_UP_THE_HATCHET] message attrs, auto generate do not change
        self.person['targetGuildGuid'] = self['targetGuildGuid']
        self.person['targetGuildName'] = self['targetGuildName']
        # end handle [GC_GUILD_ASK_DIG_UP_THE_HATCHET] message attrs, auto generate do not change
        pass


class GC_COPYSCENE_EXITEFFECT (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_EXITEFFECT] message attrs, auto generate do not change
        # end handle [GC_COPYSCENE_EXITEFFECT] message attrs, auto generate do not change
        pass


class CG_BATTLEFIELD_SIGNUP (Packet):
    pass


class CG_DOMAIN_REQ_DECLAREWAR (Packet):
    pass


class GC_GUILD_RET_LEVELUPFINISH (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_LEVELUPFINISH] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['level'] = self['level']
        # end handle [GC_GUILD_RET_LEVELUPFINISH] message attrs, auto generate do not change
        pass


class GC_SYNC_FIRST_ENTERCOPYSCENE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FIRST_ENTERCOPYSCENE] message attrs, auto generate do not change
        # end handle [GC_SYNC_FIRST_ENTERCOPYSCENE] message attrs, auto generate do not change
        pass


class GC_CREATE_ZOMBIEPLAYER (Packet):
    def handle(self):
        # begin handle [GC_CREATE_ZOMBIEPLAYER] message attrs, auto generate do not change
        self.person['charBaseAttr'] = self['charBaseAttr']
        self.person['sceneInst'] = self['sceneInst']
        self.person['sceneClass'] = self['sceneClass']
        self.person['profession'] = self['profession']
        self.person['sex'] = self['sex']
        self.person['bodyVisualId'] = self['bodyVisualId']
        self.person['weaponVisualId'] = self['weaponVisualId']
        self.person['faceVisualId'] = self['faceVisualId']
        self.person['FollowTargetObjId'] = self['FollowTargetObjId']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairVisualId'] = self['HairVisualId']
        self.person['BWPvPEffigyIndex'] = self['BWPvPEffigyIndex']
        self.person['BodyColorvisual'] = self['BodyColorvisual']
        self.person['nierenvalue'] = self['nierenvalue']
        self.person['guid'] = self['guid']
        self.person['BattleFairyId'] = self['BattleFairyId']
        self.person['FairyTargetId'] = self['FairyTargetId']
        self.person['zombietype'] = self['zombietype']
        self.person['szParam'] = self['szParam']
        self.person['intParam'] = self['intParam']
        self.person['BodyColorIndex'] = self['BodyColorIndex']
        self.person['HairColorIndex'] = self['HairColorIndex']
        self.person['WeaponColorIndex'] = self['WeaponColorIndex']
        self.person['BodyFashionId'] = self['BodyFashionId']
        self.person['HairFashionId'] = self['HairFashionId']
        self.person['WeaponFashionId'] = self['WeaponFashionId']
        self.person['accountname'] = self['accountname']
        self.person['bios'] = self['bios']
        self.person['BattleFairyEvolvePhase'] = self['BattleFairyEvolvePhase']
        self.person['UseBodyFreeDyeSlotId'] = self['UseBodyFreeDyeSlotId']
        self.person['UseHairFreeDyeSlotId'] = self['UseHairFreeDyeSlotId']
        self.person['BodyFreeDyeColorInfo'] = self['BodyFreeDyeColorInfo']
        self.person['HairFreeDyeColorInfo'] = self['HairFreeDyeColorInfo']
        self.person['BackFashionId'] = self['BackFashionId']
        self.person['BackColorIndex'] = self['BackColorIndex']
        self.person['BuffTransId'] = self['BuffTransId']
        self.person['StrFirstTitleContent'] = self['StrFirstTitleContent']
        self.person['StrSecondTitleContent'] = self['StrSecondTitleContent']
        self.person['CurTitleID'] = self['CurTitleID']
        self.person['AircraftId'] = self['AircraftId']
        # end handle [GC_CREATE_ZOMBIEPLAYER] message attrs, auto generate do not change
        pass


class GC_BEGIN_CHOOSE_REWARDBOX (Packet):
    def handle(self):
        # begin handle [GC_BEGIN_CHOOSE_REWARDBOX] message attrs, auto generate do not change
        self.person['BoxGuid'] = self['BoxGuid']
        # end handle [GC_BEGIN_CHOOSE_REWARDBOX] message attrs, auto generate do not change
        pass


class GC_PRAYEXP_SYNC (Packet):
    def handle(self):
        # begin handle [GC_PRAYEXP_SYNC] message attrs, auto generate do not change
        self.person['PrayExp_Activity_Normal'] = self['PrayExp_Activity_Normal']
        self.person['PrayExp_PoolVal'] = self['PrayExp_PoolVal']
        self.person['IsDayReset'] = self['IsDayReset']
        # end handle [GC_PRAYEXP_SYNC] message attrs, auto generate do not change
        pass


class GC_DEBUGSYNCPOS (Packet):
    def handle(self):
        # begin handle [GC_DEBUGSYNCPOS] message attrs, auto generate do not change
        self.person['targetPosX'] = self['targetPosX']
        self.person['targetPosY'] = self['targetPosY']
        self.person['targetPosZ'] = self['targetPosZ']
        # end handle [GC_DEBUGSYNCPOS] message attrs, auto generate do not change
        pass


class CG_REBATE_ASKINFO (Packet):
    pass


class CG_REQ_HOME_REGION_INFO (Packet):
    pass


class CG_HUILIULIMITSHOP_REQ (Packet):
    pass


class GC_REMIND_SET_OR_INPUT_SECPASSWORD (Packet):
    def handle(self):
        # begin handle [GC_REMIND_SET_OR_INPUT_SECPASSWORD] message attrs, auto generate do not change
        self.person['pushtype'] = self['pushtype']
        self.person['optiontype'] = self['optiontype']
        self.person['releastype'] = self['releastype']
        # end handle [GC_REMIND_SET_OR_INPUT_SECPASSWORD] message attrs, auto generate do not change
        pass


class CG_REQ_RESET_HOME_STYLE (Packet):
    pass


class CG_GUILD_REQ_STOP_DEMISE (Packet):
    pass


class GC_STALL_RETRECORD (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETRECORD] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['targetguid'] = self['targetguid']
        self.person['targetname'] = self['targetname']
        self.person['price'] = self['price']
        self.person['itemid'] = self['itemid']
        self.person['reserved'] = self['reserved']
        self.person['recordtime'] = self['recordtime']
        self.person['stackcount'] = self['stackcount']
        # end handle [GC_STALL_RETRECORD] message attrs, auto generate do not change
        pass


class GC_STALL_APPEAL (Packet):
    def handle(self):
        # begin handle [GC_STALL_APPEAL] message attrs, auto generate do not change
        self.person['StallGuid'] = self['StallGuid']
        self.person['AppealStartTime'] = self['AppealStartTime']
        # end handle [GC_STALL_APPEAL] message attrs, auto generate do not change
        pass


class GC_ACCLOGIN_SYNCINFO (Packet):
    def handle(self):
        # begin handle [GC_ACCLOGIN_SYNCINFO] message attrs, auto generate do not change
        self.person['version'] = self['version']
        self.person['name'] = self['name']
        self.person['startDate'] = self['startDate']
        self.person['startTime'] = self['startTime']
        self.person['endDate'] = self['endDate']
        self.person['endTime'] = self['endTime']
        self.person['duration'] = self['duration']
        self.person['showLevel'] = self['showLevel']
        self.person['openLevel'] = self['openLevel']
        self.person['awardIndex'] = self['awardIndex']
        self.person['awardContent'] = self['awardContent']
        self.person['param1'] = self['param1']
        self.person['param2'] = self['param2']
        self.person['param3'] = self['param3']
        self.person['param4'] = self['param4']
        self.person['param5'] = self['param5']
        # end handle [GC_ACCLOGIN_SYNCINFO] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILD_ACTIVITY_OPEN_TIME (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_ACTIVITY_OPEN_TIME] message attrs, auto generate do not change
        self.person['openTime'] = self['openTime']
        # end handle [GC_SYNC_GUILD_ACTIVITY_OPEN_TIME] message attrs, auto generate do not change
        pass


class GC_SHEDAOSAIMA_USEDAOJUMESSAGE (Packet):
    def handle(self):
        # begin handle [GC_SHEDAOSAIMA_USEDAOJUMESSAGE] message attrs, auto generate do not change
        self.person['PlayerName'] = self['PlayerName']
        self.person['DaoJuId'] = self['DaoJuId']
        # end handle [GC_SHEDAOSAIMA_USEDAOJUMESSAGE] message attrs, auto generate do not change
        pass


class GC_FLY_AIRCRAFTCOLLECTED_FLAG (Packet):
    def handle(self):
        # begin handle [GC_FLY_AIRCRAFTCOLLECTED_FLAG] message attrs, auto generate do not change
        self.person['AutoAircraftFlag'] = self['AutoAircraftFlag']
        self.person['CurAircraftID'] = self['CurAircraftID']
        self.person['AircraftCollectedFlag'] = self['AircraftCollectedFlag']
        self.person['AircraftLeftTime'] = self['AircraftLeftTime']
        # end handle [GC_FLY_AIRCRAFTCOLLECTED_FLAG] message attrs, auto generate do not change
        pass


class CG_QUEST_CHANGETO_ORIGINWORLD (Packet):
    pass


class CG_REQ_GUILD_WAR_SIGN_UP (Packet):
    pass


class CG_GUILD_INVITE_CONFIRM (Packet):
    pass


class GC_SYNC_FRIENDS_MUTUALHELP_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FRIENDS_MUTUALHELP_DATA] message attrs, auto generate do not change
        self.person['nCompletedActionList'] = self['nCompletedActionList']
        self.person['bNeedRedTips'] = self['bNeedRedTips']
        self.person['nIdList'] = self['nIdList']
        self.person['nTypeList'] = self['nTypeList']
        self.person['nOpenDayList'] = self['nOpenDayList']
        self.person['nItemIdList'] = self['nItemIdList']
        self.person['nItemNumList'] = self['nItemNumList']
        self.person['nTriggerActionTimeList'] = self['nTriggerActionTimeList']
        # end handle [GC_SYNC_FRIENDS_MUTUALHELP_DATA] message attrs, auto generate do not change
        pass


class GC_RES_JIANMUXB_FILLING (Packet):
    def handle(self):
        # begin handle [GC_RES_JIANMUXB_FILLING] message attrs, auto generate do not change
        self.person['slot'] = self['slot']
        # end handle [GC_RES_JIANMUXB_FILLING] message attrs, auto generate do not change
        pass


class CG_REQ_SHOWRECHARGE (Packet):
    pass


class CG_ACCPET_IMMORTALITY_WAY_REWARD (Packet):
    pass


class GC_NPC_PAOPAOCHAT (Packet):
    def handle(self):
        # begin handle [GC_NPC_PAOPAOCHAT] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['paopaoContent'] = self['paopaoContent']
        self.person['lastTime'] = self['lastTime']
        # end handle [GC_NPC_PAOPAOCHAT] message attrs, auto generate do not change
        pass


class GC_REQ_ARMY_CHANGE_RTROLE (Packet):
    def handle(self):
        # begin handle [GC_REQ_ARMY_CHANGE_RTROLE] message attrs, auto generate do not change
        self.person['RealTimeRole'] = self['RealTimeRole']
        self.person['ArmyLeaderGuid'] = self['ArmyLeaderGuid']
        # end handle [GC_REQ_ARMY_CHANGE_RTROLE] message attrs, auto generate do not change
        pass


class GC_SYNC_MIS_QIYU_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MIS_QIYU_INFO] message attrs, auto generate do not change
        self.person['qiyuCircleData'] = self['qiyuCircleData']
        self.person['CircleIndex'] = self['CircleIndex']
        # end handle [GC_SYNC_MIS_QIYU_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYSTEMTRADE_BUY] message attrs, auto generate do not change
        self.person['IsBuySuccess'] = self['IsBuySuccess']
        # end handle [GC_SYSTEMTRADE_BUY] message attrs, auto generate do not change
        pass


class CG_COPYSCENE_SET_DONTNPCDORP (Packet):
    pass


class CG_REQ_CHANGEINST (Packet):
    pass


class GC_STALL_RETITEM_SELLINFO (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETITEM_SELLINFO] message attrs, auto generate do not change
        self.person['itemid'] = self['itemid']
        self.person['stackcount'] = self['stackcount']
        self.person['price'] = self['price']
        # end handle [GC_STALL_RETITEM_SELLINFO] message attrs, auto generate do not change
        pass


class CG_ASK_GETREWARDFORSIGNIN (Packet):
    pass


class GC_CAMERA_LOCK (Packet):
    def handle(self):
        # begin handle [GC_CAMERA_LOCK] message attrs, auto generate do not change
        self.person['locktime'] = self['locktime']
        self.person['islock'] = self['islock']
        # end handle [GC_CAMERA_LOCK] message attrs, auto generate do not change
        pass


class GC_GUILDLOG_RET (Packet):
    def handle(self):
        # begin handle [GC_GUILDLOG_RET] message attrs, auto generate do not change
        self.person['nBehaviorType'] = self['nBehaviorType']
        self.person['nArgType'] = self['nArgType']
        self.person['Arg1'] = self['Arg1']
        self.person['Arg2'] = self['Arg2']
        self.person['Arg3'] = self['Arg3']
        # end handle [GC_GUILDLOG_RET] message attrs, auto generate do not change
        pass


class CG_ASK_WILDSCENEDUELINFO (Packet):
    pass


class CG_REQ_FAIRY_EVOLVE (Packet):
    pass


class GC_WEATHER (Packet):
    def handle(self):
        # begin handle [GC_WEATHER] message attrs, auto generate do not change
        self.person['WeatherType'] = self['WeatherType']
        self.person['WeatherDesc'] = self['WeatherDesc']
        self.person['nextWeatherDesc'] = self['nextWeatherDesc']
        self.person['sceneclassid'] = self['sceneclassid']
        self.person['timeid'] = self['timeid']
        self.person['addseconds'] = self['addseconds']
        self.person['bGM'] = self['bGM']
        self.person['bFakeWeather'] = self['bFakeWeather']
        # end handle [GC_WEATHER] message attrs, auto generate do not change
        pass


class CG_MOUNT_UNMOUNT (Packet):
    pass


class CG_MISSION_PICK_ITEM (Packet):
    pass


class GC_RET_PICKUP_ITEM (Packet):
    def handle(self):
        # begin handle [GC_RET_PICKUP_ITEM] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['isSuc'] = self['isSuc']
        # end handle [GC_RET_PICKUP_ITEM] message attrs, auto generate do not change
        pass


class CG_SYSTEMTRADE_ASKSELLLIST (Packet):
    pass


class GC_RET_GUILDWAR_HISTROY_RANK_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILDWAR_HISTROY_RANK_INFO] message attrs, auto generate do not change
        self.person['scroeOfWeek'] = self['scroeOfWeek']
        self.person['rankList'] = self['rankList']
        self.person['timeList'] = self['timeList']
        self.person['serverVersion'] = self['serverVersion']
        # end handle [GC_RET_GUILDWAR_HISTROY_RANK_INFO] message attrs, auto generate do not change
        pass


class GC_COMMONACTIVITYINFO_USEITEM (Packet):
    def handle(self):
        # begin handle [GC_COMMONACTIVITYINFO_USEITEM] message attrs, auto generate do not change
        self.person['username'] = self['username']
        self.person['addvalue'] = self['addvalue']
        # end handle [GC_COMMONACTIVITYINFO_USEITEM] message attrs, auto generate do not change
        pass


class GC_SYNC_XIUZHEN_PRACTICE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_XIUZHEN_PRACTICE_DATA] message attrs, auto generate do not change
        self.person['xiuZhenPracticeData'] = self['xiuZhenPracticeData']
        # end handle [GC_SYNC_XIUZHEN_PRACTICE_DATA] message attrs, auto generate do not change
        pass


class GC_TARGET_ALREADYHASTEAM (Packet):
    def handle(self):
        # begin handle [GC_TARGET_ALREADYHASTEAM] message attrs, auto generate do not change
        self.person['playerguid'] = self['playerguid']
        self.person['inviteTeamType'] = self['inviteTeamType']
        # end handle [GC_TARGET_ALREADYHASTEAM] message attrs, auto generate do not change
        pass


class GC_NEAR_TEAMLIST (Packet):
    def handle(self):
        # begin handle [GC_NEAR_TEAMLIST] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['TeamID'] = self['TeamID']
        self.person['Com'] = self['Com']
        self.person['TeamNum'] = self['TeamNum']
        self.person['memberlevel'] = self['memberlevel']
        self.person['memberprof'] = self['memberprof']
        self.person['LeaderSex'] = self['LeaderSex']
        self.person['bArmyList'] = self['bArmyList']
        self.person['ArmyID'] = self['ArmyID']
        self.person['ProfCamp'] = self['ProfCamp']
        self.person['mercenaryNum'] = self['mercenaryNum']
        self.person['merProf'] = self['merProf']
        self.person['merLevel'] = self['merLevel']
        # end handle [GC_NEAR_TEAMLIST] message attrs, auto generate do not change
        pass


class GC_SYNC_CHRISTMAS_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CHRISTMAS_DATA] message attrs, auto generate do not change
        self.person['open'] = self['open']
        self.person['startTime'] = self['startTime']
        self.person['awardEndTime'] = self['awardEndTime']
        self.person['endTime'] = self['endTime']
        self.person['loginAwardItemId'] = self['loginAwardItemId']
        self.person['loginAwardItemNum'] = self['loginAwardItemNum']
        self.person['tourstartTime'] = self['tourstartTime']
        self.person['tourEndTime'] = self['tourEndTime']
        self.person['monsterstartTime'] = self['monsterstartTime']
        self.person['monsterEndTime'] = self['monsterEndTime']
        self.person['tourTime'] = self['tourTime']
        self.person['monsterTime'] = self['monsterTime']
        self.person['monsterScene'] = self['monsterScene']
        # end handle [GC_SYNC_CHRISTMAS_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_QIANZHUANG_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_QIANZHUANG_DATA] message attrs, auto generate do not change
        self.person['nTotalRechargeRMB'] = self['nTotalRechargeRMB']
        self.person['bIsGetTouZhi'] = self['bIsGetTouZhi']
        self.person['nChZCount'] = self['nChZCount']
        self.person['nYueKaWanHuaCount'] = self['nYueKaWanHuaCount']
        self.person['nYueKaZuLongCount'] = self['nYueKaZuLongCount']
        # end handle [GC_SYNC_QIANZHUANG_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_SHARE_GAME_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SHARE_GAME_DATA] message attrs, auto generate do not change
        self.person['nDrawTypeList'] = self['nDrawTypeList']
        self.person['nSharedTypeList'] = self['nSharedTypeList']
        self.person['GiftConfigList'] = self['GiftConfigList']
        # end handle [GC_SYNC_SHARE_GAME_DATA] message attrs, auto generate do not change
        pass


class GC_UPDATEACTIVITY_POINT (Packet):
    def handle(self):
        # begin handle [GC_UPDATEACTIVITY_POINT] message attrs, auto generate do not change
        self.person['activenessValue'] = self['activenessValue']
        self.person['activenessBounsFlag'] = self['activenessBounsFlag']
        # end handle [GC_UPDATEACTIVITY_POINT] message attrs, auto generate do not change
        pass


class CG_RECOMMEND_FRIEND (Packet):
    pass


class CG_NIEREN_CHANGE (Packet):
    pass


class GC_REQ_CHANGETOBIGWORLD (Packet):
    def handle(self):
        # begin handle [GC_REQ_CHANGETOBIGWORLD] message attrs, auto generate do not change
        self.person['reqType'] = self['reqType']
        # end handle [GC_REQ_CHANGETOBIGWORLD] message attrs, auto generate do not change
        pass


class GC_SYNC_IMMORTALITY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_IMMORTALITY_INFO] message attrs, auto generate do not change
        self.person['wayData'] = self['wayData']
        self.person['activityData'] = self['activityData']
        self.person['immortalityActivityState'] = self['immortalityActivityState']
        self.person['immortalityActiveDays'] = self['immortalityActiveDays']
        self.person['immortalityFinalRewardState'] = self['immortalityFinalRewardState']
        # end handle [GC_SYNC_IMMORTALITY_INFO] message attrs, auto generate do not change
        pass


class CG_ASK_ACTIVENESSINFO (Packet):
    pass


class GC_NIEREN_SUPER (Packet):
    def handle(self):
        # begin handle [GC_NIEREN_SUPER] message attrs, auto generate do not change
        self.person['nierendata'] = self['nierendata']
        # end handle [GC_NIEREN_SUPER] message attrs, auto generate do not change
        pass


class CG_START_CATCHGHOST (Packet):
    pass


class CG_YINZHEN_LEVELUP (Packet):
    pass


class CG_GUILD_REQ_ENTER_GUILD_CITY (Packet):
    pass


class GC_SYNC_XIAOYUE_TIPS (Packet):
    def handle(self):
        # begin handle [GC_SYNC_XIAOYUE_TIPS] message attrs, auto generate do not change
        self.person['bXiaoyueNewTips'] = self['bXiaoyueNewTips']
        # end handle [GC_SYNC_XIAOYUE_TIPS] message attrs, auto generate do not change
        pass


class GC_RET_WILDSCENEDUELINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_WILDSCENEDUELINFO] message attrs, auto generate do not change
        self.person['DuelGuid'] = self['DuelGuid']
        self.person['DuelName'] = self['DuelName']
        self.person['DuelLev'] = self['DuelLev']
        self.person['DuelProId'] = self['DuelProId']
        self.person['DuelTime'] = self['DuelTime']
        self.person['IsOnline'] = self['IsOnline']
        self.person['DuelSexType'] = self['DuelSexType']
        self.person['DuelCombat'] = self['DuelCombat']
        # end handle [GC_RET_WILDSCENEDUELINFO] message attrs, auto generate do not change
        pass


class GC_DOMAINSTATUE_RET_KNEEL (Packet):
    def handle(self):
        # begin handle [GC_DOMAINSTATUE_RET_KNEEL] message attrs, auto generate do not change
        self.person['kneelType'] = self['kneelType']
        self.person['kneelState'] = self['kneelState']
        # end handle [GC_DOMAINSTATUE_RET_KNEEL] message attrs, auto generate do not change
        pass


class GC_SYNSELTRAGET_ATTR (Packet):
    def handle(self):
        # begin handle [GC_SYNSELTRAGET_ATTR] message attrs, auto generate do not change
        self.person['ObjId'] = self['ObjId']
        self.person['CurHp'] = self['CurHp']
        self.person['CurMp'] = self['CurMp']
        self.person['MaxHP'] = self['MaxHP']
        self.person['MaxMP'] = self['MaxMP']
        self.person['CurLev'] = self['CurLev']
        self.person['Name'] = self['Name']
        self.person['BelongTeamID'] = self['BelongTeamID']
        self.person['BelongObjID'] = self['BelongObjID']
        self.person['TeamID'] = self['TeamID']
        self.person['IsshowImp'] = self['IsshowImp']
        self.person['impId'] = self['impId']
        self.person['impReTime'] = self['impReTime']
        self.person['impWrapNum'] = self['impWrapNum']
        self.person['CurCC'] = self['CurCC']
        self.person['MaxCC'] = self['MaxCC']
        self.person['CCType'] = self['CCType']
        self.person['TargetSelObjId'] = self['TargetSelObjId']
        self.person['TargetSelCurHp'] = self['TargetSelCurHp']
        self.person['TargetName'] = self['TargetName']
        self.person['TargetSelMaxHp'] = self['TargetSelMaxHp']
        self.person['CurRage'] = self['CurRage']
        self.person['MaxRage'] = self['MaxRage']
        self.person['BrotherhoodGuid'] = self['BrotherhoodGuid']
        self.person['SwordTeamGuid'] = self['SwordTeamGuid']
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['CurDefenceBreakValue'] = self['CurDefenceBreakValue']
        self.person['CurDefenceEndTime'] = self['CurDefenceEndTime']
        # end handle [GC_SYNSELTRAGET_ATTR] message attrs, auto generate do not change
        pass


class GC_WAITPAY_REFUSE (Packet):
    def handle(self):
        # begin handle [GC_WAITPAY_REFUSE] message attrs, auto generate do not change
        self.person['BillGuid'] = self['BillGuid']
        # end handle [GC_WAITPAY_REFUSE] message attrs, auto generate do not change
        pass


class CG_GWSKILL_STARTSKILL (Packet):
    pass


class CG_CANCEL_SECPASSWORD (Packet):
    pass


class GC_RECASTINHERIT_GUIDE_RET (Packet):
    def handle(self):
        # begin handle [GC_RECASTINHERIT_GUIDE_RET] message attrs, auto generate do not change
        self.person['targuid'] = self['targuid']
        self.person['srcguid'] = self['srcguid']
        # end handle [GC_RECASTINHERIT_GUIDE_RET] message attrs, auto generate do not change
        pass


class CG_MISSION_ABANDON (Packet):
    pass


class CG_STATICSYSTEMSHOP_BUY (Packet):
    pass


class GC_SYNC_COMMONDATA64 (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COMMONDATA64] message attrs, auto generate do not change
        self.person['nIndex'] = self['nIndex']
        self.person['nValue'] = self['nValue']
        # end handle [GC_SYNC_COMMONDATA64] message attrs, auto generate do not change
        pass


class GC_MOUNTCOLLECTED_FLAG (Packet):
    def handle(self):
        # begin handle [GC_MOUNTCOLLECTED_FLAG] message attrs, auto generate do not change
        self.person['AutoMountFlag'] = self['AutoMountFlag']
        self.person['CurMountID'] = self['CurMountID']
        self.person['MountCollectedFlag'] = self['MountCollectedFlag']
        self.person['MountLeftTime'] = self['MountLeftTime']
        # end handle [GC_MOUNTCOLLECTED_FLAG] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_CREATE_FAILED (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_CREATE_FAILED] message attrs, auto generate do not change
        self.person['reason'] = self['reason']
        # end handle [GC_BROTHERHOOD_CREATE_FAILED] message attrs, auto generate do not change
        pass


class GC_REQ_MASTER_CONFIGM_APPRENTICE (Packet):
    def handle(self):
        # begin handle [GC_REQ_MASTER_CONFIGM_APPRENTICE] message attrs, auto generate do not change
        self.person['apprenticeGuid'] = self['apprenticeGuid']
        self.person['apprenticeName'] = self['apprenticeName']
        # end handle [GC_REQ_MASTER_CONFIGM_APPRENTICE] message attrs, auto generate do not change
        pass


class GC_EQUIP_ENCHANT_RESULT (Packet):
    def handle(self):
        # begin handle [GC_EQUIP_ENCHANT_RESULT] message attrs, auto generate do not change
        self.person['nEquipSlot'] = self['nEquipSlot']
        self.person['nEnchantSlot'] = self['nEnchantSlot']
        self.person['nItemId'] = self['nItemId']
        self.person['nResult'] = self['nResult']
        self.person['nOperaType'] = self['nOperaType']
        # end handle [GC_EQUIP_ENCHANT_RESULT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_RET_MIS_QIYU_HISTORY] message attrs, auto generate do not change
        self.person['misHistory'] = self['misHistory']
        self.person['index'] = self['index']
        self.person['totalCount'] = self['totalCount']
        # end handle [GC_RET_MIS_QIYU_HISTORY] message attrs, auto generate do not change
        pass


class GC_GET_HONORCOIN (Packet):
    def handle(self):
        # begin handle [GC_GET_HONORCOIN] message attrs, auto generate do not change
        self.person['count'] = self['count']
        # end handle [GC_GET_HONORCOIN] message attrs, auto generate do not change
        pass


class GC_GIVESIGN_FORPICDETECTION (Packet):
    def handle(self):
        # begin handle [GC_GIVESIGN_FORPICDETECTION] message attrs, auto generate do not change
        self.person['fileId'] = self['fileId']
        self.person['sign'] = self['sign']
        self.person['bucketname'] = self['bucketname']
        self.person['appid'] = self['appid']
        self.person['reqSignType'] = self['reqSignType']
        # end handle [GC_GIVESIGN_FORPICDETECTION] message attrs, auto generate do not change
        pass


class GC_SYNC_PET_BASE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PET_BASE_INFO] message attrs, auto generate do not change
        self.person['pets'] = self['pets']
        self.person['combatPetGuid'] = self['combatPetGuid']
        self.person['packSize'] = self['packSize']
        # end handle [GC_SYNC_PET_BASE_INFO] message attrs, auto generate do not change
        pass


class GC_MERCENARY_LEFTTIMES (Packet):
    def handle(self):
        # begin handle [GC_MERCENARY_LEFTTIMES] message attrs, auto generate do not change
        # end handle [GC_MERCENARY_LEFTTIMES] message attrs, auto generate do not change
        pass


class CG_ASK_RANK (Packet):
    pass


class GC_WISHING_REQUEST_LOTTERY_RESULT (Packet):
    def handle(self):
        # begin handle [GC_WISHING_REQUEST_LOTTERY_RESULT] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['id'] = self['id']
        self.person['index'] = self['index']
        # end handle [GC_WISHING_REQUEST_LOTTERY_RESULT] message attrs, auto generate do not change
        pass


class GC_SYNC_OTHERTEAMINFOATTR (Packet):
    def handle(self):
        # begin handle [GC_SYNC_OTHERTEAMINFOATTR] message attrs, auto generate do not change
        self.person['playerguid'] = self['playerguid']
        self.person['syncop'] = self['syncop']
        # end handle [GC_SYNC_OTHERTEAMINFOATTR] message attrs, auto generate do not change
        pass


class CG_REQUIRE_PLAT_FORM_MESSAGE (Packet):
    pass


class GC_UPDATE_NEEDIMPACTINFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_NEEDIMPACTINFO] message attrs, auto generate do not change
        self.person['impactId'] = self['impactId']
        self.person['optype'] = self['optype']
        self.person['uniqueId'] = self['uniqueId']
        self.person['continueTime'] = self['continueTime']
        self.person['remainTime'] = self['remainTime']
        self.person['wrapNum'] = self['wrapNum']
        self.person['isDisableMove'] = self['isDisableMove']
        self.person['isDisableSkill'] = self['isDisableSkill']
        self.person['isReliveContine'] = self['isReliveContine']
        self.person['reliveSenderName'] = self['reliveSenderName']
        self.person['isSendByMe'] = self['isSendByMe']
        self.person['disableSkillLevel'] = self['disableSkillLevel']
        self.person['isSceneDisable'] = self['isSceneDisable']
        self.person['sendskillid'] = self['sendskillid']
        # end handle [GC_UPDATE_NEEDIMPACTINFO] message attrs, auto generate do not change
        pass


class CG_REQ_CHANGEPROFESSIONCONDITIONINFO (Packet):
    pass


class CG_REQ_GET_HOMEGIFT (Packet):
    pass


class GC_NOTICE_WARPATH_FULL (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_WARPATH_FULL] message attrs, auto generate do not change
        self.person['equipGuid'] = self['equipGuid']
        # end handle [GC_NOTICE_WARPATH_FULL] message attrs, auto generate do not change
        pass


class GC_SYN_COOLDOWN_LAYER_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYN_COOLDOWN_LAYER_INFO] message attrs, auto generate do not change
        self.person['nSkillBaseId'] = self['nSkillBaseId']
        self.person['nCoolDownLayers'] = self['nCoolDownLayers']
        # end handle [GC_SYN_COOLDOWN_LAYER_INFO] message attrs, auto generate do not change
        pass


class GC_CLOSE_BLACKMARKET (Packet):
    def handle(self):
        # begin handle [GC_CLOSE_BLACKMARKET] message attrs, auto generate do not change
        self.person['noparam'] = self['noparam']
        # end handle [GC_CLOSE_BLACKMARKET] message attrs, auto generate do not change
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


class GC_KICK_OUT_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_KICK_OUT_NOTICE] message attrs, auto generate do not change
        self.person['optype'] = self['optype']
        self.person['reason'] = self['reason']
        # end handle [GC_KICK_OUT_NOTICE] message attrs, auto generate do not change
        pass


class GC_SYS_PRESTIGEREWARDINFO (Packet):
    def handle(self):
        # begin handle [GC_SYS_PRESTIGEREWARDINFO] message attrs, auto generate do not change
        self.person['info'] = self['info']
        # end handle [GC_SYS_PRESTIGEREWARDINFO] message attrs, auto generate do not change
        pass


class CG_COMPOUND_GEM (Packet):
    pass


class CG_MISSION_PARAM (Packet):
    pass


class GC_TGCFAWARD_DATA (Packet):
    def handle(self):
        # begin handle [GC_TGCFAWARD_DATA] message attrs, auto generate do not change
        self.person['AwardID'] = self['AwardID']
        self.person['IsStart'] = self['IsStart']
        # end handle [GC_TGCFAWARD_DATA] message attrs, auto generate do not change
        pass


class CG_VERIFYCODE_INPUT (Packet):
    pass


class CG_OPEN_COPYSCENE (Packet):
    pass


class CG_TGLOG_CLIENT_BEHAVIOR (Packet):
    pass


class GC_DELIVER_FINISH (Packet):
    def handle(self):
        # begin handle [GC_DELIVER_FINISH] message attrs, auto generate do not change
        self.person['missionID'] = self['missionID']
        # end handle [GC_DELIVER_FINISH] message attrs, auto generate do not change
        pass


class GC_TSS_ANTI_SEND_DATA (Packet):
    def handle(self):
        # begin handle [GC_TSS_ANTI_SEND_DATA] message attrs, auto generate do not change
        self.person['m_AntiData'] = self['m_AntiData']
        # end handle [GC_TSS_ANTI_SEND_DATA] message attrs, auto generate do not change
        pass


class GC_PLAT_FORM_MESSAGE (Packet):
    def handle(self):
        # begin handle [GC_PLAT_FORM_MESSAGE] message attrs, auto generate do not change
        self.person['allCount'] = self['allCount']
        self.person['leftCount'] = self['leftCount']
        self.person['messageInfos'] = self['messageInfos']
        # end handle [GC_PLAT_FORM_MESSAGE] message attrs, auto generate do not change
        pass


class CG_NEW_PLAYER_BEHAVIOR_UI (Packet):
    pass


class GC_SYNC_DESTINY_ATTRIBUTE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DESTINY_ATTRIBUTE] message attrs, auto generate do not change
        self.person['houny'] = self['houny']
        self.person['sagacity'] = self['sagacity']
        self.person['fate'] = self['fate']
        self.person['secret'] = self['secret']
        self.person['contact'] = self['contact']
        self.person['talent'] = self['talent']
        # end handle [GC_SYNC_DESTINY_ATTRIBUTE] message attrs, auto generate do not change
        pass


class CG_ASK_PLAYERAPPLYMATCH (Packet):
    pass


class GC_RES_QINGYIVALUE_DAILY_INFO (Packet):
    def handle(self):
        # begin handle [GC_RES_QINGYIVALUE_DAILY_INFO] message attrs, auto generate do not change
        self.person['values'] = self['values']
        self.person['maxValues'] = self['maxValues']
        # end handle [GC_RES_QINGYIVALUE_DAILY_INFO] message attrs, auto generate do not change
        pass


class CG_LIFESKILL_MAKE (Packet):
    pass


class GC_SYNC_REDPOINT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_REDPOINT] message attrs, auto generate do not change
        self.person['redPoints'] = self['redPoints']
        # end handle [GC_SYNC_REDPOINT] message attrs, auto generate do not change
        pass


class CG_SiQingRedPacket_TLOG (Packet):
    pass


class CG_TEAM_HANREN (Packet):
    pass


class CG_RESET_RUBKI_CBE_ACTIVITY (Packet):
    pass


class GC_REQUEST_ARMYLEADER_POSITION_RET (Packet):
    def handle(self):
        # begin handle [GC_REQUEST_ARMYLEADER_POSITION_RET] message attrs, auto generate do not change
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        self.person['sceneId'] = self['sceneId']
        self.person['sceneinst'] = self['sceneinst']
        # end handle [GC_REQUEST_ARMYLEADER_POSITION_RET] message attrs, auto generate do not change
        pass


class GC_MIDAS_QUERY_SUBSCRIBE (Packet):
    def handle(self):
        # begin handle [GC_MIDAS_QUERY_SUBSCRIBE] message attrs, auto generate do not change
        self.person['Ret'] = self['Ret']
        self.person['Message'] = self['Message']
        self.person['Items'] = self['Items']
        # end handle [GC_MIDAS_QUERY_SUBSCRIBE] message attrs, auto generate do not change
        pass


class CG_REQ_CHANGE_SCENE_TELEPORT (Packet):
    pass


class GC_SYNC_GUILDCONVOY_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILDCONVOY_STATE] message attrs, auto generate do not change
        self.person['curState'] = self['curState']
        # end handle [GC_SYNC_GUILDCONVOY_STATE] message attrs, auto generate do not change
        pass


class CG_MIDAS_QUERY_SUBSCRIBE (Packet):
    pass


class GC_UPDATE_CHAR_IMPACT_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_CHAR_IMPACT_INFO] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['isAdd'] = self['isAdd']
        self.person['impactInfo'] = self['impactInfo']
        # end handle [GC_UPDATE_CHAR_IMPACT_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_REDPACKETRAIN_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_REDPACKETRAIN_INFO] message attrs, auto generate do not change
        self.person['starttime'] = self['starttime']
        self.person['endtime'] = self['endtime']
        self.person['bhaveaward'] = self['bhaveaward']
        self.person['state'] = self['state']
        self.person['awardvalue'] = self['awardvalue']
        self.person['redpacketID'] = self['redpacketID']
        self.person['awardtype'] = self['awardtype']
        self.person['activitystarttime'] = self['activitystarttime']
        self.person['activityendtime'] = self['activityendtime']
        self.person['maxawardvalue'] = self['maxawardvalue']
        self.person['needlevel'] = self['needlevel']
        self.person['IsOpenRedPacketRain'] = self['IsOpenRedPacketRain']
        # end handle [GC_SYNC_REDPACKETRAIN_INFO] message attrs, auto generate do not change
        pass


class CG_GUILD_REQ_CHANGEAUTHORITY (Packet):
    pass


class CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE (Packet):
    pass


class GC_OPERATE_SCENE_BUILDING (Packet):
    def handle(self):
        # begin handle [GC_OPERATE_SCENE_BUILDING] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['OperateType'] = self['OperateType']
        self.person['Building'] = self['Building']
        # end handle [GC_OPERATE_SCENE_BUILDING] message attrs, auto generate do not change
        pass


class CG_ARMY_COPYSCENE_INVITEVIEW_RET (Packet):
    pass


class GC_DEL_GATHER_POINT (Packet):
    def handle(self):
        # begin handle [GC_DEL_GATHER_POINT] message attrs, auto generate do not change
        self.person['posid'] = self['posid']
        self.person['index'] = self['index']
        # end handle [GC_DEL_GATHER_POINT] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_DELETE_RECRUIT_APPLY (Packet):
    pass


class CG_REQUEST_SWTICH_HOME_EXTERIOR (Packet):
    pass


class GC_RET_HATEPEOPLEINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_HATEPEOPLEINFO] message attrs, auto generate do not change
        self.person['DuelGuid'] = self['DuelGuid']
        self.person['DuelName'] = self['DuelName']
        self.person['DuelLev'] = self['DuelLev']
        self.person['DuelProId'] = self['DuelProId']
        self.person['DuelTime'] = self['DuelTime']
        self.person['DuelSexType'] = self['DuelSexType']
        self.person['DuelCombat'] = self['DuelCombat']
        # end handle [GC_RET_HATEPEOPLEINFO] message attrs, auto generate do not change
        pass


class GC_GUILD_CREATE (Packet):
    def handle(self):
        # begin handle [GC_GUILD_CREATE] message attrs, auto generate do not change
        self.person['guildGuid'] = self['guildGuid']
        self.person['guildName'] = self['guildName']
        self.person['guildNotice'] = self['guildNotice']
        self.person['guildShortName'] = self['guildShortName']
        self.person['guildShortNameColor'] = self['guildShortNameColor']
        self.person['guildCreateGroupMoney'] = self['guildCreateGroupMoney']
        # end handle [GC_GUILD_CREATE] message attrs, auto generate do not change
        pass


class GC_PLAY_TIMESCALE (Packet):
    def handle(self):
        # begin handle [GC_PLAY_TIMESCALE] message attrs, auto generate do not change
        self.person['Scale'] = self['Scale']
        self.person['Duration'] = self['Duration']
        # end handle [GC_PLAY_TIMESCALE] message attrs, auto generate do not change
        pass


class GC_RET_GETREWARDFORSIGNIN_DAILY (Packet):
    def handle(self):
        # begin handle [GC_RET_GETREWARDFORSIGNIN_DAILY] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        # end handle [GC_RET_GETREWARDFORSIGNIN_DAILY] message attrs, auto generate do not change
        pass


class CG_GUILD_REQ_LEAVE_GUILD_CITY (Packet):
    pass


class GC_PLAYER_PAOPAOCHAT (Packet):
    def handle(self):
        # begin handle [GC_PLAYER_PAOPAOCHAT] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['paopaoContent'] = self['paopaoContent']
        # end handle [GC_PLAYER_PAOPAOCHAT] message attrs, auto generate do not change
        pass


class GC_QUIT_GAME_RET (Packet):
    def handle(self):
        # begin handle [GC_QUIT_GAME_RET] message attrs, auto generate do not change
        self.person['quittype'] = self['quittype']
        self.person['bigworldip'] = self['bigworldip']
        self.person['bigworldport'] = self['bigworldport']
        self.person['bigworldipv6'] = self['bigworldipv6']
        # end handle [GC_QUIT_GAME_RET] message attrs, auto generate do not change
        pass


class CG_WATERMELON_GET_KEY_ITEM (Packet):
    pass


class GC_REQ_ROLE_SHARE_DATA (Packet):
    def handle(self):
        # begin handle [GC_REQ_ROLE_SHARE_DATA] message attrs, auto generate do not change
        self.person['createRoleTime'] = self['createRoleTime']
        self.person['killedBossNum'] = self['killedBossNum']
        self.person['todayRechargeNum'] = self['todayRechargeNum']
        self.person['todayRefineLevel'] = self['todayRefineLevel']
        self.person['todayBuyFashion'] = self['todayBuyFashion']
        self.person['todayOnlineTime'] = self['todayOnlineTime']
        # end handle [GC_REQ_ROLE_SHARE_DATA] message attrs, auto generate do not change
        pass


class GC_UNLOCK_HOME_ZONE (Packet):
    def handle(self):
        # begin handle [GC_UNLOCK_HOME_ZONE] message attrs, auto generate do not change
        self.person['m_Result'] = self['m_Result']
        self.person['m_ZoneIndex'] = self['m_ZoneIndex']
        # end handle [GC_UNLOCK_HOME_ZONE] message attrs, auto generate do not change
        pass


class CG_ASK_HATEPEOPLEINFO (Packet):
    pass


class GC_SYNC_AUTOTEAM_BW_NUMBER (Packet):
    def handle(self):
        # begin handle [GC_SYNC_AUTOTEAM_BW_NUMBER] message attrs, auto generate do not change
        self.person['shownumber'] = self['shownumber']
        # end handle [GC_SYNC_AUTOTEAM_BW_NUMBER] message attrs, auto generate do not change
        pass


class CG_MOUNT_MARK (Packet):
    pass


class CG_USE_MIDSENDLANTERN (Packet):
    pass


class GC_SYNC_TGCFAWARDTABLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TGCFAWARDTABLE] message attrs, auto generate do not change
        self.person['IsShow'] = self['IsShow']
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['NeedLv'] = self['NeedLv']
        self.person['id'] = self['id']
        self.person['lefttime'] = self['lefttime']
        self.person['bindYB'] = self['bindYB']
        self.person['BindGold'] = self['BindGold']
        self.person['BindSilver'] = self['BindSilver']
        self.person['itemdataid1'] = self['itemdataid1']
        self.person['itemcount1'] = self['itemcount1']
        self.person['itemrefinelv1'] = self['itemrefinelv1']
        self.person['itemdataid2'] = self['itemdataid2']
        self.person['itemcount2'] = self['itemcount2']
        self.person['itemrefinelv2'] = self['itemrefinelv2']
        self.person['iconicId'] = self['iconicId']
        self.person['ShowLv'] = self['ShowLv']
        self.person['Model1'] = self['Model1']
        self.person['Model2'] = self['Model2']
        # end handle [GC_SYNC_TGCFAWARDTABLE] message attrs, auto generate do not change
        pass


class GC_HideModel (Packet):
    def handle(self):
        # begin handle [GC_HideModel] message attrs, auto generate do not change
        self.person['bhidemodel'] = self['bhidemodel']
        self.person['bhidetime'] = self['bhidetime']
        # end handle [GC_HideModel] message attrs, auto generate do not change
        pass


class GC_SYNC_RUBKICUBE_SCENE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RUBKICUBE_SCENE_INFO] message attrs, auto generate do not change
        self.person['rubkiCubePlayId'] = self['rubkiCubePlayId']
        self.person['rubkiCubeEndTime'] = self['rubkiCubeEndTime']
        self.person['isRubkiCubeRun'] = self['isRubkiCubeRun']
        self.person['subRubkiCubePlayId'] = self['subRubkiCubePlayId']
        self.person['subRubkiCubeEndTime'] = self['subRubkiCubeEndTime']
        self.person['isSubRubkiCubeRun'] = self['isSubRubkiCubeRun']
        self.person['rubkiCubePlayExistTime'] = self['rubkiCubePlayExistTime']
        self.person['serverTime'] = self['serverTime']
        # end handle [GC_SYNC_RUBKICUBE_SCENE_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_RUBKICUBE_AWAY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RUBKICUBE_AWAY_INFO] message attrs, auto generate do not change
        self.person['playerOxygenInfos'] = self['playerOxygenInfos']
        self.person['maxOxygenCount'] = self['maxOxygenCount']
        # end handle [GC_SYNC_RUBKICUBE_AWAY_INFO] message attrs, auto generate do not change
        pass


class GC_CHALLENGERANKLIST (Packet):
    def handle(self):
        # begin handle [GC_CHALLENGERANKLIST] message attrs, auto generate do not change
        self.person['level'] = self['level']
        self.person['profession'] = self['profession']
        self.person['combatNum'] = self['combatNum']
        self.person['name'] = self['name']
        self.person['pos'] = self['pos']
        self.person['playerGuid'] = self['playerGuid']
        self.person['HonorCoins'] = self['HonorCoins']
        self.person['sex'] = self['sex']
        self.person['customHeadPic'] = self['customHeadPic']
        self.person['TeamId'] = self['TeamId']
        self.person['TeamCount'] = self['TeamCount']
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['GuidName'] = self['GuidName']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        # end handle [GC_CHALLENGERANKLIST] message attrs, auto generate do not change
        pass


class GC_REBATE_STEPDATA (Packet):
    def handle(self):
        # begin handle [GC_REBATE_STEPDATA] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['mystep'] = self['mystep']
        self.person['mybonus'] = self['mybonus']
        # end handle [GC_REBATE_STEPDATA] message attrs, auto generate do not change
        pass


class GC_RET_SELOBJ_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_SELOBJ_INFO] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['seleobjId'] = self['seleobjId']
        # end handle [GC_RET_SELOBJ_INFO] message attrs, auto generate do not change
        pass


class CG_ASK_FORDETECTION_SIGN (Packet):
    pass


class GC_PLAYSTORY (Packet):
    def handle(self):
        # begin handle [GC_PLAYSTORY] message attrs, auto generate do not change
        self.person['storyID'] = self['storyID']
        # end handle [GC_PLAYSTORY] message attrs, auto generate do not change
        pass


class CG_ITEM_COMPOUND (Packet):
    pass


class GC_XCTJAWARD_DATA (Packet):
    def handle(self):
        # begin handle [GC_XCTJAWARD_DATA] message attrs, auto generate do not change
        self.person['AwardID'] = self['AwardID']
        self.person['IsStart'] = self['IsStart']
        # end handle [GC_XCTJAWARD_DATA] message attrs, auto generate do not change
        pass


class GC_GUILDFIGHT_WORLDBOSS_SOUL (Packet):
    def handle(self):
        # begin handle [GC_GUILDFIGHT_WORLDBOSS_SOUL] message attrs, auto generate do not change
        self.person['BossSouls'] = self['BossSouls']
        # end handle [GC_GUILDFIGHT_WORLDBOSS_SOUL] message attrs, auto generate do not change
        pass


class CG_GODWEAPON_STUNT_LVUP (Packet):
    pass


class CG_MULPVP_AGREEAGAIN (Packet):
    pass


class GC_PROMOTE_FRIENDMAXNUM_RET (Packet):
    def handle(self):
        # begin handle [GC_PROMOTE_FRIENDMAXNUM_RET] message attrs, auto generate do not change
        self.person['bRet'] = self['bRet']
        # end handle [GC_PROMOTE_FRIENDMAXNUM_RET] message attrs, auto generate do not change
        pass


class GC_SYNC_IOS_REVIEW_GUILD_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_IOS_REVIEW_GUILD_DATA] message attrs, auto generate do not change
        self.person['nAlreadyReviewClientVersion'] = self['nAlreadyReviewClientVersion']
        # end handle [GC_SYNC_IOS_REVIEW_GUILD_DATA] message attrs, auto generate do not change
        pass


class GC_SET_ORMODIFY_SECPASSWORD_SUCCESS (Packet):
    def handle(self):
        # begin handle [GC_SET_ORMODIFY_SECPASSWORD_SUCCESS] message attrs, auto generate do not change
        self.person['optiontype'] = self['optiontype']
        self.person['isoptionsuccess'] = self['isoptionsuccess']
        # end handle [GC_SET_ORMODIFY_SECPASSWORD_SUCCESS] message attrs, auto generate do not change
        pass


class GC_STALL_RETBUY (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETBUY] message attrs, auto generate do not change
        self.person['stallguid'] = self['stallguid']
        # end handle [GC_STALL_RETBUY] message attrs, auto generate do not change
        pass


class CG_READY_CONFIRM (Packet):
    pass


class CG_NATIONALDAY_TRIBUTE_HAND_IN (Packet):
    pass


class GC_RET_ARTIFACT_PROVE_REWARD (Packet):
    def handle(self):
        # begin handle [GC_RET_ARTIFACT_PROVE_REWARD] message attrs, auto generate do not change
        self.person['ProveRewardId'] = self['ProveRewardId']
        self.person['ProveState'] = self['ProveState']
        # end handle [GC_RET_ARTIFACT_PROVE_REWARD] message attrs, auto generate do not change
        pass


class CG_AUCTION_LOOK (Packet):
    pass


class CG_SYSTEMTRADE_SELL (Packet):
    pass


class GC_MSG_BOX (Packet):
    def handle(self):
        # begin handle [GC_MSG_BOX] message attrs, auto generate do not change
        self.person['info'] = self['info']
        self.person['title'] = self['title']
        # end handle [GC_MSG_BOX] message attrs, auto generate do not change
        pass


class GC_EXIT_COPY_SCENE_ENVIROMENT (Packet):
    def handle(self):
        # begin handle [GC_EXIT_COPY_SCENE_ENVIROMENT] message attrs, auto generate do not change
        # end handle [GC_EXIT_COPY_SCENE_ENVIROMENT] message attrs, auto generate do not change
        pass


class CG_CHANGE_FAIRY_NAME (Packet):
    pass


class CG_WEDDING_OPEN_FEAST (Packet):
    pass


class GC_ISHATEPEOPLEONLINE (Packet):
    def handle(self):
        # begin handle [GC_ISHATEPEOPLEONLINE] message attrs, auto generate do not change
        self.person['tarGuid'] = self['tarGuid']
        self.person['IsOnline'] = self['IsOnline']
        # end handle [GC_ISHATEPEOPLEONLINE] message attrs, auto generate do not change
        pass


class GC_UPDATE_HOME_PRODUCE_STATE (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_HOME_PRODUCE_STATE] message attrs, auto generate do not change
        self.person['m_HomeGuid'] = self['m_HomeGuid']
        self.person['m_HomeOwnerGuid'] = self['m_HomeOwnerGuid']
        self.person['m_BuildingGuid'] = self['m_BuildingGuid']
        self.person['m_Operate'] = self['m_Operate']
        self.person['m_Param0'] = self['m_Param0']
        self.person['m_Param1'] = self['m_Param1']
        # end handle [GC_UPDATE_HOME_PRODUCE_STATE] message attrs, auto generate do not change
        pass


class GC_SYNC_PAPER_TIPS (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PAPER_TIPS] message attrs, auto generate do not change
        self.person['tiplist'] = self['tiplist']
        self.person['contect'] = self['contect']
        # end handle [GC_SYNC_PAPER_TIPS] message attrs, auto generate do not change
        pass


class CG_BOSS_PICK_ITEM (Packet):
    pass


class CG_REQ_RECEIVE_GUILD_GIFTPACKAGE (Packet):
    pass


class GC_GUILD_WAR_SYNC_SIGN_UP_MEMBERS (Packet):
    def handle(self):
        # begin handle [GC_GUILD_WAR_SYNC_SIGN_UP_MEMBERS] message attrs, auto generate do not change
        self.person['memberGuids'] = self['memberGuids']
        self.person['states'] = self['states']
        self.person['bIsCreate'] = self['bIsCreate']
        # end handle [GC_GUILD_WAR_SYNC_SIGN_UP_MEMBERS] message attrs, auto generate do not change
        pass


class GC_STOP_LIGHTNING_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_STOP_LIGHTNING_EFFECT] message attrs, auto generate do not change
        self.person['LightingEffectId'] = self['LightingEffectId']
        self.person['OwnCharServerID'] = self['OwnCharServerID']
        # end handle [GC_STOP_LIGHTNING_EFFECT] message attrs, auto generate do not change
        pass


class GC_GUILD_ROBBERS_RANK (Packet):
    def handle(self):
        # begin handle [GC_GUILD_ROBBERS_RANK] message attrs, auto generate do not change
        self.person['RankData'] = self['RankData']
        # end handle [GC_GUILD_ROBBERS_RANK] message attrs, auto generate do not change
        pass


class GC_EQUIPMIRROR_FORGE_INFO (Packet):
    def handle(self):
        # begin handle [GC_EQUIPMIRROR_FORGE_INFO] message attrs, auto generate do not change
        self.person['mirrorForgeLevel'] = self['mirrorForgeLevel']
        # end handle [GC_EQUIPMIRROR_FORGE_INFO] message attrs, auto generate do not change
        pass


class GC_WEDDING_RETINFO (Packet):
    def handle(self):
        # begin handle [GC_WEDDING_RETINFO] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['groomname'] = self['groomname']
        self.person['bridename'] = self['bridename']
        self.person['groomguid'] = self['groomguid']
        self.person['brideguid'] = self['brideguid']
        self.person['sceneindex'] = self['sceneindex']
        # end handle [GC_WEDDING_RETINFO] message attrs, auto generate do not change
        pass


class GC_ITEMSCRIPT_RET (Packet):
    def handle(self):
        # begin handle [GC_ITEMSCRIPT_RET] message attrs, auto generate do not change
        self.person['ScriptID'] = self['ScriptID']
        self.person['DataId'] = self['DataId']
        self.person['Param1'] = self['Param1']
        self.person['Param2'] = self['Param2']
        # end handle [GC_ITEMSCRIPT_RET] message attrs, auto generate do not change
        pass


class CG_COMMONACTIVITYINFO_USEITEM (Packet):
    pass


class CG_MULPVP_ANSWER_MEM (Packet):
    pass


class CG_GUILDLOG_REQ (Packet):
    pass


class GC_TEAM_SYNC_MEMBERINFO (Packet):
    def handle(self):
        # begin handle [GC_TEAM_SYNC_MEMBERINFO] message attrs, auto generate do not change
        self.person['index'] = self['index']
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberProf'] = self['memberProf']
        self.person['memberHP'] = self['memberHP']
        self.person['memberMaxHP'] = self['memberMaxHP']
        self.person['sceneclass'] = self['sceneclass']
        self.person['sceneinst'] = self['sceneinst']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        self.person['memberState'] = self['memberState']
        self.person['memberSex'] = self['memberSex']
        self.person['memberBodyId'] = self['memberBodyId']
        self.person['memberFaceId'] = self['memberFaceId']
        self.person['memberWeaponId'] = self['memberWeaponId']
        self.person['memberWeaponRefineVisual'] = self['memberWeaponRefineVisual']
        self.person['memberHairId'] = self['memberHairId']
        self.person['reserved'] = self['reserved']
        self.person['familyGuid'] = self['familyGuid']
        self.person['memberbodycolorVisual'] = self['memberbodycolorVisual']
        self.person['professionOrientationIndex'] = self['professionOrientationIndex']
        self.person['memberMP'] = self['memberMP']
        self.person['memberMaxMP'] = self['memberMaxMP']
        self.person['teamIndex'] = self['teamIndex']
        self.person['armyID'] = self['armyID']
        self.person['bodyFashionId'] = self['bodyFashionId']
        self.person['bodyColorIndex'] = self['bodyColorIndex']
        self.person['nierenvalue'] = self['nierenvalue']
        self.person['onlyupdatehpmp'] = self['onlyupdatehpmp']
        self.person['memberBiaoJi'] = self['memberBiaoJi']
        self.person['memberReadyState'] = self['memberReadyState']
        self.person['memberArmyFollowState'] = self['memberArmyFollowState']
        self.person['memberImpactClassId1'] = self['memberImpactClassId1']
        self.person['memberImpactClassId2'] = self['memberImpactClassId2']
        self.person['hairFashionId'] = self['hairFashionId']
        self.person['hairColorIndex'] = self['hairColorIndex']
        self.person['weaponFashionId'] = self['weaponFashionId']
        self.person['weaponColorIndex'] = self['weaponColorIndex']
        self.person['memberPglMmr'] = self['memberPglMmr']
        self.person['memberPglRemainTimes'] = self['memberPglRemainTimes']
        self.person['rtMemberInfo'] = self['rtMemberInfo']
        self.person['memberProfCamp'] = self['memberProfCamp']
        self.person['memberGemSetId'] = self['memberGemSetId']
        self.person['memberImpactLayer1'] = self['memberImpactLayer1']
        self.person['memberImpactLayer2'] = self['memberImpactLayer2']
        self.person['memberAutoCombat'] = self['memberAutoCombat']
        self.person['memberHaveAsuraKey1'] = self['memberHaveAsuraKey1']
        self.person['memberHaveAsuraKey2'] = self['memberHaveAsuraKey2']
        self.person['memberOriginalWorldName'] = self['memberOriginalWorldName']
        self.person['memberGuildGuid'] = self['memberGuildGuid']
        self.person['memberXiuZhenLevel'] = self['memberXiuZhenLevel']
        self.person['memberCombatValue'] = self['memberCombatValue']
        self.person['memberLoverGuid'] = self['memberLoverGuid']
        self.person['memberHaveDispelBuff'] = self['memberHaveDispelBuff']
        self.person['memberHaveHuiliuIdentity'] = self['memberHaveHuiliuIdentity']
        self.person['memberHomeGuid'] = self['memberHomeGuid']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['memberBodyUseFreedomDyeColorIndex'] = self['memberBodyUseFreedomDyeColorIndex']
        self.person['memberHairUseFreedomDyeColorIndex'] = self['memberHairUseFreedomDyeColorIndex']
        self.person['BodyFreeDyeColorInfo'] = self['BodyFreeDyeColorInfo']
        self.person['HairFreeDyeColorInfo'] = self['HairFreeDyeColorInfo']
        self.person['BackFashionId'] = self['BackFashionId']
        self.person['BackColorIndex'] = self['BackColorIndex']
        self.person['memberIsNewPlayerCatch'] = self['memberIsNewPlayerCatch']
        self.person['memberActivityFinishFlag'] = self['memberActivityFinishFlag']
        self.person['memberHaveFestivalHuiliuIdentity'] = self['memberHaveFestivalHuiliuIdentity']
        # end handle [GC_TEAM_SYNC_MEMBERINFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_FIREWORKS_CONFIG] message attrs, auto generate do not change
        self.person['open'] = self['open']
        self.person['startTime'] = self['startTime']
        self.person['blessEndTime'] = self['blessEndTime']
        self.person['awardTime'] = self['awardTime']
        self.person['endTime'] = self['endTime']
        self.person['smallFireWorkId'] = self['smallFireWorkId']
        self.person['smallFireWorkBless'] = self['smallFireWorkBless']
        self.person['bigFireWorkId'] = self['bigFireWorkId']
        self.person['bigFireWorkBless'] = self['bigFireWorkBless']
        self.person['awardStep'] = self['awardStep']
        self.person['awardIdA'] = self['awardIdA']
        self.person['awardNumA'] = self['awardNumA']
        self.person['awardIdB'] = self['awardIdB']
        self.person['awardNumB'] = self['awardNumB']
        self.person['awardIdC'] = self['awardIdC']
        self.person['awardNumC'] = self['awardNumC']
        # end handle [GC_SYNC_FIREWORKS_CONFIG] message attrs, auto generate do not change
        pass


class GC_PLAYCOUNTDOWNEFFECT (Packet):
    def handle(self):
        # begin handle [GC_PLAYCOUNTDOWNEFFECT] message attrs, auto generate do not change
        # end handle [GC_PLAYCOUNTDOWNEFFECT] message attrs, auto generate do not change
        pass


class GC_SHOW_HELMET (Packet):
    def handle(self):
        # begin handle [GC_SHOW_HELMET] message attrs, auto generate do not change
        self.person['showhelmet'] = self['showhelmet']
        # end handle [GC_SHOW_HELMET] message attrs, auto generate do not change
        pass


class CG_HPFOODLIST_CHANGED (Packet):
    pass


class GC_RET_SELFROLEVIEWINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_SELFROLEVIEWINFO] message attrs, auto generate do not change
        self.person['selfRoleViewInfo'] = self['selfRoleViewInfo']
        self.person['energyValue'] = self['energyValue']
        self.person['activeness'] = self['activeness']
        self.person['vigorValue'] = self['vigorValue']
        self.person['MilitaryRank'] = self['MilitaryRank']
        self.person['Reputation'] = self['Reputation']
        # end handle [GC_RET_SELFROLEVIEWINFO] message attrs, auto generate do not change
        pass


class GC_FACETOLOOKPOINT (Packet):
    def handle(self):
        # begin handle [GC_FACETOLOOKPOINT] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        # end handle [GC_FACETOLOOKPOINT] message attrs, auto generate do not change
        pass


class GC_RET_WORLDBOSS_NUM (Packet):
    def handle(self):
        # begin handle [GC_RET_WORLDBOSS_NUM] message attrs, auto generate do not change
        self.person['num'] = self['num']
        # end handle [GC_RET_WORLDBOSS_NUM] message attrs, auto generate do not change
        pass


class CG_ASK_QUITFOLLOW (Packet):
    pass


class GC_RET_GUILD_THIEF_NUM (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILD_THIEF_NUM] message attrs, auto generate do not change
        self.person['num'] = self['num']
        # end handle [GC_RET_GUILD_THIEF_NUM] message attrs, auto generate do not change
        pass


class CG_SECPASSWORD_RELEASELOCK (Packet):
    pass


class CG_REQ_YLTX_SCENELIST (Packet):
    pass


class CG_REQ_JIANMUXB_REWARD (Packet):
    pass


class GC_NOTICE_PLAYER_AUTOTEAM_TIMEOUT (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_PLAYER_AUTOTEAM_TIMEOUT] message attrs, auto generate do not change
        self.person['nTeamNum'] = self['nTeamNum']
        self.person['nPlayerNum'] = self['nPlayerNum']
        # end handle [GC_NOTICE_PLAYER_AUTOTEAM_TIMEOUT] message attrs, auto generate do not change
        pass


class CG_REQ_ACCEPT_APPRENTICE_TASK (Packet):
    pass


class CG_PANDORA_TLOG (Packet):
    pass


class GC_RES_PET_FEED (Packet):
    def handle(self):
        # begin handle [GC_RES_PET_FEED] message attrs, auto generate do not change
        self.person['petGuid'] = self['petGuid']
        self.person['itemID'] = self['itemID']
        # end handle [GC_RES_PET_FEED] message attrs, auto generate do not change
        pass


class GC_SYNC_HOME_HORDE_SHOP (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HOME_HORDE_SHOP] message attrs, auto generate do not change
        self.person['ItemTabId'] = self['ItemTabId']
        self.person['BuyCount'] = self['BuyCount']
        # end handle [GC_SYNC_HOME_HORDE_SHOP] message attrs, auto generate do not change
        pass


class CG_TRIGGER (Packet):
    pass


class CG_REQ_SET_PET_AUTO_FEED (Packet):
    pass


class GC_JOIN_TEAM_REQUEST (Packet):
    def handle(self):
        # begin handle [GC_JOIN_TEAM_REQUEST] message attrs, auto generate do not change
        self.person['requestGuid'] = self['requestGuid']
        self.person['requestName'] = self['requestName']
        self.person['requestLv'] = self['requestLv']
        self.person['sceneId'] = self['sceneId']
        self.person['sceneinst'] = self['sceneinst']
        self.person['guildGuid'] = self['guildGuid']
        self.person['familyGuid'] = self['familyGuid']
        self.person['prof'] = self['prof']
        self.person['com'] = self['com']
        self.person['haveHuiliuIdentity'] = self['haveHuiliuIdentity']
        self.person['requesterIsNewCatchPlayer'] = self['requesterIsNewCatchPlayer']
        self.person['sex'] = self['sex']
        self.person['haveFestivalHuiliuIdentity'] = self['haveFestivalHuiliuIdentity']
        # end handle [GC_JOIN_TEAM_REQUEST] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_RECRUIT_LIST (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_RECRUIT_LIST] message attrs, auto generate do not change
        self.person['pageId'] = self['pageId']
        self.person['pageCount'] = self['pageCount']
        self.person['prof'] = self['prof']
        self.person['memberCount'] = self['memberCount']
        self.person['brotherhoodCombatVal'] = self['brotherhoodCombatVal']
        self.person['brotherhoodGuid'] = self['brotherhoodGuid']
        self.person['brotherhoodName'] = self['brotherhoodName']
        self.person['profOfMemberHave'] = self['profOfMemberHave']
        self.person['profOfMemberNeed'] = self['profOfMemberNeed']
        self.person['profCountOfMember'] = self['profCountOfMember']
        self.person['activeBrotherhood'] = self['activeBrotherhood']
        self.person['brotherhoodTags'] = self['brotherhoodTags']
        self.person['brotherhoodDeclaration'] = self['brotherhoodDeclaration']
        self.person['brotherhoodLevel'] = self['brotherhoodLevel']
        self.person['RecruitAmount'] = self['RecruitAmount']
        self.person['leaderGuid'] = self['leaderGuid']
        self.person['leaderName'] = self['leaderName']
        self.person['leaderProfession'] = self['leaderProfession']
        self.person['leaderLevel'] = self['leaderLevel']
        self.person['leaderSex'] = self['leaderSex']
        self.person['leaderCustomHeadPic'] = self['leaderCustomHeadPic']
        self.person['leaderPhotoFrameId'] = self['leaderPhotoFrameId']
        self.person['PublishTime'] = self['PublishTime']
        self.person['brotherhoodMemCount'] = self['brotherhoodMemCount']
        self.person['onlyActiveBrotherhood'] = self['onlyActiveBrotherhood']
        # end handle [GC_BROTHERHOOD_RECRUIT_LIST] message attrs, auto generate do not change
        pass


class GC_FORCE_STOP_JUMP (Packet):
    def handle(self):
        # begin handle [GC_FORCE_STOP_JUMP] message attrs, auto generate do not change
        self.person['server_id'] = self['server_id']
        self.person['jump_times'] = self['jump_times']
        self.person['x'] = self['x']
        self.person['y'] = self['y']
        self.person['z'] = self['z']
        self.person['curJumpSection'] = self['curJumpSection']
        self.person['dir_x'] = self['dir_x']
        self.person['dir_y'] = self['dir_y']
        self.person['dir_z'] = self['dir_z']
        # end handle [GC_FORCE_STOP_JUMP] message attrs, auto generate do not change
        pass


class GC_GUILDAUCTION_ATTEND_INFO (Packet):
    def handle(self):
        # begin handle [GC_GUILDAUCTION_ATTEND_INFO] message attrs, auto generate do not change
        self.person['actType'] = self['actType']
        self.person['attendNum'] = self['attendNum']
        # end handle [GC_GUILDAUCTION_ATTEND_INFO] message attrs, auto generate do not change
        pass


class GC_DOMAIN_RET_DECLAREWAR (Packet):
    def handle(self):
        # begin handle [GC_DOMAIN_RET_DECLAREWAR] message attrs, auto generate do not change
        self.person['domainId'] = self['domainId']
        self.person['money'] = self['money']
        self.person['cnt'] = self['cnt']
        # end handle [GC_DOMAIN_RET_DECLAREWAR] message attrs, auto generate do not change
        pass


class GC_MERGE_FAIRY_RET (Packet):
    def handle(self):
        # begin handle [GC_MERGE_FAIRY_RET] message attrs, auto generate do not change
        self.person['fairy'] = self['fairy']
        # end handle [GC_MERGE_FAIRY_RET] message attrs, auto generate do not change
        pass


class GC_SYNC_RUBKICUBE_REWARD_COUNT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RUBKICUBE_REWARD_COUNT] message attrs, auto generate do not change
        self.person['nSmallRewardCount'] = self['nSmallRewardCount']
        self.person['nBigRewardCount'] = self['nBigRewardCount']
        # end handle [GC_SYNC_RUBKICUBE_REWARD_COUNT] message attrs, auto generate do not change
        pass


class GC_ACTIVITYMULTI_SYNC (Packet):
    def handle(self):
        # begin handle [GC_ACTIVITYMULTI_SYNC] message attrs, auto generate do not change
        self.person['SceneId'] = self['SceneId']
        self.person['ExpFactor'] = self['ExpFactor']
        self.person['ExpStartTime'] = self['ExpStartTime']
        self.person['ExpEndTime'] = self['ExpEndTime']
        self.person['GoldCoinFactor'] = self['GoldCoinFactor']
        self.person['GoldCoinStartTime'] = self['GoldCoinStartTime']
        self.person['GoldCoinEndTime'] = self['GoldCoinEndTime']
        self.person['SilverCoinFactor'] = self['SilverCoinFactor']
        self.person['SilverCoinStartTime'] = self['SilverCoinStartTime']
        self.person['SilverCoinEndTime'] = self['SilverCoinEndTime']
        self.person['ItemInfo'] = self['ItemInfo']
        self.person['PrestigeFactor'] = self['PrestigeFactor']
        self.person['PrestigeStartTime'] = self['PrestigeStartTime']
        self.person['PrestigeEndTime'] = self['PrestigeEndTime']
        # end handle [GC_ACTIVITYMULTI_SYNC] message attrs, auto generate do not change
        pass


class CG_REQ_ENTER_HOME_SHOWROOM (Packet):
    pass


class GC_SEND_IMPACT (Packet):
    def handle(self):
        # begin handle [GC_SEND_IMPACT] message attrs, auto generate do not change
        self.person['SenderId'] = self['SenderId']
        self.person['TargetId'] = self['TargetId']
        self.person['ImpactID'] = self['ImpactID']
        # end handle [GC_SEND_IMPACT] message attrs, auto generate do not change
        pass


class CG_SKILL_WASH (Packet):
    pass


class CG_TIANSHUBOARD_SETUP (Packet):
    pass


class GC_LUCKY_CONNECT_ACTIVE_DATA (Packet):
    def handle(self):
        # begin handle [GC_LUCKY_CONNECT_ACTIVE_DATA] message attrs, auto generate do not change
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['IsOpen'] = self['IsOpen']
        self.person['IsLogin'] = self['IsLogin']
        # end handle [GC_LUCKY_CONNECT_ACTIVE_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_LEVELREWARDINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_LEVELREWARDINFO] message attrs, auto generate do not change
        self.person['rank'] = self['rank']
        self.person['rewardId'] = self['rewardId']
        self.person['state'] = self['state']
        self.person['day'] = self['day']
        # end handle [GC_SYNC_LEVELREWARDINFO] message attrs, auto generate do not change
        pass


class CG_FRIENDS_MUTUALHELP_TLOG (Packet):
    pass


class GC_PRESENT_WAITPAY_SYNC (Packet):
    def handle(self):
        # begin handle [GC_PRESENT_WAITPAY_SYNC] message attrs, auto generate do not change
        self.person['PresentList'] = self['PresentList']
        self.person['WaitPayList'] = self['WaitPayList']
        # end handle [GC_PRESENT_WAITPAY_SYNC] message attrs, auto generate do not change
        pass


class CG_REQ_GUILDLOG (Packet):
    pass


class GC_DOMAINWAR_RESULT (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_RESULT] message attrs, auto generate do not change
        self.person['warResult'] = self['warResult']
        self.person['userData'] = self['userData']
        self.person['normalRewardId'] = self['normalRewardId']
        self.person['specailRewardId'] = self['specailRewardId']
        self.person['domainId'] = self['domainId']
        self.person['guildCoin'] = self['guildCoin']
        # end handle [GC_DOMAINWAR_RESULT] message attrs, auto generate do not change
        pass


class CG_EQUIP_INHERIT (Packet):
    pass


class CG_REQ_MARRIAGE_DIVORCE (Packet):
    pass


class GC_UPDATE_SKILL_UNLOCK_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_SKILL_UNLOCK_INFO] message attrs, auto generate do not change
        self.person['nSkillClassId'] = self['nSkillClassId']
        self.person['bUnlockFlag'] = self['bUnlockFlag']
        self.person['bIsAuto'] = self['bIsAuto']
        self.person['bNewUnlock'] = self['bNewUnlock']
        self.person['bXiuZhenUnlock'] = self['bXiuZhenUnlock']
        # end handle [GC_UPDATE_SKILL_UNLOCK_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_GET_ITEM] message attrs, auto generate do not change
        self.person['itemId'] = self['itemId']
        self.person['count'] = self['count']
        # end handle [GC_GET_ITEM] message attrs, auto generate do not change
        pass


class GC_KXJFAWARD_DATA (Packet):
    def handle(self):
        # begin handle [GC_KXJFAWARD_DATA] message attrs, auto generate do not change
        self.person['AwardID'] = self['AwardID']
        self.person['LeftTime'] = self['LeftTime']
        self.person['IsStart'] = self['IsStart']
        # end handle [GC_KXJFAWARD_DATA] message attrs, auto generate do not change
        pass


class CG_USE_ITEM_PETAGG (Packet):
    pass


class GC_GUILDFIGHT_WORLDBOSS_RANK (Packet):
    def handle(self):
        # begin handle [GC_GUILDFIGHT_WORLDBOSS_RANK] message attrs, auto generate do not change
        self.person['BossDataId'] = self['BossDataId']
        self.person['RankData1'] = self['RankData1']
        self.person['RankData2'] = self['RankData2']
        self.person['RankData3'] = self['RankData3']
        self.person['IsBoss1Dead'] = self['IsBoss1Dead']
        self.person['IsBoss2Dead'] = self['IsBoss2Dead']
        self.person['IsBoss3Dead'] = self['IsBoss3Dead']
        # end handle [GC_GUILDFIGHT_WORLDBOSS_RANK] message attrs, auto generate do not change
        pass


class GC_SKILLBAR_EXTRA_CD (Packet):
    def handle(self):
        # begin handle [GC_SKILLBAR_EXTRA_CD] message attrs, auto generate do not change
        self.person['barSkillID'] = self['barSkillID']
        self.person['cdSkillID'] = self['cdSkillID']
        # end handle [GC_SKILLBAR_EXTRA_CD] message attrs, auto generate do not change
        pass


class GC_BROADCAST_ATTR (Packet):
    def handle(self):
        # begin handle [GC_BROADCAST_ATTR] message attrs, auto generate do not change
        self.person['ObjId'] = self['ObjId']
        self.person['CurProfession'] = self['CurProfession']
        self.person['Name'] = self['Name']
        self.person['CurForce'] = self['CurForce']
        self.person['MoveSpeed'] = self['MoveSpeed']
        self.person['bDie'] = self['bDie']
        self.person['StealthLev'] = self['StealthLev']
        self.person['BodyVisualId'] = self['BodyVisualId']
        self.person['WeaponVisualId'] = self['WeaponVisualId']
        self.person['FaceVisualId'] = self['FaceVisualId']
        self.person['IsInCombat'] = self['IsInCombat']
        self.person['SexType'] = self['SexType']
        self.person['bindparent'] = self['bindparent']
        self.person['bindchildren'] = self['bindchildren']
        self.person['PkState'] = self['PkState']
        self.person['PKValue'] = self['PKValue']
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['FamilyGuid'] = self['FamilyGuid']
        self.person['TransforId'] = self['TransforId']
        self.person['Level'] = self['Level']
        self.person['TeamId'] = self['TeamId']
        self.person['TeamLeader'] = self['TeamLeader']
        self.person['FollowMem'] = self['FollowMem']
        self.person['Reserved1'] = self['Reserved1']
        self.person['Reserved2'] = self['Reserved2']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['ShowCombat'] = self['ShowCombat']
        self.person['HairVisualId'] = self['HairVisualId']
        self.person['Refine10Times'] = self['Refine10Times']
        self.person['CombatEffectId'] = self['CombatEffectId']
        self.person['DigUpTheHatchetGuildGuid'] = self['DigUpTheHatchetGuildGuid']
        self.person['IsTeamLeader'] = self['IsTeamLeader']
        self.person['BodyColorEffectVisual'] = self['BodyColorEffectVisual']
        self.person['SkillTransId'] = self['SkillTransId']
        self.person['BuffTransId'] = self['BuffTransId']
        self.person['CurHp'] = self['CurHp']
        self.person['TransformType'] = self['TransformType']
        self.person['ArmyID'] = self['ArmyID']
        self.person['IsArmyLeader'] = self['IsArmyLeader']
        self.person['BodyFashoinId'] = self['BodyFashoinId']
        self.person['BodyColorIndex'] = self['BodyColorIndex']
        self.person['AircraftFashoinId'] = self['AircraftFashoinId']
        self.person['AircraftColorIndex'] = self['AircraftColorIndex']
        self.person['MountFashoinId'] = self['MountFashoinId']
        self.person['MountColorIndex'] = self['MountColorIndex']
        self.person['PhysicalDefence'] = self['PhysicalDefence']
        self.person['MagicalDefence'] = self['MagicalDefence']
        self.person['BattleFairyId'] = self['BattleFairyId']
        self.person['FairyTargetServerID'] = self['FairyTargetServerID']
        self.person['HairFashoinId'] = self['HairFashoinId']
        self.person['HairColorIndex'] = self['HairColorIndex']
        self.person['WeaponFashoinId'] = self['WeaponFashoinId']
        self.person['WeaponColorIndex'] = self['WeaponColorIndex']
        self.person['ProfessionCamp'] = self['ProfessionCamp']
        self.person['GemSetId'] = self['GemSetId']
        self.person['LuckyValue'] = self['LuckyValue']
        self.person['BasicSkillSpeed'] = self['BasicSkillSpeed']
        self.person['SpecialSkillSpeed'] = self['SpecialSkillSpeed']
        self.person['IsShowHelmet'] = self['IsShowHelmet']
        self.person['showtail'] = self['showtail']
        self.person['bindobjtype'] = self['bindobjtype']
        self.person['BattleFairyEvolvePhase'] = self['BattleFairyEvolvePhase']
        self.person['BodyFreeDyeUseSlotIndex'] = self['BodyFreeDyeUseSlotIndex']
        self.person['HairFreeDyeUseSlotIndex'] = self['HairFreeDyeUseSlotIndex']
        self.person['BodyFreeDyeColorInfo'] = self['BodyFreeDyeColorInfo']
        self.person['HairFreeDyeColorInfo'] = self['HairFreeDyeColorInfo']
        self.person['BackFashionId'] = self['BackFashionId']
        self.person['BackColorIndex'] = self['BackColorIndex']
        self.person['BuffBodyVisualId'] = self['BuffBodyVisualId']
        self.person['BuffHairVisualId'] = self['BuffHairVisualId']
        self.person['BuffWeaponVisualId'] = self['BuffWeaponVisualId']
        self.person['BuffBodyFashionId'] = self['BuffBodyFashionId']
        self.person['BuffHairFashionId'] = self['BuffHairFashionId']
        self.person['BuffWeaponFashionId'] = self['BuffWeaponFashionId']
        self.person['BuffBackFashionId'] = self['BuffBackFashionId']
        self.person['BuffBodyColorIndex'] = self['BuffBodyColorIndex']
        self.person['BuffHairColorIndex'] = self['BuffHairColorIndex']
        self.person['BuffWeaponColorIndex'] = self['BuffWeaponColorIndex']
        self.person['BuffBodyFreeDyeSlotIndex'] = self['BuffBodyFreeDyeSlotIndex']
        self.person['BuffHairFreeDyeSlotIndex'] = self['BuffHairFreeDyeSlotIndex']
        self.person['BuffBodyFreeDyeColorInfo'] = self['BuffBodyFreeDyeColorInfo']
        self.person['BuffHairFreeDyeColorInfo'] = self['BuffHairFreeDyeColorInfo']
        self.person['GuildProclaimWarGuid'] = self['GuildProclaimWarGuid']
        self.person['MirrorZombieId'] = self['MirrorZombieId']
        self.person['showear'] = self['showear']
        # end handle [GC_BROADCAST_ATTR] message attrs, auto generate do not change
        pass


class GC_SYNC_BIGBATTLE_TIMES (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BIGBATTLE_TIMES] message attrs, auto generate do not change
        self.person['FoodBigBattleTimes'] = self['FoodBigBattleTimes']
        # end handle [GC_SYNC_BIGBATTLE_TIMES] message attrs, auto generate do not change
        pass


class CG_GUILD_REQ_CHANGENAME (Packet):
    pass


class CG_ASK_SUBSCIBE_INFO (Packet):
    pass


class GC_TIANSHU_DECOMPOSE (Packet):
    def handle(self):
        # begin handle [GC_TIANSHU_DECOMPOSE] message attrs, auto generate do not change
        self.person['debrisCount'] = self['debrisCount']
        # end handle [GC_TIANSHU_DECOMPOSE] message attrs, auto generate do not change
        pass


class GC_COPYSCENE_COMBATSTATE (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_COMBATSTATE] message attrs, auto generate do not change
        self.person['copyscenecombatstate'] = self['copyscenecombatstate']
        # end handle [GC_COPYSCENE_COMBATSTATE] message attrs, auto generate do not change
        pass


class CG_MIS_OPERATE_NPC (Packet):
    pass


class GC_GET_EXP (Packet):
    def handle(self):
        # begin handle [GC_GET_EXP] message attrs, auto generate do not change
        self.person['count'] = self['count']
        self.person['prayCount'] = self['prayCount']
        # end handle [GC_GET_EXP] message attrs, auto generate do not change
        pass


class GC_GET_XX (Packet):
    def handle(self):
        # begin handle [GC_GET_XX] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['id'] = self['id']
        self.person['count'] = self['count']
        # end handle [GC_GET_XX] message attrs, auto generate do not change
        pass


class GC_PLAY_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_PLAY_EFFECT] message attrs, auto generate do not change
        self.person['ObjID'] = self['ObjID']
        self.person['EffectID'] = self['EffectID']
        self.person['isForCreateObj'] = self['isForCreateObj']
        self.person['isForEffectCamera'] = self['isForEffectCamera']
        self.person['EffectLookObjId'] = self['EffectLookObjId']
        self.person['SenderPositionX'] = self['SenderPositionX']
        self.person['SenderPositionY'] = self['SenderPositionY']
        self.person['SenderPositionZ'] = self['SenderPositionZ']
        self.person['TargetPositionX'] = self['TargetPositionX']
        self.person['TargetPositionY'] = self['TargetPositionY']
        self.person['TargetPositionZ'] = self['TargetPositionZ']
        self.person['senderID'] = self['senderID']
        self.person['worldAngle'] = self['worldAngle']
        self.person['speed'] = self['speed']
        self.person['isBindToScene'] = self['isBindToScene']
        self.person['text'] = self['text']
        # end handle [GC_PLAY_EFFECT] message attrs, auto generate do not change
        pass


class GC_RET_ADVENTURE_EVENT_COMPLETED (Packet):
    def handle(self):
        # begin handle [GC_RET_ADVENTURE_EVENT_COMPLETED] message attrs, auto generate do not change
        self.person['eventId'] = self['eventId']
        self.person['time'] = self['time']
        # end handle [GC_RET_ADVENTURE_EVENT_COMPLETED] message attrs, auto generate do not change
        pass


class CG_FASHION_RANDOM_COLOR_CHANGE (Packet):
    pass


class GC_SyncXueChiState (Packet):
    def handle(self):
        # begin handle [GC_SyncXueChiState] message attrs, auto generate do not change
        self.person['xueChiState'] = self['xueChiState']
        # end handle [GC_SyncXueChiState] message attrs, auto generate do not change
        pass


class CG_SET_BLOCK_FRIENDAPPLY (Packet):
    pass


class CG_CHANGE_TITLE (Packet):
    pass


class GC_MISSION_IGNOREMISPREFLAG (Packet):
    def handle(self):
        # begin handle [GC_MISSION_IGNOREMISPREFLAG] message attrs, auto generate do not change
        self.person['flag'] = self['flag']
        # end handle [GC_MISSION_IGNOREMISPREFLAG] message attrs, auto generate do not change
        pass


class CG_ACCEPT_XIUZHEN_LEVEL_REWARD (Packet):
    pass


class GC_UPDATE_PRODUCE_OBJ_DATA (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_PRODUCE_OBJ_DATA] message attrs, auto generate do not change
        self.person['BuildingGuid'] = self['BuildingGuid']
        self.person['nObjIdList'] = self['nObjIdList']
        # end handle [GC_UPDATE_PRODUCE_OBJ_DATA] message attrs, auto generate do not change
        pass


class CG_XIUZHEN_INCREASE (Packet):
    pass


class CG_MILITARY_REQ_GET_BADGE (Packet):
    pass


class CG_REQ_GUILD_THIEF_NUM (Packet):
    pass


class GC_RET_PKNOTICE (Packet):
    def handle(self):
        # begin handle [GC_RET_PKNOTICE] message attrs, auto generate do not change
        # end handle [GC_RET_PKNOTICE] message attrs, auto generate do not change
        pass


class GC_SPOKESMAN_SYNC_DIALOGUE (Packet):
    def handle(self):
        # begin handle [GC_SPOKESMAN_SYNC_DIALOGUE] message attrs, auto generate do not change
        self.person['CurrentDialogueGroup'] = self['CurrentDialogueGroup']
        self.person['CurrentDialogueId'] = self['CurrentDialogueId']
        # end handle [GC_SPOKESMAN_SYNC_DIALOGUE] message attrs, auto generate do not change
        pass


class GC_SYNC_SKILL_LAYER_CD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SKILL_LAYER_CD] message attrs, auto generate do not change
        self.person['skillBaseID'] = self['skillBaseID']
        self.person['layer'] = self['layer']
        # end handle [GC_SYNC_SKILL_LAYER_CD] message attrs, auto generate do not change
        pass


class CG_SKILL_ACTIVE (Packet):
    pass


class CG_REQ_GUILDWAR_HISTROY_RANK_INFO (Packet):
    pass


class CG_FAIRY_RAISE_ACTION (Packet):
    pass


class GC_PLAY_BULLET_IN_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_PLAY_BULLET_IN_CONFIG] message attrs, auto generate do not change
        self.person['senderObjID'] = self['senderObjID']
        self.person['bulletDataID'] = self['bulletDataID']
        self.person['tarType'] = self['tarType']
        self.person['targetObjID'] = self['targetObjID']
        self.person['PosX'] = self['PosX']
        self.person['PosY'] = self['PosY']
        self.person['PosZ'] = self['PosZ']
        # end handle [GC_PLAY_BULLET_IN_CONFIG] message attrs, auto generate do not change
        pass


class GC_RET_GUILD_ADDITION (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILD_ADDITION] message attrs, auto generate do not change
        self.person['index'] = self['index']
        self.person['level'] = self['level']
        self.person['exp'] = self['exp']
        self.person['contribute'] = self['contribute']
        self.person['silver'] = self['silver']
        # end handle [GC_RET_GUILD_ADDITION] message attrs, auto generate do not change
        pass


class GC_REPLY_YIRONG_CARD (Packet):
    def handle(self):
        # begin handle [GC_REPLY_YIRONG_CARD] message attrs, auto generate do not change
        self.person['carddays'] = self['carddays']
        self.person['starttime'] = self['starttime']
        # end handle [GC_REPLY_YIRONG_CARD] message attrs, auto generate do not change
        pass


class CG_REQUEST_BUY_HOME_EXTERIOR (Packet):
    pass


class GC_RET_SIGNININFO (Packet):
    def handle(self):
        # begin handle [GC_RET_SIGNININFO] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        self.person['index'] = self['index']
        self.person['status'] = self['status']
        self.person['reserved'] = self['reserved']
        self.person['Exp'] = self['Exp']
        self.person['Jinbin'] = self['Jinbin']
        self.person['Yinbin'] = self['Yinbin']
        self.person['Yuanbao'] = self['Yuanbao']
        self.person['BindYuanbao'] = self['BindYuanbao']
        self.person['Item1DataID'] = self['Item1DataID']
        self.person['Item1Count'] = self['Item1Count']
        self.person['Item2DataID'] = self['Item2DataID']
        self.person['Item2count'] = self['Item2count']
        self.person['supplySignCost'] = self['supplySignCost']
        self.person['curNaturalIndex'] = self['curNaturalIndex']
        self.person['curMounthIndex'] = self['curMounthIndex']
        self.person['firstCanSignIndex'] = self['firstCanSignIndex']
        self.person['alreadySignedCount'] = self['alreadySignedCount']
        self.person['allowShow'] = self['allowShow']
        self.person['allowSign'] = self['allowSign']
        # end handle [GC_RET_SIGNININFO] message attrs, auto generate do not change
        pass


class CG_REQ_ACCEPT_APPRENTICE (Packet):
    pass


class CG_ASK_KXJFAWARD (Packet):
    pass


class CG_MISSION_STATE (Packet):
    pass


class GC_CHAT (Packet):
    def handle(self):
        # begin handle [GC_CHAT] message attrs, auto generate do not change
        self.person['Content'] = self['Content']
        self.person['Channel'] = self['Channel']
        self.person['Link'] = self['Link']
        self.person['LinkData'] = self['LinkData']
        self.person['VoiceIndex'] = self['VoiceIndex']
        self.person['VoiceDuration'] = self['VoiceDuration']
        self.person['LinkDownloadIndex'] = self['LinkDownloadIndex']
        self.person['LinkColorParam'] = self['LinkColorParam']
        self.person['SenderActor'] = self['SenderActor']
        self.person['ReceiverActor'] = self['ReceiverActor']
        self.person['ChannelParam'] = self['ChannelParam']
        self.person['VoiceLanguage'] = self['VoiceLanguage']
        self.person['ChatTime'] = self['ChatTime']
        # end handle [GC_CHAT] message attrs, auto generate do not change
        pass


class CG_DELFRIEND (Packet):
    pass


class CG_LOCK_FAIRY_SKILL (Packet):
    pass


class GC_GODWEAPON_EQUIP (Packet):
    def handle(self):
        # begin handle [GC_GODWEAPON_EQUIP] message attrs, auto generate do not change
        self.person['CurEquipPos'] = self['CurEquipPos']
        # end handle [GC_GODWEAPON_EQUIP] message attrs, auto generate do not change
        pass


class GC_BIGWORLDPVP_PRE_RET_LIST (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDPVP_PRE_RET_LIST] message attrs, auto generate do not change
        self.person['rettype'] = self['rettype']
        self.person['nowstate'] = self['nowstate']
        self.person['self'] = self['self']
        self.person['leaveTimes'] = self['leaveTimes']
        self.person['firstTeam'] = self['firstTeam']
        self.person['secondTeam'] = self['secondTeam']
        self.person['thirdTeam'] = self['thirdTeam']
        self.person['matchTime'] = self['matchTime']
        self.person['finalList'] = self['finalList']
        self.person['page'] = self['page']
        self.person['totalpage'] = self['totalpage']
        self.person['turnNum'] = self['turnNum']
        self.person['winFlags'] = self['winFlags']
        self.person['seasonNum'] = self['seasonNum']
        self.person['serverLv'] = self['serverLv']
        # end handle [GC_BIGWORLDPVP_PRE_RET_LIST] message attrs, auto generate do not change
        pass


class GC_ENTER_COPY_SCENE_ENVIROMENT (Packet):
    def handle(self):
        # begin handle [GC_ENTER_COPY_SCENE_ENVIROMENT] message attrs, auto generate do not change
        self.person['enviromentDataId'] = self['enviromentDataId']
        # end handle [GC_ENTER_COPY_SCENE_ENVIROMENT] message attrs, auto generate do not change
        pass


class CG_REQ_FAIRY_NEIDAN_LEVELUP (Packet):
    pass


class GC_MENTOR_BUY_RESULT (Packet):
    def handle(self):
        # begin handle [GC_MENTOR_BUY_RESULT] message attrs, auto generate do not change
        self.person['MentorShopID'] = self['MentorShopID']
        self.person['BuyCount'] = self['BuyCount']
        self.person['TeachingPoint'] = self['TeachingPoint']
        # end handle [GC_MENTOR_BUY_RESULT] message attrs, auto generate do not change
        pass


class GC_RET_GUILDCONVOY_CONFIRM (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILDCONVOY_CONFIRM] message attrs, auto generate do not change
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberProfession'] = self['memberProfession']
        self.person['memberstatus'] = self['memberstatus']
        self.person['panelStatus'] = self['panelStatus']
        self.person['hasRewardCount'] = self['hasRewardCount']
        self.person['pathId'] = self['pathId']
        self.person['count'] = self['count']
        # end handle [GC_RET_GUILDCONVOY_CONFIRM] message attrs, auto generate do not change
        pass


class CG_UNEQUIP_ITEM (Packet):
    pass


class CG_REQ_TEAM_JOIN (Packet):
    pass


class CG_ASKENEMYMEMINFO (Packet):
    pass


class GC_BREAK_LIFESKILL_PREOCESS (Packet):
    def handle(self):
        # begin handle [GC_BREAK_LIFESKILL_PREOCESS] message attrs, auto generate do not change
        self.person['type'] = self['type']
        # end handle [GC_BREAK_LIFESKILL_PREOCESS] message attrs, auto generate do not change
        pass


class GC_OFFLINE_CHAT_PERSONAL (Packet):
    def handle(self):
        # begin handle [GC_OFFLINE_CHAT_PERSONAL] message attrs, auto generate do not change
        self.person['Content'] = self['Content']
        self.person['SenderGuid'] = self['SenderGuid']
        self.person['SenderName'] = self['SenderName']
        self.person['SenderProfession'] = self['SenderProfession']
        self.person['SenderSex'] = self['SenderSex']
        self.person['reserved1'] = self['reserved1']
        self.person['Link'] = self['Link']
        self.person['LinkData'] = self['LinkData']
        self.person['ReciverGuid'] = self['ReciverGuid']
        self.person['ReciverName'] = self['ReciverName']
        self.person['ReciverProfession'] = self['ReciverProfession']
        self.person['ReciverSex'] = self['ReciverSex']
        self.person['reserved2'] = self['reserved2']
        self.person['SendTime'] = self['SendTime']
        # end handle [GC_OFFLINE_CHAT_PERSONAL] message attrs, auto generate do not change
        pass


class GC_RES_SET_PET_AUTO_FEED (Packet):
    def handle(self):
        # begin handle [GC_RES_SET_PET_AUTO_FEED] message attrs, auto generate do not change
        self.person['tagList'] = self['tagList']
        # end handle [GC_RES_SET_PET_AUTO_FEED] message attrs, auto generate do not change
        pass


class CG_STALL_SELL (Packet):
    pass


class CG_STALL_SEARCH (Packet):
    pass


class GC_MAKE_INTERACT (Packet):
    def handle(self):
        # begin handle [GC_MAKE_INTERACT] message attrs, auto generate do not change
        self.person['inviterServerID'] = self['inviterServerID']
        self.person['inviteeServerID'] = self['inviteeServerID']
        self.person['interactType'] = self['interactType']
        # end handle [GC_MAKE_INTERACT] message attrs, auto generate do not change
        pass


class GC_SYNC_COMMONFLAG (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COMMONFLAG] message attrs, auto generate do not change
        self.person['nIndex'] = self['nIndex']
        self.person['bFlag'] = self['bFlag']
        # end handle [GC_SYNC_COMMONFLAG] message attrs, auto generate do not change
        pass


class CG_SKILL_LEVEL_UP (Packet):
    pass


class GC_UPDATE_XIUZHEN_PRACTICE_DATA (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_XIUZHEN_PRACTICE_DATA] message attrs, auto generate do not change
        self.person['xiuZhenPracticeData'] = self['xiuZhenPracticeData']
        # end handle [GC_UPDATE_XIUZHEN_PRACTICE_DATA] message attrs, auto generate do not change
        pass


class GC_SWITCH_HOME_PLAN (Packet):
    def handle(self):
        # begin handle [GC_SWITCH_HOME_PLAN] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        # end handle [GC_SWITCH_HOME_PLAN] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_ASK_RELIVESKILL] message attrs, auto generate do not change
        self.person['sendername'] = self['sendername']
        self.person['buffID'] = self['buffID']
        # end handle [GC_ASK_RELIVESKILL] message attrs, auto generate do not change
        pass


class GC_INTERACT_JUMP (Packet):
    def handle(self):
        # begin handle [GC_INTERACT_JUMP] message attrs, auto generate do not change
        self.person['inviterServerID'] = self['inviterServerID']
        self.person['interactType'] = self['interactType']
        # end handle [GC_INTERACT_JUMP] message attrs, auto generate do not change
        pass


class GC_SYNC_FIREWORKS_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FIREWORKS_DATA] message attrs, auto generate do not change
        self.person['activityId'] = self['activityId']
        self.person['blessNum'] = self['blessNum']
        self.person['awardFlag'] = self['awardFlag']
        self.person['guildBlessNum'] = self['guildBlessNum']
        # end handle [GC_SYNC_FIREWORKS_DATA] message attrs, auto generate do not change
        pass


class GC_SYNCFLYMISREWARD (Packet):
    def handle(self):
        # begin handle [GC_SYNCFLYMISREWARD] message attrs, auto generate do not change
        self.person['getreward'] = self['getreward']
        # end handle [GC_SYNCFLYMISREWARD] message attrs, auto generate do not change
        pass


class CG_SEARCHSDKCHECK_GUILD (Packet):
    pass


class GC_BATTLEFIELD_REWARD (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_REWARD] message attrs, auto generate do not change
        self.person['itemId'] = self['itemId']
        self.person['itemNumber'] = self['itemNumber']
        # end handle [GC_BATTLEFIELD_REWARD] message attrs, auto generate do not change
        pass


class CG_DELBLACKLIST (Packet):
    pass


class GC_BUY_NIEREN_SUPER (Packet):
    def handle(self):
        # begin handle [GC_BUY_NIEREN_SUPER] message attrs, auto generate do not change
        # end handle [GC_BUY_NIEREN_SUPER] message attrs, auto generate do not change
        pass


class GC_RET_REPLACE_EQUIP_REBIRTH_RECASE_TRICK (Packet):
    def handle(self):
        # begin handle [GC_RET_REPLACE_EQUIP_REBIRTH_RECASE_TRICK] message attrs, auto generate do not change
        self.person['nResult'] = self['nResult']
        # end handle [GC_RET_REPLACE_EQUIP_REBIRTH_RECASE_TRICK] message attrs, auto generate do not change
        pass


class GC_CREATE_ROLE_RET (Packet):
    def handle(self):
        # begin handle [GC_CREATE_ROLE_RET] message attrs, auto generate do not change
        self.person['createresult'] = self['createresult']
        self.person['name'] = self['name']
        self.person['sex'] = self['sex']
        self.person['profession'] = self['profession']
        self.person['guid'] = self['guid']
        self.person['hairvisual'] = self['hairvisual']
        self.person['facevisual'] = self['facevisual']
        self.person['bodyvisual'] = self['bodyvisual']
        self.person['createroletime'] = self['createroletime']
        self.person['NieRenValue'] = self['NieRenValue']
        # end handle [GC_CREATE_ROLE_RET] message attrs, auto generate do not change
        pass


class GC_TOURNAMENT_SYNC_INFO (Packet):
    def handle(self):
        # begin handle [GC_TOURNAMENT_SYNC_INFO] message attrs, auto generate do not change
        self.person['rankList'] = self['rankList']
        self.person['myRankInfo'] = self['myRankInfo']
        self.person['recordInfo'] = self['recordInfo']
        self.person['killCount'] = self['killCount']
        # end handle [GC_TOURNAMENT_SYNC_INFO] message attrs, auto generate do not change
        pass


class GC_SYSTEMTRADE_RETSELLLIST (Packet):
    def handle(self):
        # begin handle [GC_SYSTEMTRADE_RETSELLLIST] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['itemid'] = self['itemid']
        self.person['buycount'] = self['buycount']
        self.person['price'] = self['price']
        self.person['tagtype'] = self['tagtype']
        self.person['discount'] = self['discount']
        # end handle [GC_SYSTEMTRADE_RETSELLLIST] message attrs, auto generate do not change
        pass


class CG_USE_CONVO_CD_SKILL_TRIGER (Packet):
    pass


class CG_REQ_CV_MARRIAGE_GIFT (Packet):
    pass


class GC_CHALLENGE_MYDATA (Packet):
    def handle(self):
        # begin handle [GC_CHALLENGE_MYDATA] message attrs, auto generate do not change
        self.person['challengeTimes'] = self['challengeTimes']
        self.person['HonorCoins'] = self['HonorCoins']
        self.person['rankPos'] = self['rankPos']
        self.person['CurChallTimes'] = self['CurChallTimes']
        self.person['MaxFreeChallengeTimes'] = self['MaxFreeChallengeTimes']
        self.person['MaxBuyChallengeTimes'] = self['MaxBuyChallengeTimes']
        self.person['fakeRankPos'] = self['fakeRankPos']
        self.person['MaxBuyTimes'] = self['MaxBuyTimes']
        self.person['NeedCost'] = self['NeedCost']
        self.person['OnceRankRewardPos'] = self['OnceRankRewardPos']
        # end handle [GC_CHALLENGE_MYDATA] message attrs, auto generate do not change
        pass


class CG_DELE_WILDSCENEDUELINFO (Packet):
    pass


class GC_CHAR_FACEDIR (Packet):
    def handle(self):
        # begin handle [GC_CHAR_FACEDIR] message attrs, auto generate do not change
        self.person['ObjId'] = self['ObjId']
        self.person['FaceDir'] = self['FaceDir']
        self.person['isCameraReset'] = self['isCameraReset']
        self.person['isSetBackHomeDir'] = self['isSetBackHomeDir']
        # end handle [GC_CHAR_FACEDIR] message attrs, auto generate do not change
        pass


class CG_LEAVE_HOME_SCENE (Packet):
    pass


class GC_GUILD_ON_BANGHUA_ACTIVE (Packet):
    def handle(self):
        # begin handle [GC_GUILD_ON_BANGHUA_ACTIVE] message attrs, auto generate do not change
        self.person['isActive'] = self['isActive']
        # end handle [GC_GUILD_ON_BANGHUA_ACTIVE] message attrs, auto generate do not change
        pass


class GC_RES_GUILDAUCTION_INFO (Packet):
    def handle(self):
        # begin handle [GC_RES_GUILDAUCTION_INFO] message attrs, auto generate do not change
        self.person['actType'] = self['actType']
        self.person['items'] = self['items']
        self.person['dividendTax'] = self['dividendTax']
        # end handle [GC_RES_GUILDAUCTION_INFO] message attrs, auto generate do not change
        pass


class GC_STALL_RETLOOK (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETLOOK] message attrs, auto generate do not change
        self.person['page'] = self['page']
        self.person['publictime'] = self['publictime']
        self.person['order'] = self['order']
        self.person['classid'] = self['classid']
        self.person['subclassid'] = self['subclassid']
        self.person['treasure'] = self['treasure']
        self.person['quality'] = self['quality']
        self.person['profession'] = self['profession']
        self.person['minlevel'] = self['minlevel']
        self.person['maxlevel'] = self['maxlevel']
        self.person['otherclass'] = self['otherclass']
        self.person['itemid'] = self['itemid']
        self.person['attr'] = self['attr']
        self.person['thirdclassid'] = self['thirdclassid']
        self.person['reserved'] = self['reserved']
        self.person['reserved1'] = self['reserved1']
        self.person['color'] = self['color']
        self.person['stallitems'] = self['stallitems']
        self.person['maxcount'] = self['maxcount']
        self.person['reserverd2'] = self['reserverd2']
        self.person['minprice'] = self['minprice']
        self.person['maxprice'] = self['maxprice']
        self.person['issearch'] = self['issearch']
        # end handle [GC_STALL_RETLOOK] message attrs, auto generate do not change
        pass


class GC_SYNC_WORDREDPACKETRAIN_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_WORDREDPACKETRAIN_INFO] message attrs, auto generate do not change
        self.person['state'] = self['state']
        self.person['endTime'] = self['endTime']
        self.person['question'] = self['question']
        self.person['result'] = self['result']
        self.person['sceneId'] = self['sceneId']
        # end handle [GC_SYNC_WORDREDPACKETRAIN_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_ACHIEVEMENT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        self.person['recordID'] = self['recordID']
        self.person['bRecordFinish'] = self['bRecordFinish']
        self.person['bRecordHaveReward'] = self['bRecordHaveReward']
        # end handle [GC_SYNC_ACHIEVEMENT_INFO] message attrs, auto generate do not change
        pass


class CG_BIGWORLDPVP_PRE_REQ_LIST (Packet):
    pass


class GC_BATTLEFIELD_RESULT (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_RESULT] message attrs, auto generate do not change
        self.person['WinnerGroupID'] = self['WinnerGroupID']
        # end handle [GC_BATTLEFIELD_RESULT] message attrs, auto generate do not change
        pass


class CG_WAITPAY_PAY (Packet):
    pass


class CG_ADDRECENTCONTACTLIST (Packet):
    pass


class GC_UPDATE_XIUZHEN_LEVEL_REWARD (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_XIUZHEN_LEVEL_REWARD] message attrs, auto generate do not change
        self.person['xiuZhenRewardData'] = self['xiuZhenRewardData']
        # end handle [GC_UPDATE_XIUZHEN_LEVEL_REWARD] message attrs, auto generate do not change
        pass


class GC_SYNC_RECHARGEDOUBLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RECHARGEDOUBLE] message attrs, auto generate do not change
        self.person['isopen'] = self['isopen']
        self.person['baseleftyuan1'] = self['baseleftyuan1']
        self.person['baseleftyuan6'] = self['baseleftyuan6']
        self.person['baseleftyuan30'] = self['baseleftyuan30']
        self.person['baseleftyuan50'] = self['baseleftyuan50']
        self.person['baseleftyuan98'] = self['baseleftyuan98']
        self.person['baseleftyuan198'] = self['baseleftyuan198']
        self.person['baseleftyuan328'] = self['baseleftyuan328']
        self.person['baseleftyuan648'] = self['baseleftyuan648']
        self.person['baseleftanynum'] = self['baseleftanynum']
        self.person['isinact'] = self['isinact']
        self.person['actbegin'] = self['actbegin']
        self.person['actend'] = self['actend']
        self.person['actleftyuan1'] = self['actleftyuan1']
        self.person['actleftyuan6'] = self['actleftyuan6']
        self.person['actleftyuan30'] = self['actleftyuan30']
        self.person['actleftyuan50'] = self['actleftyuan50']
        self.person['actleftyuan98'] = self['actleftyuan98']
        self.person['actleftyuan198'] = self['actleftyuan198']
        self.person['actleftyuan328'] = self['actleftyuan328']
        self.person['actleftyuan648'] = self['actleftyuan648']
        # end handle [GC_SYNC_RECHARGEDOUBLE] message attrs, auto generate do not change
        pass


class CG_REQ_BUY_HOME_HORDE_SHOP (Packet):
    pass


class GC_SYNC_SAMSARA_PRE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SAMSARA_PRE_DATA] message attrs, auto generate do not change
        self.person['presubmititemid'] = self['presubmititemid']
        self.person['prestatus'] = self['prestatus']
        self.person['prebegtm'] = self['prebegtm']
        self.person['preendtm'] = self['preendtm']
        self.person['realopentm'] = self['realopentm']
        self.person['prenowprocess'] = self['prenowprocess']
        self.person['premaxprocess'] = self['premaxprocess']
        self.person['minplayerlv'] = self['minplayerlv']
        self.person['maxitempersubmit'] = self['maxitempersubmit']
        # end handle [GC_SYNC_SAMSARA_PRE_DATA] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_TEAMUP (Packet):
    pass


class CG_REQ_SHARE_GAME_DATA (Packet):
    pass


class GC_TOWER_FIGHT_TIME (Packet):
    def handle(self):
        # begin handle [GC_TOWER_FIGHT_TIME] message attrs, auto generate do not change
        self.person['EndTime'] = self['EndTime']
        # end handle [GC_TOWER_FIGHT_TIME] message attrs, auto generate do not change
        pass


class GC_TOURNAMENT_SYNC_BATTLE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_TOURNAMENT_SYNC_BATTLE_RESULT] message attrs, auto generate do not change
        self.person['isWin'] = self['isWin']
        self.person['addScore'] = self['addScore']
        self.person['conWinScore'] = self['conWinScore']
        self.person['conWinTimes'] = self['conWinTimes']
        self.person['rewardExp'] = self['rewardExp']
        self.person['rewardSilver'] = self['rewardSilver']
        self.person['rewardItemId'] = self['rewardItemId']
        self.person['rewardItemCount'] = self['rewardItemCount']
        self.person['currentRewardTimes'] = self['currentRewardTimes']
        self.person['totalRewardTimes'] = self['totalRewardTimes']
        # end handle [GC_TOURNAMENT_SYNC_BATTLE_RESULT] message attrs, auto generate do not change
        pass


class CG_REQ_UPDATE_AUCTION_ONE (Packet):
    pass


class CG_HOLIDAY_REDPOINT_REQ (Packet):
    pass


class GC_MOVABLE_STORAGEPACK_INFO (Packet):
    def handle(self):
        # begin handle [GC_MOVABLE_STORAGEPACK_INFO] message attrs, auto generate do not change
        self.person['OverDurTime'] = self['OverDurTime']
        self.person['IsUseItemAddTime'] = self['IsUseItemAddTime']
        # end handle [GC_MOVABLE_STORAGEPACK_INFO] message attrs, auto generate do not change
        pass


class CG_GATHER_POINT (Packet):
    pass


class CG_PA_OPERATE_RESPONSE (Packet):
    pass


class CG_UPDATE_SUPERR_REDDOT (Packet):
    pass


class GC_UPDATE_SKILL_ACTIVE_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_SKILL_ACTIVE_INFO] message attrs, auto generate do not change
        self.person['nSkillClassId'] = self['nSkillClassId']
        self.person['bActiveFlag'] = self['bActiveFlag']
        self.person['bIsAuto'] = self['bIsAuto']
        self.person['bNewActive'] = self['bNewActive']
        # end handle [GC_UPDATE_SKILL_ACTIVE_INFO] message attrs, auto generate do not change
        pass


class GC_SYSTEMTRADE_SELL (Packet):
    def handle(self):
        # begin handle [GC_SYSTEMTRADE_SELL] message attrs, auto generate do not change
        # end handle [GC_SYSTEMTRADE_SELL] message attrs, auto generate do not change
        pass


class GC_BANGHUA_SYNCSCORE (Packet):
    def handle(self):
        # begin handle [GC_BANGHUA_SYNCSCORE] message attrs, auto generate do not change
        self.person['score'] = self['score']
        self.person['nextScore'] = self['nextScore']
        # end handle [GC_BANGHUA_SYNCSCORE] message attrs, auto generate do not change
        pass


class CG_STALL_LOOK (Packet):
    pass


class GC_GWSKILL_ASKHELP (Packet):
    def handle(self):
        # begin handle [GC_GWSKILL_ASKHELP] message attrs, auto generate do not change
        self.person['UserGuid'] = self['UserGuid']
        # end handle [GC_GWSKILL_ASKHELP] message attrs, auto generate do not change
        pass


class CG_ASK_SAMSARA_PRE_REWARD (Packet):
    pass


class GC_SYNC_SURVEY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SURVEY_INFO] message attrs, auto generate do not change
        self.person['versionID'] = self['versionID']
        self.person['url'] = self['url']
        self.person['startTime'] = self['startTime']
        self.person['endTime'] = self['endTime']
        # end handle [GC_SYNC_SURVEY_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_KIT_PACK (Packet):
    def handle(self):
        # begin handle [GC_SYNC_KIT_PACK] message attrs, auto generate do not change
        self.person['validCount'] = self['validCount']
        self.person['items'] = self['items']
        self.person['itemUnlockState'] = self['itemUnlockState']
        # end handle [GC_SYNC_KIT_PACK] message attrs, auto generate do not change
        pass


class CG_FLY_FLY (Packet):
    pass


class CG_PRESENT_RECEIVE (Packet):
    pass


class GC_GUILDWAR_SCORE (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_SCORE] message attrs, auto generate do not change
        self.person['armyAid'] = self['armyAid']
        self.person['armyAscore'] = self['armyAscore']
        self.person['armyBid'] = self['armyBid']
        self.person['armyBscore'] = self['armyBscore']
        # end handle [GC_GUILDWAR_SCORE] message attrs, auto generate do not change
        pass


class GC_CHATLINK_DOWNLOAD (Packet):
    def handle(self):
        # begin handle [GC_CHATLINK_DOWNLOAD] message attrs, auto generate do not change
        self.person['LinkItem'] = self['LinkItem']
        self.person['LinkFairy'] = self['LinkFairy']
        self.person['LinkTitle'] = self['LinkTitle']
        self.person['LinkFashion'] = self['LinkFashion']
        self.person['LinkGemSlotList'] = self['LinkGemSlotList']
        self.person['PlayerLevel'] = self['PlayerLevel']
        self.person['EquipSlotIndex'] = self['EquipSlotIndex']
        self.person['LinkInscriptionSlotList'] = self['LinkInscriptionSlotList']
        self.person['PlayerProfession'] = self['PlayerProfession']
        self.person['SenderGuid'] = self['SenderGuid']
        self.person['LinkEngraveSlot'] = self['LinkEngraveSlot']
        self.person['LinkPet'] = self['LinkPet']
        self.person['EnchantingData'] = self['EnchantingData']
        self.person['LinkRebirthSlot'] = self['LinkRebirthSlot']
        self.person['EquipMirrorForgeLevel'] = self['EquipMirrorForgeLevel']
        self.person['MaxExtendWarpath'] = self['MaxExtendWarpath']
        self.person['RefineMeter'] = self['RefineMeter']
        self.person['LinkKitPack'] = self['LinkKitPack']
        self.person['LinkKitLock'] = self['LinkKitLock']
        self.person['kitPackSize'] = self['kitPackSize']
        self.person['GodWeapon'] = self['GodWeapon']
        self.person['marriageInfo'] = self['marriageInfo']
        self.person['XinPoList'] = self['XinPoList']
        self.person['SignetbuffList'] = self['SignetbuffList']
        self.person['wushenData'] = self['wushenData']
        self.person['JadeEffectLevel'] = self['JadeEffectLevel']
        # end handle [GC_CHATLINK_DOWNLOAD] message attrs, auto generate do not change
        pass


class GC_USE_REDLINE (Packet):
    def handle(self):
        # begin handle [GC_USE_REDLINE] message attrs, auto generate do not change
        self.person['success'] = self['success']
        self.person['receiverGuid'] = self['receiverGuid']
        self.person['retCode'] = self['retCode']
        # end handle [GC_USE_REDLINE] message attrs, auto generate do not change
        pass


class CG_SELECT_ROLE (Packet):
    pass


class GC_RET_GUILDWAR_HISTROY_BATTLE_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILDWAR_HISTROY_BATTLE_INFO] message attrs, auto generate do not change
        self.person['scroeOfWeek'] = self['scroeOfWeek']
        self.person['leadernameList'] = self['leadernameList']
        self.person['roundidxList'] = self['roundidxList']
        self.person['resultList'] = self['resultList']
        self.person['serverVersion'] = self['serverVersion']
        self.person['scoreList'] = self['scoreList']
        # end handle [GC_RET_GUILDWAR_HISTROY_BATTLE_INFO] message attrs, auto generate do not change
        pass


class GC_BROTHERHOOD_CREATE_SUCCESS (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_CREATE_SUCCESS] message attrs, auto generate do not change
        # end handle [GC_BROTHERHOOD_CREATE_SUCCESS] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_RECRUIT (Packet):
    pass


class GC_JUMP_NOTIFY (Packet):
    def handle(self):
        # begin handle [GC_JUMP_NOTIFY] message attrs, auto generate do not change
        self.person['server_id'] = self['server_id']
        self.person['jump_times'] = self['jump_times']
        self.person['x'] = self['x']
        self.person['y'] = self['y']
        self.person['z'] = self['z']
        self.person['nowTime'] = self['nowTime']
        self.person['curJumpSection'] = self['curJumpSection']
        self.person['dir_x'] = self['dir_x']
        self.person['dir_y'] = self['dir_y']
        self.person['dir_z'] = self['dir_z']
        self.person['deltaTime'] = self['deltaTime']
        # end handle [GC_JUMP_NOTIFY] message attrs, auto generate do not change
        pass


class GC_FAIRY_RAISE_ACTION_RET (Packet):
    def handle(self):
        # begin handle [GC_FAIRY_RAISE_ACTION_RET] message attrs, auto generate do not change
        self.person['fairyGuid'] = self['fairyGuid']
        self.person['actionType'] = self['actionType']
        self.person['retCode'] = self['retCode']
        # end handle [GC_FAIRY_RAISE_ACTION_RET] message attrs, auto generate do not change
        pass


class CG_GODWEAPON_ENCHANT (Packet):
    pass


class GC_SYNC_GUILD_REAMTIME_VOICEROOM_CHANGEINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_REAMTIME_VOICEROOM_CHANGEINFO] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['syncType'] = self['syncType']
        self.person['roomType'] = self['roomType']
        self.person['roomId'] = self['roomId']
        self.person['roomName'] = self['roomName']
        self.person['roomDesc'] = self['roomDesc']
        self.person['roomIconId'] = self['roomIconId']
        # end handle [GC_SYNC_GUILD_REAMTIME_VOICEROOM_CHANGEINFO] message attrs, auto generate do not change
        pass


class GC_MISSION_COMMIT_RET (Packet):
    def handle(self):
        # begin handle [GC_MISSION_COMMIT_RET] message attrs, auto generate do not change
        self.person['nMisID'] = self['nMisID']
        self.person['bRet'] = self['bRet']
        # end handle [GC_MISSION_COMMIT_RET] message attrs, auto generate do not change
        pass


class CG_REQ_MIS_QIYU_HISTORY (Packet):
    pass


class GC_RET_HOME_REGION_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_HOME_REGION_INFO] message attrs, auto generate do not change
        self.person['RegionIndex'] = self['RegionIndex']
        self.person['HordeIndex'] = self['HordeIndex']
        self.person['HordeName'] = self['HordeName']
        self.person['BoomVal'] = self['BoomVal']
        self.person['DailyBoomVal'] = self['DailyBoomVal']
        self.person['LeaderName'] = self['LeaderName']
        # end handle [GC_RET_HOME_REGION_INFO] message attrs, auto generate do not change
        pass


class CG_GUILD_REQ_SET_FULLACCEPT (Packet):
    pass


class GC_UPDATE_POS (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_POS] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['pos_x'] = self['pos_x']
        self.person['pos_y'] = self['pos_y']
        self.person['pos_z'] = self['pos_z']
        self.person['dir'] = self['dir']
        # end handle [GC_UPDATE_POS] message attrs, auto generate do not change
        pass


class GC_SYNC_EXCHANGECOUNT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_EXCHANGECOUNT] message attrs, auto generate do not change
        self.person['index'] = self['index']
        self.person['excDataID'] = self['excDataID']
        self.person['exccount'] = self['exccount']
        self.person['excCatchCount'] = self['excCatchCount']
        # end handle [GC_SYNC_EXCHANGECOUNT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_BWPVPFINAL_COPYSCENERET] message attrs, auto generate do not change
        self.person['isWinner'] = self['isWinner']
        self.person['nextStartTime'] = self['nextStartTime']
        self.person['myRank'] = self['myRank']
        # end handle [GC_BWPVPFINAL_COPYSCENERET] message attrs, auto generate do not change
        pass


class CG_REQUEST_RECOVERYFOODINFO (Packet):
    pass


class CG_CVFIREFLY_CANCEL_SIGNUP (Packet):
    pass


class GC_FASHION_SYNC (Packet):
    def handle(self):
        # begin handle [GC_FASHION_SYNC] message attrs, auto generate do not change
        self.person['FashionList'] = self['FashionList']
        self.person['CurFashionId'] = self['CurFashionId']
        self.person['ShowFashion'] = self['ShowFashion']
        # end handle [GC_FASHION_SYNC] message attrs, auto generate do not change
        pass


class GC_SYNC_SUPER_R_LVEL (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SUPER_R_LVEL] message attrs, auto generate do not change
        self.person['bIsSuperR'] = self['bIsSuperR']
        # end handle [GC_SYNC_SUPER_R_LVEL] message attrs, auto generate do not change
        pass


class GC_WEDDING_SYC_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_WEDDING_SYC_CONFIG] message attrs, auto generate do not change
        self.person['MarriageCostItemId1'] = self['MarriageCostItemId1']
        self.person['MarriageCostItemCount1'] = self['MarriageCostItemCount1']
        self.person['MarriageCostItemId2'] = self['MarriageCostItemId2']
        self.person['MarriageCostItemCount2'] = self['MarriageCostItemCount2']
        self.person['MarriageCostGoldCoin'] = self['MarriageCostGoldCoin']
        self.person['MarriageCostYuanBao'] = self['MarriageCostYuanBao']
        self.person['MarriageFriendPoint'] = self['MarriageFriendPoint']
        self.person['ChineseWeddingCostGoldCoin'] = self['ChineseWeddingCostGoldCoin']
        self.person['MarriageLevelLimit'] = self['MarriageLevelLimit']
        self.person['AgreeDevoiceCostGoldCoin'] = self['AgreeDevoiceCostGoldCoin']
        self.person['ForceDevoiceCostGoldCoin'] = self['ForceDevoiceCostGoldCoin']
        self.person['FreeCompulsoryDivorceDay'] = self['FreeCompulsoryDivorceDay']
        self.person['WeddingGuestLevelLimit'] = self['WeddingGuestLevelLimit']
        self.person['HoldWeddingCoolDown'] = self['HoldWeddingCoolDown']
        # end handle [GC_WEDDING_SYC_CONFIG] message attrs, auto generate do not change
        pass


class GC_SHEDAOSAIMA_SYSDAOJU (Packet):
    def handle(self):
        # begin handle [GC_SHEDAOSAIMA_SYSDAOJU] message attrs, auto generate do not change
        self.person['DaoJu1Id'] = self['DaoJu1Id']
        self.person['DaoJu2Id'] = self['DaoJu2Id']
        # end handle [GC_SHEDAOSAIMA_SYSDAOJU] message attrs, auto generate do not change
        pass


class CG_RECEIVE_ACHIEVEMENT_RECORD_REWARD (Packet):
    pass


class CG_REQ_GUILDCONVOY_FINISH (Packet):
    pass


class CG_START_KIT_PACK (Packet):
    pass


class GC_GUILDWAR_BATTLE_START (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_BATTLE_START] message attrs, auto generate do not change
        self.person['armyAid'] = self['armyAid']
        self.person['armyBid'] = self['armyBid']
        self.person['countdown'] = self['countdown']
        self.person['ansiSecTime'] = self['ansiSecTime']
        self.person['guildAName'] = self['guildAName']
        self.person['guildBName'] = self['guildBName']
        self.person['armyAposx'] = self['armyAposx']
        self.person['armyAposy'] = self['armyAposy']
        self.person['armyAposz'] = self['armyAposz']
        self.person['armyBposx'] = self['armyBposx']
        self.person['armyBposy'] = self['armyBposy']
        self.person['armyBposz'] = self['armyBposz']
        # end handle [GC_GUILDWAR_BATTLE_START] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_INVITE_CONFIRM (Packet):
    pass


class GC_SYNC_BOUNTY_REFREST_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BOUNTY_REFREST_STATE] message attrs, auto generate do not change
        self.person['refreshID'] = self['refreshID']
        self.person['npcList'] = self['npcList']
        # end handle [GC_SYNC_BOUNTY_REFREST_STATE] message attrs, auto generate do not change
        pass


class CG_REQUEST_RECHARGE (Packet):
    pass


class GC_RET_GUILD_MONSTER_RANK_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILD_MONSTER_RANK_INFO] message attrs, auto generate do not change
        self.person['score'] = self['score']
        self.person['playrName'] = self['playrName']
        self.person['selfRank'] = self['selfRank']
        self.person['guildScore'] = self['guildScore']
        self.person['leftTime'] = self['leftTime']
        # end handle [GC_RET_GUILD_MONSTER_RANK_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_GUILD_REALTIME_VOICEROOM_CHANGE_MEMBER_ROLE_NOTICE_LEADER (Packet):
    pass


class CG_LUCKY_CONNECT_GAIN_REWARD (Packet):
    pass


class GC_SYNC_MONITOR_NPC_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MONITOR_NPC_INFO] message attrs, auto generate do not change
        self.person['DataId'] = self['DataId']
        self.person['CurHp'] = self['CurHp']
        self.person['MaxHP'] = self['MaxHP']
        # end handle [GC_SYNC_MONITOR_NPC_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_XIUZHEN_COPYSCENE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_XIUZHEN_COPYSCENE_DATA] message attrs, auto generate do not change
        self.person['xiuZhenCopySceneData'] = self['xiuZhenCopySceneData']
        # end handle [GC_SYNC_XIUZHEN_COPYSCENE_DATA] message attrs, auto generate do not change
        pass


class CG_MILITARY_REQ_BUYITEM (Packet):
    pass


class GC_SYNC_CHANGEPROFESSIONCONDITIONINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CHANGEPROFESSIONCONDITIONINFO] message attrs, auto generate do not change
        self.person['conditioninfo'] = self['conditioninfo']
        # end handle [GC_SYNC_CHANGEPROFESSIONCONDITIONINFO] message attrs, auto generate do not change
        pass


class GC_YAOSHOU_CHANGE_TRIGER_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_YAOSHOU_CHANGE_TRIGER_NOTICE] message attrs, auto generate do not change
        # end handle [GC_YAOSHOU_CHANGE_TRIGER_NOTICE] message attrs, auto generate do not change
        pass


class GC_SYNC_STATISTICS_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_STATISTICS_DATA] message attrs, auto generate do not change
        self.person['allFlag'] = self['allFlag']
        self.person['actorGuid'] = self['actorGuid']
        self.person['actorName'] = self['actorName']
        self.person['professionType'] = self['professionType']
        self.person['nowCureVal'] = self['nowCureVal']
        self.person['nowAttackVal'] = self['nowAttackVal']
        self.person['nowDmgVal'] = self['nowDmgVal']
        self.person['nowCombatTime'] = self['nowCombatTime']
        self.person['originalWorldName'] = self['originalWorldName']
        self.person['fairyAttackVal'] = self['fairyAttackVal']
        self.person['fairyCureVal'] = self['fairyCureVal']
        self.person['bossStatisticsData'] = self['bossStatisticsData']
        self.person['curCopyScenePhase'] = self['curCopyScenePhase']
        # end handle [GC_SYNC_STATISTICS_DATA] message attrs, auto generate do not change
        pass


class GC_SEND_RUBKICUBE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_SEND_RUBKICUBE_RESULT] message attrs, auto generate do not change
        self.person['nResuktType'] = self['nResuktType']
        self.person['nSucessType'] = self['nSucessType']
        self.person['nItemId'] = self['nItemId']
        self.person['nItemCount'] = self['nItemCount']
        self.person['nItemBind'] = self['nItemBind']
        self.person['nRubkiCubeId'] = self['nRubkiCubeId']
        self.person['nRubkiCubePlayTime'] = self['nRubkiCubePlayTime']
        # end handle [GC_SEND_RUBKICUBE_RESULT] message attrs, auto generate do not change
        pass


class GC_RANK_RET_FAIRYINFO (Packet):
    def handle(self):
        # begin handle [GC_RANK_RET_FAIRYINFO] message attrs, auto generate do not change
        self.person['bfind'] = self['bfind']
        self.person['FairyInfo'] = self['FairyInfo']
        # end handle [GC_RANK_RET_FAIRYINFO] message attrs, auto generate do not change
        pass


class CG_REQ_AUCTION_BID (Packet):
    pass


class CG_REQ_PET_DELETE (Packet):
    pass


class GC_HOMEBUILDING_PLAY (Packet):
    def handle(self):
        # begin handle [GC_HOMEBUILDING_PLAY] message attrs, auto generate do not change
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['MasterGuid'] = self['MasterGuid']
        self.person['PlayerGuid'] = self['PlayerGuid']
        self.person['BuildingGuid'] = self['BuildingGuid']
        self.person['BuildingId'] = self['BuildingId']
        self.person['PlayBuildingIndex'] = self['PlayBuildingIndex']
        # end handle [GC_HOMEBUILDING_PLAY] message attrs, auto generate do not change
        pass


class CG_ASK_ACTIVENESSAWARD (Packet):
    pass


class CG_JOIN_TEAM_REQUEST_RESULT (Packet):
    pass


class CG_HOMEBUILDING_PLAY (Packet):
    pass


class GC_RET_ARTIFACT_EXCHANGE (Packet):
    def handle(self):
        # begin handle [GC_RET_ARTIFACT_EXCHANGE] message attrs, auto generate do not change
        self.person['ArtifactId'] = self['ArtifactId']
        # end handle [GC_RET_ARTIFACT_EXCHANGE] message attrs, auto generate do not change
        pass


class GC_NEWPRESTIGEUNLOCK (Packet):
    def handle(self):
        # begin handle [GC_NEWPRESTIGEUNLOCK] message attrs, auto generate do not change
        self.person['ForceId'] = self['ForceId']
        # end handle [GC_NEWPRESTIGEUNLOCK] message attrs, auto generate do not change
        pass


class GC_TEAM_SYNC_TEAMINFO (Packet):
    def handle(self):
        # begin handle [GC_TEAM_SYNC_TEAMINFO] message attrs, auto generate do not change
        self.person['teamGuid'] = self['teamID']
        self.person['targetId'] = self['targetId']
        self.person['minLevel'] = self['minLevel']
        self.person['maxLevel'] = self['maxLevel']
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberProf'] = self['memberProf']
        self.person['memberHP'] = self['memberHP']
        self.person['memberMaxHP'] = self['memberMaxHP']
        self.person['sceneclass'] = self['sceneclass']
        self.person['sceneinst'] = self['sceneinst']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        self.person['memberState'] = self['memberState']
        self.person['memberSex'] = self['memberSex']
        self.person['memberBodyId'] = self['memberBodyId']
        self.person['memberFaceId'] = self['memberFaceId']
        self.person['memberWeaponId'] = self['memberWeaponId']
        self.person['memberWeaponRefineVisual'] = self['memberWeaponRefineVisual']
        self.person['memberHairId'] = self['memberHairId']
        self.person['reserved'] = self['reserved']
        self.person['familyGuid'] = self['familyGuid']
        self.person['memberBodyColorVisual'] = self['memberBodyColorVisual']
        self.person['professionOrientationIndex'] = self['professionOrientationIndex']
        self.person['professionOrientationParentID'] = self['professionOrientationParentID']
        self.person['professionOrientationChildID'] = self['professionOrientationChildID']
        self.person['memberMP'] = self['memberMP']
        self.person['memberMaxMP'] = self['memberMaxMP']
        self.person['teamIndex'] = self['teamIndex']
        self.person['armyID'] = self['armyID']
        self.person['memberBodyFashionId'] = self['memberBodyFashionId']
        self.person['memberBodyColorIndex'] = self['memberBodyColorIndex']
        self.person['rolenierenlist'] = self['rolenierenlist']
        self.person['memberBiaoJi'] = self['memberBiaoJi']
        self.person['memberReadyState'] = self['memberReadyState']
        self.person['memberArmyFollowState'] = self['memberArmyFollowState']
        self.person['memberimpactclassid1'] = self['memberimpactclassid1']
        self.person['memberimpactclassid2'] = self['memberimpactclassid2']
        self.person['memberHairFashionId'] = self['memberHairFashionId']
        self.person['memberHairColorIndex'] = self['memberHairColorIndex']
        self.person['memberWeaponFashionId'] = self['memberWeaponFashionId']
        self.person['memberWeaponColorIndex'] = self['memberWeaponColorIndex']
        self.person['memberPglMmr'] = self['memberPglMmr']
        self.person['memberPglRemainTimes'] = self['memberPglRemainTimes']
        self.person['rtMemberList'] = self['rtMemberList']
        self.person['memberProfCamp'] = self['memberProfCamp']
        self.person['memberGemSetId'] = self['memberGemSetId']
        self.person['memberAutoCombat'] = self['memberAutoCombat']
        self.person['memberOriginalWorldName'] = self['memberOriginalWorldName']
        self.person['memberXiuZhenLevel'] = self['memberXiuZhenLevel']
        self.person['memberDispelBuff'] = self['memberDispelBuff']
        self.person['memberCombatValue'] = self['memberCombatValue']
        self.person['memberGuildGuid'] = self['memberGuildGuid']
        self.person['memberLoverGuid'] = self['memberLoverGuid']
        self.person['memberHaveHuiliuIdentity'] = self['memberHaveHuiliuIdentity']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['memberBodyUseFreedomDyeColorIndex'] = self['memberBodyUseFreedomDyeColorIndex']
        self.person['memberHairUseFreedomDyeColorIndex'] = self['memberHairUseFreedomDyeColorIndex']
        self.person['BodyFreeDyeColorInfos'] = self['BodyFreeDyeColorInfos']
        self.person['HairFreeDyeColorInfos'] = self['HairFreeDyeColorInfos']
        self.person['BackFashionId'] = self['BackFashionId']
        self.person['BackColorIndex'] = self['BackColorIndex']
        self.person['memberIsNewPlayerCatch'] = self['memberIsNewPlayerCatch']
        self.person['memberActivityFinishFlag'] = self['memberActivityFinishFlag']
        self.person['memberHaveFestivalHuiliuIdentity'] = self['memberHaveFestivalHuiliuIdentity']
        # end handle [GC_TEAM_SYNC_TEAMINFO] message attrs, auto generate do not change
        pass


class GC_RET_VIEWOTHERROLEINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_VIEWOTHERROLEINFO] message attrs, auto generate do not change
        self.person['roleviewinfo'] = self['roleviewinfo']
        self.person['equipitem0'] = self['equipitem0']
        self.person['equipitem1'] = self['equipitem1']
        self.person['equipitem2'] = self['equipitem2']
        self.person['equipitem3'] = self['equipitem3']
        self.person['equipitem4'] = self['equipitem4']
        self.person['equipitem5'] = self['equipitem5']
        self.person['equipitem6'] = self['equipitem6']
        self.person['equipitem7'] = self['equipitem7']
        self.person['equipitem8'] = self['equipitem8']
        self.person['equipitem9'] = self['equipitem9']
        self.person['equipitem10'] = self['equipitem10']
        self.person['equipitem11'] = self['equipitem11']
        self.person['BodyId'] = self['BodyId']
        self.person['FaceId'] = self['FaceId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['reserved'] = self['reserved']
        self.person['playername'] = self['playername']
        self.person['pkvalue'] = self['pkvalue']
        self.person['bindyuanbao'] = self['bindyuanbao']
        self.person['yuanbao'] = self['yuanbao']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairId'] = self['HairId']
        self.person['reserved1'] = self['reserved1']
        self.person['lovername'] = self['lovername']
        self.person['matrixID'] = self['matrixID']
        self.person['matrixAttrLevels'] = self['matrixAttrLevels']
        self.person['BodyColorEffectVisual'] = self['BodyColorEffectVisual']
        self.person['nierenvalue'] = self['nierenvalue']
        self.person['BodyFashionId'] = self['BodyFashionId']
        self.person['BodyColorIndex'] = self['BodyColorIndex']
        self.person['HairFashionId'] = self['HairFashionId']
        self.person['HairColorIndex'] = self['HairColorIndex']
        self.person['WeaponFashionId'] = self['WeaponFashionId']
        self.person['WeaponColorIndex'] = self['WeaponColorIndex']
        self.person['gemSlotList'] = self['gemSlotList']
        self.person['gemSetId'] = self['gemSetId']
        self.person['tianshuSlotList'] = self['tianshuSlotList']
        self.person['combatValList'] = self['combatValList']
        self.person['inscriptionSlotDataList'] = self['inscriptionSlotDataList']
        self.person['accrechargestep'] = self['accrechargestep']
        self.person['militaryRank'] = self['militaryRank']
        self.person['EngraveSlotList'] = self['EngraveSlotList']
        self.person['tianshuMasterId'] = self['tianshuMasterId']
        self.person['tianshuMasterLevel'] = self['tianshuMasterLevel']
        self.person['equipitem12'] = self['equipitem12']
        self.person['equipitem13'] = self['equipitem13']
        self.person['openMirror'] = self['openMirror']
        self.person['openSignet'] = self['openSignet']
        self.person['FairyList'] = self['FairyList']
        self.person['EnchantingData'] = self['EnchantingData']
        self.person['tianshu_zhenweiIndex'] = self['tianshu_zhenweiIndex']
        self.person['tianshu_zhenwei_dataId'] = self['tianshu_zhenwei_dataId']
        self.person['tianshu_currentZhenfaId'] = self['tianshu_currentZhenfaId']
        self.person['tianshu_zhenfaDataId'] = self['tianshu_zhenfaDataId']
        self.person['tianshu_zhenfaLevel'] = self['tianshu_zhenfaLevel']
        self.person['tianshu_yinzhenId'] = self['tianshu_yinzhenId']
        self.person['tianshu_yinzhenLevel'] = self['tianshu_yinzhenLevel']
        self.person['EquipRebirthDataList'] = self['EquipRebirthDataList']
        self.person['equipServant'] = self['equipServant']
        self.person['activekizuna'] = self['activekizuna']
        self.person['EquipMirrorForgeLevel'] = self['EquipMirrorForgeLevel']
        self.person['MaxExtendWarpath'] = self['MaxExtendWarpath']
        self.person['RefineMeter'] = self['RefineMeter']
        self.person['KitItems'] = self['KitItems']
        self.person['KitLock'] = self['KitLock']
        self.person['KitPackSize'] = self['KitPackSize']
        self.person['equipitem14'] = self['equipitem14']
        self.person['Godweapon'] = self['Godweapon']
        self.person['GodWeaponCollectLv'] = self['GodWeaponCollectLv']
        self.person['GodWeaponQiLingLvs'] = self['GodWeaponQiLingLvs']
        self.person['GodWeaponCoordIds'] = self['GodWeaponCoordIds']
        self.person['GodWeaponCoordLvs'] = self['GodWeaponCoordLvs']
        self.person['isOffline'] = self['isOffline']
        self.person['IsHuiLiu'] = self['IsHuiLiu']
        self.person['UseBodyFreeDyeSlotId'] = self['UseBodyFreeDyeSlotId']
        self.person['UseHairFreeDyeSlotId'] = self['UseHairFreeDyeSlotId']
        self.person['BodyFreeDyeColorInfo'] = self['BodyFreeDyeColorInfo']
        self.person['HairFreeDyeColorInfo'] = self['HairFreeDyeColorInfo']
        self.person['DyeCharm'] = self['DyeCharm']
        self.person['TitleCharm'] = self['TitleCharm']
        self.person['BackFashionId'] = self['BackFashionId']
        self.person['BackColorIndex'] = self['BackColorIndex']
        self.person['IsNewPlayerCatch'] = self['IsNewPlayerCatch']
        self.person['IsFriend'] = self['IsFriend']
        self.person['IsLover'] = self['IsLover']
        self.person['IsBrotherhood'] = self['IsBrotherhood']
        self.person['OpType'] = self['OpType']
        self.person['TotalCharmValue'] = self['TotalCharmValue']
        self.person['ChallRankPos'] = self['ChallRankPos']
        self.person['GuildName'] = self['GuildName']
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['SwordTeamGuid'] = self['SwordTeamGuid']
        self.person['SwordTeamName'] = self['SwordTeamName']
        self.person['SwordTeamGroup'] = self['SwordTeamGroup']
        self.person['SwordTeamPlaceInGroup'] = self['SwordTeamPlaceInGroup']
        self.person['TitleId'] = self['TitleId']
        self.person['FirstTitleUserDef'] = self['FirstTitleUserDef']
        self.person['SecondTitleUserDef'] = self['SecondTitleUserDef']
        self.person['ArmyID'] = self['ArmyID']
        self.person['TeamID'] = self['TeamID']
        self.person['ServerID'] = self['ServerID']
        self.person['BrotherhoodGuid'] = self['BrotherhoodGuid']
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['CustomHeadPic'] = self['CustomHeadPic']
        self.person['ServantEquipItems'] = self['ServantEquipItems']
        self.person['xinpodata'] = self['xinpodata']
        self.person['GuildShortName'] = self['GuildShortName']
        self.person['GuildShortNameColor'] = self['GuildShortNameColor']
        self.person['BWGWRankNum'] = self['BWGWRankNum']
        self.person['ActiveWarPathBuffList'] = self['ActiveWarPathBuffList']
        self.person['CurSelectBackGroundId'] = self['CurSelectBackGroundId']
        self.person['CurSelectCardId'] = self['CurSelectCardId']
        self.person['IsFestivalHuiLiu'] = self['IsFestivalHuiLiu']
        self.person['GuildType'] = self['GuildType']
        self.person['LingShiInfo'] = self['LingShiInfo']
        self.person['wushenData'] = self['wushenData']
        self.person['Jades'] = self['Jades']
        self.person['HideAccRechargeLv'] = self['HideAccRechargeLv']
        # end handle [GC_RET_VIEWOTHERROLEINFO] message attrs, auto generate do not change
        pass


class GC_WILDWORLDBOSS_NUM (Packet):
    def handle(self):
        # begin handle [GC_WILDWORLDBOSS_NUM] message attrs, auto generate do not change
        self.person['joinNum'] = self['joinNum']
        # end handle [GC_WILDWORLDBOSS_NUM] message attrs, auto generate do not change
        pass


class GC_BATTLEFIELD_SIGNUP_INFO (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_SIGNUP_INFO] message attrs, auto generate do not change
        self.person['SignupID'] = self['SignupID']
        self.person['LeftSignupCount'] = self['LeftSignupCount']
        self.person['SignupPlayerCount'] = self['SignupPlayerCount']
        self.person['MatchedID'] = self['MatchedID']
        self.person['WeeklyScore'] = self['WeeklyScore']
        # end handle [GC_BATTLEFIELD_SIGNUP_INFO] message attrs, auto generate do not change
        pass


class CG_GUILDFIGHT_WORLDBOSS_RANK (Packet):
    pass


class GC_RET_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['roomId'] = self['roomId']
        # end handle [GC_RET_GUILD_REALTIME_VOICEROOM_KICK_OUT_ROOM] message attrs, auto generate do not change
        pass


class GC_GUILD_RET_WORSHIP_CHIEFMODEL (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_WORSHIP_CHIEFMODEL] message attrs, auto generate do not change
        # end handle [GC_GUILD_RET_WORSHIP_CHIEFMODEL] message attrs, auto generate do not change
        pass


class GC_TOURNAMENT_SYNC_MY_INFO (Packet):
    def handle(self):
        # begin handle [GC_TOURNAMENT_SYNC_MY_INFO] message attrs, auto generate do not change
        self.person['myGroupType'] = self['myGroupType']
        self.person['lastLotteryTimes'] = self['lastLotteryTimes']
        self.person['firstWinStatus'] = self['firstWinStatus']
        self.person['fiveWinStatus'] = self['fiveWinStatus']
        self.person['tenBattleStatus'] = self['tenBattleStatus']
        self.person['rankRewardStatus'] = self['rankRewardStatus']
        self.person['myRank'] = self['myRank']
        self.person['myScore'] = self['myScore']
        self.person['myWinTimes'] = self['myWinTimes']
        self.person['myBattleTimes'] = self['myBattleTimes']
        self.person['isCloseRankReward'] = self['isCloseRankReward']
        self.person['closeLastTime'] = self['closeLastTime']
        # end handle [GC_TOURNAMENT_SYNC_MY_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_SQRE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SQRE_RESULT] message attrs, auto generate do not change
        self.person['m_SQREAct'] = self['m_SQREAct']
        self.person['m_SQREREType'] = self['m_SQREREType']
        # end handle [GC_SYNC_SQRE_RESULT] message attrs, auto generate do not change
        pass


class GC_DELFRIEND (Packet):
    def handle(self):
        # begin handle [GC_DELFRIEND] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        # end handle [GC_DELFRIEND] message attrs, auto generate do not change
        pass


class CG_NOTIFY_GUILD_REALTIME_VOICEROOM_CHANGE_RTMEMBERINFO (Packet):
    pass


class CG_REQ_CHANGE_GUILD_REALTIME_VOICE_ROOM_INFO (Packet):
    pass


class GC_STALL_RETSELLINFO (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETSELLINFO] message attrs, auto generate do not change
        self.person['itemid'] = self['itemid']
        self.person['averageprice'] = self['averageprice']
        self.person['recommandprice'] = self['recommandprice']
        self.person['taxrate'] = self['taxrate']
        self.person['othersames'] = self['othersames']
        self.person['taxmax'] = self['taxmax']
        self.person['taxmin'] = self['taxmin']
        self.person['valuelevel'] = self['valuelevel']
        self.person['buytaxrate'] = self['buytaxrate']
        self.person['freenumber'] = self['freenumber']
        self.person['stepmin'] = self['stepmin']
        self.person['stepmax'] = self['stepmax']
        self.person['stepvalue'] = self['stepvalue']
        self.person['stackcount'] = self['stackcount']
        self.person['averagepricemultiple'] = self['averagepricemultiple']
        self.person['stepprices'] = self['stepprices']
        # end handle [GC_STALL_RETSELLINFO] message attrs, auto generate do not change
        pass


class CG_REQ_ARTIFACT_INFO (Packet):
    pass


class GC_MISSION_ACCEPT_RET (Packet):
    def handle(self):
        # begin handle [GC_MISSION_ACCEPT_RET] message attrs, auto generate do not change
        self.person['Mission'] = self['Mission']
        self.person['bRet'] = self['bRet']
        # end handle [GC_MISSION_ACCEPT_RET] message attrs, auto generate do not change
        pass


class CG_UNLOCK_HOME_PLAN (Packet):
    pass


class CG_SHOW_TAIL (Packet):
    pass


class GC_AUTOFORWARDMOVE (Packet):
    def handle(self):
        # begin handle [GC_AUTOFORWARDMOVE] message attrs, auto generate do not change
        self.person['IsMove'] = self['IsMove']
        # end handle [GC_AUTOFORWARDMOVE] message attrs, auto generate do not change
        pass


class GC_HOME_SYNC_GUEST_DATA (Packet):
    def handle(self):
        # begin handle [GC_HOME_SYNC_GUEST_DATA] message attrs, auto generate do not change
        self.person['MyLandLoard'] = self['MyLandLoard']
        self.person['MyGuestList'] = self['MyGuestList']
        # end handle [GC_HOME_SYNC_GUEST_DATA] message attrs, auto generate do not change
        pass


class CG_TEAM_INVITEFOLLOW (Packet):
    pass


class CG_BWPVPFINAL_ASKADDSCORE (Packet):
    pass


class CG_FLY_LANDING (Packet):
    pass


class GC_RET_BLACKMARKETITEMINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_BLACKMARKETITEMINFO] message attrs, auto generate do not change
        self.person['ItemIndex'] = self['ItemIndex']
        self.person['ItemDataId'] = self['ItemDataId']
        self.person['ItemCount'] = self['ItemCount']
        self.person['ItemPrice'] = self['ItemPrice']
        self.person['ItemMoneyType'] = self['ItemMoneyType']
        self.person['IsBind'] = self['IsBind']
        self.person['MaxPage'] = self['MaxPage']
        # end handle [GC_RET_BLACKMARKETITEMINFO] message attrs, auto generate do not change
        pass


class CG_CHANGE_STEWARD_NAME (Packet):
    pass


class CG_ASK_MOVETO_WILDWORLDBOSS (Packet):
    pass


class CG_REQ_APPLY_LEADER_VOTE (Packet):
    pass


class GC_SYNC_PLAYER_RUBKICUBE_OXYGEN_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PLAYER_RUBKICUBE_OXYGEN_INFO] message attrs, auto generate do not change
        self.person['palyerGuid'] = self['palyerGuid']
        self.person['curOxyGen'] = self['curOxyGen']
        # end handle [GC_SYNC_PLAYER_RUBKICUBE_OXYGEN_INFO] message attrs, auto generate do not change
        pass


class GC_SYC_FULL_BLACK_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYC_FULL_BLACK_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['Reserved'] = self['Reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['haveHuiliuIdentity'] = self['haveHuiliuIdentity']
        self.person['ReportFlag'] = self['ReportFlag']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['haveFestivalHuiliuIdentity'] = self['haveFestivalHuiliuIdentity']
        self.person['haveNewPlayerCatch'] = self['haveNewPlayerCatch']
        # end handle [GC_SYC_FULL_BLACK_LIST] message attrs, auto generate do not change
        pass


class GC_CREATE_PLAYER (Packet):
    def handle(self):
        # begin handle [GC_CREATE_PLAYER] message attrs, auto generate do not change
        self.person['charBaseAttr'] = self['charBaseAttr']
        self.person['sceneInst'] = self['sceneInst']
        self.person['sceneClass'] = self['sceneClass']
        self.person['guid'] = self['guid']
        self.person['curProfession'] = self['curProfession']
        self.person['firsttitlecontent'] = self['firsttitlecontent']
        self.person['MountID'] = self['MountID']
        self.person['CurTitleID'] = self['CurTitleID']
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['SexType'] = self['SexType']
        self.person['BodyVisualId'] = self['BodyVisualId']
        self.person['WeaponVisualId'] = self['WeaponVisualId']
        self.person['FaceVisualId'] = self['FaceVisualId']
        self.person['interactState'] = self['interactState']
        self.person['interactType'] = self['interactType']
        self.person['interactPartnerID'] = self['interactPartnerID']
        self.person['followState'] = self['followState']
        self.person['PKState'] = self['PKState']
        self.person['PKValue'] = self['PKValue']
        self.person['FamilyGuid'] = self['FamilyGuid']
        self.person['TransforId'] = self['TransforId']
        self.person['TeamLeader'] = self['TeamLeader']
        self.person['FollowMem'] = self['FollowMem']
        self.person['Reserved1'] = self['Reserved1']
        self.person['Reserved2'] = self['Reserved2']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['isInTargetfDuelList'] = self['isInTargetfDuelList']
        self.person['isInSelfDuelList'] = self['isInSelfDuelList']
        self.person['HairVisualId'] = self['HairVisualId']
        self.person['Reserved3'] = self['Reserved3']
        self.person['CombatEffect'] = self['CombatEffect']
        self.person['LoverEffect'] = self['LoverEffect']
        self.person['isPvPAudience'] = self['isPvPAudience']
        self.person['DigUpTheHatchetGuildGuid'] = self['DigUpTheHatchetGuildGuid']
        self.person['TeamId'] = self['TeamId']
        self.person['IsTeamLeader'] = self['IsTeamLeader']
        self.person['IsPvPAudience_FightA'] = self['IsPvPAudience_FightA']
        self.person['IsPvPAudience_FightB'] = self['IsPvPAudience_FightB']
        self.person['OriginalWorldName'] = self['OriginalWorldName']
        self.person['BodyColorEffectVisual'] = self['BodyColorEffectVisual']
        self.person['worldId'] = self['worldId']
        self.person['NieRenValue'] = self['NieRenValue']
        self.person['SkillTransformId'] = self['SkillTransformId']
        self.person['BuffTransId'] = self['BuffTransId']
        self.person['AircraftID'] = self['AircraftID']
        self.person['GuildShortName'] = self['GuildShortName']
        self.person['GuildShortNameColor'] = self['GuildShortNameColor']
        self.person['TransformType'] = self['TransformType']
        self.person['ExState'] = self['ExState']
        self.person['ArmyID'] = self['ArmyID']
        self.person['IsArmyLeader'] = self['IsArmyLeader']
        self.person['BodyFashoinId'] = self['BodyFashoinId']
        self.person['BodyColorIndex'] = self['BodyColorIndex']
        self.person['AircraftFashoinId'] = self['AircraftFashoinId']
        self.person['AircraftColorIndex'] = self['AircraftColorIndex']
        self.person['MountFashoinId'] = self['MountFashoinId']
        self.person['MountColorIndex'] = self['MountColorIndex']
        self.person['XiandanGuid'] = self['XiandanGuid']
        self.person['BattleFairyId'] = self['BattleFairyId']
        self.person['FairyTargetId'] = self['FairyTargetId']
        self.person['HPPool'] = self['HPPool']
        self.person['MPPool'] = self['MPPool']
        self.person['HairFashoinId'] = self['HairFashoinId']
        self.person['HairColorIndex'] = self['HairColorIndex']
        self.person['WeaponFashoinId'] = self['WeaponFashoinId']
        self.person['WeaponColorIndex'] = self['WeaponColorIndex']
        self.person['ProfessionCamp'] = self['ProfessionCamp']
        self.person['GemSetId'] = self['GemSetId']
        self.person['AirBusLineId'] = self['AirBusLineId']
        self.person['NextAirBusPathIdx'] = self['NextAirBusPathIdx']
        self.person['secondtitlecontent'] = self['secondtitlecontent']
        self.person['showhelmet'] = self['showhelmet']
        self.person['showtail'] = self['showtail']
        self.person['BattleFairyEvolvePhase'] = self['BattleFairyEvolvePhase']
        self.person['SwordTeamGuid'] = self['SwordTeamGuid']
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['HomePlayBuildingGuid'] = self['HomePlayBuildingGuid']
        self.person['HomePlayBuildingId'] = self['HomePlayBuildingId']
        self.person['HomePlayBuildingIndex'] = self['HomePlayBuildingIndex']
        self.person['NeedCreateImmed'] = self['NeedCreateImmed']
        self.person['LastLogoutTime'] = self['LastLogoutTime']
        self.person['NewPrestigeCamp'] = self['NewPrestigeCamp']
        self.person['UseBodyFreeDyeSlotId'] = self['UseBodyFreeDyeSlotId']
        self.person['UseHairFreeDyeSlotId'] = self['UseHairFreeDyeSlotId']
        self.person['BodyFreeDyeColorInfo'] = self['BodyFreeDyeColorInfo']
        self.person['HairFreeDyeColorInfo'] = self['HairFreeDyeColorInfo']
        self.person['backFashionId'] = self['backFashionId']
        self.person['backColorIndex'] = self['backColorIndex']
        self.person['SwordTeamName'] = self['SwordTeamName']
        self.person['BWGWRankNum'] = self['BWGWRankNum']
        self.person['MirrorZombieId'] = self['MirrorZombieId']
        self.person['HaveNewPlayerCatch'] = self['HaveNewPlayerCatch']
        self.person['showear'] = self['showear']
        # end handle [GC_CREATE_PLAYER] message attrs, auto generate do not change
        pass


class GC_USE_CONVO_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_USE_CONVO_EFFECT] message attrs, auto generate do not change
        self.person['nConvoItemId'] = self['nConvoItemId']
        # end handle [GC_USE_CONVO_EFFECT] message attrs, auto generate do not change
        pass


class GC_DELRECENTCONTACTLIST (Packet):
    def handle(self):
        # begin handle [GC_DELRECENTCONTACTLIST] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        # end handle [GC_DELRECENTCONTACTLIST] message attrs, auto generate do not change
        pass


class GC_QBZ_USE_ITEM_RESULT (Packet):
    def handle(self):
        # begin handle [GC_QBZ_USE_ITEM_RESULT] message attrs, auto generate do not change
        self.person['itemId'] = self['itemId']
        # end handle [GC_QBZ_USE_ITEM_RESULT] message attrs, auto generate do not change
        pass


class GC_TRIGGER_FRIENDS_MUTUALHELP (Packet):
    def handle(self):
        # begin handle [GC_TRIGGER_FRIENDS_MUTUALHELP] message attrs, auto generate do not change
        self.person['nActiionId'] = self['nActiionId']
        # end handle [GC_TRIGGER_FRIENDS_MUTUALHELP] message attrs, auto generate do not change
        pass


class GC_OPPONENT_LIST (Packet):
    def handle(self):
        # begin handle [GC_OPPONENT_LIST] message attrs, auto generate do not change
        self.person['opponum'] = self['opponum']
        self.person['level'] = self['level']
        self.person['profession'] = self['profession']
        self.person['combatNum'] = self['combatNum']
        self.person['name'] = self['name']
        self.person['rankPos'] = self['rankPos']
        self.person['playerGuid'] = self['playerGuid']
        self.person['sex'] = self['sex']
        self.person['needCost'] = self['needCost']
        self.person['bodyId'] = self['bodyId']
        self.person['faceid'] = self['faceid']
        self.person['weaponId'] = self['weaponId']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['hairid'] = self['hairid']
        self.person['BodyColorvisual'] = self['BodyColorvisual']
        self.person['bChallengeFail'] = self['bChallengeFail']
        self.person['locktime'] = self['locktime']
        self.person['rolenierenlist'] = self['rolenierenlist']
        self.person['BodyColorIndex'] = self['BodyColorIndex']
        self.person['HairColorIndex'] = self['HairColorIndex']
        self.person['WeaponColorIndex'] = self['WeaponColorIndex']
        self.person['BodyFashionId'] = self['BodyFashionId']
        self.person['HairFashionId'] = self['HairFashionId']
        self.person['WeaponFashionId'] = self['WeaponFashionId']
        self.person['guildGuid'] = self['guildGuid']
        self.person['customHeadPic'] = self['customHeadPic']
        self.person['memberBodyUseFreedomDyeColorIndex'] = self['memberBodyUseFreedomDyeColorIndex']
        self.person['memberHairUseFreedomDyeColorIndex'] = self['memberHairUseFreedomDyeColorIndex']
        self.person['BodyFreeDyeColorInfos'] = self['BodyFreeDyeColorInfos']
        self.person['HairFreeDyeColorInfos'] = self['HairFreeDyeColorInfos']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        # end handle [GC_OPPONENT_LIST] message attrs, auto generate do not change
        pass


class CG_BWPVPFINAL_REQHELP (Packet):
    pass


class GC_BROTHERHOOD_CHANGE_NAME (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_CHANGE_NAME] message attrs, auto generate do not change
        self.person['retCode'] = self['retCode']
        # end handle [GC_BROTHERHOOD_CHANGE_NAME] message attrs, auto generate do not change
        pass


class CG_SELECT_RIDE_MISSION (Packet):
    pass


class GC_SYNC_CUSTOMHEAD_RESULT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CUSTOMHEAD_RESULT] message attrs, auto generate do not change
        self.person['customHeadPic'] = self['customHeadPic']
        # end handle [GC_SYNC_CUSTOMHEAD_RESULT] message attrs, auto generate do not change
        pass


class CG_REQ_EXCHANGE_GUILD_MONSTER_BUFF (Packet):
    pass


class GC_UPDATE_SKILLZHUANJING_LEVELUP_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_SKILLZHUANJING_LEVELUP_INFO] message attrs, auto generate do not change
        self.person['nSkillZhuanJingId'] = self['nSkillZhuanJingId']
        # end handle [GC_UPDATE_SKILLZHUANJING_LEVELUP_INFO] message attrs, auto generate do not change
        pass


class GC_SWORDTEAM_LEAVE (Packet):
    def handle(self):
        # begin handle [GC_SWORDTEAM_LEAVE] message attrs, auto generate do not change
        self.person['swordteamGuid'] = self['swordteamGuid']
        # end handle [GC_SWORDTEAM_LEAVE] message attrs, auto generate do not change
        pass


class CG_ASK_PASSPORT_DATA (Packet):
    pass


class GC_RESPOND_EXCHANGE_CURRENCY (Packet):
    def handle(self):
        # begin handle [GC_RESPOND_EXCHANGE_CURRENCY] message attrs, auto generate do not change
        self.person['isSuccess'] = self['isSuccess']
        self.person['index'] = self['index']
        # end handle [GC_RESPOND_EXCHANGE_CURRENCY] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILD_REALTIME_VOICE_ROOM_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_REALTIME_VOICE_ROOM_INFO] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['syncType'] = self['syncType']
        self.person['roomInfoList'] = self['roomInfoList']
        self.person['guildGuid'] = self['guildGuid']
        # end handle [GC_SYNC_GUILD_REALTIME_VOICE_ROOM_INFO] message attrs, auto generate do not change
        pass


class CG_PUT_ITEM_STORAGEPACK (Packet):
    pass


class GC_CHANGE_ARMY_MEMBER_POSITION_OVER (Packet):
    def handle(self):
        # begin handle [GC_CHANGE_ARMY_MEMBER_POSITION_OVER] message attrs, auto generate do not change
        # end handle [GC_CHANGE_ARMY_MEMBER_POSITION_OVER] message attrs, auto generate do not change
        pass


class GC_SYNC_NPCPICKUP_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NPCPICKUP_STATE] message attrs, auto generate do not change
        self.person['serverid'] = self['serverid']
        self.person['iscanpickup'] = self['iscanpickup']
        # end handle [GC_SYNC_NPCPICKUP_STATE] message attrs, auto generate do not change
        pass


class GC_COMMONCOMMAND (Packet):
    def handle(self):
        # begin handle [GC_COMMONCOMMAND] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['param'] = self['param']
        # end handle [GC_COMMONCOMMAND] message attrs, auto generate do not change
        pass


class CG_REQ_QIANZHUANG_DATA (Packet):
    pass


class CG_REQ_TIMELIMITACTSCENE_ENTER (Packet):
    pass


class GC_VERIFYCODE_SYNC (Packet):
    def handle(self):
        # begin handle [GC_VERIFYCODE_SYNC] message attrs, auto generate do not change
        self.person['typeId'] = self['typeId']
        self.person['question'] = self['question']
        self.person['verifyNode'] = self['verifyNode']
        # end handle [GC_VERIFYCODE_SYNC] message attrs, auto generate do not change
        pass


class CG_REQ_RECRUIT (Packet):
    pass


class GC_LUCKY_CONNECT_SYNC (Packet):
    def handle(self):
        # begin handle [GC_LUCKY_CONNECT_SYNC] message attrs, auto generate do not change
        self.person['BrandStateList'] = self['BrandStateList']
        self.person['RewardList'] = self['RewardList']
        self.person['GrandRewardID'] = self['GrandRewardID']
        self.person['GrandRewardCount'] = self['GrandRewardCount']
        self.person['RemainTime'] = self['RemainTime']
        self.person['RemainResetTime'] = self['RemainResetTime']
        self.person['IsItemReset'] = self['IsItemReset']
        self.person['ResetItemID'] = self['ResetItemID']
        self.person['ResetItemCount'] = self['ResetItemCount']
        self.person['DrawItemID'] = self['DrawItemID']
        self.person['DrawItemCount'] = self['DrawItemCount']
        self.person['NewBrandIndex'] = self['NewBrandIndex']
        self.person['HasGrandReward'] = self['HasGrandReward']
        # end handle [GC_LUCKY_CONNECT_SYNC] message attrs, auto generate do not change
        pass


class GC_EQUIP_REFINE_RET (Packet):
    def handle(self):
        # begin handle [GC_EQUIP_REFINE_RET] message attrs, auto generate do not change
        self.person['success'] = self['success']
        self.person['level'] = self['level']
        # end handle [GC_EQUIP_REFINE_RET] message attrs, auto generate do not change
        pass


class GC_STALL_REVIEW_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_STALL_REVIEW_UPDATE] message attrs, auto generate do not change
        self.person['StallGuid'] = self['StallGuid']
        self.person['StallState'] = self['StallState']
        self.person['StallTime'] = self['StallTime']
        # end handle [GC_STALL_REVIEW_UPDATE] message attrs, auto generate do not change
        pass


class GC_SYNC_FEEDBACK_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FEEDBACK_INFO] message attrs, auto generate do not change
        self.person['url'] = self['url']
        self.person['startTime'] = self['startTime']
        self.person['endTime'] = self['endTime']
        # end handle [GC_SYNC_FEEDBACK_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_GUILD_MONSTER_DATA (Packet):
    pass


class GC_SYNC_FREEZE_SKILL_RELEASE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FREEZE_SKILL_RELEASE] message attrs, auto generate do not change
        self.person['freezeSkillReleaseSceneClassId'] = self['freezeSkillReleaseSceneClassId']
        # end handle [GC_SYNC_FREEZE_SKILL_RELEASE] message attrs, auto generate do not change
        pass


class GC_SHEDAOSAIMA_RANK (Packet):
    def handle(self):
        # begin handle [GC_SHEDAOSAIMA_RANK] message attrs, auto generate do not change
        self.person['PaiMing'] = self['PaiMing']
        self.person['GameState'] = self['GameState']
        # end handle [GC_SHEDAOSAIMA_RANK] message attrs, auto generate do not change
        pass


class CG_STALL_APPEAL (Packet):
    pass


class CG_BUY_NIEREN_SUPER (Packet):
    pass


class GC_SHOW_DEVICE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SHOW_DEVICE_INFO] message attrs, auto generate do not change
        # end handle [GC_SHOW_DEVICE_INFO] message attrs, auto generate do not change
        pass


class CG_ADVENTURE_REQ_BUY_ITEM (Packet):
    pass


class GC_SYSTEMTRADE_CANSELLLIST (Packet):
    def handle(self):
        # begin handle [GC_SYSTEMTRADE_CANSELLLIST] message attrs, auto generate do not change
        self.person['itemguid'] = self['itemguid']
        # end handle [GC_SYSTEMTRADE_CANSELLLIST] message attrs, auto generate do not change
        pass


class GC_StopShangGuEMoEnergy (Packet):
    def handle(self):
        # begin handle [GC_StopShangGuEMoEnergy] message attrs, auto generate do not change
        self.person['curEnergyLayers'] = self['curEnergyLayers']
        self.person['maxEnergyLayers'] = self['maxEnergyLayers']
        # end handle [GC_StopShangGuEMoEnergy] message attrs, auto generate do not change
        pass


class GC_CREATE_SNARE (Packet):
    def handle(self):
        # begin handle [GC_CREATE_SNARE] message attrs, auto generate do not change
        self.person['serverId'] = self['serverId']
        self.person['OwerId'] = self['OwerId']
        self.person['Owerguid'] = self['Owerguid']
        self.person['sceneInst'] = self['sceneInst']
        self.person['sceneClass'] = self['sceneClass']
        self.person['SnareId'] = self['SnareId']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        self.person['nState'] = self['nState']
        # end handle [GC_CREATE_SNARE] message attrs, auto generate do not change
        pass


class CG_REQ_PET_FEED (Packet):
    pass


class CG_PICK_RANDOM_COLOR_ITEM_STORAGE (Packet):
    pass


class GC_WISHING_UPDATE_SELECTED_STATUS_RESULT (Packet):
    def handle(self):
        # begin handle [GC_WISHING_UPDATE_SELECTED_STATUS_RESULT] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['id'] = self['id']
        self.person['index'] = self['index']
        self.person['status'] = self['status']
        # end handle [GC_WISHING_UPDATE_SELECTED_STATUS_RESULT] message attrs, auto generate do not change
        pass


class GC_GUILDWAR_MATCH_RESULT (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_MATCH_RESULT] message attrs, auto generate do not change
        self.person['armyAid'] = self['armyAid']
        self.person['armyAname'] = self['armyAname']
        self.person['armyBid'] = self['armyBid']
        self.person['armyName'] = self['armyName']
        # end handle [GC_GUILDWAR_MATCH_RESULT] message attrs, auto generate do not change
        pass


class GC_PLAYER_CHANGESCENE_MOVETO (Packet):
    def handle(self):
        # begin handle [GC_PLAYER_CHANGESCENE_MOVETO] message attrs, auto generate do not change
        self.person['sceneId'] = self['sceneId']
        self.person['tarposx'] = self['tarposx']
        self.person['tarposy'] = self['tarposy']
        self.person['tarposz'] = self['tarposz']
        # end handle [GC_PLAYER_CHANGESCENE_MOVETO] message attrs, auto generate do not change
        pass


class CG_REQ_DESTINY_ATTRIBUTE (Packet):
    pass


class CG_REQ_QQ_UNREG_FRIENDS (Packet):
    pass


class GC_BOSS_PICK_ITEM_RET (Packet):
    def handle(self):
        # begin handle [GC_BOSS_PICK_ITEM_RET] message attrs, auto generate do not change
        self.person['rewardInfos'] = self['rewardInfos']
        # end handle [GC_BOSS_PICK_ITEM_RET] message attrs, auto generate do not change
        pass


class GC_FAIRY_RAISE_OPEN_BUY_FEED_TIME_UI (Packet):
    def handle(self):
        # begin handle [GC_FAIRY_RAISE_OPEN_BUY_FEED_TIME_UI] message attrs, auto generate do not change
        self.person['feedTimeLeft'] = self['feedTimeLeft']
        self.person['feedTimeCanBuy'] = self['feedTimeCanBuy']
        # end handle [GC_FAIRY_RAISE_OPEN_BUY_FEED_TIME_UI] message attrs, auto generate do not change
        pass


class CG_SAVE_HOME_BUILDING (Packet):
    pass


class CG_NEW_PLAYER_BEHAVIOR_MISSION (Packet):
    pass


class GC_START_RUBKICUBE_SUB_PLAY (Packet):
    def handle(self):
        # begin handle [GC_START_RUBKICUBE_SUB_PLAY] message attrs, auto generate do not change
        self.person['subRubkiCubePlayId'] = self['subRubkiCubePlayId']
        self.person['endTime'] = self['endTime']
        self.person['serverTime'] = self['serverTime']
        # end handle [GC_START_RUBKICUBE_SUB_PLAY] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_PLAY_TIANJIEGU_EFFECT] message attrs, auto generate do not change
        self.person['effectId'] = self['effectId']
        # end handle [GC_PLAY_TIANJIEGU_EFFECT] message attrs, auto generate do not change
        pass


class GC_WAITPAY_ADD (Packet):
    def handle(self):
        # begin handle [GC_WAITPAY_ADD] message attrs, auto generate do not change
        # end handle [GC_WAITPAY_ADD] message attrs, auto generate do not change
        pass


class GC_TOURNAMENT_RET_LOTTERY (Packet):
    def handle(self):
        # begin handle [GC_TOURNAMENT_RET_LOTTERY] message attrs, auto generate do not change
        self.person['stoneId'] = self['stoneId']
        # end handle [GC_TOURNAMENT_RET_LOTTERY] message attrs, auto generate do not change
        pass


class CG_ASK_YIRONG_CARD (Packet):
    pass


class CG_GUILD_REQ_SET_QUICKJOIN (Packet):
    pass


class GC_ASURA_UPDATE_BATTLE_INFO (Packet):
    def handle(self):
        # begin handle [GC_ASURA_UPDATE_BATTLE_INFO] message attrs, auto generate do not change
        self.person['floorId'] = self['floorId']
        self.person['keyCount'] = self['keyCount']
        self.person['keyPicked'] = self['keyPicked']
        self.person['keyOwner'] = self['keyOwner']
        # end handle [GC_ASURA_UPDATE_BATTLE_INFO] message attrs, auto generate do not change
        pass


class GC_TEAMFOLLOW_SEAMLESS (Packet):
    def handle(self):
        # begin handle [GC_TEAMFOLLOW_SEAMLESS] message attrs, auto generate do not change
        self.person['sceneId'] = self['sceneId']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        self.person['serverPosX'] = self['serverPosX']
        self.person['serverPosY'] = self['serverPosY']
        self.person['serverPosZ'] = self['serverPosZ']
        # end handle [GC_TEAMFOLLOW_SEAMLESS] message attrs, auto generate do not change
        pass


class GC_SHOW_ACHIEVEMENT (Packet):
    def handle(self):
        # begin handle [GC_SHOW_ACHIEVEMENT] message attrs, auto generate do not change
        self.person['achievementId'] = self['achievementId']
        # end handle [GC_SHOW_ACHIEVEMENT] message attrs, auto generate do not change
        pass


class GC_SYNC_TEAM_PVPZOMBIE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TEAM_PVPZOMBIE] message attrs, auto generate do not change
        self.person['PvPZombieList'] = self['PvPZombieList']
        # end handle [GC_SYNC_TEAM_PVPZOMBIE] message attrs, auto generate do not change
        pass


class CG_EQUIPMIRROR_FORGE (Packet):
    pass


class CG_TOURNAMENT_TAKE_REWARD (Packet):
    pass


class GC_BEGIN_CHANGENAME (Packet):
    def handle(self):
        # begin handle [GC_BEGIN_CHANGENAME] message attrs, auto generate do not change
        self.person['nametype'] = self['nametype']
        self.person['itemid'] = self['itemid']
        # end handle [GC_BEGIN_CHANGENAME] message attrs, auto generate do not change
        pass


class GC_RET_FAIRY_SKILL_LEVEL_UP_RESULT (Packet):
    def handle(self):
        # begin handle [GC_RET_FAIRY_SKILL_LEVEL_UP_RESULT] message attrs, auto generate do not change
        self.person['fairyGuid'] = self['fairyGuid']
        self.person['skillId'] = self['skillId']
        self.person['isCore'] = self['isCore']
        # end handle [GC_RET_FAIRY_SKILL_LEVEL_UP_RESULT] message attrs, auto generate do not change
        pass


class GC_SYNC_COMMONDATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COMMONDATA] message attrs, auto generate do not change
        self.person['nIndex'] = self['nIndex']
        self.person['nValue'] = self['nValue']
        # end handle [GC_SYNC_COMMONDATA] message attrs, auto generate do not change
        pass


class GC_SYNC_HOME_FORTUNE_TELLING_RESULT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HOME_FORTUNE_TELLING_RESULT] message attrs, auto generate do not change
        self.person['result'] = self['result']
        # end handle [GC_SYNC_HOME_FORTUNE_TELLING_RESULT] message attrs, auto generate do not change
        pass


class GC_DOMAIN_UPDATEEVT (Packet):
    def handle(self):
        # begin handle [GC_DOMAIN_UPDATEEVT] message attrs, auto generate do not change
        self.person['evts'] = self['evts']
        # end handle [GC_DOMAIN_UPDATEEVT] message attrs, auto generate do not change
        pass


class CG_ChangeMentorName (Packet):
    pass


class GC_AUTOTEAM_OVERTIME_REQUEST (Packet):
    def handle(self):
        # begin handle [GC_AUTOTEAM_OVERTIME_REQUEST] message attrs, auto generate do not change
        self.person['nRequest_type'] = self['nRequest_type']
        # end handle [GC_AUTOTEAM_OVERTIME_REQUEST] message attrs, auto generate do not change
        pass


class GC_COLLECT_INFO (Packet):
    def handle(self):
        # begin handle [GC_COLLECT_INFO] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['ownerGuid'] = self['ownerGuid']
        self.person['collectid'] = self['collectid']
        self.person['pos_x'] = self['pos_x']
        self.person['pos_y'] = self['pos_y']
        self.person['pos_z'] = self['pos_z']
        self.person['cotype'] = self['cotype']
        self.person['bornTime'] = self['bornTime']
        # end handle [GC_COLLECT_INFO] message attrs, auto generate do not change
        pass


class GC_MULPVP_INVITE (Packet):
    def handle(self):
        # begin handle [GC_MULPVP_INVITE] message attrs, auto generate do not change
        self.person['inviterPlayerGuid'] = self['inviterPlayerGuid']
        self.person['inviterName'] = self['inviterName']
        self.person['inviterIsTeam'] = self['inviterIsTeam']
        # end handle [GC_MULPVP_INVITE] message attrs, auto generate do not change
        pass


class CG_REQ_FAIRY_NEIDAN_FEED (Packet):
    pass


class CG_REQ_ARMY_CHANGE_RTROLE (Packet):
    pass


class GC_UPDATE_GROWWAY_INFO (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_GROWWAY_INFO] message attrs, auto generate do not change
        self.person['GrowWayData'] = self['GrowWayData']
        self.person['ActivityData'] = self['ActivityData']
        self.person['GrowWayActivityState'] = self['GrowWayActivityState']
        self.person['GrowWayActiveDays'] = self['GrowWayActiveDays']
        self.person['StageOpenDay'] = self['StageOpenDay']
        # end handle [GC_UPDATE_GROWWAY_INFO] message attrs, auto generate do not change
        pass


class GC_BATTLEFIELD_BROADCAST (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_BROADCAST] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['achievementID'] = self['achievementID']
        self.person['ObjId'] = self['ObjId']
        self.person['szName'] = self['szName']
        self.person['prof'] = self['prof']
        self.person['isFriend'] = self['isFriend']
        self.person['sex'] = self['sex']
        # end handle [GC_BATTLEFIELD_BROADCAST] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_MULPVP_FIGHTSTATE] message attrs, auto generate do not change
        self.person['stateType'] = self['stateType']
        self.person['isLeader'] = self['isLeader']
        self.person['Charguid'] = self['Charguid']
        self.person['Charname'] = self['Charname']
        self.person['LeaderFlag'] = self['LeaderFlag']
        self.person['ProId'] = self['ProId']
        self.person['Lev'] = self['Lev']
        self.person['KillCount'] = self['KillCount']
        self.person['DeathCount'] = self['DeathCount']
        self.person['memGuid'] = self['memGuid']
        # end handle [GC_MULPVP_FIGHTSTATE] message attrs, auto generate do not change
        pass


class GC_TOWER_ENTER_NEXT (Packet):
    def handle(self):
        # begin handle [GC_TOWER_ENTER_NEXT] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        # end handle [GC_TOWER_ENTER_NEXT] message attrs, auto generate do not change
        pass


class GC_RECOMMEND_FRIENDRET (Packet):
    def handle(self):
        # begin handle [GC_RECOMMEND_FRIENDRET] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['RealSex'] = self['RealSex']
        self.person['Birthday'] = self['Birthday']
        self.person['Address'] = self['Address']
        self.person['Ret'] = self['Ret']
        self.person['SpaceSex'] = self['SpaceSex']
        self.person['Reserved'] = self['Reserved']
        self.person['headPicname'] = self['headPicname']
        self.person['PhotoFrame'] = self['PhotoFrame']
        # end handle [GC_RECOMMEND_FRIENDRET] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_JOIN_OTHERPLAYER (Packet):
    pass


class CG_ACTIVITY_BUYBACK_ASK_DATA (Packet):
    pass


class CG_BROTHERHOOD_RECRUIT_PUBLISH (Packet):
    pass


class GC_BWPVPFINAL_MEMINFOINCOPYSCENE (Packet):
    def handle(self):
        # begin handle [GC_BWPVPFINAL_MEMINFOINCOPYSCENE] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['waitTime'] = self['waitTime']
        self.person['readTime'] = self['readTime']
        self.person['MemName'] = self['MemName']
        self.person['MemLev'] = self['MemLev']
        self.person['MemPro'] = self['MemPro']
        self.person['MemSwordGuid'] = self['MemSwordGuid']
        self.person['selfNum'] = self['selfNum']
        self.person['enemyNum'] = self['enemyNum']
        self.person['endTime'] = self['endTime']
        self.person['TotalRound'] = self['TotalRound']
        # end handle [GC_BWPVPFINAL_MEMINFOINCOPYSCENE] message attrs, auto generate do not change
        pass


class GC_GET_CURRENCY (Packet):
    def handle(self):
        # begin handle [GC_GET_CURRENCY] message attrs, auto generate do not change
        self.person['currencyType'] = self['currencyType']
        self.person['count'] = self['count']
        self.person['suffix'] = self['suffix']
        # end handle [GC_GET_CURRENCY] message attrs, auto generate do not change
        pass


class CG_TOURNAMENT_REQ_LOTTERY (Packet):
    pass


class GC_HONGBAO_SEND (Packet):
    def handle(self):
        # begin handle [GC_HONGBAO_SEND] message attrs, auto generate do not change
        self.person['nNoParam'] = self['nNoParam']
        # end handle [GC_HONGBAO_SEND] message attrs, auto generate do not change
        pass


class GC_SEARCHSDKCHECK_GUILD_RET (Packet):
    def handle(self):
        # begin handle [GC_SEARCHSDKCHECK_GUILD_RET] message attrs, auto generate do not change
        self.person['isok'] = self['isok']
        self.person['pageuid'] = self['pageuid']
        # end handle [GC_SEARCHSDKCHECK_GUILD_RET] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_COPYSCENE_PROGRESS] message attrs, auto generate do not change
        self.person['curvalue'] = self['curvalue']
        self.person['maxvalue'] = self['maxvalue']
        self.person['sceneid'] = self['sceneid']
        self.person['timecount'] = self['timecount']
        # end handle [GC_COPYSCENE_PROGRESS] message attrs, auto generate do not change
        pass


class GC_SERVANT_RETOP (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_RETOP] message attrs, auto generate do not change
        self.person['m_OpType'] = self['m_OpType']
        self.person['m_ServantId'] = self['m_ServantId']
        self.person['m_Ret'] = self['m_Ret']
        # end handle [GC_SERVANT_RETOP] message attrs, auto generate do not change
        pass


class CG_SEND_COUPLE_BP_RESULT (Packet):
    pass


class CG_DOMAIN_REQ_HISTORYLIST (Packet):
    pass


class GC_BROADCAST_GUILDSHORTNAME (Packet):
    def handle(self):
        # begin handle [GC_BROADCAST_GUILDSHORTNAME] message attrs, auto generate do not change
        self.person['PlayerGuid'] = self['PlayerGuid']
        self.person['GuildShortName'] = self['GuildShortName']
        self.person['GuildShortNameColor'] = self['GuildShortNameColor']
        self.person['bwgwRankNum'] = self['bwgwRankNum']
        # end handle [GC_BROADCAST_GUILDSHORTNAME] message attrs, auto generate do not change
        pass


class GC_SYNC_FAIRY_SKILL_LOCK (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FAIRY_SKILL_LOCK] message attrs, auto generate do not change
        self.person['num'] = self['num']
        # end handle [GC_SYNC_FAIRY_SKILL_LOCK] message attrs, auto generate do not change
        pass


class GC_DELAPPLYLIST (Packet):
    def handle(self):
        # begin handle [GC_DELAPPLYLIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        # end handle [GC_DELAPPLYLIST] message attrs, auto generate do not change
        pass


class GC_SYNC_SKILLSOUL_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SKILLSOUL_STATE] message attrs, auto generate do not change
        self.person['state'] = self['state']
        self.person['sceneId'] = self['sceneId']
        # end handle [GC_SYNC_SKILLSOUL_STATE] message attrs, auto generate do not change
        pass


class CG_FASHION_PROLONG (Packet):
    pass


class GC_DOMAINWAR_OP_RET (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_OP_RET] message attrs, auto generate do not change
        self.person['domainId'] = self['domainId']
        self.person['opType'] = self['opType']
        self.person['opRet'] = self['opRet']
        # end handle [GC_DOMAINWAR_OP_RET] message attrs, auto generate do not change
        pass


class CG_CHATLINK_DOWNLOAD (Packet):
    pass


class CG_EQUIP_REFINE (Packet):
    pass


class CG_REQ_REPLACE_EQUIP_REBIRTH_RECASE_TRICK (Packet):
    pass


class GC_RET_AUCTION_LOOK (Packet):
    def handle(self):
        # begin handle [GC_RET_AUCTION_LOOK] message attrs, auto generate do not change
        self.person['page'] = self['page']
        self.person['publictime'] = self['publictime']
        self.person['order'] = self['order']
        self.person['classid'] = self['classid']
        self.person['subclassid'] = self['subclassid']
        self.person['treasure'] = self['treasure']
        self.person['quality'] = self['quality']
        self.person['profession'] = self['profession']
        self.person['minlevel'] = self['minlevel']
        self.person['maxlevel'] = self['maxlevel']
        self.person['otherclass'] = self['otherclass']
        self.person['itemid'] = self['itemid']
        self.person['attr'] = self['attr']
        self.person['thirdclassid'] = self['thirdclassid']
        self.person['reserved'] = self['reserved']
        self.person['reserved1'] = self['reserved1']
        self.person['color'] = self['color']
        self.person['auctionitems'] = self['auctionitems']
        self.person['maxcount'] = self['maxcount']
        self.person['sellmoneytype'] = self['sellmoneytype']
        self.person['minprice'] = self['minprice']
        self.person['maxprice'] = self['maxprice']
        self.person['issearch'] = self['issearch']
        # end handle [GC_RET_AUCTION_LOOK] message attrs, auto generate do not change
        pass


class CG_EQUIPMIRROR_COMPOUND (Packet):
    pass


class CG_WEDDING_CREATE (Packet):
    pass


class GC_SYNC_SKILLBARINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SKILLBARINFO] message attrs, auto generate do not change
        self.person['barInfo'] = self['barInfo']
        self.person['flyBarInfo'] = self['flyBarInfo']
        self.person['bar2Info'] = self['bar2Info']
        self.person['bar3Info'] = self['bar3Info']
        self.person['bar4Info'] = self['bar4Info']
        # end handle [GC_SYNC_SKILLBARINFO] message attrs, auto generate do not change
        pass


class GC_CREATE_NPC (Packet):
    def handle(self):
        # begin handle [GC_CREATE_NPC] message attrs, auto generate do not change
        self.person['charBaseAttr'] = self['charBaseAttr']
        self.person['isBorn'] = self['isBorn']
        self.person['NpcTitle'] = self['NpcTitle']
        self.person['curSelectObjId'] = self['curSelectObjId']
        self.person['NpcGuildShortName'] = self['NpcGuildShortName']
        self.person['NpcGuildName'] = self['NpcGuildName']
        self.person['NpcGuildFlagLv'] = self['NpcGuildFlagLv']
        self.person['NpcGuildShortNameColor'] = self['NpcGuildShortNameColor']
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['OwnTeamId'] = self['OwnTeamId']
        self.person['RubkiCubeId'] = self['RubkiCubeId']
        self.person['buffTransID'] = self['buffTransID']
        # end handle [GC_CREATE_NPC] message attrs, auto generate do not change
        pass


class GC_ON_DIE_KILLER_ID (Packet):
    def handle(self):
        # begin handle [GC_ON_DIE_KILLER_ID] message attrs, auto generate do not change
        self.person['killerID'] = self['killerID']
        # end handle [GC_ON_DIE_KILLER_ID] message attrs, auto generate do not change
        pass


class CG_REQ_WORLD_GROUPINFO (Packet):
    pass


class GC_RET_COPYPLAYERINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_COPYPLAYERINFO] message attrs, auto generate do not change
        self.person['CopyPlayerGuid'] = self['CopyPlayerGuid']
        self.person['CopyPlayerName'] = self['CopyPlayerName']
        self.person['CopyPlayerCombat'] = self['CopyPlayerCombat']
        self.person['CopyPlayerProId'] = self['CopyPlayerProId']
        self.person['CopyPlayerLev'] = self['CopyPlayerLev']
        # end handle [GC_RET_COPYPLAYERINFO] message attrs, auto generate do not change
        pass


class GC_SET_PET_HUNGER (Packet):
    def handle(self):
        # begin handle [GC_SET_PET_HUNGER] message attrs, auto generate do not change
        self.person['petGuid'] = self['petGuid']
        self.person['hungerValue'] = self['hungerValue']
        # end handle [GC_SET_PET_HUNGER] message attrs, auto generate do not change
        pass


class CG_REQUEST_LASTRECAST_INFO (Packet):
    pass


class GC_SYNC_COPYSCENE_ENTERCOUNT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COPYSCENE_ENTERCOUNT] message attrs, auto generate do not change
        self.person['nID'] = self['nID']
        self.person['nCount'] = self['nCount']
        self.person['nEnterCount'] = self['nEnterCount']
        # end handle [GC_SYNC_COPYSCENE_ENTERCOUNT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_RET_GETREWARDFORSIGNIN] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        # end handle [GC_RET_GETREWARDFORSIGNIN] message attrs, auto generate do not change
        pass


class GC_COPYSCENE_HIDINGBOSS (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_HIDINGBOSS] message attrs, auto generate do not change
        self.person['playerguid'] = self['playerguid']
        self.person['playerstatus'] = self['playerstatus']
        self.person['sceneclass'] = self['sceneclass']
        self.person['bInit'] = self['bInit']
        self.person['itemCount'] = self['itemCount']
        self.person['bCloseWindow'] = self['bCloseWindow']
        self.person['itemids'] = self['itemids']
        # end handle [GC_COPYSCENE_HIDINGBOSS] message attrs, auto generate do not change
        pass


class CG_ASK_PICKUP_ITEM (Packet):
    pass


class GC_ACTIVITY_BUYBACK_SYNC_DATA (Packet):
    def handle(self):
        # begin handle [GC_ACTIVITY_BUYBACK_SYNC_DATA] message attrs, auto generate do not change
        self.person['canUseList'] = self['canUseList']
        self.person['ownList'] = self['ownList']
        self.person['isLogin'] = self['isLogin']
        # end handle [GC_ACTIVITY_BUYBACK_SYNC_DATA] message attrs, auto generate do not change
        pass


class GC_RES_RECOMMEND_MEMBER_INFO (Packet):
    def handle(self):
        # begin handle [GC_RES_RECOMMEND_MEMBER_INFO] message attrs, auto generate do not change
        self.person['playerGuid'] = self['playerGuid']
        self.person['playerName'] = self['playerName']
        self.person['profession'] = self['profession']
        self.person['sex'] = self['sex']
        self.person['level'] = self['level']
        self.person['combatNum'] = self['combatNum']
        self.person['haveNewPlayerCatch'] = self['haveNewPlayerCatch']
        # end handle [GC_RES_RECOMMEND_MEMBER_INFO] message attrs, auto generate do not change
        pass


class CG_STALL_CANCELSELL (Packet):
    pass


class GC_PLAY_WARN_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_PLAY_WARN_EFFECT] message attrs, auto generate do not change
        self.person['objID'] = self['objID']
        self.person['warnID'] = self['warnID']
        self.person['TargetPositionX'] = self['TargetPositionX']
        self.person['TargetPositionY'] = self['TargetPositionY']
        self.person['TargetPositionZ'] = self['TargetPositionZ']
        self.person['speed'] = self['speed']
        # end handle [GC_PLAY_WARN_EFFECT] message attrs, auto generate do not change
        pass


class GC_SYNC_OBCELEBRATION_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_OBCELEBRATION_INFO] message attrs, auto generate do not change
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['ExchangeStartTime'] = self['ExchangeStartTime']
        self.person['ExchangeEndTime'] = self['ExchangeEndTime']
        self.person['WishTotalGroupPhotoNumber'] = self['WishTotalGroupPhotoNumber']
        self.person['CurrentShareNumber'] = self['CurrentShareNumber']
        self.person['WishStep'] = self['WishStep']
        # end handle [GC_SYNC_OBCELEBRATION_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_AUTO_DECOMPOSE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_AUTO_DECOMPOSE] message attrs, auto generate do not change
        self.person['decomposeInfos'] = self['decomposeInfos']
        # end handle [GC_SYNC_AUTO_DECOMPOSE] message attrs, auto generate do not change
        pass


class GC_MISSION_DONE (Packet):
    def handle(self):
        # begin handle [GC_MISSION_DONE] message attrs, auto generate do not change
        self.person['missionId'] = self['missionId']
        self.person['isDone'] = self['isDone']
        # end handle [GC_MISSION_DONE] message attrs, auto generate do not change
        pass


class GC_RET_ADVENTURE_EVENT_ACCEPT (Packet):
    def handle(self):
        # begin handle [GC_RET_ADVENTURE_EVENT_ACCEPT] message attrs, auto generate do not change
        self.person['eventId'] = self['eventId']
        # end handle [GC_RET_ADVENTURE_EVENT_ACCEPT] message attrs, auto generate do not change
        pass


class CG_TSS_ANTI_RECV_DATA (Packet):
    pass


class CG_QTE_PLAYOVER (Packet):
    pass


class CG_STARMAP_REDPOINT_INFO (Packet):
    pass


class GC_MOUNT_DATA (Packet):
    def handle(self):
        # begin handle [GC_MOUNT_DATA] message attrs, auto generate do not change
        self.person['ObjServerID'] = self['ObjServerID']
        self.person['MountID'] = self['MountID']
        self.person['MountFashoinId'] = self['MountFashoinId']
        self.person['MountColorIndex'] = self['MountColorIndex']
        # end handle [GC_MOUNT_DATA] message attrs, auto generate do not change
        pass


class CG_BANGHUA_INTERACTIVE (Packet):
    pass


class GC_SYNC_COMMONACTIVITYINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COMMONACTIVITYINFO] message attrs, auto generate do not change
        self.person['endtime'] = self['endtime']
        self.person['itemid'] = self['itemid']
        self.person['addvalue'] = self['addvalue']
        # end handle [GC_SYNC_COMMONACTIVITYINFO] message attrs, auto generate do not change
        pass


class CG_ASK_RELIVE (Packet):
    pass


class GC_ENTER_SCENE (Packet):
    def handle(self):
        # begin handle [GC_ENTER_SCENE] message attrs, auto generate do not change
        self.person['sceneclass'] = self['sceneclass']
        self.person['sceneinst'] = self['sceneinst']
        self.person['sceneinstcount'] = self['sceneinstcount']
        self.person['sceneactivation'] = self['sceneactivation']
        self.person['mainplayerserverid'] = self['mainplayerserverid']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        self.person['createroletime'] = self['createroletime']
        self.person['isServerSeamless'] = self['isServerSeamless']
        self.person['opendynamiclevel'] = self['opendynamiclevel']
        self.person['sceneplayercount'] = self['sceneplayercount']
        # end handle [GC_ENTER_SCENE] message attrs, auto generate do not change
        loadlog.debug(__class__.__name__)
        loadlog.debug(self.obj)
        pass


class CG_AID_RESPONSE (Packet):
    pass


class GC_CREATE_SCENE_GATHER (Packet):
    def handle(self):
        # begin handle [GC_CREATE_SCENE_GATHER] message attrs, auto generate do not change
        self.person['posid'] = self['posid']
        self.person['isRich'] = self['isRich']
        self.person['state'] = self['state']
        # end handle [GC_CREATE_SCENE_GATHER] message attrs, auto generate do not change
        pass


class GC_RET_YLTXINST_DES_REMAIN_NUM (Packet):
    def handle(self):
        # begin handle [GC_RET_YLTXINST_DES_REMAIN_NUM] message attrs, auto generate do not change
        self.person['nResult'] = self['nResult']
        self.person['bIsEnterScene'] = self['bIsEnterScene']
        self.person['yltxNpcPosData'] = self['yltxNpcPosData']
        # end handle [GC_RET_YLTXINST_DES_REMAIN_NUM] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_UPDATE_BATTLE_FAIRY_LIST] message attrs, auto generate do not change
        self.person['fairyGuid'] = self['fairyGuid']
        # end handle [GC_UPDATE_BATTLE_FAIRY_LIST] message attrs, auto generate do not change
        pass


class CG_MILITARY_REQ_PROMOTERANK (Packet):
    pass


class GC_SYNC_TITLEINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TITLEINFO] message attrs, auto generate do not change
        self.person['SystemTitleId'] = self['SystemTitleId']
        self.person['SystemCreateTime'] = self['SystemCreateTime']
        self.person['UserDefTitleId'] = self['UserDefTitleId']
        self.person['FirstUserDefContent'] = self['FirstUserDefContent']
        self.person['SecondUserDefContent'] = self['SecondUserDefContent']
        self.person['UserDefCreateTime'] = self['UserDefCreateTime']
        self.person['CurTitleId'] = self['CurTitleId']
        self.person['IsLockCurrent'] = self['IsLockCurrent']
        self.person['ExtraLifeTime'] = self['ExtraLifeTime']
        # end handle [GC_SYNC_TITLEINFO] message attrs, auto generate do not change
        pass


class GC_DELETE_CUTSCENE_TRIGGER (Packet):
    def handle(self):
        # begin handle [GC_DELETE_CUTSCENE_TRIGGER] message attrs, auto generate do not change
        self.person['DynamicAreaId'] = self['DynamicAreaId']
        # end handle [GC_DELETE_CUTSCENE_TRIGGER] message attrs, auto generate do not change
        pass


class CG_REQ_JIANMUXB_FILLING_HELP (Packet):
    pass


class GC_RET_JOIN_GUILD_REALTIME_VOICE_ROOM (Packet):
    def handle(self):
        # begin handle [GC_RET_JOIN_GUILD_REALTIME_VOICE_ROOM] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['roomId'] = self['roomId']
        # end handle [GC_RET_JOIN_GUILD_REALTIME_VOICE_ROOM] message attrs, auto generate do not change
        pass


class GC_BROADCAST_CURTITLE (Packet):
    def handle(self):
        # begin handle [GC_BROADCAST_CURTITLE] message attrs, auto generate do not change
        self.person['PlayerGuid'] = self['PlayerGuid']
        self.person['TitleId'] = self['TitleId']
        self.person['FirstTitleUserDef'] = self['FirstTitleUserDef']
        self.person['SecondTitleUserDef'] = self['SecondTitleUserDef']
        # end handle [GC_BROADCAST_CURTITLE] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_GUILD_ALLIANCE_APPLY_LIST] message attrs, auto generate do not change
        self.person['ApplyGuild'] = self['ApplyGuild']
        self.person['BeApplyedGuild'] = self['BeApplyedGuild']
        # end handle [GC_GUILD_ALLIANCE_APPLY_LIST] message attrs, auto generate do not change
        pass


class CG_GROUPPHOTO_REQUEST (Packet):
    pass


class CG_REQ_AUCTION_FAVORITE (Packet):
    pass


class CG_USE_DIRECTSENDGIDT (Packet):
    pass


class GC_SINGLE_INTERACT (Packet):
    def handle(self):
        # begin handle [GC_SINGLE_INTERACT] message attrs, auto generate do not change
        self.person['actid'] = self['actid']
        self.person['actserverid'] = self['actserverid']
        self.person['isreset'] = self['isreset']
        self.person['qxsMusic'] = self['qxsMusic']
        # end handle [GC_SINGLE_INTERACT] message attrs, auto generate do not change
        pass


class GC_FASHION_DEL (Packet):
    def handle(self):
        # begin handle [GC_FASHION_DEL] message attrs, auto generate do not change
        self.person['FashionPart'] = self['FashionPart']
        self.person['FashionId'] = self['FashionId']
        self.person['DeleteType'] = self['DeleteType']
        # end handle [GC_FASHION_DEL] message attrs, auto generate do not change
        pass


class GC_STALL_REVIEW_DELETE (Packet):
    def handle(self):
        # begin handle [GC_STALL_REVIEW_DELETE] message attrs, auto generate do not change
        self.person['StallGuid'] = self['StallGuid']
        # end handle [GC_STALL_REVIEW_DELETE] message attrs, auto generate do not change
        pass


class GC_SKILL_SWITCH_TYPE_SKILL (Packet):
    def handle(self):
        # begin handle [GC_SKILL_SWITCH_TYPE_SKILL] message attrs, auto generate do not change
        self.person['baseID'] = self['baseID']
        self.person['bIsOpen'] = self['bIsOpen']
        # end handle [GC_SKILL_SWITCH_TYPE_SKILL] message attrs, auto generate do not change
        pass


class GC_SYNC_HOME_HORDE_COLLECTION (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HOME_HORDE_COLLECTION] message attrs, auto generate do not change
        self.person['collectionIndex'] = self['collectionIndex']
        self.person['homeGuid'] = self['homeGuid']
        self.person['homeName'] = self['homeName']
        self.person['regionIndex'] = self['regionIndex']
        self.person['hordeIndex'] = self['hordeIndex']
        self.person['homeIndex'] = self['homeIndex']
        # end handle [GC_SYNC_HOME_HORDE_COLLECTION] message attrs, auto generate do not change
        pass


class CG_GUILD_ALLIANCE_APPLY (Packet):
    pass


class GC_RET_COPYSCENE_REWARD (Packet):
    def handle(self):
        # begin handle [GC_RET_COPYSCENE_REWARD] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        # end handle [GC_RET_COPYSCENE_REWARD] message attrs, auto generate do not change
        pass


class GC_DIG_TREASURE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_DIG_TREASURE_RESULT] message attrs, auto generate do not change
        self.person['nResult'] = self['nResult']
        self.person['actionCode'] = self['actionCode']
        self.person['modelId'] = self['modelId']
        # end handle [GC_DIG_TREASURE_RESULT] message attrs, auto generate do not change
        pass


class CG_PLAYER_LEVELUP_MANUAL (Packet):
    pass


class GC_SYC_CUSTOMHEAD_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYC_CUSTOMHEAD_INFO] message attrs, auto generate do not change
        self.person['customHeadPic'] = self['customHeadPic']
        self.person['serviceType'] = self['serviceType']
        self.person['openLv'] = self['openLv']
        self.person['uploadPicUrl'] = self['uploadPicUrl']
        self.person['viewPicUrl'] = self['viewPicUrl']
        # end handle [GC_SYC_CUSTOMHEAD_INFO] message attrs, auto generate do not change
        pass


class GC_UPDATE_FRIEND_OR_RECENTCONTACT_LIST (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_FRIEND_OR_RECENTCONTACT_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Combat'] = self['Combat']
        self.person['State'] = self['State']
        self.person['TimeInfo'] = self['TimeInfo']
        self.person['RelationPoint'] = self['RelationPoint']
        self.person['LittleHeadPicName'] = self['LittleHeadPicName']
        self.person['MediumHeadPicName'] = self['MediumHeadPicName']
        self.person['LargeHeadPicName'] = self['LargeHeadPicName']
        self.person['VoiceSignName'] = self['VoiceSignName']
        self.person['TextSign'] = self['TextSign']
        self.person['Sex'] = self['Sex']
        self.person['Birthday'] = self['Birthday']
        self.person['PersonalLocation'] = self['PersonalLocation']
        self.person['reserved'] = self['reserved']
        self.person['DelFriendTime'] = self['DelFriendTime']
        self.person['BodyId'] = self['BodyId']
        self.person['FaceId'] = self['FaceId']
        self.person['WeaponId'] = self['WeaponId']
        self.person['PlayerSex'] = self['PlayerSex']
        self.person['updatesocialtype'] = self['updatesocialtype']
        self.person['WeaponRefineVisual'] = self['WeaponRefineVisual']
        self.person['HairId'] = self['HairId']
        self.person['rewardstatus'] = self['rewardstatus']
        self.person['loverName'] = self['loverName']
        self.person['loverGuid'] = self['loverGuid']
        self.person['ArmyId'] = self['ArmyId']
        self.person['TeamId'] = self['TeamId']
        self.person['haveHuiliuIdentity'] = self['haveHuiliuIdentity']
        self.person['TowerFloor'] = self['TowerFloor']
        self.person['TowerTime'] = self['TowerTime']
        self.person['AddDatas'] = self['AddDatas']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        self.person['remakeName'] = self['remakeName']
        self.person['haveFestivalHuiliuIdentity'] = self['haveFestivalHuiliuIdentity']
        self.person['haveNewPlayerCatch'] = self['haveNewPlayerCatch']
        # end handle [GC_UPDATE_FRIEND_OR_RECENTCONTACT_LIST] message attrs, auto generate do not change
        pass


class GC_STALL_RETFAVORITE (Packet):
    def handle(self):
        # begin handle [GC_STALL_RETFAVORITE] message attrs, auto generate do not change
        self.person['stallguid'] = self['stallguid']
        self.person['optype'] = self['optype']
        self.person['sellpoint'] = self['sellpoint']
        # end handle [GC_STALL_RETFAVORITE] message attrs, auto generate do not change
        pass


class CG_SERVANT_REQADDEXP (Packet):
    pass


class CG_REQ_TEAM_CHANGE_LEADER (Packet):
    pass


class GC_SYNC_LIFESKILL_LEVEL (Packet):
    def handle(self):
        # begin handle [GC_SYNC_LIFESKILL_LEVEL] message attrs, auto generate do not change
        self.person['FishingLevel'] = self['FishingLevel']
        self.person['HerbGatheringLevel'] = self['HerbGatheringLevel']
        self.person['ProductDrugLevel'] = self['ProductDrugLevel']
        self.person['CookingLevel'] = self['CookingLevel']
        self.person['LuckyLevel'] = self['LuckyLevel']
        self.person['HealthLevel'] = self['HealthLevel']
        self.person['gatherlist'] = self['gatherlist']
        self.person['TodayGatherCount'] = self['TodayGatherCount']
        self.person['TodayMakeCount'] = self['TodayMakeCount']
        self.person['TodayAlchemyCount'] = self['TodayAlchemyCount']
        # end handle [GC_SYNC_LIFESKILL_LEVEL] message attrs, auto generate do not change
        pass


class CG_XIANDAN_EQUIP (Packet):
    pass


class GC_RET_QUIT_GUILD_REALTIME_VOICE_ROOM (Packet):
    def handle(self):
        # begin handle [GC_RET_QUIT_GUILD_REALTIME_VOICE_ROOM] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['roomId'] = self['roomId']
        self.person['isLeaveGuild'] = self['isLeaveGuild']
        # end handle [GC_RET_QUIT_GUILD_REALTIME_VOICE_ROOM] message attrs, auto generate do not change
        pass


class CG_GUILD_WORSHIP_OVER (Packet):
    pass


class GC_JOIN_TEAM_APPLICANT_INFO (Packet):
    def handle(self):
        # begin handle [GC_JOIN_TEAM_APPLICANT_INFO] message attrs, auto generate do not change
        self.person['armyID'] = self['armyID']
        self.person['teamID'] = self['teamID']
        self.person['isjoin'] = self['isjoin']
        # end handle [GC_JOIN_TEAM_APPLICANT_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_CENTERCONTROL_OPERATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CENTERCONTROL_OPERATE] message attrs, auto generate do not change
        self.person['Type'] = self['Type']
        self.person['TraceId'] = self['TraceId']
        self.person['Message'] = self['Message']
        # end handle [GC_SYNC_CENTERCONTROL_OPERATE] message attrs, auto generate do not change
        pass


class CG_EQUIP_ITEM (Packet):
    pass


class GC_RET_NATIONALDAY_TRIBUTE_STATE (Packet):
    def handle(self):
        # begin handle [GC_RET_NATIONALDAY_TRIBUTE_STATE] message attrs, auto generate do not change
        self.person['curHandInTime'] = self['curHandInTime']
        self.person['progRewardGainedList'] = self['progRewardGainedList']
        self.person['curProgressValue'] = self['curProgressValue']
        self.person['isLogin'] = self['isLogin']
        # end handle [GC_RET_NATIONALDAY_TRIBUTE_STATE] message attrs, auto generate do not change
        pass


class CG_JUBAOPLAYER (Packet):
    pass


class CG_TITLE_UNEQUIP (Packet):
    pass


class GC_STALL_REVIEW_SYNC (Packet):
    def handle(self):
        # begin handle [GC_STALL_REVIEW_SYNC] message attrs, auto generate do not change
        self.person['StallGuid'] = self['StallGuid']
        self.person['StallState'] = self['StallState']
        self.person['SellItemId'] = self['SellItemId']
        self.person['SellFellowId'] = self['SellFellowId']
        self.person['SellCount'] = self['SellCount']
        self.person['ReviewMoney'] = self['ReviewMoney']
        self.person['StallTime'] = self['StallTime']
        self.person['IsGold'] = self['IsGold']
        self.person['Tax'] = self['Tax']
        # end handle [GC_STALL_REVIEW_SYNC] message attrs, auto generate do not change
        pass


class GC_EQUIP_RECOIN_RET (Packet):
    def handle(self):
        # begin handle [GC_EQUIP_RECOIN_RET] message attrs, auto generate do not change
        self.person['equipguid'] = self['equipguid']
        self.person['AttrId'] = self['AttrId']
        self.person['AttrVal'] = self['AttrVal']
        self.person['AttrType'] = self['AttrType']
        self.person['AttrIdx'] = self['AttrIdx']
        # end handle [GC_EQUIP_RECOIN_RET] message attrs, auto generate do not change
        pass


class CG_REQ_PK_DEATHAID (Packet):
    pass


class CG_STATICSYSTEMSHOP_BUYBACK (Packet):
    pass


class GC_UPDATEFRIEND_POINTVALUE (Packet):
    def handle(self):
        # begin handle [GC_UPDATEFRIEND_POINTVALUE] message attrs, auto generate do not change
        self.person['friendGuid'] = self['friendGuid']
        self.person['friendname'] = self['friendname']
        self.person['curFriendPoint'] = self['curFriendPoint']
        self.person['addtype'] = self['addtype']
        # end handle [GC_UPDATEFRIEND_POINTVALUE] message attrs, auto generate do not change
        pass


class GC_UPDATE_FOLLOWSTATE (Packet):
    def handle(self):
        # begin handle [GC_UPDATE_FOLLOWSTATE] message attrs, auto generate do not change
        self.person['ObjID'] = self['ObjID']
        self.person['FollowState'] = self['FollowState']
        self.person['LastFollowState'] = self['LastFollowState']
        # end handle [GC_UPDATE_FOLLOWSTATE] message attrs, auto generate do not change
        pass


class CG_IOS_REVIEW_GUILD_COMPLETED (Packet):
    pass


class CG_REQ_HOME_FITMENT (Packet):
    pass


class GC_ASURA_ENROLL (Packet):
    def handle(self):
        # begin handle [GC_ASURA_ENROLL] message attrs, auto generate do not change
        self.person['enrolled'] = self['enrolled']
        # end handle [GC_ASURA_ENROLL] message attrs, auto generate do not change
        pass


class CG_APPLY_SHOWROOM (Packet):
    pass


class GC_GUILD_RET_PRESERVE_LIST (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_PRESERVE_LIST] message attrs, auto generate do not change
        self.person['preserveGuildGuid'] = self['preserveGuildGuid']
        # end handle [GC_GUILD_RET_PRESERVE_LIST] message attrs, auto generate do not change
        pass


class CG_REQ_YUANLINGNPC_POS (Packet):
    pass


class GC_SYNC_WEEKSCARD_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_WEEKSCARD_STATE] message attrs, auto generate do not change
        self.person['state'] = self['state']
        # end handle [GC_SYNC_WEEKSCARD_STATE] message attrs, auto generate do not change
        pass


class GC_MAKE_SECOND_INTERACT (Packet):
    def handle(self):
        # begin handle [GC_MAKE_SECOND_INTERACT] message attrs, auto generate do not change
        self.person['inviterServerID'] = self['inviterServerID']
        self.person['inviteeServerID'] = self['inviteeServerID']
        self.person['interactType'] = self['interactType']
        # end handle [GC_MAKE_SECOND_INTERACT] message attrs, auto generate do not change
        pass


class CG_BWPP_GOTOBIGWORLD (Packet):
    pass


class CG_REQ_EQUIP_REBIRTH_INFO (Packet):
    pass


class GC_YAOSHOU_CHANGE_TRIGER_GUIDE (Packet):
    def handle(self):
        # begin handle [GC_YAOSHOU_CHANGE_TRIGER_GUIDE] message attrs, auto generate do not change
        # end handle [GC_YAOSHOU_CHANGE_TRIGER_GUIDE] message attrs, auto generate do not change
        pass


class CG_OPEN_LUCKYEGG (Packet):
    pass


class GC_EQUIP_REBIRTH_RESULT (Packet):
    def handle(self):
        # begin handle [GC_EQUIP_REBIRTH_RESULT] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['nSlotType'] = self['nSlotType']
        self.person['nRebirthLevel'] = self['nRebirthLevel']
        self.person['nOldResonanceLevel'] = self['nOldResonanceLevel']
        self.person['nNewResonanceLevel'] = self['nNewResonanceLevel']
        # end handle [GC_EQUIP_REBIRTH_RESULT] message attrs, auto generate do not change
        pass


class GC_UPGRADE_PRACTICE_RESPONSE (Packet):
    def handle(self):
        # begin handle [GC_UPGRADE_PRACTICE_RESPONSE] message attrs, auto generate do not change
        self.person['nPracticeId'] = self['nPracticeId']
        self.person['nPracticeLevel'] = self['nPracticeLevel']
        # end handle [GC_UPGRADE_PRACTICE_RESPONSE] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_KICK (Packet):
    pass


class CG_NATIONALDAY_TRIBUTE_GET_REWARD (Packet):
    pass


class GC_TOURNAMENT_SYNC_MATCH_INFO (Packet):
    def handle(self):
        # begin handle [GC_TOURNAMENT_SYNC_MATCH_INFO] message attrs, auto generate do not change
        self.person['matchStatus'] = self['matchStatus']
        self.person['memberInfo'] = self['memberInfo']
        # end handle [GC_TOURNAMENT_SYNC_MATCH_INFO] message attrs, auto generate do not change
        pass


class CG_GUILDFIGHT_WORLDBOSS_PICKUP_SOUL (Packet):
    pass


class CG_GUILD_ROBBERS_RANK (Packet):
    pass


class CG_ASK_BACK_AWARD (Packet):
    pass


class GC_FASHION_COLOR (Packet):
    def handle(self):
        # begin handle [GC_FASHION_COLOR] message attrs, auto generate do not change
        self.person['FashionId'] = self['FashionId']
        self.person['FashionInfo'] = self['FashionInfo']
        # end handle [GC_FASHION_COLOR] message attrs, auto generate do not change
        pass


class CG_REQ_PHOTORANDOM_SHARE_DATA (Packet):
    pass


class GC_WATERMELON_SYNC_PLAY_COUNT (Packet):
    def handle(self):
        # begin handle [GC_WATERMELON_SYNC_PLAY_COUNT] message attrs, auto generate do not change
        self.person['playCount'] = self['playCount']
        # end handle [GC_WATERMELON_SYNC_PLAY_COUNT] message attrs, auto generate do not change
        pass


class GC_ASURA_ASK_ENROLL (Packet):
    def handle(self):
        # begin handle [GC_ASURA_ASK_ENROLL] message attrs, auto generate do not change
        self.person['param'] = self['param']
        # end handle [GC_ASURA_ASK_ENROLL] message attrs, auto generate do not change
        pass


class GC_SHOW_TAIL_PAK (Packet):
    def handle(self):
        # begin handle [GC_SHOW_TAIL_PAK] message attrs, auto generate do not change
        self.person['showtail'] = self['showtail']
        # end handle [GC_SHOW_TAIL_PAK] message attrs, auto generate do not change
        pass


class CG_GUILD_WAR_REFUSE_SIGN_UP (Packet):
    pass


class CG_AUCTION_UPDATA_UISTATE (Packet):
    pass


class CG_GODWEAPON_CONCRETE (Packet):
    pass


class GC_GUILDWAR_UPDATE_STATE (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_UPDATE_STATE] message attrs, auto generate do not change
        self.person['State'] = self['State']
        # end handle [GC_GUILDWAR_UPDATE_STATE] message attrs, auto generate do not change
        pass


class GC_TEAM_SYNC_APPLICANTINFO (Packet):
    def handle(self):
        # begin handle [GC_TEAM_SYNC_APPLICANTINFO] message attrs, auto generate do not change
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberProf'] = self['memberProf']
        self.person['memberSex'] = self['memberSex']
        self.person['memberBodyId'] = self['memberBodyId']
        self.person['memberFaceId'] = self['memberFaceId']
        self.person['memberWeaponId'] = self['memberWeaponId']
        self.person['memberWeaponRefineVisual'] = self['memberWeaponRefineVisual']
        self.person['memberHairId'] = self['memberHairId']
        self.person['memberBodyColorVisual'] = self['memberBodyColorVisual']
        self.person['memberBodyFashionId'] = self['memberBodyFashionId']
        self.person['memberBodyColorIndex'] = self['memberBodyColorIndex']
        self.person['memberHairFashionId'] = self['memberHairFashionId']
        self.person['memberHairColorIndex'] = self['memberHairColorIndex']
        self.person['memberWeaponFashionId'] = self['memberWeaponFashionId']
        self.person['memberWeaponColorIndex'] = self['memberWeaponColorIndex']
        self.person['memberProfCamp'] = self['memberProfCamp']
        self.person['memberCombatValue'] = self['memberCombatValue']
        self.person['memberHaveHuiliuIdentity'] = self['memberHaveHuiliuIdentity']
        self.person['memberBodyUseFreedomDyeColorIndex'] = self['memberBodyUseFreedomDyeColorIndex']
        self.person['memberHairUseFreedomDyeColorIndex'] = self['memberHairUseFreedomDyeColorIndex']
        self.person['BodyFreeDyeColorInfos'] = self['BodyFreeDyeColorInfos']
        self.person['HairFreeDyeColorInfos'] = self['HairFreeDyeColorInfos']
        self.person['memberHaveFestivalHuiliuIdentity'] = self['memberHaveFestivalHuiliuIdentity']
        # end handle [GC_TEAM_SYNC_APPLICANTINFO] message attrs, auto generate do not change
        pass


class CG_FLY_FASTSPEED (Packet):
    pass


class CG_SPOKESMAN_ANSWER_DIALOGUE (Packet):
    pass


class CG_ORIENTATION_CHANGE (Packet):
    pass


class GC_DELETE_OBJ (Packet):
    def handle(self):
        # begin handle [GC_DELETE_OBJ] message attrs, auto generate do not change
        self.person['serverId'] = self['serverId']
        # end handle [GC_DELETE_OBJ] message attrs, auto generate do not change
        pass


class GC_SYNC_PHOTORANDOM_SHARE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PHOTORANDOM_SHARE_DATA] message attrs, auto generate do not change
        self.person['nDrawAccDayRewardList'] = self['nDrawAccDayRewardList']
        self.person['bAlreadyShareToday'] = self['bAlreadyShareToday']
        self.person['nAccDay'] = self['nAccDay']
        # end handle [GC_SYNC_PHOTORANDOM_SHARE_DATA] message attrs, auto generate do not change
        pass


class GC_HONGBAO_RET_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_HONGBAO_RET_UPDATE] message attrs, auto generate do not change
        self.person['Guid'] = self['Guid']
        self.person['SenderGuid'] = self['SenderGuid']
        self.person['strSenderName'] = self['strSenderName']
        self.person['nSenderProfession'] = self['nSenderProfession']
        self.person['strDesc'] = self['strDesc']
        self.person['nType'] = self['nType']
        self.person['nChannel'] = self['nChannel']
        self.person['nMaxCount'] = self['nMaxCount']
        self.person['nMoneyType'] = self['nMoneyType']
        self.person['nMoney'] = self['nMoney']
        self.person['RobberData'] = self['RobberData']
        self.person['nSenderSex'] = self['nSenderSex']
        self.person['nCoverId'] = self['nCoverId']
        # end handle [GC_HONGBAO_RET_UPDATE] message attrs, auto generate do not change
        pass


class GC_RET_HOME_HORDE_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_HOME_HORDE_INFO] message attrs, auto generate do not change
        self.person['RegionIndex'] = self['RegionIndex']
        self.person['HordeIndex'] = self['HordeIndex']
        self.person['HomeIndex'] = self['HomeIndex']
        self.person['HomeGuid'] = self['HomeGuid']
        self.person['HomeLevel'] = self['HomeLevel']
        self.person['LeaderGuid'] = self['LeaderGuid']
        # end handle [GC_RET_HOME_HORDE_INFO] message attrs, auto generate do not change
        pass


class CG_DELAPPLYLIST (Packet):
    pass


class CG_AUTOTEAM_OVERTIME_REQUEST_RESULT (Packet):
    pass


class GC_RET_TEAMPLATFORMINFO (Packet):
    def handle(self):
        # begin handle [GC_RET_TEAMPLATFORMINFO] message attrs, auto generate do not change
        self.person['teamID'] = self['teamID']
        self.person['leaderGuid'] = self['leaderGuid']
        self.person['leaderName'] = self['leaderName']
        self.person['leaderLevel'] = self['leaderLevel']
        self.person['leaderProf'] = self['leaderProf']
        self.person['targetId'] = self['targetId']
        self.person['memberCount'] = self['memberCount']
        self.person['memberProf'] = self['memberProf']
        self.person['memberLevel'] = self['memberLevel']
        self.person['leaderSceneid'] = self['leaderSceneid']
        self.person['leaderSex'] = self['leaderSex']
        self.person['bArmyInfo'] = self['bArmyInfo']
        self.person['mercenaryNum'] = self['mercenaryNum']
        self.person['merProf'] = self['merProf']
        self.person['merLevel'] = self['merLevel']
        self.person['binapplicantlist'] = self['binapplicantlist']
        # end handle [GC_RET_TEAMPLATFORMINFO] message attrs, auto generate do not change
        pass


class CG_GODWEAPON_BASE_LEVALUP (Packet):
    pass


class GC_AUCTION_SYNC (Packet):
    def handle(self):
        # begin handle [GC_AUCTION_SYNC] message attrs, auto generate do not change
        self.person['cursellcount'] = self['cursellcount']
        self.person['maxsellcount'] = self['maxsellcount']
        # end handle [GC_AUCTION_SYNC] message attrs, auto generate do not change
        pass


class GC_REQ_ADD_HOMEGUEST (Packet):
    def handle(self):
        # begin handle [GC_REQ_ADD_HOMEGUEST] message attrs, auto generate do not change
        self.person['m_LandlordHomeGuid'] = self['m_LandlordHomeGuid']
        self.person['m_RequirerGuid'] = self['m_RequirerGuid']
        self.person['m_RequirerName'] = self['m_RequirerName']
        # end handle [GC_REQ_ADD_HOMEGUEST] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_DELBLACKLIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        # end handle [GC_DELBLACKLIST] message attrs, auto generate do not change
        pass


class GC_GUILDBANGHUA_RESULT (Packet):
    def handle(self):
        # begin handle [GC_GUILDBANGHUA_RESULT] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['Score'] = self['Score']
        self.person['Time'] = self['Time']
        self.person['ParamEx'] = self['ParamEx']
        self.person['GuildMoney'] = self['GuildMoney']
        self.person['GoldCoin'] = self['GoldCoin']
        self.person['SilverCoin'] = self['SilverCoin']
        self.person['RewardItemId'] = self['RewardItemId']
        self.person['RewardItemCount'] = self['RewardItemCount']
        # end handle [GC_GUILDBANGHUA_RESULT] message attrs, auto generate do not change
        pass


class GC_VOICE_OVER (Packet):
    def handle(self):
        # begin handle [GC_VOICE_OVER] message attrs, auto generate do not change
        self.person['voiceOverID'] = self['voiceOverID']
        # end handle [GC_VOICE_OVER] message attrs, auto generate do not change
        pass


class GC_RET_GUILD_MONSTER_DATA (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILD_MONSTER_DATA] message attrs, auto generate do not change
        self.person['guildMonsterScore'] = self['guildMonsterScore']
        self.person['selfMonsterScore'] = self['selfMonsterScore']
        # end handle [GC_RET_GUILD_MONSTER_DATA] message attrs, auto generate do not change
        pass


class GC_OPERATE_GEM_RET (Packet):
    def handle(self):
        # begin handle [GC_OPERATE_GEM_RET] message attrs, auto generate do not change
        self.person['operateType'] = self['operateType']
        # end handle [GC_OPERATE_GEM_RET] message attrs, auto generate do not change
        pass


class GC_GUILD_RET_LEVELUP (Packet):
    def handle(self):
        # begin handle [GC_GUILD_RET_LEVELUP] message attrs, auto generate do not change
        self.person['level'] = self['level']
        self.person['guildBuildingLeftTime'] = self['guildBuildingLeftTime']
        # end handle [GC_GUILD_RET_LEVELUP] message attrs, auto generate do not change
        pass


class GC_SYNC_ORIGINALTOREAL_WORLDID (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ORIGINALTOREAL_WORLDID] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['OriginalToRealDatas'] = self['OriginalToRealDatas']
        # end handle [GC_SYNC_ORIGINALTOREAL_WORLDID] message attrs, auto generate do not change
        pass


class CG_REQ_REGION_HOME_NUM (Packet):
    pass


class GC_SYNC_STARMAP_ALL_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_STARMAP_ALL_INFO] message attrs, auto generate do not change
        self.person['nStarMapId'] = self['nStarMapId']
        self.person['nEyesStarId'] = self['nEyesStarId']
        self.person['nNowHaveEyesStarTimes'] = self['nNowHaveEyesStarTimes']
        self.person['nNowUsedEyesStarTimes'] = self['nNowUsedEyesStarTimes']
        self.person['nStarId'] = self['nStarId']
        self.person['nStarZhiWeiValue'] = self['nStarZhiWeiValue']
        self.person['nStarState'] = self['nStarState']
        self.person['nResultEyesStarId'] = self['nResultEyesStarId']
        self.person['isResultSuccess'] = self['isResultSuccess']
        self.person['activitystarttime'] = self['activitystarttime']
        self.person['activityendtime'] = self['activityendtime']
        self.person['isActivityOpen'] = self['isActivityOpen']
        self.person['isstartentimes'] = self['isstartentimes']
        # end handle [GC_SYNC_STARMAP_ALL_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_BIGBATTLE_STATUS (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BIGBATTLE_STATUS] message attrs, auto generate do not change
        self.person['playerName'] = self['playerName']
        self.person['playerGuid'] = self['playerGuid']
        self.person['playerId'] = self['playerId']
        self.person['playerScore'] = self['playerScore']
        self.person['rewardItemId'] = self['rewardItemId']
        self.person['rewardItemCount'] = self['rewardItemCount']
        self.person['syncMode'] = self['syncMode']
        # end handle [GC_SYNC_BIGBATTLE_STATUS] message attrs, auto generate do not change
        pass


class CG_REQ_TEACHER (Packet):
    pass


class CG_REQ_ARTIFACT_EXCHANGE (Packet):
    pass


class GC_PUBLISH_MENTOR_MESSAGE (Packet):
    def handle(self):
        # begin handle [GC_PUBLISH_MENTOR_MESSAGE] message attrs, auto generate do not change
        self.person['info'] = self['info']
        # end handle [GC_PUBLISH_MENTOR_MESSAGE] message attrs, auto generate do not change
        pass


class CG_GUILD_JOIN_OTHERPLAYER (Packet):
    pass


class CG_BIGBATTLE_PICKITEM (Packet):
    pass


class GC_ACCRECHARGE_RESPONSE_DATA (Packet):
    def handle(self):
        # begin handle [GC_ACCRECHARGE_RESPONSE_DATA] message attrs, auto generate do not change
        self.person['open'] = self['open']
        self.person['amt'] = self['amt']
        self.person['step'] = self['step']
        self.person['ranklist'] = self['ranklist']
        self.person['refresh'] = self['refresh']
        self.person['assignindex'] = self['assignindex']
        # end handle [GC_ACCRECHARGE_RESPONSE_DATA] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_AID_RESOPNSE_CONFIG] message attrs, auto generate do not change
        self.person['name'] = self['name']
        self.person['guid'] = self['guid']
        self.person['misID'] = self['misID']
        self.person['misName'] = self['misName']
        self.person['memname'] = self['memname']
        self.person['memguid'] = self['memguid']
        # end handle [GC_AID_RESOPNSE_CONFIG] message attrs, auto generate do not change
        pass


class GC_PLAY_LIGHTNING_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_PLAY_LIGHTNING_EFFECT] message attrs, auto generate do not change
        self.person['LightingEffectId'] = self['LightingEffectId']
        self.person['OwnCharServerID'] = self['OwnCharServerID']
        self.person['TargetCharServerId'] = self['TargetCharServerId']
        self.person['connecntPoint'] = self['connecntPoint']
        # end handle [GC_PLAY_LIGHTNING_EFFECT] message attrs, auto generate do not change
        pass


class CG_LOCK_CURTITLE (Packet):
    pass


class GC_REBATE_RANKDATA (Packet):
    def handle(self):
        # begin handle [GC_REBATE_RANKDATA] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['curPage'] = self['curPage']
        self.person['totalPage'] = self['totalPage']
        self.person['rankvalue'] = self['rankvalue']
        self.person['guid'] = self['guid']
        self.person['name'] = self['name']
        self.person['myrank'] = self['myrank']
        # end handle [GC_REBATE_RANKDATA] message attrs, auto generate do not change
        pass


class CG_REQ_MENTOR_RECURIT (Packet):
    pass


class GC_GUILDWAR_SYNC_SIGNUPMEMBER_COUNT (Packet):
    def handle(self):
        # begin handle [GC_GUILDWAR_SYNC_SIGNUPMEMBER_COUNT] message attrs, auto generate do not change
        self.person['nCount'] = self['nCount']
        # end handle [GC_GUILDWAR_SYNC_SIGNUPMEMBER_COUNT] message attrs, auto generate do not change
        pass


class GC_FASHION_COLOR_CHANGE (Packet):
    def handle(self):
        # begin handle [GC_FASHION_COLOR_CHANGE] message attrs, auto generate do not change
        self.person['FashionId'] = self['FashionId']
        self.person['CurColor'] = self['CurColor']
        # end handle [GC_FASHION_COLOR_CHANGE] message attrs, auto generate do not change
        pass


class GC_MAIL_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_MAIL_UPDATE] message attrs, auto generate do not change
        self.person['MailGuid'] = self['MailGuid']
        self.person['MailType'] = self['MailType']
        self.person['WriterGuid'] = self['WriterGuid']
        self.person['WriterName'] = self['WriterName']
        self.person['WriteTime'] = self['WriteTime']
        self.person['ReaderGuid'] = self['ReaderGuid']
        self.person['ReadTime'] = self['ReadTime']
        self.person['Content'] = self['Content']
        self.person['Sliver'] = self['Sliver']
        self.person['Gold'] = self['Gold']
        self.person['Yuanbao'] = self['Yuanbao']
        self.person['BindYB'] = self['BindYB']
        self.person['Origin'] = self['Origin']
        self.person['AttachedItem'] = self['AttachedItem']
        self.person['AttachedFairy'] = self['AttachedFairy']
        self.person['YuanBaoSilver'] = self['YuanBaoSilver']
        self.person['IsAttachmentAccepted'] = self['IsAttachmentAccepted']
        # end handle [GC_MAIL_UPDATE] message attrs, auto generate do not change
        pass


class CG_ACTIVITY_BUYBACK_BUY (Packet):
    pass


class CG_RELEASE_FAIRY (Packet):
    pass


class CG_LEARN_FAIRY_SKILL (Packet):
    pass


class GC_COPYSCENE_INVITE (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_INVITE] message attrs, auto generate do not change
        self.person['SceneID'] = self['SceneID']
        self.person['Invitor'] = self['Invitor']
        self.person['Tier'] = self['Tier']
        self.person['InvitorGuid'] = self['InvitorGuid']
        # end handle [GC_COPYSCENE_INVITE] message attrs, auto generate do not change
        pass


class CG_WEDDING_JOIN (Packet):
    pass


class GC_EQUIPMIRROR_FORGE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_EQUIPMIRROR_FORGE_RESULT] message attrs, auto generate do not change
        self.person['mirrorguid'] = self['mirrorguid']
        self.person['mirrorForgeLevel'] = self['mirrorForgeLevel']
        # end handle [GC_EQUIPMIRROR_FORGE_RESULT] message attrs, auto generate do not change
        pass


class GC_SYNC_USER_CHRISTMAS_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_USER_CHRISTMAS_DATA] message attrs, auto generate do not change
        self.person['activityId'] = self['activityId']
        # end handle [GC_SYNC_USER_CHRISTMAS_DATA] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_GUILD_RET_QUICKJOIN] message attrs, auto generate do not change
        self.person['guildGuid'] = self['guildGuid']
        self.person['guildShortNameColor'] = self['guildShortNameColor']
        self.person['guildShortName'] = self['guildShortName']
        # end handle [GC_GUILD_RET_QUICKJOIN] message attrs, auto generate do not change
        pass


class CG_EXAM_SELECTCATEGORY (Packet):
    pass


class GC_ITEMPACK_RESIZE (Packet):
    def handle(self):
        # begin handle [GC_ITEMPACK_RESIZE] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['size'] = self['size']
        self.person['packtype'] = self['packtype']
        self.person['unlockindex'] = self['unlockindex']
        # end handle [GC_ITEMPACK_RESIZE] message attrs, auto generate do not change
        pass


class GC_DOMAINWAR_LINEINFO (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_LINEINFO] message attrs, auto generate do not change
        self.person['domainId'] = self['domainId']
        self.person['szEnermyName'] = self['szEnermyName']
        self.person['lineinfo'] = self['lineinfo']
        # end handle [GC_DOMAINWAR_LINEINFO] message attrs, auto generate do not change
        pass


class CG_GUILDMONSTER_ACTIVE (Packet):
    pass


class GC_RET_YLTX_SCENELIST (Packet):
    def handle(self):
        # begin handle [GC_RET_YLTX_SCENELIST] message attrs, auto generate do not change
        self.person['result'] = self['result']
        self.person['sceneListInfos'] = self['sceneListInfos']
        # end handle [GC_RET_YLTX_SCENELIST] message attrs, auto generate do not change
        pass


class CG_EQUIP_RECOIN (Packet):
    pass


class GC_ASK_FISH_RET (Packet):
    def handle(self):
        # begin handle [GC_ASK_FISH_RET] message attrs, auto generate do not change
        self.person['fishid'] = self['fishid']
        self.person['issucc'] = self['issucc']
        self.person['type'] = self['type']
        self.person['isfinish'] = self['isfinish']
        # end handle [GC_ASK_FISH_RET] message attrs, auto generate do not change
        pass


class CG_ACCPET_GROWWAY_REWARD (Packet):
    pass


class GC_MULPVP_CACEL (Packet):
    def handle(self):
        # begin handle [GC_MULPVP_CACEL] message attrs, auto generate do not change
        # end handle [GC_MULPVP_CACEL] message attrs, auto generate do not change
        pass


class GC_TIANSHU_PACK (Packet):
    def handle(self):
        # begin handle [GC_TIANSHU_PACK] message attrs, auto generate do not change
        self.person['dataId'] = self['dataId']
        # end handle [GC_TIANSHU_PACK] message attrs, auto generate do not change
        pass


class CG_REQ_EQUIP_REBIRTH_RECASE (Packet):
    pass


class GC_RET_ELITENPCCREATECD (Packet):
    def handle(self):
        # begin handle [GC_RET_ELITENPCCREATECD] message attrs, auto generate do not change
        self.person['NpcSceneInsId'] = self['NpcSceneInsId']
        self.person['NpcDataId'] = self['NpcDataId']
        self.person['NpcCDTime'] = self['NpcCDTime']
        # end handle [GC_RET_ELITENPCCREATECD] message attrs, auto generate do not change
        pass


class GC_REQ_SWITCH_PET_FIGHT_STATE (Packet):
    def handle(self):
        # begin handle [GC_REQ_SWITCH_PET_FIGHT_STATE] message attrs, auto generate do not change
        self.person['stateIndex'] = self['stateIndex']
        # end handle [GC_REQ_SWITCH_PET_FIGHT_STATE] message attrs, auto generate do not change
        pass


class CG_SWORDTEAM_JOB_CHANGE (Packet):
    pass


class CG_GUILD_LEAVE (Packet):
    pass


class GC_RET_BOUNTY_CHANGE_SCENE (Packet):
    def handle(self):
        # begin handle [GC_RET_BOUNTY_CHANGE_SCENE] message attrs, auto generate do not change
        self.person['sceneClassID'] = self['sceneClassID']
        self.person['sceneInstID'] = self['sceneInstID']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        # end handle [GC_RET_BOUNTY_CHANGE_SCENE] message attrs, auto generate do not change
        pass


class CG_TOWER_SWEEP (Packet):
    pass


class GC_SYNC_AIRWALL_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_AIRWALL_INFO] message attrs, auto generate do not change
        self.person['nAirWallIds'] = self['nAirWallIds']
        # end handle [GC_SYNC_AIRWALL_INFO] message attrs, auto generate do not change
        pass


class GC_SYN_ATTR (Packet):
    def handle(self):
        # begin handle [GC_SYN_ATTR] message attrs, auto generate do not change
        self.person['ObjId'] = self['ObjId']
        self.person['CurHp'] = self['CurHp']
        self.person['CurMp'] = self['CurMp']
        self.person['CurXp'] = self['CurXp']
        self.person['MaxHP'] = self['MaxHP']
        self.person['MaxMP'] = self['MaxMP']
        self.person['MaxXP'] = self['MaxXP']
        self.person['MaxAutoLevel'] = self['MaxAutoLevel']
        self.person['CurExp'] = self['CurExp']
        self.person['CurSilverCoin'] = self['CurSilverCoin']
        self.person['CurGoldCoin'] = self['CurGoldCoin']
        self.person['CurYuanBao'] = self['CurYuanBao']
        self.person['CurYuanBaoSilver'] = self['CurYuanBaoSilver']
        self.person['combatvalue'] = self['combatvalue']
        self.person['skillSoul'] = self['skillSoul']
        self.person['skillWashFreeTimes'] = self['skillWashFreeTimes']
        self.person['DebtSilverCoin'] = self['DebtSilverCoin']
        self.person['DebtGoldCoin'] = self['DebtGoldCoin']
        self.person['DebtYuanBao'] = self['DebtYuanBao']
        self.person['DebtYuanBaoSilver'] = self['DebtYuanBaoSilver']
        self.person['skillLayer'] = self['skillLayer']
        self.person['PKProtectMode'] = self['PKProtectMode']
        self.person['PrayExp_Activity'] = self['PrayExp_Activity']
        self.person['isOldAccountPlayer'] = self['isOldAccountPlayer']
        self.person['isHaveOldAccountBonus'] = self['isHaveOldAccountBonus']
        self.person['isPvPAudience'] = self['isPvPAudience']
        self.person['EnergyValue'] = self['EnergyValue']
        self.person['HPStore'] = self['HPStore']
        self.person['MPStore'] = self['MPStore']
        self.person['GuildContribute'] = self['GuildContribute']
        self.person['PkValue_OrgBak'] = self['PkValue_OrgBak']
        self.person['CurEnergyForFastFly'] = self['CurEnergyForFastFly']
        self.person['SkillXiuZhenLevel'] = self['SkillXiuZhenLevel']
        self.person['CurRage'] = self['CurRage']
        self.person['SkillXiuZhenExp'] = self['SkillXiuZhenExp']
        self.person['PlayerRealHp'] = self['PlayerRealHp']
        self.person['PlayerRealPhysicalAtk'] = self['PlayerRealPhysicalAtk']
        self.person['PlayerRealMagicalAtk'] = self['PlayerRealMagicalAtk']
        self.person['HPPool'] = self['HPPool']
        self.person['MPPool'] = self['MPPool']
        self.person['XiuZhenLev'] = self['XiuZhenLev']
        self.person['SkyLayers'] = self['SkyLayers']
        self.person['CurSkillEnergyValue'] = self['CurSkillEnergyValue']
        self.person['MaxSkillEnergyValue'] = self['MaxSkillEnergyValue']
        self.person['IsWashTime'] = self['IsWashTime']
        self.person['IsXiuZhenMaxLvel'] = self['IsXiuZhenMaxLvel']
        self.person['GloryCoins'] = self['GloryCoins']
        self.person['VigorValue'] = self['VigorValue']
        self.person['CurYuanBaoVice'] = self['CurYuanBaoVice']
        self.person['DebtYuanBaoVice'] = self['DebtYuanBaoVice']
        self.person['HonorCoins'] = self['HonorCoins']
        self.person['SkillXiuZhenPoint'] = self['SkillXiuZhenPoint']
        self.person['LuckyValue'] = self['LuckyValue']
        self.person['SkillWashReturnPoint'] = self['SkillWashReturnPoint']
        self.person['QingYiValue'] = self['QingYiValue']
        self.person['AchievementPoints'] = self['AchievementPoints']
        self.person['SkillZhuanJingUseWashTimes'] = self['SkillZhuanJingUseWashTimes']
        self.person['SkillZhuanJingUseOpenTimes'] = self['SkillZhuanJingUseOpenTimes']
        self.person['IDIPBanPlayerRank'] = self['IDIPBanPlayerRank']
        self.person['IDIPBanPlayerRankContent'] = self['IDIPBanPlayerRankContent']
        self.person['InfiniteDreamLandLayer'] = self['InfiniteDreamLandLayer']
        self.person['InfiniteDreamLandRewardCount'] = self['InfiniteDreamLandRewardCount']
        self.person['XiuZhenCamp'] = self['XiuZhenCamp']
        self.person['FutuCoin'] = self['FutuCoin']
        self.person['serverLevelUnlockTimeMax'] = self['serverLevelUnlockTimeMax']
        self.person['MarriageLoverPoint'] = self['MarriageLoverPoint']
        self.person['CombatVal_Level'] = self['CombatVal_Level']
        self.person['CombatVal_Skill'] = self['CombatVal_Skill']
        self.person['CombatVal_Equip'] = self['CombatVal_Equip']
        self.person['CombatVal_Refine'] = self['CombatVal_Refine']
        self.person['CombatVal_Gem'] = self['CombatVal_Gem']
        self.person['CombatVal_Fairy'] = self['CombatVal_Fairy']
        self.person['CombatVal_Tianshu'] = self['CombatVal_Tianshu']
        self.person['CombatVal_GuildAddition'] = self['CombatVal_GuildAddition']
        self.person['CombatVal_Engrave'] = self['CombatVal_Engrave']
        self.person['CombatVal_Practice'] = self['CombatVal_Practice']
        self.person['OpenServerLevel'] = self['OpenServerLevel']
        self.person['BountyMoney'] = self['BountyMoney']
        self.person['StarCoins'] = self['StarCoins']
        self.person['CombatVal_Servant'] = self['CombatVal_Servant']
        self.person['ShowStarMapRedPoint'] = self['ShowStarMapRedPoint']
        self.person['CombatVal_Rebirth'] = self['CombatVal_Rebirth']
        self.person['ServantDust'] = self['ServantDust']
        self.person['CopysceneDifficultySelectType'] = self['CopysceneDifficultySelectType']
        self.person['CombatVal_Home'] = self['CombatVal_Home']
        self.person['BigWorldPvPCoin'] = self['BigWorldPvPCoin']
        self.person['CombatVal_RefineMeter'] = self['CombatVal_RefineMeter']
        self.person['SkillZhuanJingSkillExtendMissionFinish'] = self['SkillZhuanJingSkillExtendMissionFinish']
        self.person['CombatVal_GodWeapon'] = self['CombatVal_GodWeapon']
        self.person['InfiniteDreamLandUseItemAddRewardCount'] = self['InfiniteDreamLandUseItemAddRewardCount']
        self.person['InfiniteDreamLandUseItemMaxCount'] = self['InfiniteDreamLandUseItemMaxCount']
        self.person['CombatVal_DiMaiJingLuo'] = self['CombatVal_DiMaiJingLuo']
        self.person['ShiLianCoin'] = self['ShiLianCoin']
        self.person['SkillCDSpeedBase'] = self['SkillCDSpeedBase']
        self.person['SkillCDSpeedFix'] = self['SkillCDSpeedFix']
        self.person['CombatVal_ServantEquip'] = self['CombatVal_ServantEquip']
        self.person['CombatVal_XinPo'] = self['CombatVal_XinPo']
        self.person['CombatVal_TianXingMiQi'] = self['CombatVal_TianXingMiQi']
        self.person['COTCoin'] = self['COTCoin']
        self.person['WithereDefence'] = self['WithereDefence']
        self.person['CombatVal_Jade'] = self['CombatVal_Jade']
        # end handle [GC_SYN_ATTR] message attrs, auto generate do not change
        pass


class CG_REQ_PET_SUMMON_OR_CALLBACK (Packet):
    pass


class GC_BATTLEFIELD_MATCHINFO (Packet):
    def handle(self):
        # begin handle [GC_BATTLEFIELD_MATCHINFO] message attrs, auto generate do not change
        self.person['BFSceneClassID'] = self['BFSceneClassID']
        self.person['BFSceneInstID'] = self['BFSceneInstID']
        self.person['BFSceneOpenIstID'] = self['BFSceneOpenIstID']
        self.person['GroupID'] = self['GroupID']
        self.person['SignupID'] = self['SignupID']
        self.person['DailyLeftCount'] = self['DailyLeftCount']
        self.person['GroupAPlayerNum'] = self['GroupAPlayerNum']
        self.person['GroupBPlayerNum'] = self['GroupBPlayerNum']
        self.person['BFCreateTime'] = self['BFCreateTime']
        # end handle [GC_BATTLEFIELD_MATCHINFO] message attrs, auto generate do not change
        pass


class CG_ASK_REMOVE_INSCRIPTION (Packet):
    pass


class GC_TEST_MUTIL_VARIABLE (Packet):
    def handle(self):
        # begin handle [GC_TEST_MUTIL_VARIABLE] message attrs, auto generate do not change
        # end handle [GC_TEST_MUTIL_VARIABLE] message attrs, auto generate do not change
        pass


class GC_TP_NOTICE_ONLINE (Packet):
    def handle(self):
        # begin handle [GC_TP_NOTICE_ONLINE] message attrs, auto generate do not change
        self.person['onlineTime'] = self['onlineTime']
        # end handle [GC_TP_NOTICE_ONLINE] message attrs, auto generate do not change
        pass


class GC_TP_KICK_PLAYE (Packet):
    def handle(self):
        # begin handle [GC_TP_KICK_PLAYE] message attrs, auto generate do not change
        self.person['kickType'] = self['kickType']
        self.person['param1'] = self['param1']
        # end handle [GC_TP_KICK_PLAYE] message attrs, auto generate do not change
        pass


class CG_CHECK_GUILDSTUDIO (Packet):
    pass


class GC_CHECK_GUILDSTUDIO_RET (Packet):
    def handle(self):
        # begin handle [GC_CHECK_GUILDSTUDIO_RET] message attrs, auto generate do not change
        self.person['jointype'] = self['jointype']
        self.person['guid'] = self['guid']
        self.person['szname'] = self['szname']
        self.person['isstudio'] = self['isstudio']
        # end handle [GC_CHECK_GUILDSTUDIO_RET] message attrs, auto generate do not change
        pass


class GC_SYNC_OPEN_SERVER_ACTIVITY_TASK_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_OPEN_SERVER_ACTIVITY_TASK_INFO] message attrs, auto generate do not change
        self.person['openServerActivityTaskInfos'] = self['openServerActivityTaskInfos']
        self.person['funyActivityRewardInfos'] = self['funyActivityRewardInfos']
        self.person['funyPoints'] = self['funyPoints']
        self.person['chargeCount'] = self['chargeCount']
        self.person['chargeFlag'] = self['chargeFlag']
        self.person['chargeMaxRewardState'] = self['chargeMaxRewardState']
        # end handle [GC_SYNC_OPEN_SERVER_ACTIVITY_TASK_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_DIRTY_OPSERVER_ACTIVITY_TASK_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DIRTY_OPSERVER_ACTIVITY_TASK_INFO] message attrs, auto generate do not change
        self.person['openServerActivityTaskInfos'] = self['openServerActivityTaskInfos']
        self.person['funyActivityRewardInfos'] = self['funyActivityRewardInfos']
        self.person['funyPoints'] = self['funyPoints']
        self.person['chargeCount'] = self['chargeCount']
        self.person['chargeFlag'] = self['chargeFlag']
        self.person['chargeMaxRewardState'] = self['chargeMaxRewardState']
        # end handle [GC_SYNC_DIRTY_OPSERVER_ACTIVITY_TASK_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_LIMITBESTSELLER_DATA] message attrs, auto generate do not change
        self.person['m_LimitBestSellerList'] = self['m_LimitBestSellerList']
        # end handle [GC_SYNC_LIMITBESTSELLER_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_SEVEN_DAY_GIFT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SEVEN_DAY_GIFT] message attrs, auto generate do not change
        self.person['loginCount'] = self['loginCount']
        self.person['getCount'] = self['getCount']
        # end handle [GC_SYNC_SEVEN_DAY_GIFT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_BIND_PHONE_AWARD] message attrs, auto generate do not change
        self.person['hasGet'] = self['hasGet']
        # end handle [GC_SYNC_BIND_PHONE_AWARD] message attrs, auto generate do not change
        pass


class GC_SYNC_REAL_NAME_CHECK_AWARD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_REAL_NAME_CHECK_AWARD] message attrs, auto generate do not change
        self.person['hasGet'] = self['hasGet']
        # end handle [GC_SYNC_REAL_NAME_CHECK_AWARD] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_HISTORY_RECHARGE_BINDGIFT] message attrs, auto generate do not change
        self.person['hasGet'] = self['hasGet']
        # end handle [GC_SYNC_HISTORY_RECHARGE_BINDGIFT] message attrs, auto generate do not change
        pass


class CG_REQ_GET_HISTORY_RECHARGE_REPAYGIFT (Packet):
    pass


class GC_SYNC_HISTORY_RECHARGE_REPAYGIFT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HISTORY_RECHARGE_REPAYGIFT] message attrs, auto generate do not change
        self.person['hasGet'] = self['hasGet']
        # end handle [GC_SYNC_HISTORY_RECHARGE_REPAYGIFT] message attrs, auto generate do not change
        pass


class CG_REQ_PSSURVEY_REWARD (Packet):
    pass


class GC_SYNC_PSSURVEY_PLAYER_VERSION (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PSSURVEY_PLAYER_VERSION] message attrs, auto generate do not change
        self.person['version'] = self['version']
        # end handle [GC_SYNC_PSSURVEY_PLAYER_VERSION] message attrs, auto generate do not change
        pass


class CG_REQ_GET_HISTORY_RECHARGE_REPAYRECHARGE (Packet):
    pass


class GC_SYNC_HISTORY_RECHARGE_REPAYRECHARGE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HISTORY_RECHARGE_REPAYRECHARGE] message attrs, auto generate do not change
        self.person['tabID'] = self['tabID']
        # end handle [GC_SYNC_HISTORY_RECHARGE_REPAYRECHARGE] message attrs, auto generate do not change
        pass


class CG_REQ_GET_HISTORY_RECHARGE_LEVELDRAW (Packet):
    pass


class GC_SYNC_HISTORY_RECHARGE_LEVELDRAW (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HISTORY_RECHARGE_LEVELDRAW] message attrs, auto generate do not change
        self.person['tabID'] = self['tabID']
        # end handle [GC_SYNC_HISTORY_RECHARGE_LEVELDRAW] message attrs, auto generate do not change
        pass


class GC_RET_HISTORY_RECHARGE_LEVELDRAW_RESULT (Packet):
    def handle(self):
        # begin handle [GC_RET_HISTORY_RECHARGE_LEVELDRAW_RESULT] message attrs, auto generate do not change
        self.person['tabID'] = self['tabID']
        self.person['rewardID'] = self['rewardID']
        # end handle [GC_RET_HISTORY_RECHARGE_LEVELDRAW_RESULT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_POSTERSTAR_SYNC_STATUE] message attrs, auto generate do not change
        self.person['npcId'] = self['npcId']
        self.person['FPValue'] = self['FPValue']
        self.person['awardStatus'] = self['awardStatus']
        # end handle [GC_POSTERSTAR_SYNC_STATUE] message attrs, auto generate do not change
        pass


class GC_SYNC_CAWARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CAWARD_INFO] message attrs, auto generate do not change
        self.person['getReward'] = self['getReward']
        self.person['version'] = self['version']
        # end handle [GC_SYNC_CAWARD_INFO] message attrs, auto generate do not change
        pass


class CG_ACCEPT_CAWARD (Packet):
    pass


class CG_REQ_BIND_HISTORY_RECHARGE (Packet):
    pass


class GC_RET_HISTORY_RECHARGE_BIND_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_HISTORY_RECHARGE_BIND_INFO] message attrs, auto generate do not change
        self.person['bindGuid'] = self['bindGuid']
        self.person['rechargeAmount'] = self['rechargeAmount']
        # end handle [GC_RET_HISTORY_RECHARGE_BIND_INFO] message attrs, auto generate do not change
        pass


class CG_ASK_ARHUNTING (Packet):
    pass


class GC_RET_ARHUNTING (Packet):
    def handle(self):
        # begin handle [GC_RET_ARHUNTING] message attrs, auto generate do not change
        self.person['itemguid'] = self['itemguid']
        self.person['radius'] = self['radius']
        self.person['vangle'] = self['vangle']
        self.person['hangle'] = self['hangle']
        # end handle [GC_RET_ARHUNTING] message attrs, auto generate do not change
        pass


class GC_SYNC_DROPINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DROPINFO] message attrs, auto generate do not change
        self.person['itemid'] = self['itemid']
        self.person['dropitemid'] = self['dropitemid']
        self.person['count'] = self['count']
        self.person['isbind'] = self['isbind']
        # end handle [GC_SYNC_DROPINFO] message attrs, auto generate do not change
        pass


class CG_CLEARN_USE_SKILL_CD (Packet):
    pass


class GC_NEWYEAR_WISH (Packet):
    def handle(self):
        # begin handle [GC_NEWYEAR_WISH] message attrs, auto generate do not change
        self.person['itemId'] = self['itemId']
        # end handle [GC_NEWYEAR_WISH] message attrs, auto generate do not change
        pass


class CG_REQ_SEND_NARRIAGE_LINK (Packet):
    pass


class CG_USE_SENDLANTERN (Packet):
    pass


class GC_WORDREDPACKETRAIN_ROLLNOTICE (Packet):
    def handle(self):
        # begin handle [GC_WORDREDPACKETRAIN_ROLLNOTICE] message attrs, auto generate do not change
        self.person['startTime'] = self['startTime']
        self.person['endTime'] = self['endTime']
        # end handle [GC_WORDREDPACKETRAIN_ROLLNOTICE] message attrs, auto generate do not change
        pass


class CG_REQ_HOLIDAY_TIMELIMITACTSCENE_ENTER (Packet):
    pass


class CG_REQ_HOLIDAY_TIMELIMITACTSCENE_EXIT (Packet):
    pass


class GC_RET_RECHARGE_ORDER_OVER (Packet):
    def handle(self):
        # begin handle [GC_RET_RECHARGE_ORDER_OVER] message attrs, auto generate do not change
        self.person['orderString'] = self['orderString']
        # end handle [GC_RET_RECHARGE_ORDER_OVER] message attrs, auto generate do not change
        pass


class GC_REQ_PAYUSER_LOG (Packet):
    def handle(self):
        # begin handle [GC_REQ_PAYUSER_LOG] message attrs, auto generate do not change
        self.person['index'] = self['index']
        # end handle [GC_REQ_PAYUSER_LOG] message attrs, auto generate do not change
        pass


class CG_SEND_PLAYANDGO_ERROR_LOG (Packet):
    pass


class GC_RET_JOIN_TEAM (Packet):
    def handle(self):
        # begin handle [GC_RET_JOIN_TEAM] message attrs, auto generate do not change
        self.person['targetId'] = self['targetId']
        self.person['combatValye'] = self['combatValye']
        # end handle [GC_RET_JOIN_TEAM] message attrs, auto generate do not change
        pass


class GC_NOTICE_DLC_VERSION_VIEW (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_DLC_VERSION_VIEW] message attrs, auto generate do not change
        # end handle [GC_NOTICE_DLC_VERSION_VIEW] message attrs, auto generate do not change
        pass


class GC_SYNC_DLC_VERSION_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DLC_VERSION_DATA] message attrs, auto generate do not change
        self.person['dlcCurVersionId'] = self['dlcCurVersionId']
        self.person['viewRewardData'] = self['viewRewardData']
        self.person['dlcRewardState'] = self['dlcRewardState']
        self.person['dlcReplaceAcceptState'] = self['dlcReplaceAcceptState']
        # end handle [GC_SYNC_DLC_VERSION_DATA] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_GOODLUCK_SYNC] message attrs, auto generate do not change
        self.person['optype'] = self['optype']
        self.person['giftid'] = self['giftid']
        self.person['moneytype'] = self['moneytype']
        self.person['money'] = self['money']
        self.person['fakemoney'] = self['fakemoney']
        self.person['itemid'] = self['itemid']
        self.person['itemcnt'] = self['itemcnt']
        self.person['dicid'] = self['dicid']
        self.person['deadline'] = self['deadline']
        self.person['fakeMoney2RealMoneyRatio'] = self['fakeMoney2RealMoneyRatio']
        # end handle [GC_GOODLUCK_SYNC] message attrs, auto generate do not change
        pass


class CG_DLC_CLICK_FUNCTION_BTN (Packet):
    pass


class CG_DLC_CLICK_DLC_VIEW_DETAIL (Packet):
    pass


class CG_CLICK_DLC_VIEW_GO (Packet):
    pass


class GC_SYNC_ONE_CHARGE_GIFT_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ONE_CHARGE_GIFT_DATA] message attrs, auto generate do not change
        self.person['oneChargeActivityId'] = self['oneChargeActivityId']
        self.person['giftDatas'] = self['giftDatas']
        # end handle [GC_SYNC_ONE_CHARGE_GIFT_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_TOTAL_COSUME_GIFT_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TOTAL_COSUME_GIFT_DATA] message attrs, auto generate do not change
        self.person['totalConsumeActivityId'] = self['totalConsumeActivityId']
        self.person['giftDatas'] = self['giftDatas']
        # end handle [GC_SYNC_TOTAL_COSUME_GIFT_DATA] message attrs, auto generate do not change
        pass


class CG_ACCEPT_COSUME_GIFT (Packet):
    pass


class CG_REQ_GET_FLASH_SALES_AWARD (Packet):
    pass


class GC_SYNC_FLASH_SALES_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FLASH_SALES_DATA] message attrs, auto generate do not change
        self.person['flashSalesId'] = self['flashSalesId']
        self.person['actData'] = self['actData']
        # end handle [GC_SYNC_FLASH_SALES_DATA] message attrs, auto generate do not change
        pass


class CG_REQ_BUY_DISCOUNT_GIFT (Packet):
    pass


class GC_SYNC_DISCOUNT_GIFT_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DISCOUNT_GIFT_DATA] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['maxRecharge'] = self['maxRecharge']
        self.person['getCount'] = self['getCount']
        # end handle [GC_SYNC_DISCOUNT_GIFT_DATA] message attrs, auto generate do not change
        pass


class CG_REQ_VIVO_GIFT (Packet):
    pass


class GC_RET_VIVO_GIFT (Packet):
    def handle(self):
        # begin handle [GC_RET_VIVO_GIFT] message attrs, auto generate do not change
        # end handle [GC_RET_VIVO_GIFT] message attrs, auto generate do not change
        pass


class GC_SYNC_VIVO_GIFT_GET_TIME (Packet):
    def handle(self):
        # begin handle [GC_SYNC_VIVO_GIFT_GET_TIME] message attrs, auto generate do not change
        self.person['time'] = self['time']
        # end handle [GC_SYNC_VIVO_GIFT_GET_TIME] message attrs, auto generate do not change
        pass


class GC_GM_LOGON_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_GM_LOGON_NOTICE] message attrs, auto generate do not change
        # end handle [GC_GM_LOGON_NOTICE] message attrs, auto generate do not change
        pass


class GC_GUILD_WORLDBOSS_STATE (Packet):
    def handle(self):
        # begin handle [GC_GUILD_WORLDBOSS_STATE] message attrs, auto generate do not change
        self.person['CurState'] = self['CurState']
        # end handle [GC_GUILD_WORLDBOSS_STATE] message attrs, auto generate do not change
        pass


class CG_GUILD_WORLDBOSS_RANK (Packet):
    pass


class GC_GUILD_WORLDBOSS_RANK (Packet):
    def handle(self):
        # begin handle [GC_GUILD_WORLDBOSS_RANK] message attrs, auto generate do not change
        self.person['BossDataId'] = self['BossDataId']
        self.person['RankData1'] = self['RankData1']
        self.person['RankData2'] = self['RankData2']
        self.person['RankData3'] = self['RankData3']
        self.person['Boss1HPPercent'] = self['Boss1HPPercent']
        self.person['Boss2HPPercent'] = self['Boss2HPPercent']
        self.person['Boss3HPPercent'] = self['Boss3HPPercent']
        # end handle [GC_GUILD_WORLDBOSS_RANK] message attrs, auto generate do not change
        pass


class CG_GUILD_WORLDBOSS_PERSONAL_RANK (Packet):
    pass


class GC_GUILD_WORLDBOSS_PERSONAL_RANK (Packet):
    def handle(self):
        # begin handle [GC_GUILD_WORLDBOSS_PERSONAL_RANK] message attrs, auto generate do not change
        self.person['BossDataId'] = self['BossDataId']
        self.person['PersonalRank1'] = self['PersonalRank1']
        self.person['PersonalRank2'] = self['PersonalRank2']
        self.person['PersonalRank3'] = self['PersonalRank3']
        # end handle [GC_GUILD_WORLDBOSS_PERSONAL_RANK] message attrs, auto generate do not change
        pass


class GC_EQUIP_ENCHANT_ITEMDETAIL (Packet):
    def handle(self):
        # begin handle [GC_EQUIP_ENCHANT_ITEMDETAIL] message attrs, auto generate do not change
        self.person['Id'] = self['Id']
        self.person['PropertyId'] = self['PropertyId']
        # end handle [GC_EQUIP_ENCHANT_ITEMDETAIL] message attrs, auto generate do not change
        pass


class GC_SYNC_NEW_IMMORTALITY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NEW_IMMORTALITY_INFO] message attrs, auto generate do not change
        self.person['useNewImortality'] = self['useNewImortality']
        self.person['isActivityFinished'] = self['isActivityFinished']
        self.person['immortalityPoints'] = self['immortalityPoints']
        self.person['immortalityActiveDays'] = self['immortalityActiveDays']
        self.person['immortalityWayInfos'] = self['immortalityWayInfos']
        self.person['immortalityStageInfos'] = self['immortalityStageInfos']
        # end handle [GC_SYNC_NEW_IMMORTALITY_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_DIRTY_NEW_IMMORTALITY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DIRTY_NEW_IMMORTALITY_INFO] message attrs, auto generate do not change
        self.person['useNewImortality'] = self['useNewImortality']
        self.person['isActivityFinished'] = self['isActivityFinished']
        self.person['immortalityPoints'] = self['immortalityPoints']
        self.person['immortalityActiveDays'] = self['immortalityActiveDays']
        self.person['immortalityWayInfos'] = self['immortalityWayInfos']
        self.person['immortalityStageInfos'] = self['immortalityStageInfos']
        # end handle [GC_SYNC_DIRTY_NEW_IMMORTALITY_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_PLAYER_NEW_PRESTIGE_INFO] message attrs, auto generate do not change
        self.person['playerPrestigeCamp'] = self['playerPrestigeCamp']
        self.person['playerPrestigeVal'] = self['playerPrestigeVal']
        self.person['playerPrestigeExploits'] = self['playerPrestigeExploits']
        self.person['infos'] = self['infos']
        self.person['prestigeBuyItemCount'] = self['prestigeBuyItemCount']
        self.person['todayPrestigeExploits'] = self['todayPrestigeExploits']
        self.person['weekPrestigeExploits'] = self['weekPrestigeExploits']
        self.person['prestigeBuyItemCatchCount'] = self['prestigeBuyItemCatchCount']
        # end handle [GC_SYNC_PLAYER_NEW_PRESTIGE_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_SERVER_NEW_PRESTIGE_INFO (Packet):
    pass


class GC_SYNC_SERVER_NEW_PRESTIGE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SERVER_NEW_PRESTIGE_INFO] message attrs, auto generate do not change
        self.person['qishaPrestigeVal'] = self['qishaPrestigeVal']
        self.person['xianyingPrestigeVal'] = self['xianyingPrestigeVal']
        # end handle [GC_SYNC_SERVER_NEW_PRESTIGE_INFO] message attrs, auto generate do not change
        pass


class CG_GUILD_REQ_LIST_BY_LABEL (Packet):
    pass


class GC_SYNC_GUILD_LABEL (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_LABEL] message attrs, auto generate do not change
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['GuildLabel'] = self['GuildLabel']
        # end handle [GC_SYNC_GUILD_LABEL] message attrs, auto generate do not change
        pass


class GC_SYNC_DAILY_LEVEL (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DAILY_LEVEL] message attrs, auto generate do not change
        self.person['level'] = self['level']
        # end handle [GC_SYNC_DAILY_LEVEL] message attrs, auto generate do not change
        pass


class CG_REQ_TOWER_FRIEND_RANK (Packet):
    pass


class GC_RET_TOWER_FRIEND_RANK (Packet):
    def handle(self):
        # begin handle [GC_RET_TOWER_FRIEND_RANK] message attrs, auto generate do not change
        # end handle [GC_RET_TOWER_FRIEND_RANK] message attrs, auto generate do not change
        pass


class CG_REQ_NEW_PRESTIGE_CAMP_ROLE_NUMER (Packet):
    pass


class GC_RESP_NEW_PRESTIGE_CAMP_ROLE_NUMBER (Packet):
    def handle(self):
        # begin handle [GC_RESP_NEW_PRESTIGE_CAMP_ROLE_NUMBER] message attrs, auto generate do not change
        self.person['qishaRoleNumber'] = self['qishaRoleNumber']
        self.person['xiayingRoleNumer'] = self['xiayingRoleNumer']
        self.person['reqType'] = self['reqType']
        # end handle [GC_RESP_NEW_PRESTIGE_CAMP_ROLE_NUMBER] message attrs, auto generate do not change
        pass


class GC_SYNC_VIEW_PLAYER_NEW_PRESTIGE_CAMP (Packet):
    def handle(self):
        # begin handle [GC_SYNC_VIEW_PLAYER_NEW_PRESTIGE_CAMP] message attrs, auto generate do not change
        self.person['playerGuid'] = self['playerGuid']
        self.person['playerNewPrestigeCamp'] = self['playerNewPrestigeCamp']
        # end handle [GC_SYNC_VIEW_PLAYER_NEW_PRESTIGE_CAMP] message attrs, auto generate do not change
        pass


class GC_SELECT_NEW_PRESTIGE_CAMP_RET (Packet):
    def handle(self):
        # begin handle [GC_SELECT_NEW_PRESTIGE_CAMP_RET] message attrs, auto generate do not change
        self.person['newPrestigeCamp'] = self['newPrestigeCamp']
        self.person['selectType'] = self['selectType']
        # end handle [GC_SELECT_NEW_PRESTIGE_CAMP_RET] message attrs, auto generate do not change
        pass


class GC_SYNC_NEW_PRESTIGE_ELITE_SCENE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NEW_PRESTIGE_ELITE_SCENE_INFO] message attrs, auto generate do not change
        self.person['sceneInfos'] = self['sceneInfos']
        # end handle [GC_SYNC_NEW_PRESTIGE_ELITE_SCENE_INFO] message attrs, auto generate do not change
        pass


class CG_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE (Packet):
    pass


class GC_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE_OK (Packet):
    def handle(self):
        # begin handle [GC_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE_OK] message attrs, auto generate do not change
        self.person['targetPosX'] = self['targetPosX']
        self.person['targetPosY'] = self['targetPosY']
        self.person['targetPosZ'] = self['targetPosZ']
        self.person['nSceneId'] = self['nSceneId']
        self.person['nSceneInstanceId'] = self['nSceneInstanceId']
        # end handle [GC_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE_OK] message attrs, auto generate do not change
        pass


class CG_GET_ALL_ACTIVENESS_BONUS_ITEM (Packet):
    pass


class GC_COMMON_RWARD_ITEM_SHOW (Packet):
    def handle(self):
        # begin handle [GC_COMMON_RWARD_ITEM_SHOW] message attrs, auto generate do not change
        self.person['rewardList'] = self['rewardList']
        # end handle [GC_COMMON_RWARD_ITEM_SHOW] message attrs, auto generate do not change
        pass


class GC_NOTICE_FIRST_CHANGE_WINDOW (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_FIRST_CHANGE_WINDOW] message attrs, auto generate do not change
        # end handle [GC_NOTICE_FIRST_CHANGE_WINDOW] message attrs, auto generate do not change
        pass


class GC_KICKOUT_MERCENARY_LEAVE_TEAM (Packet):
    def handle(self):
        # begin handle [GC_KICKOUT_MERCENARY_LEAVE_TEAM] message attrs, auto generate do not change
        # end handle [GC_KICKOUT_MERCENARY_LEAVE_TEAM] message attrs, auto generate do not change
        pass


class CG_REQ_CHANGE_FRIEND_GROUPNAME (Packet):
    pass


class GC_RET_CHANGENAME_FRIEND_GROUPNAME (Packet):
    def handle(self):
        # begin handle [GC_RET_CHANGENAME_FRIEND_GROUPNAME] message attrs, auto generate do not change
        self.person['curPage'] = self['curPage']
        self.person['value'] = self['value']
        # end handle [GC_RET_CHANGENAME_FRIEND_GROUPNAME] message attrs, auto generate do not change
        pass


class GC_SYNC_NEW_PRESTIGE_BOSS_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NEW_PRESTIGE_BOSS_INFO] message attrs, auto generate do not change
        self.person['bRun'] = self['bRun']
        self.person['qiShaRankInfo'] = self['qiShaRankInfo']
        self.person['xiaYingRankInfo'] = self['xiaYingRankInfo']
        # end handle [GC_SYNC_NEW_PRESTIGE_BOSS_INFO] message attrs, auto generate do not change
        pass


class CG_ENTER_NEW_PRESTIGE_BOSS_SCENE (Packet):
    pass


class CG_REQ_GET_PLAYANDGO_AWARD (Packet):
    pass


class GC_SYNC_PLAYANDGO_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PLAYANDGO_INFO] message attrs, auto generate do not change
        self.person['canGetAward'] = self['canGetAward']
        # end handle [GC_SYNC_PLAYANDGO_INFO] message attrs, auto generate do not change
        pass


class CG_NEW_PRESTIGE_BOSS_OPENBOX (Packet):
    pass


class CG_REQ_SHAKE_REWARD (Packet):
    pass


class CG_RET_SHAKE_REWARD (Packet):
    pass


class GC_SYNC_SHAKE_ACTIVITY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SHAKE_ACTIVITY_INFO] message attrs, auto generate do not change
        self.person['ActivityId'] = self['ActivityId']
        self.person['ShakeCoin'] = self['ShakeCoin']
        self.person['ShakeScore'] = self['ShakeScore']
        self.person['ShopItemIdList'] = self['ShopItemIdList']
        self.person['ShopBuyCountList'] = self['ShopBuyCountList']
        # end handle [GC_SYNC_SHAKE_ACTIVITY_INFO] message attrs, auto generate do not change
        pass


class CG_SHAKE_SHOP_BUY (Packet):
    pass


class GC_SHAKE_SHOP_BUY_RET (Packet):
    def handle(self):
        # begin handle [GC_SHAKE_SHOP_BUY_RET] message attrs, auto generate do not change
        self.person['ShopItemId'] = self['ShopItemId']
        self.person['BuyCount'] = self['BuyCount']
        # end handle [GC_SHAKE_SHOP_BUY_RET] message attrs, auto generate do not change
        pass


class GC_RET_SHAKE_REWARD (Packet):
    def handle(self):
        # begin handle [GC_RET_SHAKE_REWARD] message attrs, auto generate do not change
        self.person['RewardList'] = self['RewardList']
        # end handle [GC_RET_SHAKE_REWARD] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILD_ROBBER_RUN (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_ROBBER_RUN] message attrs, auto generate do not change
        self.person['RubberRun'] = self['RubberRun']
        # end handle [GC_SYNC_GUILD_ROBBER_RUN] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILDFIGHT_BOSS_RUN (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILDFIGHT_BOSS_RUN] message attrs, auto generate do not change
        self.person['BossRun'] = self['BossRun']
        # end handle [GC_SYNC_GUILDFIGHT_BOSS_RUN] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILD_WORD_BOSS_RUN (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILD_WORD_BOSS_RUN] message attrs, auto generate do not change
        self.person['BossRun'] = self['BossRun']
        # end handle [GC_SYNC_GUILD_WORD_BOSS_RUN] message attrs, auto generate do not change
        pass


class GC_SYNC_MONSTER_NIAN (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MONSTER_NIAN] message attrs, auto generate do not change
        self.person['MonsterNians'] = self['MonsterNians']
        self.person['MonsterNianRankItems'] = self['MonsterNianRankItems']
        self.person['CurMonsterNianId'] = self['CurMonsterNianId']
        # end handle [GC_SYNC_MONSTER_NIAN] message attrs, auto generate do not change
        pass


class CG_MONSTER_NIAN_DRIVEAWAY (Packet):
    pass


class GC_MONSTER_NIAN_DRIVEAWAY (Packet):
    def handle(self):
        # begin handle [GC_MONSTER_NIAN_DRIVEAWAY] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['Id'] = self['Id']
        self.person['TotalDamage'] = self['TotalDamage']
        # end handle [GC_MONSTER_NIAN_DRIVEAWAY] message attrs, auto generate do not change
        pass


class CG_MONSTER_NIAN_REQ_RANK (Packet):
    pass


class GC_MONSTER_NIAN_REQ_RANK (Packet):
    def handle(self):
        # begin handle [GC_MONSTER_NIAN_REQ_RANK] message attrs, auto generate do not change
        self.person['Page'] = self['Page']
        self.person['RankItems'] = self['RankItems']
        # end handle [GC_MONSTER_NIAN_REQ_RANK] message attrs, auto generate do not change
        pass


class CG_MONSTER_NIAN_ACCEPT_STAGE_REWARD (Packet):
    pass


class CG_FESTIVAL_LUCKYCARD_CHOOSE (Packet):
    pass


class GC_FESTIVAL_LUCKYCARD_CHOOSE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_FESTIVAL_LUCKYCARD_CHOOSE_RESULT] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['Id'] = self['Id']
        self.person['ChooseNum'] = self['ChooseNum']
        # end handle [GC_FESTIVAL_LUCKYCARD_CHOOSE_RESULT] message attrs, auto generate do not change
        pass


class GC_FESTIVAL_LUCKYCARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_FESTIVAL_LUCKYCARD_INFO] message attrs, auto generate do not change
        self.person['LuckyCards'] = self['LuckyCards']
        self.person['CurAcitivityId'] = self['CurAcitivityId']
        self.person['CurSendReward'] = self['CurSendReward']
        self.person['CurChooseNum'] = self['CurChooseNum']
        self.person['CurRewardPool'] = self['CurRewardPool']
        # end handle [GC_FESTIVAL_LUCKYCARD_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_FESTIVAL_LUCKCARD_INFO (Packet):
    pass


class GC_SYNC_HUADENGCHUSHANG_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HUADENGCHUSHANG_INFO] message attrs, auto generate do not change
        self.person['useItemDays'] = self['useItemDays']
        self.person['GetItemToday'] = self['GetItemToday']
        self.person['GetUseItemAward'] = self['GetUseItemAward']
        # end handle [GC_SYNC_HUADENGCHUSHANG_INFO] message attrs, auto generate do not change
        pass


class GC_ActivyCanBuyBackRewardAllInfo (Packet):
    def handle(self):
        # begin handle [GC_ActivyCanBuyBackRewardAllInfo] message attrs, auto generate do not change
        # end handle [GC_ActivyCanBuyBackRewardAllInfo] message attrs, auto generate do not change
        pass


class CG_ActivityRewardBuyBackNotice (Packet):
    pass


class CG_ActivyRewardBuyOne (Packet):
    pass


class CG_ActivityRewardBuyAll (Packet):
    pass


class GC_ActivityRewardBuyBackNotice (Packet):
    def handle(self):
        # begin handle [GC_ActivityRewardBuyBackNotice] message attrs, auto generate do not change
        # end handle [GC_ActivityRewardBuyBackNotice] message attrs, auto generate do not change
        pass


class GC_ACTIVITY_CAN_BUYBACK_REWARD_ALLINFO (Packet):
    def handle(self):
        # begin handle [GC_ACTIVITY_CAN_BUYBACK_REWARD_ALLINFO] message attrs, auto generate do not change
        self.person['AllInfo'] = self['AllInfo']
        self.person['normalRewardAllCostType'] = self['normalRewardAllCostType']
        self.person['normalRewardAllCost'] = self['normalRewardAllCost']
        self.person['perfectRewardAllCost'] = self['perfectRewardAllCost']
        # end handle [GC_ACTIVITY_CAN_BUYBACK_REWARD_ALLINFO] message attrs, auto generate do not change
        pass


class GC_ACTIVITY_REWARD_BUYBACK_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_ACTIVITY_REWARD_BUYBACK_NOTICE] message attrs, auto generate do not change
        self.person['NoticeDic'] = self['NoticeDic']
        self.person['Param1'] = self['Param1']
        self.person['Param2'] = self['Param2']
        self.person['Param3'] = self['Param3']
        # end handle [GC_ACTIVITY_REWARD_BUYBACK_NOTICE] message attrs, auto generate do not change
        pass


class CG_ACTIVITY_REWARD_BUYONE (Packet):
    pass


class CG_ACTIVITY_REWARD_BUY_ALL (Packet):
    pass


class CG_REQ_GET_WMKEFU_TRIAL_ITEM (Packet):
    pass


class GC_SYNC_GET_WMKEFU_TRIAL_ITEM (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GET_WMKEFU_TRIAL_ITEM] message attrs, auto generate do not change
        self.person['bGet'] = self['bGet']
        # end handle [GC_SYNC_GET_WMKEFU_TRIAL_ITEM] message attrs, auto generate do not change
        pass


class GC_SYNC_GIVE_GIFT_RANK_ACTIVITY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GIVE_GIFT_RANK_ACTIVITY_INFO] message attrs, auto generate do not change
        self.person['version'] = self['version']
        self.person['todayLikeCount'] = self['todayLikeCount']
        self.person['allLikeCount'] = self['allLikeCount']
        self.person['sendRankLikeGuid'] = self['sendRankLikeGuid']
        self.person['receiveRankLikeGuid'] = self['receiveRankLikeGuid']
        self.person['sendValue'] = self['sendValue']
        self.person['receiveValue'] = self['receiveValue']
        # end handle [GC_SYNC_GIVE_GIFT_RANK_ACTIVITY_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_GIVE_GIFT_RANK_LIKE (Packet):
    pass


class GC_RESP_GIVE_GIFT_RANK_LIKE (Packet):
    def handle(self):
        # begin handle [GC_RESP_GIVE_GIFT_RANK_LIKE] message attrs, auto generate do not change
        self.person['rankLikeGuid'] = self['rankLikeGuid']
        self.person['rankType'] = self['rankType']
        self.person['targetGuid'] = self['targetGuid']
        self.person['todayLikeCount'] = self['todayLikeCount']
        self.person['allLikeCount'] = self['allLikeCount']
        self.person['targetLikeCount'] = self['targetLikeCount']
        # end handle [GC_RESP_GIVE_GIFT_RANK_LIKE] message attrs, auto generate do not change
        pass


class CG_REQ_GIVE_RANK_GIFT (Packet):
    pass


class GC_RESP_GIVE_RANK_GIFT (Packet):
    def handle(self):
        # begin handle [GC_RESP_GIVE_RANK_GIFT] message attrs, auto generate do not change
        self.person['targetGuid'] = self['targetGuid']
        self.person['targetReceiveValue'] = self['targetReceiveValue']
        self.person['selfSendValue'] = self['selfSendValue']
        # end handle [GC_RESP_GIVE_RANK_GIFT] message attrs, auto generate do not change
        pass


class CG_REQ_GET_HUADENGCHUSHANG_ITEM (Packet):
    pass


class CG_REQ_OPEN_LIUSHUIXI (Packet):
    pass


class CG_REQ_GET_LIUSHUIXI_ITEM (Packet):
    pass


class GC_UNFORGETABLE_PROMISE_INFO (Packet):
    def handle(self):
        # begin handle [GC_UNFORGETABLE_PROMISE_INFO] message attrs, auto generate do not change
        self.person['AllPlayerRewardHaveGet'] = self['AllPlayerRewardHaveGet']
        self.person['MarriageGiftHaveGet'] = self['MarriageGiftHaveGet']
        # end handle [GC_UNFORGETABLE_PROMISE_INFO] message attrs, auto generate do not change
        pass


class CG_UNFORGETABLE_PROMISE_GET_REWARD (Packet):
    pass


class GC_SYNC_SHAKE_CHALLENGE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SHAKE_CHALLENGE_DATA] message attrs, auto generate do not change
        self.person['ActivityId'] = self['ActivityId']
        self.person['ChallengeList'] = self['ChallengeList']
        # end handle [GC_SYNC_SHAKE_CHALLENGE_DATA] message attrs, auto generate do not change
        pass


class CG_GET_SHAKE_CHALLENGE_REWARD (Packet):
    pass


class GC_GET_SHAKE_CHALLENGE_REWARD_RET (Packet):
    def handle(self):
        # begin handle [GC_GET_SHAKE_CHALLENGE_REWARD_RET] message attrs, auto generate do not change
        self.person['ChallengeInfo'] = self['ChallengeInfo']
        # end handle [GC_GET_SHAKE_CHALLENGE_REWARD_RET] message attrs, auto generate do not change
        pass


class CG_REQ_GET_HUADENGCHUSHANG_USE_ITEM_AWARD (Packet):
    pass


class GC_MONSTER_NIAN_STAGE_REWARD_STATE (Packet):
    def handle(self):
        # begin handle [GC_MONSTER_NIAN_STAGE_REWARD_STATE] message attrs, auto generate do not change
        self.person['Id'] = self['Id']
        self.person['StageRewardState'] = self['StageRewardState']
        # end handle [GC_MONSTER_NIAN_STAGE_REWARD_STATE] message attrs, auto generate do not change
        pass


class GC_FESTIVAL_LUCKCARD_AWARD (Packet):
    def handle(self):
        # begin handle [GC_FESTIVAL_LUCKCARD_AWARD] message attrs, auto generate do not change
        # end handle [GC_FESTIVAL_LUCKCARD_AWARD] message attrs, auto generate do not change
        pass


class GC_SYNC_DIMAI_TANXIAN_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DIMAI_TANXIAN_INFO] message attrs, auto generate do not change
        self.person['LingBaoNangStartTime'] = self['LingBaoNangStartTime']
        self.person['LingBaoNangProgress'] = self['LingBaoNangProgress']
        self.person['LingBaoNangRewardState'] = self['LingBaoNangRewardState']
        self.person['JingCuQuality'] = self['JingCuQuality']
        self.person['CurDiMaiHongXiProgress'] = self['CurDiMaiHongXiProgress']
        self.person['DiMaiHongXiFullTime'] = self['DiMaiHongXiFullTime']
        self.person['YuanSuNingJuTimes'] = self['YuanSuNingJuTimes']
        self.person['BuyHongXiProgress'] = self['BuyHongXiProgress']
        self.person['LastJingLingDialogTime'] = self['LastJingLingDialogTime']
        self.person['JingLingDialogTimes'] = self['JingLingDialogTimes']
        self.person['DiMaiPenFaRewardState'] = self['DiMaiPenFaRewardState']
        self.person['DiMaiMiJingStartTime'] = self['DiMaiMiJingStartTime']
        self.person['DiMaiMiJingRareType'] = self['DiMaiMiJingRareType']
        self.person['DiMaiMiJingHelpPassCnt'] = self['DiMaiMiJingHelpPassCnt']
        self.person['DiMaiMiJingTriggerCnt'] = self['DiMaiMiJingTriggerCnt']
        # end handle [GC_SYNC_DIMAI_TANXIAN_INFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_REGRESS_INFO] message attrs, auto generate do not change
        self.person['RegressTime'] = self['RegressTime']
        self.person['RegressRewardGet'] = self['RegressRewardGet']
        self.person['RegressServerLevel'] = self['RegressServerLevel']
        self.person['RegressPlayerLevel'] = self['RegressPlayerLevel']
        self.person['RegressDays'] = self['RegressDays']
        self.person['LoginGetDay'] = self['LoginGetDay']
        self.person['LoginRewardGet'] = self['LoginRewardGet']
        self.person['NoticeFriend'] = self['NoticeFriend']
        self.person['JoinGuid'] = self['JoinGuid']
        self.person['DailyActiveness'] = self['DailyActiveness']
        self.person['TotalActivenessVaule'] = self['TotalActivenessVaule']
        self.person['TotalActivenessReward'] = self['TotalActivenessReward']
        self.person['RegressGiftBuy'] = self['RegressGiftBuy']
        self.person['ActType'] = self['ActType']
        self.person['FestivalTaskId'] = self['FestivalTaskId']
        self.person['FestivalTaskCompletedTimes'] = self['FestivalTaskCompletedTimes']
        self.person['FestivalTaskGetRewardTimes'] = self['FestivalTaskGetRewardTimes']
        self.person['FestivalRegressLoginInfo'] = self['FestivalRegressLoginInfo']
        # end handle [GC_SYNC_REGRESS_INFO] message attrs, auto generate do not change
        pass


class CG_FirstOpenDiMaiUI (Packet):
    pass


class GC_SYNC_DIMAI_CHALLENGE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DIMAI_CHALLENGE_INFO] message attrs, auto generate do not change
        self.person['AutoStartTime'] = self['AutoStartTime']
        self.person['HasPassStageId'] = self['HasPassStageId']
        self.person['CurPassStage'] = self['CurPassStage']
        # end handle [GC_SYNC_DIMAI_CHALLENGE_INFO] message attrs, auto generate do not change
        pass


class CG_REQUEST_DIMAI_CHALLENGE (Packet):
    pass


class CG_ACCEPT_DIMAI_AUTO_REWARD (Packet):
    pass


class GC_DIMAI_CHALLENGE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_DIMAI_CHALLENGE_RESULT] message attrs, auto generate do not change
        self.person['nResult'] = self['nResult']
        self.person['nStageId'] = self['nStageId']
        self.person['nLastStageId'] = self['nLastStageId']
        self.person['Time'] = self['Time']
        self.person['LeftTime'] = self['LeftTime']
        self.person['CanGetProfit'] = self['CanGetProfit']
        # end handle [GC_DIMAI_CHALLENGE_RESULT] message attrs, auto generate do not change
        pass


class CG_FIRST_OPEN_DIMAI_UI (Packet):
    pass


class GC_SYNC_DIMAIJINGLUO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DIMAIJINGLUO] message attrs, auto generate do not change
        self.person['GroupStates'] = self['GroupStates']
        self.person['Combat'] = self['Combat']
        self.person['LastActivated'] = self['LastActivated']
        # end handle [GC_SYNC_DIMAIJINGLUO] message attrs, auto generate do not change
        pass


class CG_REQ_DIMAIJINGLUO_ACTIVATE (Packet):
    pass


class GC_RESP_DIMAIJINGLUO_ACTIVATE (Packet):
    def handle(self):
        # begin handle [GC_RESP_DIMAIJINGLUO_ACTIVATE] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        self.person['GroupStates'] = self['GroupStates']
        self.person['Combat'] = self['Combat']
        self.person['LastActivatedNodeId'] = self['LastActivatedNodeId']
        # end handle [GC_RESP_DIMAIJINGLUO_ACTIVATE] message attrs, auto generate do not change
        pass


class GC_DIMAI_TANXIAN_OPTION_RESULT (Packet):
    def handle(self):
        # begin handle [GC_DIMAI_TANXIAN_OPTION_RESULT] message attrs, auto generate do not change
        self.person['OpType'] = self['OpType']
        self.person['Result'] = self['Result']
        self.person['RewardItemId'] = self['RewardItemId']
        self.person['RewardItemCount'] = self['RewardItemCount']
        # end handle [GC_DIMAI_TANXIAN_OPTION_RESULT] message attrs, auto generate do not change
        pass


class CG_GET_FREE_REGRESS_GIFT (Packet):
    pass


class GC_ENTER_DIMAI_CHALLENGE_STAGE (Packet):
    def handle(self):
        # begin handle [GC_ENTER_DIMAI_CHALLENGE_STAGE] message attrs, auto generate do not change
        self.person['DiMaiStageId'] = self['DiMaiStageId']
        # end handle [GC_ENTER_DIMAI_CHALLENGE_STAGE] message attrs, auto generate do not change
        pass


class CG_CHALLENGEFRIENDRANKLIST_REQ (Packet):
    pass


class GC_CHALLENGEFRIENDRANKLIST (Packet):
    def handle(self):
        # begin handle [GC_CHALLENGEFRIENDRANKLIST] message attrs, auto generate do not change
        self.person['level'] = self['level']
        self.person['profession'] = self['profession']
        self.person['combatNum'] = self['combatNum']
        self.person['name'] = self['name']
        self.person['pos'] = self['pos']
        self.person['playerGuid'] = self['playerGuid']
        self.person['HonorCoins'] = self['HonorCoins']
        self.person['sex'] = self['sex']
        self.person['customHeadPic'] = self['customHeadPic']
        self.person['realPos'] = self['realPos']
        self.person['TeamId'] = self['TeamId']
        self.person['TeamCount'] = self['TeamCount']
        self.person['GuildGuid'] = self['GuildGuid']
        self.person['GuidName'] = self['GuidName']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        # end handle [GC_CHALLENGEFRIENDRANKLIST] message attrs, auto generate do not change
        pass


class GC_SYNC_SHILIAN_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SHILIAN_INFO] message attrs, auto generate do not change
        self.person['MaxWinLevel'] = self['MaxWinLevel']
        self.person['MaxNotWinLevel'] = self['MaxNotWinLevel']
        self.person['BestFightStage'] = self['BestFightStage']
        self.person['MaxCanFightLevel'] = self['MaxCanFightLevel']
        self.person['HistoryBestRankPos'] = self['HistoryBestRankPos']
        self.person['HistoryBestWinLevel'] = self['HistoryBestWinLevel']
        self.person['RankValue'] = self['RankValue']
        self.person['OpenServerLv'] = self['OpenServerLv']
        self.person['TotalCiZhui'] = self['TotalCiZhui']
        # end handle [GC_SYNC_SHILIAN_INFO] message attrs, auto generate do not change
        pass


class GC_SHILIAN_CITIAO (Packet):
    def handle(self):
        # begin handle [GC_SHILIAN_CITIAO] message attrs, auto generate do not change
        self.person['CiTiaoId'] = self['CiTiaoId']
        # end handle [GC_SHILIAN_CITIAO] message attrs, auto generate do not change
        pass


class CG_SHILIAN_CITIAO_SELECT (Packet):
    pass


class GC_SHILIAN_FIGHT_RESULT (Packet):
    def handle(self):
        # begin handle [GC_SHILIAN_FIGHT_RESULT] message attrs, auto generate do not change
        self.person['Level'] = self['Level']
        self.person['Result'] = self['Result']
        self.person['Result_Level'] = self['Result_Level']
        self.person['Result_Stage'] = self['Result_Stage']
        self.person['MaxCanFightLevel'] = self['MaxCanFightLevel']
        self.person['FightTimeLen'] = self['FightTimeLen']
        self.person['RankValue'] = self['RankValue']
        self.person['UnLockCiTiao'] = self['UnLockCiTiao']
        # end handle [GC_SHILIAN_FIGHT_RESULT] message attrs, auto generate do not change
        pass


class CG_REQ_CHALLENGE_RANK_SWAP_INFO (Packet):
    pass


class GC_RESP_CHALLENGE_RANK_SWAP (Packet):
    def handle(self):
        # begin handle [GC_RESP_CHALLENGE_RANK_SWAP] message attrs, auto generate do not change
        self.person['OldFakePos'] = self['OldFakePos']
        self.person['OldRankPos'] = self['OldRankPos']
        self.person['NewFakePos'] = self['NewFakePos']
        self.person['NewRankPos'] = self['NewRankPos']
        self.person['level'] = self['level']
        self.person['profession'] = self['profession']
        self.person['combatNum'] = self['combatNum']
        self.person['name'] = self['name']
        self.person['playerGuid'] = self['playerGuid']
        self.person['sex'] = self['sex']
        self.person['customHeadPic'] = self['customHeadPic']
        self.person['PhotoFrameId'] = self['PhotoFrameId']
        # end handle [GC_RESP_CHALLENGE_RANK_SWAP] message attrs, auto generate do not change
        pass


class GC_SHOW_LIVEBROADCAST_RED (Packet):
    def handle(self):
        # begin handle [GC_SHOW_LIVEBROADCAST_RED] message attrs, auto generate do not change
        self.person['bShow'] = self['bShow']
        # end handle [GC_SHOW_LIVEBROADCAST_RED] message attrs, auto generate do not change
        pass


class CG_REQ_TIANSHU_RECOMMEND (Packet):
    pass


class GC_RESP_TIANSHU_RECOMMEND (Packet):
    def handle(self):
        # begin handle [GC_RESP_TIANSHU_RECOMMEND] message attrs, auto generate do not change
        # end handle [GC_RESP_TIANSHU_RECOMMEND] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_EVERYDAYBANK_INFO] message attrs, auto generate do not change
        self.person['dataId'] = self['dataId']
        self.person['getAward'] = self['getAward']
        self.person['rechargeDays'] = self['rechargeDays']
        self.person['dailyRecharge'] = self['dailyRecharge']
        # end handle [GC_SYNC_EVERYDAYBANK_INFO] message attrs, auto generate do not change
        pass


class CG_TREASURE_COMPASS_DRAW (Packet):
    pass


class GC_TREASURE_COMPASS_DRAW_RET (Packet):
    def handle(self):
        # begin handle [GC_TREASURE_COMPASS_DRAW_RET] message attrs, auto generate do not change
        self.person['Turn'] = self['Turn']
        self.person['RewardIndex'] = self['RewardIndex']
        self.person['type'] = self['type']
        # end handle [GC_TREASURE_COMPASS_DRAW_RET] message attrs, auto generate do not change
        pass


class GC_SYNC_TREASRE_COMPASS_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TREASRE_COMPASS_INFO] message attrs, auto generate do not change
        self.person['ActivityId'] = self['ActivityId']
        self.person['CurTurn'] = self['CurTurn']
        self.person['CurRechargeNum'] = self['CurRechargeNum']
        self.person['TreasureRecord'] = self['TreasureRecord']
        self.person['CurRound'] = self['CurRound']
        self.person['Type'] = self['Type']
        # end handle [GC_SYNC_TREASRE_COMPASS_INFO] message attrs, auto generate do not change
        pass


class CG_GUILDTEAM_AWARD (Packet):
    pass


class GC_SYNC_CHARM_VALUE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CHARM_VALUE] message attrs, auto generate do not change
        self.person['titleCharm'] = self['titleCharm']
        self.person['fashionCharm'] = self['fashionCharm']
        self.person['dyeCharm'] = self['dyeCharm']
        # end handle [GC_SYNC_CHARM_VALUE] message attrs, auto generate do not change
        pass


class CG_ASK_NOTIFICATION_REWARD (Packet):
    pass


class GC_SYNC_NOTIFICATION_REWARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NOTIFICATION_REWARD_INFO] message attrs, auto generate do not change
        self.person['RewardTime'] = self['RewardTime']
        # end handle [GC_SYNC_NOTIFICATION_REWARD_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_CHARM_BUYITEM (Packet):
    pass


class GC_SYNC_CHARM_LIMITINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CHARM_LIMITINFO] message attrs, auto generate do not change
        self.person['nSaveIndex'] = self['nSaveIndex']
        self.person['nCanBuyCount'] = self['nCanBuyCount']
        # end handle [GC_SYNC_CHARM_LIMITINFO] message attrs, auto generate do not change
        pass


class GC_SERVANT_SYNC_FATE (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_SYNC_FATE] message attrs, auto generate do not change
        self.person['m_servantFate'] = self['m_servantFate']
        self.person['m_synctype'] = self['m_synctype']
        # end handle [GC_SERVANT_SYNC_FATE] message attrs, auto generate do not change
        pass


class CG_REQ_FASHION_FREEDOM_DYE (Packet):
    pass


class GC_RET_FASHION_FREEDOM_DYE (Packet):
    def handle(self):
        # begin handle [GC_RET_FASHION_FREEDOM_DYE] message attrs, auto generate do not change
        self.person['fashionId'] = self['fashionId']
        self.person['fashion'] = self['fashion']
        # end handle [GC_RET_FASHION_FREEDOM_DYE] message attrs, auto generate do not change
        pass


class CG_REQ_BWGW_SIGN_UP (Packet):
    pass


class CG_DRAW_BWGW_REWARD (Packet):
    pass


class CG_REQ_BWGW_SELF_RANK (Packet):
    pass


class GC_RET_BWGW_SELF_RANK_DATA (Packet):
    def handle(self):
        # begin handle [GC_RET_BWGW_SELF_RANK_DATA] message attrs, auto generate do not change
        self.person['guildWeekScore'] = self['guildWeekScore']
        self.person['guildSeasonScore'] = self['guildSeasonScore']
        self.person['worldSeasonScore'] = self['worldSeasonScore']
        self.person['guildWeekRank'] = self['guildWeekRank']
        self.person['guildSeasonRank'] = self['guildSeasonRank']
        self.person['worldSeasonRank'] = self['worldSeasonRank']
        self.person['bOwnQualification'] = self['bOwnQualification']
        self.person['nBwgwSeason'] = self['nBwgwSeason']
        self.person['nBwgwRound'] = self['nBwgwRound']
        # end handle [GC_RET_BWGW_SELF_RANK_DATA] message attrs, auto generate do not change
        pass


class CG_REQ_REJOIN_BWGW_SCENE (Packet):
    pass


class GC_SYNC_BWGW_ACTIVITY_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BWGW_ACTIVITY_DATA] message attrs, auto generate do not change
        self.person['IsAlreadySignup'] = self['IsAlreadySignup']
        self.person['SceneMemberNum'] = self['SceneMemberNum']
        self.person['IsInBattle'] = self['IsInBattle']
        # end handle [GC_SYNC_BWGW_ACTIVITY_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_BWGW_ARMY_BLOCK (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BWGW_ARMY_BLOCK] message attrs, auto generate do not change
        self.person['Available'] = self['Available']
        # end handle [GC_SYNC_BWGW_ARMY_BLOCK] message attrs, auto generate do not change
        pass


class GC_BWGW_MATCH_RESULT (Packet):
    def handle(self):
        # begin handle [GC_BWGW_MATCH_RESULT] message attrs, auto generate do not change
        # end handle [GC_BWGW_MATCH_RESULT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_WD_RETURNDATA] message attrs, auto generate do not change
        self.person['buytime'] = self['buytime']
        self.person['wdperiods'] = self['wdperiods']
        self.person['wdtype'] = self['wdtype']
        self.person['loginreward'] = self['loginreward']
        self.person['boxreward'] = self['boxreward']
        self.person['wdactiveness'] = self['wdactiveness']
        self.person['exdata'] = self['exdata']
        # end handle [GC_WD_RETURNDATA] message attrs, auto generate do not change
        pass


class CG_WD_BUYWD (Packet):
    pass


class CG_WD_UPGRADEINFO (Packet):
    pass


class GC_WD_UPGRADEINFO (Packet):
    def handle(self):
        # begin handle [GC_WD_UPGRADEINFO] message attrs, auto generate do not change
        # end handle [GC_WD_UPGRADEINFO] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_WD_ISVALIDBUY] message attrs, auto generate do not change
        self.person['buytype'] = self['buytype']
        self.person['valid'] = self['valid']
        # end handle [GC_WD_ISVALIDBUY] message attrs, auto generate do not change
        pass


class CG_WD_BUQIAN (Packet):
    pass


class CG_GET_COTWARMUP_REWARD (Packet):
    pass


class GC_SYNC_PHOTOFRAME (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PHOTOFRAME] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['deadline'] = self['deadline']
        self.person['curId'] = self['curId']
        # end handle [GC_SYNC_PHOTOFRAME] message attrs, auto generate do not change
        pass


class CG_REQ_SET_PHOTOFRAME (Packet):
    pass


class GC_SYNC_COTWARMUP_REWARD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COTWARMUP_REWARD] message attrs, auto generate do not change
        self.person['gotcotwarmupreward'] = self['gotcotwarmupreward']
        # end handle [GC_SYNC_COTWARMUP_REWARD] message attrs, auto generate do not change
        pass


class CG_REQUEST_VIEW_BWPPGAME (Packet):
    pass


class CG_QIXISTAR_TEAM_INVITE (Packet):
    pass


class CG_QIXISTAR_TEAM_RESPONSE (Packet):
    pass


class GC_SYNC_QIXISTAR_TEAM_INVITE_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYNC_QIXISTAR_TEAM_INVITE_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['name'] = self['name']
        # end handle [GC_SYNC_QIXISTAR_TEAM_INVITE_LIST] message attrs, auto generate do not change
        pass


class GC_QIXISTAR_DISMISS (Packet):
    def handle(self):
        # begin handle [GC_QIXISTAR_DISMISS] message attrs, auto generate do not change
        # end handle [GC_QIXISTAR_DISMISS] message attrs, auto generate do not change
        pass


class CG_QIXISTAR_UNLOCK (Packet):
    pass


class CG_QIXISTAR_SAVE_MUSIC (Packet):
    pass


class GC_SYNC_QIXISTAR_STARS_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_QIXISTAR_STARS_INFO] message attrs, auto generate do not change
        self.person['op'] = self['op']
        self.person['stars'] = self['stars']
        self.person['speed'] = self['speed']
        self.person['mateOp'] = self['mateOp']
        # end handle [GC_SYNC_QIXISTAR_STARS_INFO] message attrs, auto generate do not change
        pass


class CG_QIXISTAR_ASK_REWARD (Packet):
    pass


class GC_SYNC_QIXISTAR_REWARD_STATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_QIXISTAR_REWARD_STATE] message attrs, auto generate do not change
        self.person['state'] = self['state']
        # end handle [GC_SYNC_QIXISTAR_REWARD_STATE] message attrs, auto generate do not change
        pass


class CG_PICK_FREEDOM_COLOR_ITEM_STORAGE (Packet):
    pass


class GC_SYNC_QIXISTAR_MATE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_QIXISTAR_MATE] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['Name'] = self['Name']
        self.person['Level'] = self['Level']
        self.person['Prof'] = self['Prof']
        self.person['Sex'] = self['Sex']
        # end handle [GC_SYNC_QIXISTAR_MATE] message attrs, auto generate do not change
        pass


class CG_QIXISTAR_DISMISS (Packet):
    pass


class CG_GOBACK_BWPP_COPYSCENE (Packet):
    pass


class GC_SYNC_GOBACK_BWPP_COPYSCENE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GOBACK_BWPP_COPYSCENE_DATA] message attrs, auto generate do not change
        self.person['m_IsNeedShow'] = self['m_IsNeedShow']
        self.person['m_StartTime'] = self['m_StartTime']
        # end handle [GC_SYNC_GOBACK_BWPP_COPYSCENE_DATA] message attrs, auto generate do not change
        pass


class GC_SYNC_NEWPLAYECATCH_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NEWPLAYECATCH_DATA] message attrs, auto generate do not change
        self.person['StarttTime'] = self['StarttTime']
        self.person['LaterDays'] = self['LaterDays']
        self.person['LevelRewardRecords'] = self['LevelRewardRecords']
        self.person['RewardDay'] = self['RewardDay']
        self.person['taskStatus'] = self['taskStatus']
        self.person['extraDay'] = self['extraDay']
        self.person['extraStartTime'] = self['extraStartTime']
        # end handle [GC_SYNC_NEWPLAYECATCH_DATA] message attrs, auto generate do not change
        pass


class CG_GET_NEWPLAYERCATCH_REWARD (Packet):
    pass


class GC_SYNC_QIXISTAR_HISTORY_MUSIC (Packet):
    def handle(self):
        # begin handle [GC_SYNC_QIXISTAR_HISTORY_MUSIC] message attrs, auto generate do not change
        self.person['qxsMusic'] = self['qxsMusic']
        # end handle [GC_SYNC_QIXISTAR_HISTORY_MUSIC] message attrs, auto generate do not change
        pass


class GC_QL_SYNCDATA (Packet):
    def handle(self):
        # begin handle [GC_QL_SYNCDATA] message attrs, auto generate do not change
        self.person['dayflowercnt'] = self['dayflowercnt']
        self.person['allflowercnt'] = self['allflowercnt']
        self.person['dayreward'] = self['dayreward']
        self.person['allreward'] = self['allreward']
        self.person['extradata'] = self['extradata']
        # end handle [GC_QL_SYNCDATA] message attrs, auto generate do not change
        pass


class CG_QL_GETREWARD (Packet):
    pass


class GC_SYNC_SERVERCATCH_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SERVERCATCH_DATA] message attrs, auto generate do not change
        self.person['InServerCatchTime'] = self['InServerCatchTime']
        self.person['CatchExpMuti'] = self['CatchExpMuti']
        self.person['CatchRewardMuti'] = self['CatchRewardMuti']
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['CatchWeekRewardMuti'] = self['CatchWeekRewardMuti']
        self.person['CatchMonthRewardMuti'] = self['CatchMonthRewardMuti']
        # end handle [GC_SYNC_SERVERCATCH_DATA] message attrs, auto generate do not change
        pass


class GC_RET_UNLOCK_PHOTOFRAME (Packet):
    def handle(self):
        # begin handle [GC_RET_UNLOCK_PHOTOFRAME] message attrs, auto generate do not change
        self.person['id'] = self['id']
        # end handle [GC_RET_UNLOCK_PHOTOFRAME] message attrs, auto generate do not change
        pass


class GC_CHATHISTORY (Packet):
    def handle(self):
        # begin handle [GC_CHATHISTORY] message attrs, auto generate do not change
        self.person['Channel'] = self['Channel']
        self.person['ChatInfo'] = self['ChatInfo']
        # end handle [GC_CHATHISTORY] message attrs, auto generate do not change
        pass


class GC_SYNC_SERVER_TREASURE_COMPASS_RECORD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SERVER_TREASURE_COMPASS_RECORD] message attrs, auto generate do not change
        self.person['TreasureRecord'] = self['TreasureRecord']
        self.person['IsMyRecord'] = self['IsMyRecord']
        # end handle [GC_SYNC_SERVER_TREASURE_COMPASS_RECORD] message attrs, auto generate do not change
        pass


class GC_PLAY_SKILLRANGE_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_PLAY_SKILLRANGE_EFFECT] message attrs, auto generate do not change
        self.person['objID'] = self['objID']
        self.person['rangeDataID'] = self['rangeDataID']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        self.person['speed'] = self['speed']
        # end handle [GC_PLAY_SKILLRANGE_EFFECT] message attrs, auto generate do not change
        pass


class GC_SYNC_ZC_TASK_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ZC_TASK_INFO] message attrs, auto generate do not change
        self.person['taskList'] = self['taskList']
        self.person['type'] = self['type']
        # end handle [GC_SYNC_ZC_TASK_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_ZC_PIECE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ZC_PIECE_INFO] message attrs, auto generate do not change
        self.person['pieceState'] = self['pieceState']
        self.person['almightyPieceCount'] = self['almightyPieceCount']
        self.person['receivePieceCount'] = self['receivePieceCount']
        # end handle [GC_SYNC_ZC_PIECE_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_ZC_TICKET_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ZC_TICKET_INFO] message attrs, auto generate do not change
        self.person['count'] = self['count']
        # end handle [GC_SYNC_ZC_TICKET_INFO] message attrs, auto generate do not change
        pass


class CG_ZC_ASK_REWARD (Packet):
    pass


class CG_ZC_PIECE_OP (Packet):
    pass


class GC_ZC_PIECE_OP_RET (Packet):
    def handle(self):
        # begin handle [GC_ZC_PIECE_OP_RET] message attrs, auto generate do not change
        self.person['reuslt'] = self['reuslt']
        self.person['type'] = self['type']
        self.person['pieceId'] = self['pieceId']
        self.person['targetGuid'] = self['targetGuid']
        # end handle [GC_ZC_PIECE_OP_RET] message attrs, auto generate do not change
        pass


class GC_SYNC_ZC_ASKER_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ZC_ASKER_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['name'] = self['name']
        self.person['level'] = self['level']
        self.person['prof'] = self['prof']
        self.person['portrait'] = self['portrait']
        self.person['portraitFrame'] = self['portraitFrame']
        self.person['pieceId'] = self['pieceId']
        self.person['sex'] = self['sex']
        self.person['hasNewAsker'] = self['hasNewAsker']
        # end handle [GC_SYNC_ZC_ASKER_LIST] message attrs, auto generate do not change
        pass


class GC_SYNC_ZC_STAGEREWARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ZC_STAGEREWARD_INFO] message attrs, auto generate do not change
        self.person['rewardState'] = self['rewardState']
        # end handle [GC_SYNC_ZC_STAGEREWARD_INFO] message attrs, auto generate do not change
        pass


class CG_USE_CLIENTDIR_FORSKILL (Packet):
    pass


class CG_FAIRY_SKILL_INHERIT (Packet):
    pass


class GC_SYNC_NEW_FIRST_RECHARGE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NEW_FIRST_RECHARGE_DATA] message attrs, auto generate do not change
        self.person['begintime'] = self['begintime']
        self.person['rewardstate'] = self['rewardstate']
        self.person['rewardtime'] = self['rewardtime']
        # end handle [GC_SYNC_NEW_FIRST_RECHARGE_DATA] message attrs, auto generate do not change
        pass


class CG_GET_NEW_FIRST_RECHARGE_REWARD (Packet):
    pass


class GC_SYNC_COLLECTION_SHOP_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_COLLECTION_SHOP_INFO] message attrs, auto generate do not change
        self.person['mainShopId'] = self['mainShopId']
        self.person['subShopId'] = self['subShopId']
        self.person['limitId'] = self['limitId']
        self.person['limitItemCount'] = self['limitItemCount']
        self.person['tokenCount'] = self['tokenCount']
        # end handle [GC_SYNC_COLLECTION_SHOP_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_BUY_COLLECTION_SHOP_ITEM (Packet):
    pass


class GC_NOTICE_NEW_FIRST_RECHARGE_WINDOW (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_NEW_FIRST_RECHARGE_WINDOW] message attrs, auto generate do not change
        # end handle [GC_NOTICE_NEW_FIRST_RECHARGE_WINDOW] message attrs, auto generate do not change
        pass


class CG_REQ_CHANGEREMAKENAME_ZJN (Packet):
    pass


class GC_CHANGEREMAKENAME_RET_ZJN (Packet):
    def handle(self):
        # begin handle [GC_CHANGEREMAKENAME_RET_ZJN] message attrs, auto generate do not change
        # end handle [GC_CHANGEREMAKENAME_RET_ZJN] message attrs, auto generate do not change
        pass


class CG_REQ_CHANGEREMAKENAME (Packet):
    pass


class GC_CHANGEREMAKENAME_RET (Packet):
    def handle(self):
        # begin handle [GC_CHANGEREMAKENAME_RET] message attrs, auto generate do not change
        self.person['ret'] = self['ret']
        # end handle [GC_CHANGEREMAKENAME_RET] message attrs, auto generate do not change
        pass


class GC_SYNC_LEVELATTRIBUTE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_LEVELATTRIBUTE] message attrs, auto generate do not change
        self.person['basehpmax'] = self['basehpmax']
        self.person['basephyattack'] = self['basephyattack']
        self.person['basephyattackmin'] = self['basephyattackmin']
        self.person['basephyattackmax'] = self['basephyattackmax']
        self.person['basemagattack'] = self['basemagattack']
        self.person['basemagattackmin'] = self['basemagattackmin']
        self.person['basemagattackmax'] = self['basemagattackmax']
        # end handle [GC_SYNC_LEVELATTRIBUTE] message attrs, auto generate do not change
        pass


class GC_SYNC_DISCOUNT_LIMIT_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DISCOUNT_LIMIT_DATA] message attrs, auto generate do not change
        self.person['BeginTime'] = self['BeginTime']
        self.person['RewardTime'] = self['RewardTime']
        self.person['AccumulateRewardState'] = self['AccumulateRewardState']
        self.person['GiftRewardState'] = self['GiftRewardState']
        self.person['RechargeAccumulate'] = self['RechargeAccumulate']
        # end handle [GC_SYNC_DISCOUNT_LIMIT_DATA] message attrs, auto generate do not change
        pass


class CG_GET_DISCOUNTLIMIT_ACCUMULATE_REWARD (Packet):
    pass


class CG_GET_DISCOUNTLIMIT_GIFT_REWARD (Packet):
    pass


class GC_NOTICE_DISCOUNTLIMIT_WINDOW (Packet):
    def handle(self):
        # begin handle [GC_NOTICE_DISCOUNTLIMIT_WINDOW] message attrs, auto generate do not change
        # end handle [GC_NOTICE_DISCOUNTLIMIT_WINDOW] message attrs, auto generate do not change
        pass


class GC_SYNC_TIANSHUBOX (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TIANSHUBOX] message attrs, auto generate do not change
        self.person['boxStateList'] = self['boxStateList']
        self.person['isLogin'] = self['isLogin']
        # end handle [GC_SYNC_TIANSHUBOX] message attrs, auto generate do not change
        pass


class GC_RET_UNLOCK_TIANSHUBOX (Packet):
    def handle(self):
        # begin handle [GC_RET_UNLOCK_TIANSHUBOX] message attrs, auto generate do not change
        self.person['boxID'] = self['boxID']
        # end handle [GC_RET_UNLOCK_TIANSHUBOX] message attrs, auto generate do not change
        pass


class CG_TIANSHUBOX_FILL (Packet):
    pass


class GC_RET_TIANSHUBOX_FILL (Packet):
    def handle(self):
        # begin handle [GC_RET_TIANSHUBOX_FILL] message attrs, auto generate do not change
        self.person['boxID'] = self['boxID']
        self.person['slotIndex'] = self['slotIndex']
        # end handle [GC_RET_TIANSHUBOX_FILL] message attrs, auto generate do not change
        pass


class CG_TIANSHUBOX_LEVELUP (Packet):
    pass


class GC_RET_TIANSHUBOX_LEVELUP (Packet):
    def handle(self):
        # begin handle [GC_RET_TIANSHUBOX_LEVELUP] message attrs, auto generate do not change
        self.person['boxID'] = self['boxID']
        self.person['level'] = self['level']
        # end handle [GC_RET_TIANSHUBOX_LEVELUP] message attrs, auto generate do not change
        pass


class CG_ADD_FAIRY_ATTR_POINTS_TEMP (Packet):
    pass


class GC_ADD_FAIRY_ATTR_POINTS_TEMP (Packet):
    def handle(self):
        # begin handle [GC_ADD_FAIRY_ATTR_POINTS_TEMP] message attrs, auto generate do not change
        self.person['fairyguid'] = self['fairyguid']
        self.person['nStrength'] = self['nStrength']
        self.person['nAgility'] = self['nAgility']
        self.person['nVitality'] = self['nVitality']
        self.person['nSpiritual'] = self['nSpiritual']
        self.person['combatValue'] = self['combatValue']
        # end handle [GC_ADD_FAIRY_ATTR_POINTS_TEMP] message attrs, auto generate do not change
        pass


class GC_SYNC_BROTHERHOOD_SELF_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BROTHERHOOD_SELF_INFO] message attrs, auto generate do not change
        self.person['weeklyRewardState'] = self['weeklyRewardState']
        self.person['milestoneRewardState'] = self['milestoneRewardState']
        self.person['taskList'] = self['taskList']
        self.person['taskDataType'] = self['taskDataType']
        self.person['curWeekServerLevel'] = self['curWeekServerLevel']
        # end handle [GC_SYNC_BROTHERHOOD_SELF_INFO] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_ASK_REWARD (Packet):
    pass


class CG_BROTHERHOOD_LOG (Packet):
    pass


class GC_BROTHERHOOD_LOG (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_LOG] message attrs, auto generate do not change
        self.person['logType'] = self['logType']
        self.person['recordTime'] = self['recordTime']
        self.person['param1'] = self['param1']
        self.person['param2'] = self['param2']
        # end handle [GC_BROTHERHOOD_LOG] message attrs, auto generate do not change
        pass


class GC_SYNC_POJUNQISHA_ENERGY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_POJUNQISHA_ENERGY_INFO] message attrs, auto generate do not change
        self.person['showEnergy'] = self['showEnergy']
        self.person['curEnergyCount'] = self['curEnergyCount']
        self.person['maxEnergyCount'] = self['maxEnergyCount']
        # end handle [GC_SYNC_POJUNQISHA_ENERGY_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_FANGONG_HELP_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_FANGONG_HELP_INFO] message attrs, auto generate do not change
        self.person['xianFengHelp'] = self['xianFengHelp']
        self.person['sunBoChengHelp'] = self['sunBoChengHelp']
        # end handle [GC_SYNC_FANGONG_HELP_INFO] message attrs, auto generate do not change
        pass


class CG_REQUEST_SERVANTEQUIP_LASTRECAST_INFO (Packet):
    pass


class GC_RET_SERVANTEQUIP_LASTRECAST_INFO (Packet):
    def handle(self):
        # begin handle [GC_RET_SERVANTEQUIP_LASTRECAST_INFO] message attrs, auto generate do not change
        self.person['equipguid'] = self['equipguid']
        self.person['AttrId'] = self['AttrId']
        self.person['AttrVal'] = self['AttrVal']
        self.person['AttrType'] = self['AttrType']
        # end handle [GC_RET_SERVANTEQUIP_LASTRECAST_INFO] message attrs, auto generate do not change
        pass


class CG_GET_ERUDITE_REWARD (Packet):
    pass


class CG_GET_KABINETT_ANECDOTE_TREWARD (Packet):
    pass


class GC_SYNC_KABINETT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_KABINETT_INFO] message attrs, auto generate do not change
        self.person['anecdotereward'] = self['anecdotereward']
        self.person['eruditenum'] = self['eruditenum']
        # end handle [GC_SYNC_KABINETT_INFO] message attrs, auto generate do not change
        pass


class CG_FV_LOBBY_OPERATE (Packet):
    pass


class GC_XINPO_INFO (Packet):
    def handle(self):
        # begin handle [GC_XINPO_INFO] message attrs, auto generate do not change
        self.person['xinpodata'] = self['xinpodata']
        self.person['gongminglv'] = self['gongminglv']
        # end handle [GC_XINPO_INFO] message attrs, auto generate do not change
        pass


class CG_USE_BINGXUEJIE_SNOWBALL (Packet):
    pass


class GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS] message attrs, auto generate do not change
        self.person['progress'] = self['progress']
        # end handle [GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS] message attrs, auto generate do not change
        pass


class GC_FIXED_CAMERA (Packet):
    def handle(self):
        # begin handle [GC_FIXED_CAMERA] message attrs, auto generate do not change
        self.person['BanScale'] = self['BanScale']
        self.person['Scale'] = self['Scale']
        self.person['BanVertical'] = self['BanVertical']
        self.person['Vertical'] = self['Vertical']
        self.person['Reserved1'] = self['Reserved1']
        self.person['Reserved2'] = self['Reserved2']
        self.person['Reserved3'] = self['Reserved3']
        # end handle [GC_FIXED_CAMERA] message attrs, auto generate do not change
        pass


class CG_CPS_PICKUP (Packet):
    pass


class CG_REQ_BINGXUEJIE_SNOWMAN_DAILY_AWARD (Packet):
    pass


class CG_REQ_BINGXUEJIE_SNOWMAN_PROGRESS_AWARD (Packet):
    pass


class GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS_AWARD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS_AWARD] message attrs, auto generate do not change
        self.person['bGet'] = self['bGet']
        self.person['getDaily'] = self['getDaily']
        # end handle [GC_SYNC_BINGXUEJIE_SNOWMAN_PROGRESS_AWARD] message attrs, auto generate do not change
        pass


class GC_SYNC_BINGXUEJIE_QUIZ_RECORD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BINGXUEJIE_QUIZ_RECORD] message attrs, auto generate do not change
        self.person['dailyBest'] = self['dailyBest']
        self.person['personalBest'] = self['personalBest']
        self.person['maxCount'] = self['maxCount']
        self.person['getBestAward'] = self['getBestAward']
        self.person['getDailyAward'] = self['getDailyAward']
        # end handle [GC_SYNC_BINGXUEJIE_QUIZ_RECORD] message attrs, auto generate do not change
        pass


class CG_TRIGGER_SPECIAL_NPC (Packet):
    pass


class CG_REQ_BINGXUEJIE_QUIZ_DAILY_AWARD (Packet):
    pass


class CG_REQ_BINGXUEJIE_QUIZ_BEST_AWARD (Packet):
    pass


class GC_FV_COPYSCENE_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_FV_COPYSCENE_NOTICE] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['param'] = self['param']
        # end handle [GC_FV_COPYSCENE_NOTICE] message attrs, auto generate do not change
        pass


class GC_FV_RESULT (Packet):
    def handle(self):
        # begin handle [GC_FV_RESULT] message attrs, auto generate do not change
        self.person['name'] = self['name']
        self.person['score'] = self['score']
        self.person['myTeamIndex'] = self['myTeamIndex']
        self.person['rewardItemIds'] = self['rewardItemIds']
        self.person['rewardItemCnts'] = self['rewardItemCnts']
        self.person['rewardBinds'] = self['rewardBinds']
        # end handle [GC_FV_RESULT] message attrs, auto generate do not change
        pass


class GC_FV_RANKMINIINFO (Packet):
    def handle(self):
        # begin handle [GC_FV_RANKMINIINFO] message attrs, auto generate do not change
        self.person['rank'] = self['rank']
        self.person['score'] = self['score']
        self.person['cyby_cnt'] = self['cyby_cnt']
        # end handle [GC_FV_RANKMINIINFO] message attrs, auto generate do not change
        pass


class GC_FV_RANK_FULLINFO (Packet):
    def handle(self):
        # begin handle [GC_FV_RANK_FULLINFO] message attrs, auto generate do not change
        self.person['rank'] = self['rank']
        self.person['score'] = self['score']
        self.person['cyby_cnt'] = self['cyby_cnt']
        self.person['names'] = self['names']
        self.person['scores'] = self['scores']
        self.person['buffNames'] = self['buffNames']
        self.person['buffDescs'] = self['buffDescs']
        self.person['syncBaseFlag'] = self['syncBaseFlag']
        self.person['syncRankFlag'] = self['syncRankFlag']
        self.person['syncBuffFlag'] = self['syncBuffFlag']
        self.person['syncTeamMemberInfoFlag'] = self['syncTeamMemberInfoFlag']
        self.person['memberInfos'] = self['memberInfos']
        self.person['hzBuffDataIds'] = self['hzBuffDataIds']
        self.person['syncMemberTeamInfoFlag'] = self['syncMemberTeamInfoFlag']
        self.person['memberTeamInfos'] = self['memberTeamInfos']
        # end handle [GC_FV_RANK_FULLINFO] message attrs, auto generate do not change
        pass


class CG_FV_REQ_RANK_FULLINFO (Packet):
    pass


class GC_FV_SKILL_LIST (Packet):
    def handle(self):
        # begin handle [GC_FV_SKILL_LIST] message attrs, auto generate do not change
        self.person['skillList'] = self['skillList']
        # end handle [GC_FV_SKILL_LIST] message attrs, auto generate do not change
        pass


class CG_FV_USE_SKILL (Packet):
    pass


class GC_FV_CYBYINFO (Packet):
    def handle(self):
        # begin handle [GC_FV_CYBYINFO] message attrs, auto generate do not change
        self.person['objServerId'] = self['objServerId']
        self.person['cybyList'] = self['cybyList']
        # end handle [GC_FV_CYBYINFO] message attrs, auto generate do not change
        pass


class CG_SERVANTEQUIP_ITEM (Packet):
    pass


class CG_UNSERVANTEQUIP_ITEM (Packet):
    pass


class CG_UPGRADE_XINPO (Packet):
    pass


class GC_FV_NPCINFO (Packet):
    def handle(self):
        # begin handle [GC_FV_NPCINFO] message attrs, auto generate do not change
        self.person['npcTypes'] = self['npcTypes']
        self.person['posX'] = self['posX']
        self.person['posY'] = self['posY']
        self.person['posZ'] = self['posZ']
        # end handle [GC_FV_NPCINFO] message attrs, auto generate do not change
        pass


class GC_BROADCAST_BINGXUEJIE_QUIZ_RESULT (Packet):
    def handle(self):
        # begin handle [GC_BROADCAST_BINGXUEJIE_QUIZ_RESULT] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['result'] = self['result']
        # end handle [GC_BROADCAST_BINGXUEJIE_QUIZ_RESULT] message attrs, auto generate do not change
        pass


class CG_WUXING_SHORTCUT_AFFIX (Packet):
    pass


class GC_WUXING_SHORTCUT_AFFIX (Packet):
    def handle(self):
        # begin handle [GC_WUXING_SHORTCUT_AFFIX] message attrs, auto generate do not change
        self.person['affixes'] = self['affixes']
        self.person['refreshCost'] = self['refreshCost']
        # end handle [GC_WUXING_SHORTCUT_AFFIX] message attrs, auto generate do not change
        pass


class CG_WUXING_SHORTCUT_FIGHT (Packet):
    pass


class CG_TREASURE_COMPASS_RESET (Packet):
    pass


class GC_TREASURE_COMPASS_RESET_RET (Packet):
    def handle(self):
        # begin handle [GC_TREASURE_COMPASS_RESET_RET] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['RewardIndex'] = self['RewardIndex']
        # end handle [GC_TREASURE_COMPASS_RESET_RET] message attrs, auto generate do not change
        pass


class CG_REQ_NEWBIEBANK_GET_AWARD (Packet):
    pass


class GC_SYNC_NEWBIEBANK_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_NEWBIEBANK_INFO] message attrs, auto generate do not change
        self.person['dataId'] = self['dataId']
        self.person['getAward'] = self['getAward']
        self.person['rechargeDays'] = self['rechargeDays']
        self.person['dailyRecharge'] = self['dailyRecharge']
        # end handle [GC_SYNC_NEWBIEBANK_INFO] message attrs, auto generate do not change
        pass


class CG_ITEM_SUBSCRIBE_OPERATION (Packet):
    pass


class GC_SYNC_ITEM_SUBSCRIBE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ITEM_SUBSCRIBE] message attrs, auto generate do not change
        self.person['shopType'] = self['shopType']
        self.person['shopId'] = self['shopId']
        # end handle [GC_SYNC_ITEM_SUBSCRIBE] message attrs, auto generate do not change
        pass


class GC_HONGBAO_COVER (Packet):
    def handle(self):
        # begin handle [GC_HONGBAO_COVER] message attrs, auto generate do not change
        self.person['Covers'] = self['Covers']
        self.person['UseCoverId'] = self['UseCoverId']
        # end handle [GC_HONGBAO_COVER] message attrs, auto generate do not change
        pass


class CG_HONGBAO_COVER_OP (Packet):
    pass


class GC_HONGYUN_INFO (Packet):
    def handle(self):
        # begin handle [GC_HONGYUN_INFO] message attrs, auto generate do not change
        self.person['SendRedPackHY'] = self['SendRedPackHY']
        self.person['ReceiveRedPakHY'] = self['ReceiveRedPakHY']
        self.person['CurRound'] = self['CurRound']
        self.person['CurRoundHY'] = self['CurRoundHY']
        self.person['CurHY'] = self['CurHY']
        self.person['nIndex'] = self['nIndex']
        self.person['bFlag'] = self['bFlag']
        # end handle [GC_HONGYUN_INFO] message attrs, auto generate do not change
        pass


class CG_HONGYUN_RECEIVE (Packet):
    pass


class GC_SYNC_GUILDVAULTDATA_ALL (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILDVAULTDATA_ALL] message attrs, auto generate do not change
        self.person['guildcashgift'] = self['guildcashgift']
        self.person['celebrationkey'] = self['celebrationkey']
        self.person['vaultlevel'] = self['vaultlevel']
        self.person['vaultprogress'] = self['vaultprogress']
        self.person['vaultnorrewardid'] = self['vaultnorrewardid']
        self.person['vaultunurewardid'] = self['vaultunurewardid']
        self.person['vaultlog'] = self['vaultlog']
        self.person['vaultunusualrewardInfo'] = self['vaultunusualrewardInfo']
        # end handle [GC_SYNC_GUILDVAULTDATA_ALL] message attrs, auto generate do not change
        pass


class GC_SYNC_GUILDVAULTDATA_SIMPLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILDVAULTDATA_SIMPLE] message attrs, auto generate do not change
        self.person['guildcashgift'] = self['guildcashgift']
        self.person['celebrationkey'] = self['celebrationkey']
        # end handle [GC_SYNC_GUILDVAULTDATA_SIMPLE] message attrs, auto generate do not change
        pass


class CG_DONATIONGUILDCASHGIFT (Packet):
    pass


class GC_DONATIONGUILDCASHGIFT_RET (Packet):
    def handle(self):
        # begin handle [GC_DONATIONGUILDCASHGIFT_RET] message attrs, auto generate do not change
        self.person['donationtype'] = self['donationtype']
        self.person['donationexp'] = self['donationexp']
        # end handle [GC_DONATIONGUILDCASHGIFT_RET] message attrs, auto generate do not change
        pass


class CG_GUILDVAULT_LOTTERY (Packet):
    pass


class CG_GUILDVAULT_LOTTERY_RET (Packet):
    pass


class GC_GUILDVAULT_LOTTERY_RET (Packet):
    def handle(self):
        # begin handle [GC_GUILDVAULT_LOTTERY_RET] message attrs, auto generate do not change
        self.person['rewardtype'] = self['rewardtype']
        self.person['rewardid'] = self['rewardid']
        self.person['rewarditemindex'] = self['rewarditemindex']
        # end handle [GC_GUILDVAULT_LOTTERY_RET] message attrs, auto generate do not change
        pass


class CG_BWGW_FASTCOMMAND (Packet):
    pass


class GC_BWGW_BATTLE_INFO (Packet):
    def handle(self):
        # begin handle [GC_BWGW_BATTLE_INFO] message attrs, auto generate do not change
        self.person['units'] = self['units']
        self.person['m_CurHonorScore'] = self['m_CurHonorScore']
        # end handle [GC_BWGW_BATTLE_INFO] message attrs, auto generate do not change
        pass


class CG_BWGW_REQ_PLAYER_DETAIL (Packet):
    pass


class GC_BWGW_BATTLE_DETAIL (Packet):
    def handle(self):
        # begin handle [GC_BWGW_BATTLE_DETAIL] message attrs, auto generate do not change
        self.person['guildsInfo'] = self['guildsInfo']
        self.person['result'] = self['result']
        self.person['winguildguid'] = self['winguildguid']
        # end handle [GC_BWGW_BATTLE_DETAIL] message attrs, auto generate do not change
        pass


class CG_SET_BWGW_MAINSCENE_GUILDROLE (Packet):
    pass


class GC_BWGW_MAINSCENE_GUILDROLE (Packet):
    def handle(self):
        # begin handle [GC_BWGW_MAINSCENE_GUILDROLE] message attrs, auto generate do not change
        self.person['TeamLimit'] = self['TeamLimit']
        self.person['CombatLimit'] = self['CombatLimit']
        self.person['JobLimit'] = self['JobLimit']
        # end handle [GC_BWGW_MAINSCENE_GUILDROLE] message attrs, auto generate do not change
        pass


class CG_GET_BWGW_GUILD_WAR_SCENEINFO (Packet):
    pass


class GC_BWGW_GUILD_WAR_SCENEINFO (Packet):
    def handle(self):
        # begin handle [GC_BWGW_GUILD_WAR_SCENEINFO] message attrs, auto generate do not change
        self.person['SceneClassId'] = self['SceneClassId']
        self.person['SceneNum'] = self['SceneNum']
        self.person['TeamLimit'] = self['TeamLimit']
        self.person['CombatLimit'] = self['CombatLimit']
        self.person['JobLimit'] = self['JobLimit']
        # end handle [GC_BWGW_GUILD_WAR_SCENEINFO] message attrs, auto generate do not change
        pass


class CG_ENTER_BWGW_GUILD_WAR_SCENE (Packet):
    pass


class GC_BWGW_RES_UPDATE (Packet):
    def handle(self):
        # begin handle [GC_BWGW_RES_UPDATE] message attrs, auto generate do not change
        self.person['index'] = self['index']
        self.person['OwnerGuildGuid'] = self['OwnerGuildGuid']
        self.person['state'] = self['state']
        self.person['groupAPlayerNum'] = self['groupAPlayerNum']
        self.person['groupBPlayerNum'] = self['groupBPlayerNum']
        self.person['progress'] = self['progress']
        self.person['GuildAGuid'] = self['GuildAGuid']
        self.person['GuildBGuid'] = self['GuildBGuid']
        # end handle [GC_BWGW_RES_UPDATE] message attrs, auto generate do not change
        pass


class CG_BWGW_USESKILL (Packet):
    pass


class CG_CBZL_GETEXP (Packet):
    pass


class CG_CBZL_GETLEVELREWARD (Packet):
    pass


class GC_CBZL_ALLINFO (Packet):
    def handle(self):
        # begin handle [GC_CBZL_ALLINFO] message attrs, auto generate do not change
        self.person['rewardid'] = self['rewardid']
        self.person['level'] = self['level']
        self.person['progress'] = self['progress']
        self.person['taskinfo'] = self['taskinfo']
        self.person['levelreward'] = self['levelreward']
        self.person['extrarewardcnt'] = self['extrarewardcnt']
        self.person['extraprogress'] = self['extraprogress']
        self.person['hasgetextrarewardcnt'] = self['hasgetextrarewardcnt']
        # end handle [GC_CBZL_ALLINFO] message attrs, auto generate do not change
        pass


class GC_CBZL_TASKINFO (Packet):
    def handle(self):
        # begin handle [GC_CBZL_TASKINFO] message attrs, auto generate do not change
        self.person['taskinfo'] = self['taskinfo']
        # end handle [GC_CBZL_TASKINFO] message attrs, auto generate do not change
        pass


class GC_BWGW_MATCH_FIGHT_DATA (Packet):
    def handle(self):
        # begin handle [GC_BWGW_MATCH_FIGHT_DATA] message attrs, auto generate do not change
        self.person['FightGuildInfo'] = self['FightGuildInfo']
        self.person['divisionId'] = self['divisionId']
        self.person['battleRound'] = self['battleRound']
        # end handle [GC_BWGW_MATCH_FIGHT_DATA] message attrs, auto generate do not change
        pass


class CG_BWGW_MATCH_FIGHT_DATA (Packet):
    pass


class CG_REQ_ITEM_SUBSCRIBE_BUY (Packet):
    pass


class GC_Sync_All_TXMQ_Info (Packet):
    def handle(self):
        # begin handle [GC_Sync_All_TXMQ_Info] message attrs, auto generate do not change
        self.person['allTXMQInfo'] = self['allTXMQInfo']
        self.person['op'] = self['op']
        self.person['MQId'] = self['MQId']
        self.person['MWId'] = self['MWId']
        # end handle [GC_Sync_All_TXMQ_Info] message attrs, auto generate do not change
        pass


class CG_TXMQ_OP (Packet):
    pass


class GC_SYNC_HONGBAO_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HONGBAO_INFO] message attrs, auto generate do not change
        self.person['HongBaoSendYuanbaoNumWeekly'] = self['HongBaoSendYuanbaoNumWeekly']
        self.person['HongBaoReceiveYuanbaoNumDaily'] = self['HongBaoReceiveYuanbaoNumDaily']
        self.person['HongBaoSendKoulingNumWeekly'] = self['HongBaoSendKoulingNumWeekly']
        self.person['HongBaoReceiveKoulingNumDaily'] = self['HongBaoReceiveKoulingNumDaily']
        # end handle [GC_SYNC_HONGBAO_INFO] message attrs, auto generate do not change
        pass


class CG_HONGBAO_REQ_INFO (Packet):
    pass


class GC_SYNC_SERVER_ROOKIE_COMPASS_RECORD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SERVER_ROOKIE_COMPASS_RECORD] message attrs, auto generate do not change
        self.person['TreasureRecord'] = self['TreasureRecord']
        self.person['IsMyRecord'] = self['IsMyRecord']
        # end handle [GC_SYNC_SERVER_ROOKIE_COMPASS_RECORD] message attrs, auto generate do not change
        pass


class CG_BWGW_GET_MAIN_SCENE_LIMIT_INFO (Packet):
    pass


class GC_SYNC_PERIODBESTSELLER_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PERIODBESTSELLER_DATA] message attrs, auto generate do not change
        self.person['m_PeriodBestSellerList'] = self['m_PeriodBestSellerList']
        # end handle [GC_SYNC_PERIODBESTSELLER_DATA] message attrs, auto generate do not change
        pass


class GC_NPC_SHOW_TARGETHEADINFO (Packet):
    def handle(self):
        # begin handle [GC_NPC_SHOW_TARGETHEADINFO] message attrs, auto generate do not change
        self.person['npcServerId'] = self['npcServerId']
        self.person['targetName'] = self['targetName']
        # end handle [GC_NPC_SHOW_TARGETHEADINFO] message attrs, auto generate do not change
        pass


class CG_USE_COTCOIN (Packet):
    pass


class GC_SERVANT_DRAW_BOX_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_DRAW_BOX_CONFIG] message attrs, auto generate do not change
        self.person['items'] = self['items']
        # end handle [GC_SERVANT_DRAW_BOX_CONFIG] message attrs, auto generate do not change
        pass


class GC_SERVANT_DRAW_SET_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_DRAW_SET_CONFIG] message attrs, auto generate do not change
        self.person['items'] = self['items']
        # end handle [GC_SERVANT_DRAW_SET_CONFIG] message attrs, auto generate do not change
        pass


class GC_SERVANT_DRAW_SELF_INFO (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_DRAW_SELF_INFO] message attrs, auto generate do not change
        self.person['unGetBigAwardDrawCnt'] = self['unGetBigAwardDrawCnt']
        self.person['unGetBigAwardDrawCntUp'] = self['unGetBigAwardDrawCntUp']
        self.person['unGetBigAwardDrawCntNp'] = self['unGetBigAwardDrawCntNp']
        self.person['weekFreeHaveGet'] = self['weekFreeHaveGet']
        self.person['score'] = self['score']
        self.person['prayInfo'] = self['prayInfo']
        # end handle [GC_SERVANT_DRAW_SELF_INFO] message attrs, auto generate do not change
        pass


class CG_SERVANT_DRAW (Packet):
    pass


class GC_SERVANT_DRAW_RESULT (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_DRAW_RESULT] message attrs, auto generate do not change
        self.person['poolType'] = self['poolType']
        self.person['opType'] = self['opType']
        self.person['itemIds'] = self['itemIds']
        self.person['itemCnts'] = self['itemCnts']
        # end handle [GC_SERVANT_DRAW_RESULT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_BATTLE_SCHEME] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['scheme'] = self['scheme']
        # end handle [GC_SYNC_BATTLE_SCHEME] message attrs, auto generate do not change
        pass


class CG_SERVANT_DRAW_BUY (Packet):
    pass


class GC_SYNC_ONLINEREMINDER (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ONLINEREMINDER] message attrs, auto generate do not change
        self.person['onlineGuid'] = self['onlineGuid']
        # end handle [GC_SYNC_ONLINEREMINDER] message attrs, auto generate do not change
        pass


class GC_SYNC_ACTIVITYNIGHTGUIDEINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ACTIVITYNIGHTGUIDEINFO] message attrs, auto generate do not change
        self.person['starttime'] = self['starttime']
        self.person['haveclick'] = self['haveclick']
        self.person['havegetreward'] = self['havegetreward']
        self.person['firsttrigger'] = self['firsttrigger']
        self.person['haveclickpapertip'] = self['haveclickpapertip']
        # end handle [GC_SYNC_ACTIVITYNIGHTGUIDEINFO] message attrs, auto generate do not change
        pass


class CG_HAVECLICK_ACTIVITYNIGHTGUIDE (Packet):
    pass


class CG_GETREWARD_ACTIVITYNIGHTGUIDE (Packet):
    pass


class GC_SCENE_TOGGLE_OBJ (Packet):
    def handle(self):
        # begin handle [GC_SCENE_TOGGLE_OBJ] message attrs, auto generate do not change
        self.person['objName'] = self['objName']
        self.person['action'] = self['action']
        self.person['sceneClassId'] = self['sceneClassId']
        # end handle [GC_SCENE_TOGGLE_OBJ] message attrs, auto generate do not change
        pass


class GC_RET_SWITCH_MAIN_BATTLE_SCHEME (Packet):
    def handle(self):
        # begin handle [GC_RET_SWITCH_MAIN_BATTLE_SCHEME] message attrs, auto generate do not change
        self.person['schemeId'] = self['schemeId']
        self.person['ret'] = self['ret']
        # end handle [GC_RET_SWITCH_MAIN_BATTLE_SCHEME] message attrs, auto generate do not change
        pass


class CG_SERVANT_DRAW_SET_PRAY (Packet):
    pass


class GC_SERVANT_DRAW_RSP_SET_PRAY (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_DRAW_RSP_SET_PRAY] message attrs, auto generate do not change
        self.person['poolType'] = self['poolType']
        self.person['servantId'] = self['servantId']
        self.person['k'] = self['k']
        self.person['success'] = self['success']
        # end handle [GC_SERVANT_DRAW_RSP_SET_PRAY] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_HUAGUANJIE_PLAY_EFFECT] message attrs, auto generate do not change
        self.person['giftId'] = self['giftId']
        self.person['senderName'] = self['senderName']
        self.person['receiverName'] = self['receiverName']
        self.person['count'] = self['count']
        # end handle [GC_HUAGUANJIE_PLAY_EFFECT] message attrs, auto generate do not change
        pass


class CG_ASK_GREETING_REWARD (Packet):
    pass


class CG_REQ_GIFT_LIST (Packet):
    pass


class GC_RET_GIFT_LIST (Packet):
    def handle(self):
        # begin handle [GC_RET_GIFT_LIST] message attrs, auto generate do not change
        self.person['guid'] = self['guid']
        self.person['name'] = self['name']
        self.person['rankVal'] = self['rankVal']
        # end handle [GC_RET_GIFT_LIST] message attrs, auto generate do not change
        pass


class GC_SYNC_HUAGUANJIE_EXCHANGE_SHOP_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HUAGUANJIE_EXCHANGE_SHOP_INFO] message attrs, auto generate do not change
        self.person['limitId'] = self['limitId']
        self.person['limitItemCount'] = self['limitItemCount']
        self.person['tokenNum'] = self['tokenNum']
        self.person['tokenCount'] = self['tokenCount']
        # end handle [GC_SYNC_HUAGUANJIE_EXCHANGE_SHOP_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_BUY_HUAGUANJIE_EXCHANGE_ITEM (Packet):
    pass


class CG_ASK_ANSWERACTIVITY_INFO (Packet):
    pass


class CG_ASK_ANSWERACTIVITY_QUESTION (Packet):
    pass


class GC_SYNC_ANSWERACTIVITY_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ANSWERACTIVITY_INFO] message attrs, auto generate do not change
        self.person['round'] = self['round']
        self.person['question'] = self['question']
        self.person['npcposx'] = self['npcposx']
        self.person['npcposy'] = self['npcposy']
        self.person['npcposz'] = self['npcposz']
        self.person['hasgetreward'] = self['hasgetreward']
        self.person['rankguidlist'] = self['rankguidlist']
        self.person['ranknamelist'] = self['ranknamelist']
        self.person['ranktimelist'] = self['ranktimelist']
        # end handle [GC_SYNC_ANSWERACTIVITY_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_ANSWERACTIVITY_QUESTION (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ANSWERACTIVITY_QUESTION] message attrs, auto generate do not change
        self.person['round'] = self['round']
        self.person['question'] = self['question']
        # end handle [GC_SYNC_ANSWERACTIVITY_QUESTION] message attrs, auto generate do not change
        pass


class CG_DOMAINWAR_SHOP_BUY (Packet):
    pass


class GC_DOMAINWAR_SHOP_RECORD (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_SHOP_RECORD] message attrs, auto generate do not change
        # end handle [GC_DOMAINWAR_SHOP_RECORD] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_HUAGUANJIE_XINYILEGOU] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['count'] = self['count']
        self.person['activeTabId'] = self['activeTabId']
        # end handle [GC_SYNC_HUAGUANJIE_XINYILEGOU] message attrs, auto generate do not change
        pass


class CG_GUILDMERGE_INVITE (Packet):
    pass


class GC_GUILDMERGE_INVITE_LIST (Packet):
    def handle(self):
        # begin handle [GC_GUILDMERGE_INVITE_LIST] message attrs, auto generate do not change
        self.person['InvitedGuildInfo'] = self['InvitedGuildInfo']
        self.person['InvitGuildInfo'] = self['InvitGuildInfo']
        self.person['IsLogin'] = self['IsLogin']
        # end handle [GC_GUILDMERGE_INVITE_LIST] message attrs, auto generate do not change
        pass


class CG_GUILDMERGE_PREVIEW (Packet):
    pass


class GC_GUILDMERGE_PREVIEW_RET (Packet):
    def handle(self):
        # begin handle [GC_GUILDMERGE_PREVIEW_RET] message attrs, auto generate do not change
        self.person['InvitGuildInfo'] = self['InvitGuildInfo']
        # end handle [GC_GUILDMERGE_PREVIEW_RET] message attrs, auto generate do not change
        pass


class CG_GUILDMERGE_OPTION (Packet):
    pass


class GC_GUILDMERGE_OPTION_RESULT (Packet):
    def handle(self):
        # begin handle [GC_GUILDMERGE_OPTION_RESULT] message attrs, auto generate do not change
        self.person['Option'] = self['Option']
        self.person['Result'] = self['Result']
        # end handle [GC_GUILDMERGE_OPTION_RESULT] message attrs, auto generate do not change
        pass


class GC_SYNC_HUAGUANJIE_ACT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HUAGUANJIE_ACT_INFO] message attrs, auto generate do not change
        self.person['FreeGiftCount'] = self['FreeGiftCount']
        self.person['GreetingRewardState'] = self['GreetingRewardState']
        self.person['GreetingRewardStage'] = self['GreetingRewardStage']
        self.person['GreetingRewardRound'] = self['GreetingRewardRound']
        self.person['IsOpen'] = self['IsOpen']
        self.person['GreetingVal'] = self['GreetingVal']
        self.person['PopularityVal'] = self['PopularityVal']
        self.person['SenderAmount'] = self['SenderAmount']
        # end handle [GC_SYNC_HUAGUANJIE_ACT_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_SIGNETNINGLIAN_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SIGNETNINGLIAN_DATA] message attrs, auto generate do not change
        self.person['signetguid'] = self['signetguid']
        self.person['attrindex'] = self['attrindex']
        self.person['attrid'] = self['attrid']
        self.person['attrval'] = self['attrval']
        self.person['attrtype'] = self['attrtype']
        self.person['extradata'] = self['extradata']
        # end handle [GC_SYNC_SIGNETNINGLIAN_DATA] message attrs, auto generate do not change
        pass


class CG_REQ_SIGNETNINGLIAN (Packet):
    pass


class CG_REQ_SIGNETNINGLIAN_REPLACE (Packet):
    pass


class GC_SYNC_WARPATHBUFF_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYNC_WARPATHBUFF_LIST] message attrs, auto generate do not change
        self.person['buffId'] = self['buffId']
        # end handle [GC_SYNC_WARPATHBUFF_LIST] message attrs, auto generate do not change
        pass


class GC_DOMAINWAR_INFO_DATA (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_INFO_DATA] message attrs, auto generate do not change
        self.person['shopRecord'] = self['shopRecord']
        self.person['doMainwarSalary'] = self['doMainwarSalary']
        self.person['seasonPlayerReward'] = self['seasonPlayerReward']
        self.person['seasonPlayerScore'] = self['seasonPlayerScore']
        # end handle [GC_DOMAINWAR_INFO_DATA] message attrs, auto generate do not change
        pass


class GC_DOMAINWAR_SEASON_INFO_DATA (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_SEASON_INFO_DATA] message attrs, auto generate do not change
        self.person['seasonGuildReward'] = self['seasonGuildReward']
        self.person['seasonTargetId'] = self['seasonTargetId']
        # end handle [GC_DOMAINWAR_SEASON_INFO_DATA] message attrs, auto generate do not change
        pass


class GC_DOMAINWAR_SERVER_LIMIT_SHOP_DATA (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_SERVER_LIMIT_SHOP_DATA] message attrs, auto generate do not change
        self.person['m_shopData'] = self['m_shopData']
        # end handle [GC_DOMAINWAR_SERVER_LIMIT_SHOP_DATA] message attrs, auto generate do not change
        pass


class CG_DOMAINWAR_SERVER_LIMIT_SHOP_DATA (Packet):
    pass


class GC_HUAGUANJIE_SEND_GIFT (Packet):
    def handle(self):
        # begin handle [GC_HUAGUANJIE_SEND_GIFT] message attrs, auto generate do not change
        self.person['senderGuid'] = self['senderGuid']
        self.person['senderName'] = self['senderName']
        self.person['giftId'] = self['giftId']
        self.person['giftCount'] = self['giftCount']
        self.person['senderProf'] = self['senderProf']
        self.person['senderCustomHead'] = self['senderCustomHead']
        self.person['senderFrame'] = self['senderFrame']
        self.person['senderSex'] = self['senderSex']
        # end handle [GC_HUAGUANJIE_SEND_GIFT] message attrs, auto generate do not change
        pass


class GC_SKILLZHUANJING_OPEN_RET (Packet):
    def handle(self):
        # begin handle [GC_SKILLZHUANJING_OPEN_RET] message attrs, auto generate do not change
        self.person['SkillZhuanjingLine'] = self['SkillZhuanjingLine']
        self.person['OrignSkill'] = self['OrignSkill']
        # end handle [GC_SKILLZHUANJING_OPEN_RET] message attrs, auto generate do not change
        pass


class CG_ASK_ALL_ROUND_GREETING_REWARD (Packet):
    pass


class GC_SYNC_DAOYI (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DAOYI] message attrs, auto generate do not change
        self.person['count'] = self['count']
        # end handle [GC_SYNC_DAOYI] message attrs, auto generate do not change
        pass


class CG_REQ_STALL_COUNT (Packet):
    pass


class GC_RET_STALL_COUNT (Packet):
    def handle(self):
        # begin handle [GC_RET_STALL_COUNT] message attrs, auto generate do not change
        self.person['index'] = self['index']
        self.person['count'] = self['count']
        self.person['isPublic'] = self['isPublic']
        # end handle [GC_RET_STALL_COUNT] message attrs, auto generate do not change
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
    def handle(self):
        # begin handle [GC_SYNC_LINGSHIBOARD_INFO] message attrs, auto generate do not change
        self.person['info'] = self['info']
        # end handle [GC_SYNC_LINGSHIBOARD_INFO] message attrs, auto generate do not change
        pass


class CG_TEAM_AUTO_FIGHT (Packet):
    pass


class GC_ChronoTriggerSelfInfo (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSelfInfo] message attrs, auto generate do not change
        self.person['weekScore'] = self['weekScore']
        self.person['seasonScore'] = self['seasonScore']
        self.person['userSeason'] = self['userSeason']
        self.person['serverNewSeasonLevel'] = self['serverNewSeasonLevel']
        self.person['chronoTriggerCoin'] = self['chronoTriggerCoin']
        self.person['needShowRed'] = self['needShowRed']
        # end handle [GC_ChronoTriggerSelfInfo] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerTalentTree (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerTalentTree] message attrs, auto generate do not change
        self.person['units'] = self['units']
        self.person['talentPoint'] = self['talentPoint']
        # end handle [GC_ChronoTriggerTalentTree] message attrs, auto generate do not change
        pass


class CG_ChronoTriggerTalentLvlUp (Packet):
    pass


class CG_ChronoTriggerFight (Packet):
    pass


class GC_ChronoTriggerLineInfo (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerLineInfo] message attrs, auto generate do not change
        self.person['lineIds'] = self['lineIds']
        self.person['currentLineId'] = self['currentLineId']
        # end handle [GC_ChronoTriggerLineInfo] message attrs, auto generate do not change
        pass


class CG_ChronoTriggerSelectServant (Packet):
    pass


class GC_ChronoTriggerSelectServant (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSelectServant] message attrs, auto generate do not change
        self.person['id'] = self['id']
        # end handle [GC_ChronoTriggerSelectServant] message attrs, auto generate do not change
        pass


class GC_ChroroTriggerSelectServantInfo (Packet):
    def handle(self):
        # begin handle [GC_ChroroTriggerSelectServantInfo] message attrs, auto generate do not change
        self.person['infos'] = self['infos']
        self.person['endTime'] = self['endTime']
        # end handle [GC_ChroroTriggerSelectServantInfo] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerGlobalData (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerGlobalData] message attrs, auto generate do not change
        self.person['phase'] = self['phase']
        self.person['round'] = self['round']
        self.person['currentPhaseEndTime'] = self['currentPhaseEndTime']
        # end handle [GC_ChronoTriggerGlobalData] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerSelectBlessCard (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSelectBlessCard] message attrs, auto generate do not change
        self.person['cards'] = self['cards']
        # end handle [GC_ChronoTriggerSelectBlessCard] message attrs, auto generate do not change
        pass


class CG_ChronoTriggerSelectBlessCard (Packet):
    pass


class GC_ChronoTriggerSelectBlessCardInfo (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSelectBlessCardInfo] message attrs, auto generate do not change
        self.person['infos'] = self['infos']
        # end handle [GC_ChronoTriggerSelectBlessCardInfo] message attrs, auto generate do not change
        pass


class CG_ChronoTriggerSelectBoss (Packet):
    pass


class GC_ChronoTriggerSelectBossInfo (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSelectBossInfo] message attrs, auto generate do not change
        self.person['infos'] = self['infos']
        self.person['showUI'] = self['showUI']
        # end handle [GC_ChronoTriggerSelectBossInfo] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerResult (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerResult] message attrs, auto generate do not change
        self.person['allBoss'] = self['allBoss']
        self.person['difficultyAdd'] = self['difficultyAdd']
        self.person['totalScore'] = self['totalScore']
        # end handle [GC_ChronoTriggerResult] message attrs, auto generate do not change
        pass


class CG_ChronoTriggerGetSeasonAward (Packet):
    pass


class CG_LINGSHI_REDUCTION (Packet):
    pass


class GC_ChronoTriggerSeasonAwardGetInfo (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSeasonAwardGetInfo] message attrs, auto generate do not change
        self.person['getIds'] = self['getIds']
        # end handle [GC_ChronoTriggerSeasonAwardGetInfo] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerServantCall_Sync (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerServantCall_Sync] message attrs, auto generate do not change
        self.person['CallValue'] = self['CallValue']
        # end handle [GC_ChronoTriggerServantCall_Sync] message attrs, auto generate do not change
        pass


class GC_SYNC_BACKGROUNDPHOTO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BACKGROUNDPHOTO] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['deadline'] = self['deadline']
        self.person['curId'] = self['curId']
        self.person['type'] = self['type']
        # end handle [GC_SYNC_BACKGROUNDPHOTO] message attrs, auto generate do not change
        pass


class CG_REQ_SET_BACKGROUNDPHOTO (Packet):
    pass


class CG_DIMAI_ENTERMIJING (Packet):
    pass


class GC_ChronoTriggerSelectBossPlayersInfo (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSelectBossPlayersInfo] message attrs, auto generate do not change
        self.person['bossId'] = self['bossId']
        self.person['players'] = self['players']
        # end handle [GC_ChronoTriggerSelectBossPlayersInfo] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerSelectBossSuccess (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSelectBossSuccess] message attrs, auto generate do not change
        self.person['info'] = self['info']
        # end handle [GC_ChronoTriggerSelectBossSuccess] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerCommand (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerCommand] message attrs, auto generate do not change
        self.person['opType'] = self['opType']
        self.person['param1'] = self['param1']
        self.person['param2'] = self['param2']
        self.person['param3'] = self['param3']
        self.person['param4'] = self['param4']
        self.person['param5'] = self['param5']
        self.person['param6'] = self['param6']
        self.person['param7'] = self['param7']
        # end handle [GC_ChronoTriggerCommand] message attrs, auto generate do not change
        pass


class GC_DIMAIMIJING_FIGHT_TIME (Packet):
    def handle(self):
        # begin handle [GC_DIMAIMIJING_FIGHT_TIME] message attrs, auto generate do not change
        self.person['EndTime'] = self['EndTime']
        # end handle [GC_DIMAIMIJING_FIGHT_TIME] message attrs, auto generate do not change
        pass


class GC_SYNC_CP_ACT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CP_ACT_INFO] message attrs, auto generate do not change
        self.person['actStartTime'] = self['actStartTime']
        self.person['actEndTime'] = self['actEndTime']
        self.person['actProf'] = self['actProf']
        self.person['toActProfItemId'] = self['toActProfItemId']
        self.person['originProf'] = self['originProf']
        self.person['toOriginProfItemId'] = self['toOriginProfItemId']
        # end handle [GC_SYNC_CP_ACT_INFO] message attrs, auto generate do not change
        pass


class GC_SYNC_CP_SKILLZHUANJINGINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CP_SKILLZHUANJINGINFO] message attrs, auto generate do not change
        self.person['info'] = self['info']
        # end handle [GC_SYNC_CP_SKILLZHUANJINGINFO] message attrs, auto generate do not change
        pass


class GC_DOMAINWAR_CAR_INFO_SYNC (Packet):
    def handle(self):
        # begin handle [GC_DOMAINWAR_CAR_INFO_SYNC] message attrs, auto generate do not change
        self.person['NpcId'] = self['NpcId']
        self.person['State'] = self['State']
        self.person['HpPercent'] = self['HpPercent']
        self.person['posx'] = self['posx']
        self.person['posy'] = self['posy']
        self.person['posz'] = self['posz']
        # end handle [GC_DOMAINWAR_CAR_INFO_SYNC] message attrs, auto generate do not change
        pass


class CG_LINGSHI_BOARD_UNLOCK (Packet):
    pass


class GC_ChronoTriggerSkillInfo (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerSkillInfo] message attrs, auto generate do not change
        self.person['playerGuid'] = self['playerGuid']
        self.person['chronoTriggerServantId'] = self['chronoTriggerServantId']
        self.person['level'] = self['level']
        self.person['currentVal'] = self['currentVal']
        # end handle [GC_ChronoTriggerSkillInfo] message attrs, auto generate do not change
        pass


class CG_TIANSHU_COLLECT (Packet):
    pass


class CG_TIANSHU_COLLECT_CANCEL (Packet):
    pass


class GC_SYNC_ALL_COLLECTED_TIANSHU (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ALL_COLLECTED_TIANSHU] message attrs, auto generate do not change
        self.person['id'] = self['id']
        # end handle [GC_SYNC_ALL_COLLECTED_TIANSHU] message attrs, auto generate do not change
        pass


class GC_DIMAIMIJING_OPENENTERDLG (Packet):
    def handle(self):
        # begin handle [GC_DIMAIMIJING_OPENENTERDLG] message attrs, auto generate do not change
        self.person['entertime'] = self['entertime']
        self.person['raretype'] = self['raretype']
        self.person['ownerguid'] = self['ownerguid']
        # end handle [GC_DIMAIMIJING_OPENENTERDLG] message attrs, auto generate do not change
        pass


class GC_PLAYSOUND_INSCENE (Packet):
    def handle(self):
        # begin handle [GC_PLAYSOUND_INSCENE] message attrs, auto generate do not change
        self.person['playServerId'] = self['playServerId']
        self.person['soundId'] = self['soundId']
        # end handle [GC_PLAYSOUND_INSCENE] message attrs, auto generate do not change
        pass


class CG_SET_PACK_NEATEN_OPTION (Packet):
    pass


class GC_SYNC_PACK_NEATEN_OPTION (Packet):
    def handle(self):
        # begin handle [GC_SYNC_PACK_NEATEN_OPTION] message attrs, auto generate do not change
        self.person['option'] = self['option']
        # end handle [GC_SYNC_PACK_NEATEN_OPTION] message attrs, auto generate do not change
        pass


class GC_SYNC_EVERYDAYGIFT_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_EVERYDAYGIFT_INFO] message attrs, auto generate do not change
        self.person['state'] = self['state']
        # end handle [GC_SYNC_EVERYDAYGIFT_INFO] message attrs, auto generate do not change
        pass


class CG_BUY_EVERYDAYGIFT (Packet):
    pass


class GC_SYNC_MONTHCARDSHOP_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MONTHCARDSHOP_INFO] message attrs, auto generate do not change
        self.person['usedrefreshcnt'] = self['usedrefreshcnt']
        self.person['itemindex'] = self['itemindex']
        self.person['buystate'] = self['buystate']
        self.person['extradata'] = self['extradata']
        # end handle [GC_SYNC_MONTHCARDSHOP_INFO] message attrs, auto generate do not change
        pass


class CG_MONTHCARDSHOP_BUYONEGOODS (Packet):
    pass


class CG_MONTHCARDSHOP_BUYALLGOODS (Packet):
    pass


class CG_MONTHCARDSHOP_REFRESH (Packet):
    pass


class CG_REQUEST_MMOUNT (Packet):
    pass


class GC_REQUEST_MMOUNT (Packet):
    def handle(self):
        # begin handle [GC_REQUEST_MMOUNT] message attrs, auto generate do not change
        self.person['sourceServerID'] = self['sourceServerID']
        self.person['inviteType'] = self['inviteType']
        # end handle [GC_REQUEST_MMOUNT] message attrs, auto generate do not change
        pass


class CG_REPLY_MMOUNT (Packet):
    pass


class GC_MAKE_MMOUNT (Packet):
    def handle(self):
        # begin handle [GC_MAKE_MMOUNT] message attrs, auto generate do not change
        self.person['masterServerID'] = self['masterServerID']
        self.person['guestServerID'] = self['guestServerID']
        # end handle [GC_MAKE_MMOUNT] message attrs, auto generate do not change
        pass


class CG_CANCEL_MMOUNT (Packet):
    pass


class GC_MOUNT_CAR_NOTICE (Packet):
    def handle(self):
        # begin handle [GC_MOUNT_CAR_NOTICE] message attrs, auto generate do not change
        self.person['strNotice'] = self['strNotice']
        # end handle [GC_MOUNT_CAR_NOTICE] message attrs, auto generate do not change
        pass


class GC_MOUNT_CAR_TOGETHER (Packet):
    def handle(self):
        # begin handle [GC_MOUNT_CAR_TOGETHER] message attrs, auto generate do not change
        self.person['mountId'] = self['mountId']
        # end handle [GC_MOUNT_CAR_TOGETHER] message attrs, auto generate do not change
        pass


class CG_REQ_MODIFY_BATTLE_SCHEME_ZHUANJING (Packet):
    pass


class GC_SYNC_TREASURE_ADVENTURE_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TREASURE_ADVENTURE_INFO] message attrs, auto generate do not change
        self.person['ActivityId'] = self['ActivityId']
        self.person['TreasureCoin'] = self['TreasureCoin']
        self.person['TreasureSuperCoin'] = self['TreasureSuperCoin']
        self.person['TreasureScore'] = self['TreasureScore']
        self.person['ShopRecord'] = self['ShopRecord']
        # end handle [GC_SYNC_TREASURE_ADVENTURE_INFO] message attrs, auto generate do not change
        pass


class CG_GENERATE_TREASURE_ADVENTURE_REWARD (Packet):
    pass


class GC_GENERATE_TREASURE_ADVENTURE_REWARD_RET (Packet):
    def handle(self):
        # begin handle [GC_GENERATE_TREASURE_ADVENTURE_REWARD_RET] message attrs, auto generate do not change
        self.person['RewardList'] = self['RewardList']
        self.person['OperateType'] = self['OperateType']
        # end handle [GC_GENERATE_TREASURE_ADVENTURE_REWARD_RET] message attrs, auto generate do not change
        pass


class CG_TREASURE_ADVENTURE_SHOP_BUY (Packet):
    pass


class GC_CONSUMEPOINT_INFO (Packet):
    def handle(self):
        # begin handle [GC_CONSUMEPOINT_INFO] message attrs, auto generate do not change
        # end handle [GC_CONSUMEPOINT_INFO] message attrs, auto generate do not change
        pass


class CG_CONSUMEPOINT_REWARD (Packet):
    pass


class GC_CONSUMEPOINT_REWARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_CONSUMEPOINT_REWARD_INFO] message attrs, auto generate do not change
        # end handle [GC_CONSUMEPOINT_REWARD_INFO] message attrs, auto generate do not change
        pass


class CG_CONSUMEPOINT_SHOP_BUY (Packet):
    pass


class GC_CONSUMESCORESHOP_INFO (Packet):
    def handle(self):
        # begin handle [GC_CONSUMESCORESHOP_INFO] message attrs, auto generate do not change
        self.person['ConsumePoint'] = self['ConsumePoint']
        self.person['ConsumeTotalYuanbao'] = self['ConsumeTotalYuanbao']
        self.person['StartTime'] = self['StartTime']
        self.person['EndTime'] = self['EndTime']
        self.person['ShopItems'] = self['ShopItems']
        self.person['RewardItems'] = self['RewardItems']
        # end handle [GC_CONSUMESCORESHOP_INFO] message attrs, auto generate do not change
        pass


class CG_CONSUMESCORESHOP_REWARD (Packet):
    pass


class GC_CONSUMESCORESHOP_REWARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_CONSUMESCORESHOP_REWARD_INFO] message attrs, auto generate do not change
        self.person['RewardItems'] = self['RewardItems']
        # end handle [GC_CONSUMESCORESHOP_REWARD_INFO] message attrs, auto generate do not change
        pass


class CG_CONSUMESCORESHOP_BUY (Packet):
    pass


class CG_MODIFY_LINGSHI_RESONANCE_BOARD_SLOT (Packet):
    pass


class CG_REQ_UNLOCK_EXTRA_LINGSHI_RESONANCE (Packet):
    pass


class CG_ChronoTriggerBossFightFailReChoose (Packet):
    pass


class CG_REQ_DIMAIJINGHAI_LevelUp (Packet):
    pass


class GC_SYNC_DIMAIJINGHAI_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_DIMAIJINGHAI_INFO] message attrs, auto generate do not change
        self.person['LvList'] = self['LvList']
        self.person['IsFirstEnter'] = self['IsFirstEnter']
        # end handle [GC_SYNC_DIMAIJINGHAI_INFO] message attrs, auto generate do not change
        pass


class CG_GET_FESTIVAL_REGRESS_TASK_REWARD (Packet):
    pass


class GC_FV_TRIAL_INFO (Packet):
    def handle(self):
        # begin handle [GC_FV_TRIAL_INFO] message attrs, auto generate do not change
        self.person['trialTeamId'] = self['trialTeamId']
        self.person['trialTime'] = self['trialTime']
        self.person['reliveNum'] = self['reliveNum']
        # end handle [GC_FV_TRIAL_INFO] message attrs, auto generate do not change
        pass


class CG_GODWEAPON_FUYUAN_LEVELUP (Packet):
    pass


class GC_FV_TRIAL_TIP (Packet):
    def handle(self):
        # begin handle [GC_FV_TRIAL_TIP] message attrs, auto generate do not change
        self.person['IsBeginTip'] = self['IsBeginTip']
        self.person['IsOverTime'] = self['IsOverTime']
        # end handle [GC_FV_TRIAL_TIP] message attrs, auto generate do not change
        pass


class GC_SHOW_GODWEAPON_FUYUAN_MODEL (Packet):
    def handle(self):
        # begin handle [GC_SHOW_GODWEAPON_FUYUAN_MODEL] message attrs, auto generate do not change
        self.person['objId'] = self['objId']
        self.person['effectId'] = self['effectId']
        # end handle [GC_SHOW_GODWEAPON_FUYUAN_MODEL] message attrs, auto generate do not change
        pass


class GC_ChronoTriggerGoldBookServantBless (Packet):
    def handle(self):
        # begin handle [GC_ChronoTriggerGoldBookServantBless] message attrs, auto generate do not change
        self.person['servanttabid'] = self['servanttabid']
        self.person['blesstype'] = self['blesstype']
        # end handle [GC_ChronoTriggerGoldBookServantBless] message attrs, auto generate do not change
        pass


class CG_REQ_FASHION_UNEQUIP (Packet):
    pass


class CG_ChronoTriggerResetTalentTree (Packet):
    pass


class CG_REQ_LINGSHI_EXCHANGE (Packet):
    pass


class CG_DIMAIJINGHAI_PlayFirstAnima (Packet):
    pass


class CG_LINGSHI_BOARD_ONEKEY_INSTALL (Packet):
    pass


class CG_EQUIPATTR_TRANS (Packet):
    pass


class GC_RESET_FRIEND_GROUP_NAME (Packet):
    def handle(self):
        # begin handle [GC_RESET_FRIEND_GROUP_NAME] message attrs, auto generate do not change
        # end handle [GC_RESET_FRIEND_GROUP_NAME] message attrs, auto generate do not change
        pass


class GC_InfiniteDreamlandRank (Packet):
    def handle(self):
        # begin handle [GC_InfiniteDreamlandRank] message attrs, auto generate do not change
        self.person['rankData'] = self['rankData']
        # end handle [GC_InfiniteDreamlandRank] message attrs, auto generate do not change
        pass


class CG_InfiniteDreamlandRank (Packet):
    pass


class CG_REQ_GET_BINGXUEJIE_FENGWUKAOCHA_AWARD (Packet):
    pass


class GC_SYNC_BINGXUEJIE_FENGWUKAOCHA_AWARD (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BINGXUEJIE_FENGWUKAOCHA_AWARD] message attrs, auto generate do not change
        self.person['getAward'] = self['getAward']
        # end handle [GC_SYNC_BINGXUEJIE_FENGWUKAOCHA_AWARD] message attrs, auto generate do not change
        pass


class GC_SYNC_BINGXUEJIE_FIREWORK_CHEST_OPEN_COUNT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BINGXUEJIE_FIREWORK_CHEST_OPEN_COUNT] message attrs, auto generate do not change
        self.person['startTime'] = self['startTime']
        self.person['openCount'] = self['openCount']
        # end handle [GC_SYNC_BINGXUEJIE_FIREWORK_CHEST_OPEN_COUNT] message attrs, auto generate do not change
        pass


class GC_CHRONOTRIGGER_RANK (Packet):
    def handle(self):
        # begin handle [GC_CHRONOTRIGGER_RANK] message attrs, auto generate do not change
        self.person['rankData'] = self['rankData']
        # end handle [GC_CHRONOTRIGGER_RANK] message attrs, auto generate do not change
        pass


class CG_REQ_CHRONOTRIGGER_RANK (Packet):
    pass


class CG_DOMAINPLUNDER_CHALLENGE (Packet):
    pass


class CG_DOMAINPLUNDER_OPERATE (Packet):
    pass


class CG_DOMAINPLUNDER_GUILDCHIEF_GRASSION (Packet):
    pass


class GC_DOMAINPLUNDER_BOARD_INFO (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_BOARD_INFO] message attrs, auto generate do not change
        self.person['domainId'] = self['domainId']
        self.person['BeginTime'] = self['BeginTime']
        self.person['AttackGuildInfo'] = self['AttackGuildInfo']
        self.person['OccupyGuildInfo'] = self['OccupyGuildInfo']
        self.person['chunkList'] = self['chunkList']
        # end handle [GC_DOMAINPLUNDER_BOARD_INFO] message attrs, auto generate do not change
        pass


class GC_STUDIO_VERIFY_INFO (Packet):
    def handle(self):
        # begin handle [GC_STUDIO_VERIFY_INFO] message attrs, auto generate do not change
        self.person['VerifyId'] = self['VerifyId']
        self.person['VerifySequenceId'] = self['VerifySequenceId']
        self.person['VerifyEndTime'] = self['VerifyEndTime']
        # end handle [GC_STUDIO_VERIFY_INFO] message attrs, auto generate do not change
        pass


class CG_STUDIO_VERIFY (Packet):
    pass


class CG_REQ_BINGXUEJIE_FIREWORK (Packet):
    pass


class CG_STUDIO_VERIFY_REFRESH (Packet):
    pass


class GC_STUDIO_VERIFY_RESULT (Packet):
    def handle(self):
        # begin handle [GC_STUDIO_VERIFY_RESULT] message attrs, auto generate do not change
        self.person['Result'] = self['Result']
        # end handle [GC_STUDIO_VERIFY_RESULT] message attrs, auto generate do not change
        pass


class CG_REQ_GET_BINGXUEJIE_PRESENT (Packet):
    pass


class GC_SYNC_BINGXUEJIE_PRESENT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BINGXUEJIE_PRESENT] message attrs, auto generate do not change
        self.person['bGet'] = self['bGet']
        # end handle [GC_SYNC_BINGXUEJIE_PRESENT] message attrs, auto generate do not change
        pass


class GC_DOMAINPLUNDER_ATTCK_RESULT (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_ATTCK_RESULT] message attrs, auto generate do not change
        self.person['IsWin'] = self['IsWin']
        self.person['domainId'] = self['domainId']
        self.person['boardId'] = self['boardId']
        self.person['occupyProcess'] = self['occupyProcess']
        self.person['enterTimes'] = self['enterTimes']
        # end handle [GC_DOMAINPLUNDER_ATTCK_RESULT] message attrs, auto generate do not change
        pass


class GC_DOMAINPLUNDER_CHALLENGE_START (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_CHALLENGE_START] message attrs, auto generate do not change
        self.person['attackGuild'] = self['attackGuild']
        self.person['occupyGuild'] = self['occupyGuild']
        self.person['attackName'] = self['attackName']
        self.person['occupyName'] = self['occupyName']
        # end handle [GC_DOMAINPLUNDER_CHALLENGE_START] message attrs, auto generate do not change
        pass


class CG_DOMAINPLUNDER_BOARD_INFO (Packet):
    pass


class GC_DOMAINPLUNDER_COMMON_ALL (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_COMMON_ALL] message attrs, auto generate do not change
        self.person['boardList'] = self['boardList']
        # end handle [GC_DOMAINPLUNDER_COMMON_ALL] message attrs, auto generate do not change
        pass


class CG_GET_DOMAINPLUNDER_COMMON_ALL (Packet):
    pass


class GC_DOAMINPLUNDEE_BASE_DATA (Packet):
    def handle(self):
        # begin handle [GC_DOAMINPLUNDEE_BASE_DATA] message attrs, auto generate do not change
        self.person['m_GuildPlunderTimes'] = self['m_GuildPlunderTimes']
        self.person['m_PlayerPlunderTimes'] = self['m_PlayerPlunderTimes']
        self.person['m_PlayerPlunderReport'] = self['m_PlayerPlunderReport']
        # end handle [GC_DOAMINPLUNDEE_BASE_DATA] message attrs, auto generate do not change
        pass


class CG_DOMAINPLUNDER_CHIEF_GARSSION_GUILDMEMBER_INFO (Packet):
    pass


class GC_DOMAINPLUNDER_CHIEF_GARSSION_GUILDMEMBER_INFO (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_CHIEF_GARSSION_GUILDMEMBER_INFO] message attrs, auto generate do not change
        self.person['guildMemberList'] = self['guildMemberList']
        # end handle [GC_DOMAINPLUNDER_CHIEF_GARSSION_GUILDMEMBER_INFO] message attrs, auto generate do not change
        pass


class CG_CBZL_BUYLEVEL (Packet):
    pass


class CG_REQ_LOCK_GODWEAPON (Packet):
    pass



class CG_BINGXUEJIE_FENGWUKAOCHA_FINISH (Packet):
	pass


class CG_CHRONOTRIGGER_SELECT_MUDDY_QI_PILL (Packet):
	pass


class GC_CHRONOTRIGGER_MUDDY_SYNC (Packet):
    def handle(self):
        # begin handle [GC_CHRONOTRIGGER_MUDDY_SYNC] message attrs, auto generate do not change
        self.person['values'] = self['values']
        # end handle [GC_CHRONOTRIGGER_MUDDY_SYNC] message attrs, auto generate do not change
        pass


class GC_DOMAINPLUNDER_SETTLE (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_SETTLE] message attrs, auto generate do not change
        self.person['attack'] = self['attack']
        self.person['attackname'] = self['attackname']
        self.person['occupy'] = self['occupy']
        self.person['occupyname'] = self['occupyname']
        self.person['winGuild'] = self['winGuild']
        # end handle [GC_DOMAINPLUNDER_SETTLE] message attrs, auto generate do not change
        pass


class GC_DOMAINPLUNDER_BATTLEREPORT (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_BATTLEREPORT] message attrs, auto generate do not change
        self.person['attack'] = self['attack']
        self.person['attackname'] = self['attackname']
        self.person['occupy'] = self['occupy']
        self.person['occupyname'] = self['occupyname']
        self.person['chunkbelong'] = self['chunkbelong']
        # end handle [GC_DOMAINPLUNDER_BATTLEREPORT] message attrs, auto generate do not change
        pass


class CG_DOMAINPLUNDER_BATTLEREPORT_OPEN (Packet):
	pass


class GC_BINGXUEJIE_FIREWORK_USE_SUCCESS (Packet):
    def handle(self):
        # begin handle [GC_BINGXUEJIE_FIREWORK_USE_SUCCESS] message attrs, auto generate do not change
        # end handle [GC_BINGXUEJIE_FIREWORK_USE_SUCCESS] message attrs, auto generate do not change
        pass


class CG_INFINITEDREAMLAND_RANK_CLICK (Packet):
	pass


class GC_DOMAINPLUNDER_OPERATE_RET (Packet):
    def handle(self):
        # begin handle [GC_DOMAINPLUNDER_OPERATE_RET] message attrs, auto generate do not change
        self.person['OperateType'] = self['OperateType']
        self.person['BoardId'] = self['BoardId']
        self.person['DomainId'] = self['DomainId']
        self.person['result'] = self['result']
        self.person['oldBelong'] = self['oldBelong']
        self.person['OperateType'] = self['OperateType']
        self.person['BoardId'] = self['BoardId']
        self.person['DomainId'] = self['DomainId']
        self.person['result'] = self['result']
        self.person['oldBelong'] = self['oldBelong']
        # end handle [GC_DOMAINPLUNDER_OPERATE_RET] message attrs, auto generate do not change
        pass




class GC_FAKEGUILD_BOTNOTICE (Packet):
    def handle(self):
        # begin handle [GC_FAKEGUILD_BOTNOTICE] message attrs, auto generate do not change
        self.person['notice'] = self['notice']
        self.person['clickto'] = self['clickto']
        # end handle [GC_FAKEGUILD_BOTNOTICE] message attrs, auto generate do not change
        pass


class GC_CelebrationCakeData (Packet):
    def handle(self):
        # begin handle [GC_CelebrationCakeData] message attrs, auto generate do not change
        self.person['tables'] = self['tables']
        # end handle [GC_CelebrationCakeData] message attrs, auto generate do not change
        pass


class CG_CelerationCakeSelfData (Packet):
	pass


class CG_CelebrationCakeOp (Packet):
	pass


class GC_CelerationCakeSelfData (Packet):
    def handle(self):
        # begin handle [GC_CelerationCakeSelfData] message attrs, auto generate do not change
        self.person['eatTime'] = self['eatTime']
        # end handle [GC_CelerationCakeSelfData] message attrs, auto generate do not change
        pass


class GC_BIGWORLDARENA_SYNC_MEMBER (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_SYNC_MEMBER] message attrs, auto generate do not change
        self.person['memberInfo'] = self['memberInfo']
        self.person['autoClose'] = self['autoClose']
        # end handle [GC_BIGWORLDARENA_SYNC_MEMBER] message attrs, auto generate do not change
        pass


class CG_BIGWORLDARENA_COMBAT_COMMAND (Packet):
	pass


class GC_BIGWORLDARENA_COMBAT_COMMAND (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_COMBAT_COMMAND] message attrs, auto generate do not change
        self.person['type'] = self['type']
        self.person['sender'] = self['sender']
        self.person['target'] = self['target']
        self.person['mySideId'] = self['mySideId']
        # end handle [GC_BIGWORLDARENA_COMBAT_COMMAND] message attrs, auto generate do not change
        pass


class GC_ReadGetRewardSelfInfo (Packet):
    def handle(self):
        # begin handle [GC_ReadGetRewardSelfInfo] message attrs, auto generate do not change
        self.person['HaveGet'] = self['HaveGet']
        # end handle [GC_ReadGetRewardSelfInfo] message attrs, auto generate do not change
        pass


class CG_GetReadGetRewardReward (Packet):
	pass


class GC_BIGWORLDARENA_ACT_INFO (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_ACT_INFO] message attrs, auto generate do not change
        self.person['tierId'] = self['tierId']
        self.person['point'] = self['point']
        self.person['winTimes'] = self['winTimes']
        self.person['battleTimes'] = self['battleTimes']
        self.person['attendRewardStatus'] = self['attendRewardStatus']
        self.person['tierRewardStatus'] = self['tierRewardStatus']
        self.person['rank'] = self['rank']
        self.person['seasonWinTimes'] = self['seasonWinTimes']
        self.person['seasonBattleTimes'] = self['seasonBattleTimes']
        self.person['protectionScore'] = self['protectionScore']
        self.person['leftMatchTimes'] = self['leftMatchTimes']
        self.person['season'] = self['season']
        self.person['round'] = self['round']
        self.person['hasShowUpgradeTip'] = self['hasShowUpgradeTip']
        self.person['gloryKingId'] = self['gloryKingId']
        self.person['hasShowNewSeasonTip'] = self['hasShowNewSeasonTip']
        self.person['lastSeasonTierId'] = self['lastSeasonTierId']
        self.person['lastSeasonPoint'] = self['lastSeasonPoint']
        self.person['lastSeasonGloryKingId'] = self['lastSeasonGloryKingId']
        self.person['hasShowUpgradeIcon'] = self['hasShowUpgradeIcon']
        # end handle [GC_BIGWORLDARENA_ACT_INFO] message attrs, auto generate do not change
        pass


class CG_BIGWORLDARENA_GET_REWARD (Packet):
	pass


class CG_BIGWORLDARENA_ENTER_LOBBY (Packet):
	pass


class CG_BIGWORLDARENA_OPERATE_MATCH (Packet):
	pass


class GC_BIGWORLDARENA_MATCH_STATUS (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_MATCH_STATUS] message attrs, auto generate do not change
        self.person['status'] = self['status']
        self.person['startMatchAnsiTime'] = self['startMatchAnsiTime']
        # end handle [GC_BIGWORLDARENA_MATCH_STATUS] message attrs, auto generate do not change
        pass


class GC_BIGWORLDARENA_BATTLE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_BATTLE_RESULT] message attrs, auto generate do not change
        self.person['isWin'] = self['isWin']
        self.person['guid'] = self['guid']
        self.person['name'] = self['name']
        self.person['prof'] = self['prof']
        self.person['sex'] = self['sex']
        self.person['level'] = self['level']
        self.person['cure'] = self['cure']
        self.person['attack'] = self['attack']
        self.person['recvDamage'] = self['recvDamage']
        self.person['kill'] = self['kill']
        self.person['bestPlayerGuid'] = self['bestPlayerGuid']
        self.person['sideId'] = self['sideId']
        # end handle [GC_BIGWORLDARENA_BATTLE_RESULT] message attrs, auto generate do not change
        pass


class CG_BIGWORLDARENA_RANK (Packet):
	pass


class GC_BIGWORLDARENA_RANK (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_RANK] message attrs, auto generate do not change
        self.person['rankType'] = self['rankType']
        self.person['rankList'] = self['rankList']
        self.person['myRankInfo'] = self['myRankInfo']
        self.person['myRankNum'] = self['myRankNum']
        self.person['nPage'] = self['nPage']
        self.person['nAllPage'] = self['nAllPage']
        self.person['topMemberList'] = self['topMemberList']
        # end handle [GC_BIGWORLDARENA_RANK] message attrs, auto generate do not change
        pass


class GC_SYNC_REFINETIME_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_REFINETIME_INFO] message attrs, auto generate do not change
        self.person['RefineTimePower'] = self['RefineTimePower']
        self.person['AddPowerActive'] = self['AddPowerActive']
        self.person['AddPowerWanLiu'] = self['AddPowerWanLiu']
        self.person['AddPowerTongTian'] = self['AddPowerTongTian']
        # end handle [GC_SYNC_REFINETIME_INFO] message attrs, auto generate do not change
        pass


class CG_REQ_REFINETIME_BACKTRACK (Packet):
	pass


class CG_REQ_WUSHEN_UPGRADE (Packet):
	pass


class CG_REQ_WUSHEN_DRILL (Packet):
	pass


class GC_RET_WUSHEN_DRILL (Packet):
    def handle(self):
        # begin handle [GC_RET_WUSHEN_DRILL] message attrs, auto generate do not change
        self.person['slot'] = self['slot']
        self.person['success'] = self['success']
        # end handle [GC_RET_WUSHEN_DRILL] message attrs, auto generate do not change
        pass


class CG_REQ_WUSHEN_ASCEND (Packet):
	pass


class CG_REQ_WUSHEN_FORGE (Packet):
	pass


class CG_REQ_WUSHEN_FORGE_SET (Packet):
	pass


class GC_SYNC_WUSHEN_ATTR (Packet):
    def handle(self):
        # begin handle [GC_SYNC_WUSHEN_ATTR] message attrs, auto generate do not change
        self.person['opType'] = self['opType']
        self.person['wushenData'] = self['wushenData']
        self.person['wuShenUnlock'] = self['wuShenUnlock']
        self.person['wuShenDrillFailCount'] = self['wuShenDrillFailCount']
        self.person['wuShenForgeNonRareCount'] = self['wuShenForgeNonRareCount']
        # end handle [GC_SYNC_WUSHEN_ATTR] message attrs, auto generate do not change
        pass


class GC_SYNC_WUSHEN_ASCEND_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYNC_WUSHEN_ASCEND_LIST] message attrs, auto generate do not change
        self.person['playerGuid'] = self['playerGuid']
        self.person['playerName'] = self['playerName']
        self.person['ascendTime'] = self['ascendTime']
        self.person['ascendLevel'] = self['ascendLevel']
        # end handle [GC_SYNC_WUSHEN_ASCEND_LIST] message attrs, auto generate do not change
        pass


class CG_BIGWORLDARENA_MEMBER (Packet):
	pass


class GC_GUILD_DAY_INFO (Packet):
    def handle(self):
        # begin handle [GC_GUILD_DAY_INFO] message attrs, auto generate do not change
        # end handle [GC_GUILD_DAY_INFO] message attrs, auto generate do not change
        pass


class CG_ASK_GUILDPROCLAIMWAR (Packet):
	pass


class CG_ASK_GUILDPROCLAIMWAR_SINGLEINFOLIST (Packet):
	pass


class GC_GUILDPROCLAIMWAR_SINGLEINFOLIST (Packet):
    def handle(self):
        # begin handle [GC_GUILDPROCLAIMWAR_SINGLEINFOLIST] message attrs, auto generate do not change
        self.person['reqtype'] = self['reqtype']
        self.person['singleinfo'] = self['singleinfo']
        # end handle [GC_GUILDPROCLAIMWAR_SINGLEINFOLIST] message attrs, auto generate do not change
        pass


class CG_ASK_GUILDPROCLAIMWAR_DETAILDATA (Packet):
	pass


class GC_GUILDPROCLAIMWAR_DETAILDATA (Packet):
    def handle(self):
        # begin handle [GC_GUILDPROCLAIMWAR_DETAILDATA] message attrs, auto generate do not change
        self.person['reqtype'] = self['reqtype']
        self.person['detalinfo'] = self['detalinfo']
        # end handle [GC_GUILDPROCLAIMWAR_DETAILDATA] message attrs, auto generate do not change
        pass


class CG_GUILD_DAY_REWARD (Packet):
	pass


class CG_ASK_GUILDPROCLAIMWAR_GUILDLIST (Packet):
	pass


class CG_RET_GUILDPROCLAIMWAR_GUILDLIST (Packet):
	pass


class GC_RET_GUILDPROCLAIMWAR_GUILDLIST (Packet):
    def handle(self):
        # begin handle [GC_RET_GUILDPROCLAIMWAR_GUILDLIST] message attrs, auto generate do not change
        self.person['guildinfo'] = self['guildinfo']
        # end handle [GC_RET_GUILDPROCLAIMWAR_GUILDLIST] message attrs, auto generate do not change
        pass


class GC_LATERN_RIDDLES_CONFIG (Packet):
    def handle(self):
        # begin handle [GC_LATERN_RIDDLES_CONFIG] message attrs, auto generate do not change
        self.person['searchPosX'] = self['searchPosX']
        self.person['searchPosY'] = self['searchPosY']
        self.person['searchPosZ'] = self['searchPosZ']
        self.person['ques'] = self['ques']
        # end handle [GC_LATERN_RIDDLES_CONFIG] message attrs, auto generate do not change
        pass


class GC_LATERN_RIDDLES_SELFINFO (Packet):
    def handle(self):
        # begin handle [GC_LATERN_RIDDLES_SELFINFO] message attrs, auto generate do not change
        self.person['todayRewardTime'] = self['todayRewardTime']
        self.person['haveGuessNpcIds'] = self['haveGuessNpcIds']
        # end handle [GC_LATERN_RIDDLES_SELFINFO] message attrs, auto generate do not change
        pass


class CG_GUESS_LATERN_RIDDLES (Packet):
	pass


class GC_GUESS_LATERN_RIDDLES (Packet):
    def handle(self):
        # begin handle [GC_GUESS_LATERN_RIDDLES] message attrs, auto generate do not change
        self.person['npcDataId'] = self['npcDataId']
        self.person['success'] = self['success']
        # end handle [GC_GUESS_LATERN_RIDDLES] message attrs, auto generate do not change
        pass


class CG_REQ_WUSHEN_UNLOCK (Packet):
	pass


class CG_BIGWORLDARENA_CLIENT_SHOW_TIP (Packet):
	pass


class CG_GUILDPROCLAIMWAR_REPLYDENUMCIATION (Packet):
	pass


class GC_SYNC_GUILDPROCLAIMWAR_FIGHTINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_GUILDPROCLAIMWAR_FIGHTINFO] message attrs, auto generate do not change
        self.person['startnumtime'] = self['startnumtime']
        self.person['srcguildguid'] = self['srcguildguid']
        self.person['targuildguid'] = self['targuildguid']
        self.person['srckillnum'] = self['srckillnum']
        self.person['tarkillnum'] = self['tarkillnum']
        self.person['srcpoint'] = self['srcpoint']
        self.person['tarpoint'] = self['tarpoint']
        # end handle [GC_SYNC_GUILDPROCLAIMWAR_FIGHTINFO] message attrs, auto generate do not change
        pass


class GC_GUILDPROCLAIMWAR_MARQUEE (Packet):
    def handle(self):
        # begin handle [GC_GUILDPROCLAIMWAR_MARQUEE] message attrs, auto generate do not change
        self.person['marqueetype'] = self['marqueetype']
        self.person['singleinfo'] = self['singleinfo']
        # end handle [GC_GUILDPROCLAIMWAR_MARQUEE] message attrs, auto generate do not change
        pass


class GC_BIGWORLDARENA_TEAM_REQ_FAILED (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_TEAM_REQ_FAILED] message attrs, auto generate do not change
        self.person['failType'] = self['failType']
        self.person['sArg'] = self['sArg']
        # end handle [GC_BIGWORLDARENA_TEAM_REQ_FAILED] message attrs, auto generate do not change
        pass


class GC_BIGWORLDARENA_SYNC_MATCH_INFO (Packet):
    def handle(self):
        # begin handle [GC_BIGWORLDARENA_SYNC_MATCH_INFO] message attrs, auto generate do not change
        self.person['matchStatus'] = self['matchStatus']
        self.person['memberInfo'] = self['memberInfo']
        # end handle [GC_BIGWORLDARENA_SYNC_MATCH_INFO] message attrs, auto generate do not change
        pass


class CG_GUILDPROCLAIMWAR_SHARE (Packet):
	pass


class GC_HUANHUAN_PAISONG_SELFINFO (Packet):
    def handle(self):
        # begin handle [GC_HUANHUAN_PAISONG_SELFINFO] message attrs, auto generate do not change
        self.person['haveBuy'] = self['haveBuy']
        self.person['rewardBatch1HaveGet'] = self['rewardBatch1HaveGet']
        self.person['rewwardBatch2HaveGet'] = self['rewwardBatch2HaveGet']
        # end handle [GC_HUANHUAN_PAISONG_SELFINFO] message attrs, auto generate do not change
        pass


class CG_HUANHUAN_PAISONG_GETREWARD (Packet):
	pass


class CG_HUANHUAN_BUY (Packet):
	pass


class CG_HUANHUAN_PAISONG_BUY (Packet):
	pass


class GC_BEGIN_CHANGE_WORLD (Packet):
    def handle(self):
        # begin handle [GC_BEGIN_CHANGE_WORLD] message attrs, auto generate do not change
        self.person['optype'] = self['optype']
        # end handle [GC_BEGIN_CHANGE_WORLD] message attrs, auto generate do not change
        pass


class GC_SYNC_CHANGE_WORLD_RANK (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CHANGE_WORLD_RANK] message attrs, auto generate do not change
        self.person['rank'] = self['rank']
        self.person['changetype'] = self['changetype']
        # end handle [GC_SYNC_CHANGE_WORLD_RANK] message attrs, auto generate do not change
        pass


class CG_CANCEL_CHANGE_WORLD (Packet):
	pass


class CG_REQ_WUSHEN_FORGE_MULTIPLE (Packet):
	pass


class CG_BWARENA_MEMINFOINVIEW (Packet):
	pass


class GC_BWARENA_MEMINFOINVIEW (Packet):
    def handle(self):
        # begin handle [GC_BWARENA_MEMINFOINVIEW] message attrs, auto generate do not change
        self.person['MemAObj'] = self['MemAObj']
        self.person['MemAName'] = self['MemAName']
        self.person['MemALev'] = self['MemALev']
        self.person['MemAPro'] = self['MemAPro']
        self.person['MemAMaxHP'] = self['MemAMaxHP']
        self.person['MemACurHp'] = self['MemACurHp']
        self.person['MemBObj'] = self['MemBObj']
        self.person['MemBName'] = self['MemBName']
        self.person['MemBLev'] = self['MemBLev']
        self.person['MemBPro'] = self['MemBPro']
        self.person['MemBMaxHP'] = self['MemBMaxHP']
        self.person['MemBCurHp'] = self['MemBCurHp']
        # end handle [GC_BWARENA_MEMINFOINVIEW] message attrs, auto generate do not change
        pass


class GC_SYNC_CUR_WUSHEN_ASCEND_LIST (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CUR_WUSHEN_ASCEND_LIST] message attrs, auto generate do not change
        self.person['playerGuid'] = self['playerGuid']
        self.person['playerName'] = self['playerName']
        self.person['ascendTime'] = self['ascendTime']
        self.person['ascendLevel'] = self['ascendLevel']
        self.person['newPlayerName'] = self['newPlayerName']
        # end handle [GC_SYNC_CUR_WUSHEN_ASCEND_LIST] message attrs, auto generate do not change
        pass


class GC_FREE_CHOICE_INFO (Packet):
    def handle(self):
        # begin handle [GC_FREE_CHOICE_INFO] message attrs, auto generate do not change
        self.person['actId'] = self['actId']
        self.person['buyLimitId'] = self['buyLimitId']
        self.person['buyCount'] = self['buyCount']
        self.person['choiceData'] = self['choiceData']
        self.person['syncType'] = self['syncType']
        # end handle [GC_FREE_CHOICE_INFO] message attrs, auto generate do not change
        pass


class CG_FREE_CHOICE_OP (Packet):
	pass


class GC_SYNC_BUBBLECHAT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BUBBLECHAT] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['deadline'] = self['deadline']
        self.person['curId'] = self['curId']
        self.person['isunlock'] = self['isunlock']
        # end handle [GC_SYNC_BUBBLECHAT] message attrs, auto generate do not change
        pass


class CG_REQ_SET_BUBBLECHAT (Packet):
	pass


class GC_SYNC_CUR_HORNSTYLE (Packet):
    def handle(self):
        # begin handle [GC_SYNC_CUR_HORNSTYLE] message attrs, auto generate do not change
        self.person['curId'] = self['curId']
        # end handle [GC_SYNC_CUR_HORNSTYLE] message attrs, auto generate do not change
        pass


class CG_REQ_SET_HORNSTYLE (Packet):
	pass


class CG_SERVANT_RECOMMEND_SETUP (Packet):
	pass


class GC_SERVANT_RECOMMEND_SETUP (Packet):
    def handle(self):
        # begin handle [GC_SERVANT_RECOMMEND_SETUP] message attrs, auto generate do not change
        self.person['tabId'] = self['tabId']
        self.person['success'] = self['success']
        self.person['equipError'] = self['equipError']
        # end handle [GC_SERVANT_RECOMMEND_SETUP] message attrs, auto generate do not change
        pass


class CG_PUTIN_MATERIALBAG_BYID (Packet):
	pass


class GC_SYNC_MATERIALBAG (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MATERIALBAG] message attrs, auto generate do not change
        self.person['itemid'] = self['itemid']
        self.person['itemcount'] = self['itemcount']
        # end handle [GC_SYNC_MATERIALBAG] message attrs, auto generate do not change
        pass


class CG_SYSTEMTRADE_SELLLIST (Packet):
	pass


class GC_SYSTEMTRADE_SELLLIST (Packet):
    def handle(self):
        # begin handle [GC_SYSTEMTRADE_SELLLIST] message attrs, auto generate do not change
        # end handle [GC_SYSTEMTRADE_SELLLIST] message attrs, auto generate do not change
        pass


class CG_REQUEST_JADE_DATA (Packet):
	pass


class GC_SYNC_JADE_DATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_JADE_DATA] message attrs, auto generate do not change
        self.person['TotalLevel'] = self['TotalLevel']
        self.person['Jades'] = self['Jades']
        self.person['JadeEquipScore'] = self['JadeEquipScore']
        # end handle [GC_SYNC_JADE_DATA] message attrs, auto generate do not change
        pass


class CG_REQUEST_INTENSIFY_GEM (Packet):
	pass


class GC_RESPONSE_INTENSIFY_GEM (Packet):
    def handle(self):
        # begin handle [GC_RESPONSE_INTENSIFY_GEM] message attrs, auto generate do not change
        self.person['JadeIndex'] = self['JadeIndex']
        self.person['GemIndex'] = self['GemIndex']
        self.person['GemAttr'] = self['GemAttr']
        # end handle [GC_RESPONSE_INTENSIFY_GEM] message attrs, auto generate do not change
        pass


class CG_REQUEST_LEVELUP_GEM (Packet):
	pass


class GC_RESPONSE_LEVELUP_GEM (Packet):
    def handle(self):
        # begin handle [GC_RESPONSE_LEVELUP_GEM] message attrs, auto generate do not change
        self.person['JadeIndex'] = self['JadeIndex']
        self.person['GemIndex'] = self['GemIndex']
        # end handle [GC_RESPONSE_LEVELUP_GEM] message attrs, auto generate do not change
        pass


class CG_REQUEST_ACTIVATE_JADE (Packet):
	pass


class GC_RESPONSE_ACTIVATE_JADE (Packet):
    def handle(self):
        # begin handle [GC_RESPONSE_ACTIVATE_JADE] message attrs, auto generate do not change
        self.person['JadeIndex'] = self['JadeIndex']
        # end handle [GC_RESPONSE_ACTIVATE_JADE] message attrs, auto generate do not change
        pass


class CG_REQUEST_FUSE_GEM (Packet):
	pass


class GC_RESPONSE_FUSE_GEM (Packet):
    def handle(self):
        # begin handle [GC_RESPONSE_FUSE_GEM] message attrs, auto generate do not change
        self.person['JadeIndex'] = self['JadeIndex']
        self.person['GemIndex'] = self['GemIndex']
        # end handle [GC_RESPONSE_FUSE_GEM] message attrs, auto generate do not change
        pass


class GC_SYNC_JADESLOT_UNLOCK (Packet):
    def handle(self):
        # begin handle [GC_SYNC_JADESLOT_UNLOCK] message attrs, auto generate do not change
        self.person['JadeId'] = self['JadeId']
        self.person['SlotIndex'] = self['SlotIndex']
        # end handle [GC_SYNC_JADESLOT_UNLOCK] message attrs, auto generate do not change
        pass


class CG_QUICK_BUY_ITEM (Packet):
	pass


class GC_QUICK_BUY_ITEM (Packet):
    def handle(self):
        # begin handle [GC_QUICK_BUY_ITEM] message attrs, auto generate do not change
        self.person['itemId'] = self['itemId']
        self.person['itemCount'] = self['itemCount']
        # end handle [GC_QUICK_BUY_ITEM] message attrs, auto generate do not change
        pass


class CG_TAKEOUT_MATERIALBAG (Packet):
	pass


class CG_HUG_UNLOCK_XPBUFF (Packet):
	pass


class GC_HUG_UNLOCK_EFFECT (Packet):
    def handle(self):
        # begin handle [GC_HUG_UNLOCK_EFFECT] message attrs, auto generate do not change
        self.person['success'] = self['success']
        self.person['id'] = self['id']
        # end handle [GC_HUG_UNLOCK_EFFECT] message attrs, auto generate do not change
        pass


class GC_HUG_INFO (Packet):
    def handle(self):
        # begin handle [GC_HUG_INFO] message attrs, auto generate do not change
        self.person['level'] = self['level']
        self.person['unlockEffects'] = self['unlockEffects']
        self.person['useEffect'] = self['useEffect']
        # end handle [GC_HUG_INFO] message attrs, auto generate do not change
        pass


class GC_WILDSCENEDUEL_MESSAGEBOX (Packet):
    def handle(self):
        # begin handle [GC_WILDSCENEDUEL_MESSAGEBOX] message attrs, auto generate do not change
        self.person['DuelGuid'] = self['DuelGuid']
        self.person['DuelName'] = self['DuelName']
        # end handle [GC_WILDSCENEDUEL_MESSAGEBOX] message attrs, auto generate do not change
        pass


class CG_HUG_UNLOCK_EFFECT (Packet):
	pass


class GC_HUG_UNLOCK_XPBUFF (Packet):
    def handle(self):
        # begin handle [GC_HUG_UNLOCK_XPBUFF] message attrs, auto generate do not change
        self.person['success'] = self['success']
        self.person['level'] = self['level']
        # end handle [GC_HUG_UNLOCK_XPBUFF] message attrs, auto generate do not change
        pass


class CG_HUG_CHANGE_USEEFFECT (Packet):
	pass


class GC_HUG_CHANGE_USEEFFECT (Packet):
    def handle(self):
        # begin handle [GC_HUG_CHANGE_USEEFFECT] message attrs, auto generate do not change
        self.person['success'] = self['success']
        self.person['id'] = self['id']
        # end handle [GC_HUG_CHANGE_USEEFFECT] message attrs, auto generate do not change
        pass


class GC_FREE_CHOICE_BUY_SUCCESS (Packet):
    def handle(self):
        # begin handle [GC_FREE_CHOICE_BUY_SUCCESS] message attrs, auto generate do not change
        self.person['id'] = self['id']
        self.person['count'] = self['count']
        self.person['bind'] = self['bind']
        # end handle [GC_FREE_CHOICE_BUY_SUCCESS] message attrs, auto generate do not change
        pass


class GC_FRIENDGROUP_INFO (Packet):
    def handle(self):
        # begin handle [GC_FRIENDGROUP_INFO] message attrs, auto generate do not change
        self.person['groupname'] = self['groupname']
        self.person['issyncclientgroup'] = self['issyncclientgroup']
        # end handle [GC_FRIENDGROUP_INFO] message attrs, auto generate do not change
        pass


class CG_SYNC_CLIENT_CLIENTFRIENDGROUP (Packet):
	pass


class CG_CHANGE_FRIENDGROUPNAME (Packet):
	pass


class CG_CHANGE_FRIENDGROUP (Packet):
	pass


class CG_REQ_SET_POYU_SWITCH (Packet):
	pass


class GC_SYNC_POYU_SWITCH (Packet):
    def handle(self):
        # begin handle [GC_SYNC_POYU_SWITCH] message attrs, auto generate do not change
        self.person['open'] = self['open']
        # end handle [GC_SYNC_POYU_SWITCH] message attrs, auto generate do not change
        pass


class GC_SYNC_ANSWERACTIVITY_ANSWERRES (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ANSWERACTIVITY_ANSWERRES] message attrs, auto generate do not change
        self.person['isRight'] = self['isRight']
        # end handle [GC_SYNC_ANSWERACTIVITY_ANSWERRES] message attrs, auto generate do not change
        pass


class CG_RECORD_AUTOPLAY_INFO (Packet):
	pass


class GC_AUTOPLAY_INFO (Packet):
    def handle(self):
        # begin handle [GC_AUTOPLAY_INFO] message attrs, auto generate do not change
        self.person['info'] = self['info']
        # end handle [GC_AUTOPLAY_INFO] message attrs, auto generate do not change
        pass


class CG_ADD_MISGUIDE_ID (Packet):
	pass


class GC_SYNC_MISGUIDE_COMPLETED_INFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_MISGUIDE_COMPLETED_INFO] message attrs, auto generate do not change
        self.person['misguideId'] = self['misguideId']
        # end handle [GC_SYNC_MISGUIDE_COMPLETED_INFO] message attrs, auto generate do not change
        pass


class CG_SCENE_LOAD_FINISH (Packet):
	pass


class CG_GOODLUCK_UI_STATE (Packet):
	pass


class GC_RESPONSE_LEVELUP_GEM_FAIL (Packet):
    def handle(self):
        # begin handle [GC_RESPONSE_LEVELUP_GEM_FAIL] message attrs, auto generate do not change
        self.person['JadeIndex'] = self['JadeIndex']
        self.person['GemIndex'] = self['GemIndex']
        # end handle [GC_RESPONSE_LEVELUP_GEM_FAIL] message attrs, auto generate do not change
        pass


class GC_COPYSCENE_UPDATE_COMBAT_CANMOUNTINLIMITTIME (Packet):
    def handle(self):
        # begin handle [GC_COPYSCENE_UPDATE_COMBAT_CANMOUNTINLIMITTIME] message attrs, auto generate do not change
        self.person['lastReliveTime'] = self['lastReliveTime']
        # end handle [GC_COPYSCENE_UPDATE_COMBAT_CANMOUNTINLIMITTIME] message attrs, auto generate do not change
        pass



class GC_SYNC_SKILLBALLDATA (Packet):
    def handle(self):
        # begin handle [GC_SYNC_SKILLBALLDATA] message attrs, auto generate do not change
        self.person['skillballlist'] = self['skillballlist']
        # end handle [GC_SYNC_SKILLBALLDATA] message attrs, auto generate do not change
        pass


class CG_REQ_HIDE_ACCAMT (Packet):
	pass


class GC_SYNC_HIDE_ACCAMT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HIDE_ACCAMT] message attrs, auto generate do not change
        self.person['bHide'] = self['bHide']
        # end handle [GC_SYNC_HIDE_ACCAMT] message attrs, auto generate do not change
        pass


class CG_REQ_HIDE_ACCRECHARGE_LV (Packet):
	pass


class GC_SYNC_HIDE_ACCRECHARGE_LV (Packet):
    def handle(self):
        # begin handle [GC_SYNC_HIDE_ACCRECHARGE_LV] message attrs, auto generate do not change
        self.person['bHide'] = self['bHide']
        # end handle [GC_SYNC_HIDE_ACCRECHARGE_LV] message attrs, auto generate do not change
        pass


class CG_BROTHERHOOD_OTHER (Packet):
	pass


class GC_BROTHERHOOD_OTHER (Packet):
    def handle(self):
        # begin handle [GC_BROTHERHOOD_OTHER] message attrs, auto generate do not change
        self.person['brotherhoodGuid'] = self['brotherhoodGuid']
        self.person['brotherhoodName'] = self['brotherhoodName']
        self.person['chiefGuid'] = self['chiefGuid']
        self.person['brotherhoodLevel'] = self['brotherhoodLevel']
        self.person['weeklyloyaltyVal'] = self['weeklyloyaltyVal']
        self.person['memberGuid'] = self['memberGuid']
        self.person['memberName'] = self['memberName']
        self.person['memberProf'] = self['memberProf']
        self.person['memberLevel'] = self['memberLevel']
        self.person['memberState'] = self['memberState']
        self.person['memberPos'] = self['memberPos']
        self.person['memberSex'] = self['memberSex']
        self.person['memberTitle'] = self['memberTitle']
        self.person['memberCustomHeadPic'] = self['memberCustomHeadPic']
        self.person['memberPhotoFrameId'] = self['memberPhotoFrameId']
        # end handle [GC_BROTHERHOOD_OTHER] message attrs, auto generate do not change
        pass


class CG_REQ_HANHUA_HELPTEAM (Packet):
	pass


class CG_REQ_INVITE_HELPTEAM (Packet):
	pass


class CG_CANCEL_TRACK_PLAYER (Packet):
	pass


class GC_SYNC_TURNTABLEINFO (Packet):
    def handle(self):
        # begin handle [GC_SYNC_TURNTABLEINFO] message attrs, auto generate do not change
        self.person['version'] = self['version']
        self.person['lotterynum'] = self['lotterynum']
        self.person['serverlevel'] = self['serverlevel']
        self.person['lotteryitemnum'] = self['lotteryitemnum']
        self.person['exchangecoinid'] = self['exchangecoinid']
        self.person['exchangecoinnum'] = self['exchangecoinnum']
        self.person['exchangelimitid'] = self['exchangelimitid']
        self.person['exchangelimitnum'] = self['exchangelimitnum']
        self.person['gotlotterynumreward'] = self['gotlotterynumreward']
        # end handle [GC_SYNC_TURNTABLEINFO] message attrs, auto generate do not change
        pass


class CG_REQ_PLAYTURNTABLE (Packet):
	pass


class GC_RET_PLAYTURNTABLE_RESULT (Packet):
    def handle(self):
        # begin handle [GC_RET_PLAYTURNTABLE_RESULT] message attrs, auto generate do not change
        self.person['result'] = self['result']
        # end handle [GC_RET_PLAYTURNTABLE_RESULT] message attrs, auto generate do not change
        pass


class CG_REQ_TURNTABLE_GETLOTTERYNUMREWARD (Packet):
	pass


class CG_REQ_TURNTABLE_EXCHANGESHOPITEM (Packet):
	pass


class GC_SYNC_ATTACK_PLAYER (Packet):
    def handle(self):
        # begin handle [GC_SYNC_ATTACK_PLAYER] message attrs, auto generate do not change
        self.person['objID'] = self['objID']
        # end handle [GC_SYNC_ATTACK_PLAYER] message attrs, auto generate do not change
        pass


class CG_REQ_JOIN_HELPTEAM (Packet):
	pass


class GC_SYNC_RIDE_TIGER_TIME (Packet):
    def handle(self):
        # begin handle [GC_SYNC_RIDE_TIGER_TIME] message attrs, auto generate do not change
        self.person['rideTime'] = self['rideTime']
        self.person['rewardStatus'] = self['rewardStatus']
        # end handle [GC_SYNC_RIDE_TIGER_TIME] message attrs, auto generate do not change
        pass


class CG_GET_RIDE_TIGER_REWARD (Packet):
	pass


class GC_SYNC_BOUNTY_FIGHT_RESULT (Packet):
    def handle(self):
        # begin handle [GC_SYNC_BOUNTY_FIGHT_RESULT] message attrs, auto generate do not change
        self.person['bossDataId'] = self['bossDataId']
        self.person['itemId'] = self['itemId']
        self.person['itemCount'] = self['itemCount']
        self.person['itemBind'] = self['itemBind']
        # end handle [GC_SYNC_BOUNTY_FIGHT_RESULT] message attrs, auto generate do not change
        pass


class GC_SYNC_VIEW_PLAYER_NEW_PLAYER_CATCH (Packet):
    def handle(self):
        # begin handle [GC_SYNC_VIEW_PLAYER_NEW_PLAYER_CATCH] message attrs, auto generate do not change
        self.person['playerGuid'] = self['playerGuid']
        self.person['haveNewPlayerCatch'] = self['haveNewPlayerCatch']
        # end handle [GC_SYNC_VIEW_PLAYER_NEW_PLAYER_CATCH] message attrs, auto generate do not change
        pass


class GC_SHOW_EAR (Packet):
    def handle(self):
        # begin handle [GC_SHOW_EAR] message attrs, auto generate do not change
        self.person['showear'] = self['showear']
        # end handle [GC_SHOW_EAR] message attrs, auto generate do not change
        pass


class CG_SHOW_EAR (Packet):
	pass



