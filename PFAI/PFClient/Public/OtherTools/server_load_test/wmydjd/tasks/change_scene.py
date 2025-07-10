import gevent
from tasks import actions
from tasks.actions import accounts
import loadlog

class change_scene:
	def __init__(self, person):
		self.person = person

	def run(self):
		gevent.sleep(2)
		self.person['cmdstr'] = 'okcs'
		res = self.person.ActionCG_GMCMDSTR()
		if not res[0]:
			return res
		gevent.sleep(2)

		loadlog.info('change to 38')
		self.person['sceneID'] = 38
		self.person['position'] = 0
		res = self.person.ActionCG_REQ_CHANGE_SCENE_WORLDMAP()
		if not res[0]:
			return res
		res = actions.Functions.wait_for_packet(self.person,'GC_USE_SKILL_XML_MainPlayer')
		if not res[0]:
			return res
		gevent.sleep(2)
		self.person['skillId'] = 900201
		self.person['targetId'] = self.person['TargetId']
		self.person['posx'] = 78.17449951171875
		self.person['posy'] = 306.3699951171875
		self.person['posz'] = 264.05999755859375
		self.person['curFaceto'] = 1.2253655195236206
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 0.0
		self.person['vTargetY'] = 0.0
		self.person['vTargetZ'] = 0.0
		res = self.person.ActionCG_SKILL_USE()
		if not res or not res[0]:
			return res

		res = actions.Functions.wait_for_packets(self.person,['GC_RET_USE_SKILL_XML','GC_SKILL_FINISH'])
		if not res or not res[0]:
			return res

		gevent.sleep(2)

		self.person['isOK'] = 1
		self.person['OKCount'] = 0
		self.person['noticetip'] = ''
		self.person['noticecon'] = ''
		self.person['restype'] = ''
		self.person['ressubtype'] = ''
		self.person['resData'] = 0
		res = self.person.ActionCG_ENTER_SCENE_OK()
		if not res or not res[0]:
			return res

		gevent.sleep(4)
		loadlog.info('change to 34')
		self.person['sceneID'] = 34
		self.person['position'] = 0
		res = self.person.ActionCG_REQ_CHANGE_SCENE_WORLDMAP()
		if not res or not res[0]:
			return res
		res = actions.Functions.wait_for_packet(self.person,'GC_USE_SKILL_XML_MainPlayer')
		if not res or not res[0]:
			return res
		self.person['skillId'] = 900201
		self.person['targetId'] = self.person['TargetId']
		self.person['posx'] = 143.4199981689453
		self.person['posy'] = 305.4100036621094
		self.person['posz'] = 271.30999755859375
		self.person['curFaceto'] = -0.7706296443939209
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 0.0
		self.person['vTargetY'] = 0.0
		self.person['vTargetZ'] = 0.0
		res = self.person.ActionCG_SKILL_USE()
		if not res or not res[0]:
			return res
		#'GC_RET_USE_SKILL_XML',
		res = actions.Functions.wait_for_packets(self.person,['GC_RET_USE_SKILL_XML', 'GC_SKILL_FINISH'])
		if not res or not res[0]:
			return res
		gevent.sleep(2)

		self.person['isOK'] = 1
		self.person['OKCount'] = 0
		self.person['noticetip'] = ''
		self.person['noticecon'] = ''
		self.person['restype'] = ''
		self.person['ressubtype'] = ''
		self.person['resData'] = 0
		res = self.person.ActionCG_ENTER_SCENE_OK()
		if not res or not res[0]:
			return res

		gevent.sleep(4)
		loadlog.info('change to 92')
		self.person['sceneID'] = 92
		self.person['position'] = 0
		res = self.person.ActionCG_REQ_CHANGE_SCENE_WORLDMAP()
		if not res or not res[0]:
			return res

		res = actions.Functions.wait_for_packet(self.person,'GC_USE_SKILL_XML_MainPlayer')
		if not res or not res[0]:
			return res

		#self.person['skillId'] = self.person['skillId']
		self.person['targetId'] = self.person['TargetId']
		self.person['posx'] = 124.93000030517578
		self.person['posy'] = 305.0
		self.person['posz'] = 92.94000244140625
		self.person['curFaceto'] = 0.0
		self.person['vDirectionX'] = 0.0
		self.person['vDirectionY'] = 0.0
		self.person['vDirectionZ'] = 0.0
		self.person['vTargetX'] = 0.0
		self.person['vTargetY'] = 0.0
		self.person['vTargetZ'] = 0.0
		res = self.person.ActionCG_SKILL_USE()
		if not res or not res[0]:
			return res
		#'GC_RET_USE_SKILL_XML',
		res = actions.Functions.wait_for_packets(self.person,['GC_RET_USE_SKILL_XML','GC_SKILL_FINISH'])
		if not res or not res[0]:
			return res
		gevent.sleep(2)
		self.person['isOK'] = 1
		self.person['OKCount'] = 0
		self.person['noticetip'] = ''
		self.person['noticecon'] = ''
		self.person['restype'] = ''
		self.person['ressubtype'] = ''
		self.person['resData'] = 0
		res = self.person.ActionCG_ENTER_SCENE_OK()
		if not res or not res[0]:
			return res
		loadlog.info("finish change scene task")
		return res
