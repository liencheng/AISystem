import gevent
from tasks import actions
from tasks.actions import accounts


class mission_displayed:
	def __init__(self, person):
		self.person = person
		self.person['profession'] = 6

	def run(self):
		res = self.person.ActionCG_GUILD_REQ_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE_OK', 'GC_SYN_ATTR', 'GC_BROADCAST_YLTX', 'GC_MOVE', 'GC_SYNC_HOME_PRAY_ATTR', 'GC_SYNC_SHAKE_ACTIVITY_INFO', 'GC_SYNC_SHAKE_CHALLENGE_DATA', 'GC_SYNC_BINGXUEJIE_QUIZ_RECORD', 'GC_SYN_SKILLINFO', 'GC_SYNC_SKILLBARINFO', 'GC_SYN_SKILLZHUANJINGINFO', 'GC_PLAYERTIPSCHANGE', 'GC_ACHIEVEMENT_VALUE_INFO', 'GC_BROADCAST_ATTR', 'GC_SYN_DIRTY_MENTOR_INFO', 'GC_STOP'])
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nBits'] = 42
		self.person['bFlag'] = True
		self.person['bIsLog'] = False
		res = self.person.ActionCG_ASK_SETCOMMONFLAG()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_ASK_COMMONFLAG_RET', 'GC_MOVE', 'GC_STOP'])
		if not res[0]:
			return res
		gevent.sleep(2)
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RECOVERYFOODINFO_SYNC', 'GC_MOVE'])
		if not res[0]:
			return res
		gevent.sleep(2)
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RECOVERYFOODINFO_SYNC', 'GC_MOVE', 'GC_WEATHER'])
		if not res[0]:
			return res
		gevent.sleep(2)
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RECOVERYFOODINFO_SYNC', 'GC_MOVE', 'GC_STOP'])
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nAchievementType'] = [96]
		self.person['nValue'] = [27]
		res = self.person.ActionCG_ACHIEVEMENT_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_ACHIEVEMENT_VALUE_INFO', 'GC_MOVE'])
		if not res[0]:
			return res
		self.person['posx'] = 93.24120330810547
		self.person['posy'] = 306.6499938964844
		self.person['posz'] = 359.913330078125
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 93.56867980957031
		self.person['posy'] = 306.64324951171875
		self.person['posz'] = 359.80035400390625
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 94.27783966064453
		self.person['posy'] = 306.5764465332031
		self.person['posz'] = 359.5556945800781
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 94.50027465820312
		self.person['posy'] = 306.5502014160156
		self.person['posz'] = 359.47894287109375
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 94.9244613647461
		self.person['posy'] = 306.5043640136719
		self.person['posz'] = 359.33258056640625
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 95.26362609863281
		self.person['posy'] = 306.4613037109375
		self.person['posz'] = 359.215576171875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 95.60491180419922
		self.person['posy'] = 306.40728759765625
		self.person['posz'] = 359.0978088378906
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 95.94934844970703
		self.person['posy'] = 306.36737060546875
		self.person['posz'] = 358.9789733886719
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 96.27737426757812
		self.person['posy'] = 306.36041259765625
		self.person['posz'] = 358.8658142089844
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packet_with_heartbeat(self.person,'GC_MOVE')
		self.person['posx'] = 96.61676788330078
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 358.7486877441406
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 96.74275970458984
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 358.7052307128906
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 97.34001159667969
		self.person['posy'] = 306.3661804199219
		self.person['posz'] = 358.4991760253906
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packet_with_heartbeat(self.person,'GC_CREATE_NPC')
		self.person['posx'] = 97.57539367675781
		self.person['posy'] = 306.3811340332031
		self.person['posz'] = 358.4179382324219
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 98.00443267822266
		self.person['posy'] = 306.3900146484375
		self.person['posz'] = 358.2699279785156
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 98.3486328125
		self.person['posy'] = 306.3831787109375
		self.person['posz'] = 358.15118408203125
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 98.57975006103516
		self.person['posy'] = 306.3733825683594
		self.person['posz'] = 358.0714416503906
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 99.03598022460938
		self.person['posy'] = 306.3620300292969
		self.person['posz'] = 357.9140319824219
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 99.37091064453125
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 357.7984924316406
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 99.71105194091797
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 357.6811218261719
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 100.0601577758789
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 357.5606689453125
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 100.39342498779297
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 357.4457092285156
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 100.73555755615234
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 357.3276672363281
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 101.05997467041016
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 357.2157287597656
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 101.41466522216797
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 357.0933532714844
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 101.73998260498047
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 356.9811096191406
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 102.07465362548828
		self.person['posy'] = 306.3599853515625
		self.person['posz'] = 356.86566162109375
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_CREATE_NPC', 'GC_MOVE', 'GC_SYNC_SHAKE_ACTIVITY_INFO', 'GC_SYNC_SHAKE_CHALLENGE_DATA', 'GC_SYNC_BINGXUEJIE_QUIZ_RECORD'])
		gevent.sleep(2)
		self.person['posx'] = 103.26329803466797
		self.person['posy'] = 306.33258056640625
		self.person['posz'] = 356.4555358886719
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 104.39726257324219
		self.person['posy'] = 306.30859375
		self.person['posz'] = 356.0643005371094
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 105.30025482177734
		self.person['posy'] = 306.2799987792969
		self.person['posz'] = 355.75274658203125
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 105.732177734375
		self.person['posy'] = 306.2799987792969
		self.person['posz'] = 355.6037292480469
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 105.95008850097656
		self.person['posy'] = 306.2757263183594
		self.person['posz'] = 355.528564453125
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_CREATE_NPC', 'GC_MOVE'])
		self.person['posx'] = 106.47320556640625
		self.person['posy'] = 306.2699890136719
		self.person['posz'] = 355.3480529785156
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 106.84142303466797
		self.person['posy'] = 306.2699890136719
		self.person['posz'] = 355.2210388183594
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 107.18671417236328
		self.person['posy'] = 306.2699890136719
		self.person['posz'] = 355.1018981933594
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 107.5253677368164
		self.person['posy'] = 306.2699890136719
		self.person['posz'] = 354.98504638671875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 107.86446380615234
		self.person['posy'] = 306.2699890136719
		self.person['posz'] = 354.8680725097656
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 108.20452117919922
		self.person['posy'] = 306.2699890136719
		self.person['posz'] = 354.750732421875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 108.54396057128906
		self.person['posy'] = 306.2699890136719
		self.person['posz'] = 354.6336364746094
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 108.8908920288086
		self.person['posy'] = 306.25042724609375
		self.person['posz'] = 354.5139465332031
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE', 'GC_CREATE_NPC'])
		self.person['posx'] = 109.24663543701172
		self.person['posy'] = 306.2319030761719
		self.person['posz'] = 354.3912048339844
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 109.56901550292969
		self.person['posy'] = 306.2174072265625
		self.person['posz'] = 354.27996826171875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_CREATE_NPC', 'GC_MOVE'])
		self.person['seleobjId'] = 10001
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		self.person['nMisId'] = 107
		self.person['nLogicID'] = 0
		self.person['nNpcType'] = 3
		self.person['nNpcServerID'] = 10001
		res = self.person.ActionCG_MIS_OPERATE_NPC()
		if not res[0]:
			return res
		self.person['posx'] = 109.91389465332031
		self.person['posy'] = 306.1955261230469
		self.person['posz'] = 354.1609802246094
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_SELOBJ_INFO', 'GC_SYNSELTRAGET_ATTR', 'GC_BUFF_SYNC_INFO', 'GC_MOVE'])
		self.person['posx'] = 111.04774475097656
		self.person['posy'] = 306.1700134277344
		self.person['posz'] = 353.769775390625
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_CREATE_NPC', 'GC_MOVE'])
		gevent.sleep(1)
		self.person['nMisID'] = 107
		res = self.person.ActionCG_MISSION_COMMIT()
		if not res[0]:
			return res
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_GET_XX', 'GC_GET_EXP', 'GC_MISSION_COMMIT_RET', 'GC_SYNC_COMMONDATA', 'GC_ACHIEVEMENT_VALUE_INFO', 'GC_RECOVERYFOODINFO_SYNC', 'GC_SYN_ATTR', 'GC_MOVE', 'GC_DELETE_OBJ'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nMisID'] = 270
		res = self.person.ActionCG_MISSION_ACCEPT()
		if not res[0]:
			return res
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MISSION_ACCEPT_RET', 'GC_MISSION_STATE', 'GC_SYN_ATTR', 'GC_SYN_SKILLINFO', 'GC_SYNC_SKILLBARINFO', 'GC_SYN_SKILLZHUANJINGINFO', 'GC_SYNC_COMMONDATA', 'GC_RECOVERYFOODINFO_SYNC', 'GC_MOVE'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nMisId'] = 270
		self.person['nLogicID'] = 0
		self.person['nNpcType'] = 3
		self.person['nNpcServerID'] = 10001
		res = self.person.ActionCG_MIS_OPERATE_NPC()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_BUFF_SYNC_INFO', 'GC_MOVE'])
		if not res[0]:
			return res
		self.person['nMisID'] = 270
		res = self.person.ActionCG_MISSION_COMMIT()
		if not res[0]:
			return res
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_UPDATE_PART_COMBATVAL', 'GC_SYNC_LEVELATTRIBUTE', 'GC_SYN_ATTR', 'GC_SYN_SKILLINFO', 'GC_SYNC_SKILLBARINFO', 'GC_SYN_SKILLZHUANJINGINFO', 'GC_PLAYERTIPSCHANGE', 'GC_ACHIEVEMENT_VALUE_INFO', 'GC_SYNC_LEVELREWARDINFO', 'GC_STALL_SYNC', 'GC_RECHARGESCORESHOP_SYNC', 'GC_ACCLOGIN_SYNCSTATUS', 'GC_SYNC_ARTIFACT_INFO', 'GC_SYNC_GROWWAY_INFO', 'GC_SYNC_NEWPLAYECATCH_DATA', 'GC_SYNC_LIMITBESTSELLER_DATA', 'GC_SYNC_PERIODBESTSELLER_DATA', 'GC_Sync_All_TXMQ_Info', 'GC_BROADCAST_ATTR', 'GC_GET_XX', 'GC_GET_EXP', 'GC_MISSION_COMMIT_RET', 'GC_SYNC_COMMONDATA', 'GC_RECOVERYFOODINFO_SYNC', 'GC_SYN_DIRTY_MENTOR_INFO', 'GC_UPDATE_GROWWAY_INFO', 'GC_LIMITSHOP_SYNC', 'GC_MOVE'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nMisID'] = 341
		res = self.person.ActionCG_MISSION_ACCEPT()
		if not res[0]:
			return res
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_DELETE_OBJ', 'GC_MISSION_ACCEPT_RET', 'GC_MISSION_STATE', 'GC_SYNC_COMMONDATA', 'GC_RECOVERYFOODINFO_SYNC', 'GC_MOVE'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['seleobjId'] = 10288
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_SELOBJ_INFO', 'GC_SYNSELTRAGET_ATTR'])
		if not res[0]:
			return res
		self.person['posx'] = 111.0677261352539
		self.person['posy'] = 306.16033935546875
		self.person['posz'] = 354.2523498535156
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE'])
		self.person['posx'] = 111.11738586425781
		self.person['posy'] = 306.1700134277344
		self.person['posz'] = 355.45123291015625
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE'])
		self.person['posx'] = 111.16339874267578
		self.person['posy'] = 306.2237854003906
		self.person['posz'] = 356.56219482421875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.21302795410156
		self.person['posy'] = 306.239990234375
		self.person['posz'] = 357.7605285644531
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_DELETE_OBJ', 'GC_MOVE'])
		self.person['posx'] = 111.23799896240234
		self.person['posy'] = 306.23590087890625
		self.person['posz'] = 358.3634338378906
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.28763580322266
		self.person['posy'] = 306.2320861816406
		self.person['posz'] = 359.5618591308594
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.30363464355469
		self.person['posy'] = 306.2665100097656
		self.person['posz'] = 359.9480285644531
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE', 'GC_DELETE_OBJ'])
		self.person['posx'] = 111.31844329833984
		self.person['posy'] = 306.3157043457031
		self.person['posz'] = 360.3055419921875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.33332824707031
		self.person['posy'] = 306.35894775390625
		self.person['posz'] = 360.66522216796875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.34883117675781
		self.person['posy'] = 306.41522216796875
		self.person['posz'] = 361.0393371582031
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.36122131347656
		self.person['posy'] = 306.45989990234375
		self.person['posz'] = 361.3385314941406
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_DELETE_OBJ', 'GC_MOVE', 'GC_STOP'])
		gevent.sleep(2)
		self.person['posx'] = 111.99980926513672
		self.person['posy'] = 306.52435302734375
		self.person['posz'] = 362.2445983886719
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['skillId'] = 70801
		self.person['targetId'] = 10288
		self.person['posx'] = 111.99980926513672
		self.person['posy'] = 306.52435302734375
		self.person['posz'] = 362.2445983886719
		self.person['curFaceto'] = 0.9568601846694946
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 112.8239974975586
		self.person['vTargetY'] = 306.55999755859375
		self.person['vTargetZ'] = 363.41400146484375
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE', 'GC_STOP', 'GC_RET_USE_SKILL_XML', 'GC_SYN_ATTR', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_BROADCAST_ATTR', 'GC_SYNSELTRAGET_ATTR', 'GC_RET_USE_SKILL'])
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['skillId'] = 70901
		self.person['targetId'] = 10288
		self.person['posx'] = 111.99980926513672
		self.person['posy'] = 306.52435302734375
		self.person['posz'] = 362.2445983886719
		self.person['curFaceto'] = 0.9568601846694946
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 0.0
		self.person['vTargetY'] = 0.0
		self.person['vTargetZ'] = 0.0
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_USE_SKILL_XML', 'GC_SYN_ATTR', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_SYNSELTRAGET_ATTR', 'GC_BROADCAST_ATTR', 'GC_RET_USE_SKILL', 'GC_BUFF_REMOVE_INFO', 'GC_MOVE'])
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['skillId'] = 71001
		self.person['targetId'] = 10288
		self.person['posx'] = 111.99980926513672
		self.person['posy'] = 306.52435302734375
		self.person['posz'] = 362.2445983886719
		self.person['curFaceto'] = 0.9568601846694946
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 0.0
		self.person['vTargetY'] = 0.0
		self.person['vTargetZ'] = 0.0
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_USE_SKILL_XML', 'GC_SYN_ATTR', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_SYNSELTRAGET_ATTR', 'GC_MOVE', 'GC_BROADCAST_ATTR', 'GC_CREATE_NPC', 'GC_RET_USE_SKILL'])
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['skillId'] = 70801
		self.person['targetId'] = 10288
		self.person['posx'] = 111.99980926513672
		self.person['posy'] = 306.52435302734375
		self.person['posz'] = 362.2445983886719
		self.person['curFaceto'] = 0.9568601846694946
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 111.99980926513672
		self.person['vTargetY'] = 306.5199890136719
		self.person['vTargetZ'] = 362.2445983886719
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_USE_SKILL_XML', 'GC_SYN_ATTR', 'GC_DAMAGEBOARD_INFO', 'GC_MISSION_PARAM', 'GC_GET_ITEM', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_SEND_IMPACT', 'GC_BROADCAST_ATTR', 'GC_SYNSELTRAGET_ATTR', 'GC_UPDATEITEM'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['seleobjId'] = -1
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_SELOBJ_INFO', 'GC_MOVE'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['seleobjId'] = 10308
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_SELOBJ_INFO', 'GC_SYNSELTRAGET_ATTR'])
		if not res[0]:
			return res
		self.person['posx'] = 112.15433502197266
		self.person['posy'] = 306.39813232421875
		self.person['posz'] = 361.7585754394531
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 112.26543426513672
		self.person['posy'] = 306.3464660644531
		self.person['posz'] = 361.40911865234375
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['skillId'] = 70801
		self.person['targetId'] = 10308
		self.person['posx'] = 112.26543426513672
		self.person['posy'] = 306.3464660644531
		self.person['posz'] = 361.40911865234375
		self.person['curFaceto'] = -1.2629663944244385
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 112.81200408935547
		self.person['vTargetY'] = 306.2200012207031
		self.person['vTargetZ'] = 359.69000244140625
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_STOP', 'GC_RET_USE_SKILL_XML', 'GC_CREATE_NPC', 'GC_SYN_ATTR', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_BROADCAST_ATTR', 'GC_SYNSELTRAGET_ATTR', 'GC_RET_USE_SKILL'])
		if not res[0]:
			return res
		self.person['skillId'] = 70901
		self.person['targetId'] = 10308
		self.person['posx'] = 112.26543426513672
		self.person['posy'] = 306.3464660644531
		self.person['posz'] = 361.40911865234375
		self.person['curFaceto'] = -1.2629663944244385
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 0.0
		self.person['vTargetY'] = 0.0
		self.person['vTargetZ'] = 0.0
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_USE_SKILL_XML', 'GC_SYN_ATTR', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_SYNSELTRAGET_ATTR', 'GC_BROADCAST_ATTR'])
		if not res[0]:
			return res
		self.person['skillId'] = 71001
		self.person['targetId'] = 10308
		self.person['posx'] = 112.26543426513672
		self.person['posy'] = 306.3464660644531
		self.person['posz'] = 361.40911865234375
		self.person['curFaceto'] = -1.2629663944244385
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 0.0
		self.person['vTargetY'] = 0.0
		self.person['vTargetZ'] = 0.0
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE', 'GC_RET_USE_SKILL_XML', 'GC_SYN_ATTR', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_SYNSELTRAGET_ATTR', 'GC_BROADCAST_ATTR'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['skillId'] = 70801
		self.person['targetId'] = 10308
		self.person['posx'] = 112.26543426513672
		self.person['posy'] = 306.3464660644531
		self.person['posz'] = 361.40911865234375
		self.person['curFaceto'] = -1.2629663944244385
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 112.26543426513672
		self.person['vTargetY'] = 306.3299865722656
		self.person['vTargetZ'] = 361.40911865234375
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_USE_SKILL_XML', 'GC_SYN_ATTR', 'GC_MISSION_PARAM', 'GC_GET_ITEM', 'GC_UPDATE_ANIMATION_STATE', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_BROADCAST_ATTR', 'GC_SYNSELTRAGET_ATTR', 'GC_UPDATEITEM'])
		if not res[0]:
			return res
		self.person['seleobjId'] = -1
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_DELETE_OBJ', 'GC_RET_SELOBJ_INFO', 'GC_MOVE', 'GC_CREATE_NPC', 'GC_BROADCAST_ATTR'])
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['type'] = 3
		info = actions.net_packets.PBMessage_pb2.SYSTEMINFO
		info.deviceModel = 'System Product Name (ASUS)'
		info.deviceName = 'PWRD-20210714BO'
		info.deviceType = 3
		info.deviceUDID = '51d6e64749e66b6accb5cf605f1f21219e8784f1'
		info.gDeviceID = 8578
		info.gDeviceName = 'NVIDIA GeForce GTX 1660 Ti'
		info.gDeviceType = 2
		info.gDeviceVendor = 'NVIDIA'
		info.gDeviceVendorID = 4318
		info.gDeviceVersion = 'Direct3D 11.0 [level 11.1]'
		info.gMemorySize = 5991
		info.gMultiThreaded = True
		info.gShaderLevel = 50
		info.maxTextureSize = 16384
		info.npotSuopported = 2
		info.osName = 'Windows 10  (10.0.19043) 64bit'
		info.processorCount = 16
		info.processorFreq = 2496
		info.processorName = '11th Gen Intel(R) Core(TM) i7-11700 @ 2.50GHz'
		info.systemMemSize = 16221
		info.platform = 0
		self.person['info'] = info
		res = self.person.ActionCG_CLIENT_BEHAVIOR()
		if not res[0]:
			return res
		res = actions.Functions.wait_packet_with_heartbeat(self.person,'GC_DELETE_OBJ')
		self.person['seleobjId'] = 10890
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		self.person['skillId'] = 70101
		self.person['targetId'] = 10890
		self.person['posx'] = 112.26543426513672
		self.person['posy'] = 306.3464660644531
		self.person['posz'] = 361.40911865234375
		self.person['curFaceto'] = -4.512198448181152
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 112.26543426513672
		self.person['vTargetY'] = 306.3299865722656
		self.person['vTargetZ'] = 361.40911865234375
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_SELOBJ_INFO', 'GC_SYNSELTRAGET_ATTR', 'GC_CDTIME_UPDATE', 'GC_RET_USE_SKILL_XML', 'GC_FORCE_SETPOS', 'GC_SYN_ATTR', 'GC_SYN_SKILLINFO', 'GC_SYNC_SKILLBARINFO', 'GC_SYN_SKILLZHUANJINGINFO', 'GC_PLAYERTIPSCHANGE', 'GC_ACHIEVEMENT_VALUE_INFO', 'GC_BROADCAST_ATTR', 'GC_TELEMOVE', 'GC_BUFF_SYNC_INFO', 'GC_CREATE_NPC', 'GC_SYN_DIRTY_MENTOR_INFO', 'GC_BUFF_REMOVE_INFO', 'GC_MISSION_PARAM', 'GC_MISSION_STATE', 'GC_GET_ITEM', 'GC_SYNC_DAMAGE_SHOW_HP', 'GC_DAMAGEBOARD_INFO', 'GC_SEND_IMPACT', 'GC_MOVE', 'GC_UPDATEITEM'])
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['seleobjId'] = -1
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_SELOBJ_INFO', 'GC_MOVE'])
		if not res[0]:
			return res
		self.person['posx'] = 112.30674743652344
		self.person['posy'] = 306.2128601074219
		self.person['posz'] = 360.4367370605469
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 112.25103759765625
		self.person['posy'] = 306.20001220703125
		self.person['posz'] = 360.0815734863281
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 112.19506072998047
		self.person['posy'] = 306.2051696777344
		self.person['posz'] = 359.7247619628906
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 112.13965606689453
		self.person['posy'] = 306.219482421875
		self.person['posz'] = 359.37152099609375
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 112.08240509033203
		self.person['posy'] = 306.2342529296875
		self.person['posz'] = 359.006591796875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 112.02629852294922
		self.person['posy'] = 306.239990234375
		self.person['posz'] = 358.64886474609375
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.97187042236328
		self.person['posy'] = 306.239990234375
		self.person['posz'] = 358.3018798828125
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.91576385498047
		self.person['posy'] = 306.239990234375
		self.person['posz'] = 357.9442138671875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.85963439941406
		self.person['posy'] = 306.239990234375
		self.person['posz'] = 357.5864562988281
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.8039779663086
		self.person['posy'] = 306.227783203125
		self.person['posz'] = 357.23162841796875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.74751281738281
		self.person['posy'] = 306.198974609375
		self.person['posz'] = 356.8716125488281
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.6927490234375
		self.person['posy'] = 306.17779541015625
		self.person['posz'] = 356.5224914550781
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.66388702392578
		self.person['posy'] = 306.1688537597656
		self.person['posz'] = 356.3384704589844
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.57743835449219
		self.person['posy'] = 306.1554260253906
		self.person['posz'] = 355.78741455078125
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.52387237548828
		self.person['posy'] = 306.1416015625
		self.person['posz'] = 355.4459228515625
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_CREATE_NPC', 'GC_MOVE'])
		self.person['seleobjId'] = 10001
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		self.person['nMisId'] = 341
		self.person['nLogicID'] = 0
		self.person['nNpcType'] = 3
		self.person['nNpcServerID'] = 10001
		res = self.person.ActionCG_MIS_OPERATE_NPC()
		if not res[0]:
			return res
		self.person['posx'] = 111.4677505493164
		self.person['posy'] = 306.15289306640625
		self.person['posz'] = 355.0882263183594
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		self.person['posx'] = 111.40807342529297
		self.person['posy'] = 306.1600036621094
		self.person['posz'] = 354.707763671875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RET_SELOBJ_INFO', 'GC_SYNSELTRAGET_ATTR', 'GC_BUFF_SYNC_INFO'])
		self.person['posx'] = 111.3847885131836
		self.person['posy'] = 306.1600036621094
		self.person['posz'] = 354.559326171875
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE', 'GC_DELETE_OBJ'])
		gevent.sleep(1)
		self.person['nMisID'] = 341
		res = self.person.ActionCG_MISSION_COMMIT()
		if not res[0]:
			return res
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MOVE', 'GC_MISSION_PARAM', 'GC_MISSION_STATE', 'GC_GET_XX', 'GC_GET_EXP', 'GC_MISSION_COMMIT_RET', 'GC_SYNC_COMMONDATA', 'GC_ACHIEVEMENT_VALUE_INFO', 'GC_RECOVERYFOODINFO_SYNC', 'GC_SYN_ATTR', 'GC_UPDATEITEM', 'GC_CREATE_NPC', 'GC_BROADCAST_ATTR'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nMisID'] = 1986
		res = self.person.ActionCG_MISSION_ACCEPT()
		if not res[0]:
			return res
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_MISSION_ACCEPT_RET', 'GC_MISSION_STATE', 'GC_RET_SELOBJ_INFO', 'GC_SYNC_COMMONDATA', 'GC_RECOVERYFOODINFO_SYNC'])
		if not res[0]:
			return res
		self.person['seleobjId'] = 10001
		res = self.person.ActionCG_ASK_SELOBJ_INFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_SYNC_LEVELATTRIBUTE', 'GC_SYN_ATTR', 'GC_SYN_SKILLINFO', 'GC_SYNC_SKILLBARINFO', 'GC_SYN_SKILLZHUANJINGINFO', 'GC_PLAYERTIPSCHANGE', 'GC_ACHIEVEMENT_VALUE_INFO', 'GC_SYNC_BOUNTY_ITEM_POS_LIST', 'GC_BUFF_CLEAR', 'GC_ENTER_SCENE', 'GC_CHAR_FACEDIR', 'GC_CREATE_PLAYER', 'GC_BUFF_SYNC_INFO', 'GC_SYNC_WARPATHBUFF_LIST', 'GC_MILITARY_SYNC_LIMITINFO', 'GC_SYNC_CHARM_VALUE', 'GC_SYNC_CHARM_LIMITINFO', 'GC_CANCEL_AUTOCOMBAT', 'GC_UPDATE_SKILL_UNLOCK_INFO', 'GC_UPDATE_SKILL_ACTIVE_INFO', 'GC_FORCE_SETPOS', 'GC_MISSION_STATE', 'GC_SYNC_FIRST_ENTERCOPYSCENE', 'GC_COPYSCENE_LEFTIME', 'GC_WEATHER', 'GC_BROADCAST_ATTR', 'GC_SYN_COOLDOWN_LAYER_INFO', 'GC_RET_SELOBJ_INFO', 'GC_SYN_DIRTY_MENTOR_INFO', 'GC_SYNC_STATISTICS_DATA', 'GC_SYC_FULL_FRIEND_LIST'])
		if not res[0]:
			return res
		self.person['isOK'] = 1
		self.person['OKCount'] = 0
		self.person['noticetip'] = ''
		self.person['noticecon'] = ''
		self.person['restype'] = ''
		self.person['ressubtype'] = ''
		self.person['resData'] = 0
		res = self.person.ActionCG_ENTER_SCENE_OK()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_SYNC_AIRWALL_INFO', 'GC_ENTER_COPY_SCENE_ENVIROMENT', 'GC_SYNC_STATISTICS_DATA', 'GC_COPYSCENE_COMBATSTATE', 'GC_NEWPRESTIGE_CHANGE_ELITE_NPC_SCENE_OK', 'GC_SYN_ATTR', 'GC_SYNC_MONITOR_NPC_INFO', 'GC_BROADCAST_YLTX'])
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['posx'] = 112.26000213623047
		self.person['posy'] = 306.20001220703125
		self.person['posz'] = 357.05999755859375
		self.person['ismoving'] = 1
		self.person['exState'] = 0
		res = self.person.ActionCG_MOVE()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_VOICE_OVER', 'GC_SYNC_MONITOR_NPC_INFO', 'GC_SYNC_STATISTICS_DATA'])
		self.person['skillId'] = 70101
		res = self.person.ActionCG_CLEARN_USE_SKILL_CD()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_CDTIME_UPDATE', 'GC_SYNC_MONITOR_NPC_INFO', 'GC_SYNC_STATISTICS_DATA', 'GC_BUFF_REMOVE_INFO', 'GC_CUTSCENE_PLAY', 'GC_CREATE_NPC', 'GC_BUFF_SYNC_INFO', 'GC_BROADCAST_ATTR'])
		gevent.sleep(2)
		self.person['cutSceneID'] = 455
		res = self.person.ActionCG_CUTSCENE_PLAYOVER()
		if not res[0]:
			return res
		res = self.person.ActionCG_REQUEST_RECOVERYFOODINFO()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_RECOVERYFOODINFO_SYNC', 'GC_SYNC_MONITOR_NPC_INFO', 'GC_SYNC_STATISTICS_DATA'])
		if not res[0]:
			return res
		self.person['skillId'] = 70101
		res = self.person.ActionCG_CLEARN_USE_SKILL_CD()
		if not res[0]:
			return res
		res = actions.Functions.wait_packets_with_heartbeat(self.person,['GC_CDTIME_UPDATE', 'GC_SYNC_MONITOR_NPC_INFO', 'GC_SYNC_STATISTICS_DATA', 'GC_BUFF_SYNC_INFO', 'GC_UI_NEWGUIDE', 'GC_SEND_IMPACT', 'GC_SYN_ATTR'])
		gevent.sleep(6)
		self.person['skillId'] = 72301
		self.person['targetId'] = 0
		self.person['posx'] = 112.26000213623047
		self.person['posy'] = 306.20001220703125
		self.person['posz'] = 357.05999755859375
		self.person['curFaceto'] = -2.619999885559082
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 112.26000213623047
		self.person['vTargetY'] = 306.20001220703125
		self.person['vTargetZ'] = 357.05999755859375
		res = self.person.ActionCG_SKILL_USE()
		if not res[0]:
			return res

		return res
