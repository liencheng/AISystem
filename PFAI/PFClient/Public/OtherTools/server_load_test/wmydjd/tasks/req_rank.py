import gevent
from tasks import actions
from tasks.actions import accounts


class req_rank:
	def __init__(self, person):
		self.person = person

	def run(self):
		self.person['nType'] = 2
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 2
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 3
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 3
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 4
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 4
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 47
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 47
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 50
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 50
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nType'] = 5
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 5
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 6
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 6
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nType'] = 7
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 7
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 8
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 8
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 52
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 52
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 59
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 59
		self.person['nPage'] = 1
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 1
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 1
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nType'] = 19
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 19
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nType'] = 20
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 20
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 22
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 22
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 9
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 9
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['nType'] = 16
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 16
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nType'] = 9
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 9
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		gevent.sleep(1)
		self.person['nType'] = 47
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		self.person['nType'] = 47
		self.person['nPage'] = 0
		res = self.person.ActionCG_ASK_RANK()
		if not res[0]:
			return res
		return res
