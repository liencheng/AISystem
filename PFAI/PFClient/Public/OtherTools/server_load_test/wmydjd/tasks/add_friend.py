import gevent
from tasks import actions
import loadlog
friends_map = {}


class add_friend:
	def __init__(self, person):
		self.person = person

	def run(self, log=loadlog):
		num = int(str(self.person['account'][2:]))
		account_index = num % 2
		if account_index == 1:
			# 请求发起者
			self.person['req_friend'] = True
			self.person['has_friend'] = False
			self.person['req_account_target'] = self.person['account'][:2]+str(num - 1)
			self.person['friends'] = []
		else:
			# 请求等待者，需要登记可查询自己的guid
			friends_map[self.person['account']] = self.person['guid']
			self.person['req_friend'] = False
			self.person['has_apply'] = False
			self.person['applylist'] = []
			self.person['friends'] = []

		gevent.sleep(2)
		if self.person['req_friend']:
			while not self.person['has_friend']:
				if friends_map[self.person['req_account_target']]:
					self.person['add_friend_guid'] = friends_map[self.person['req_account_target']]
					self.person['realAddFrienType'] = 0
					self.person['checkSignCode'] = 0
					self.person['addfriendmsg'] = ''
					self.person['checkcreditscore'] = True
					res = self.person.ActionCG_ADDFRIEND()
					if not res[0]:
						return res
					res = actions.Functions.wait_for_packet(self.person, "GC_ADDFRIEND", 10, True)
					if len(self.person['friends']) > 0:
						self.person['has_friend'] = True

				else:
					gevent.sleep(2)
		else:
			while not self.person['has_apply'] or len(self.person['applylist']) < 1:
				res = actions.Functions.wait_for_packet(self.person, 'GC_ADDAPPLYLIST', 10, True)
				if not res[0]:
					gevent.sleep(2)
				if len(self.person['applylist']) > 0:
					apply = self.person['applylist'][-1]
					log.info(f"account {self.person['account']} receive friend apply from {apply['guid']} {apply['Name']}")
					self.person['add_friend_guid'] = apply['guid']
					self.person['realAddFrienType'] = 1
					self.person['checkSignCode'] = 0
					self.person['addfriendmsg'] = ''
					self.person['checkcreditscore'] = True
					res = self.person.ActionCG_ADDFRIEND()
					if not res[0]:
						return res

		self.person['isOpen'] = 0
		res = self.person.ActionCG_SET_SOCIALUI_IS_NEEDTO_UPDATE()
		if not res[0]:
			return res
		gevent.sleep(2)

		self.person['isOpen'] = 1
		res = self.person.ActionCG_SET_SOCIALUI_IS_NEEDTO_UPDATE()
		if not res[0]:
			return res
		gevent.sleep(2)

		self.person['isOpen'] = 0
		res = self.person.ActionCG_SET_SOCIALUI_IS_NEEDTO_UPDATE()
		if not res[0]:
			return res

		return res
