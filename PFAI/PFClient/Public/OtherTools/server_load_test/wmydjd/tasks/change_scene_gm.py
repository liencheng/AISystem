import gevent
from tasks import actions
from tasks.actions import accounts
import random
import loadlog

scene_data = [
[4,'通天湖',58.37,304,36.28],
[6,'祖龙城',181.45,300.23,266.92],
[11,'剑仙城',206.42,323.463,201],
[34,'祖龙城郊',124.93,305,92.94],
[38,'积羽城',143.42,305.403,271.31],
[91,'万化城',76.107,314.447,152.419],
[92,'寻梦港',55.9552,297.43,316.1614],
[93,'灵渡汀州',74,300,60],
[130,'青铜优胜组',49.17,59.07,129.26],
[131,'青铜普通组',49.17,59.07,129.26],
[132,'秘银优胜组',49.17,59.07,129.26],
[133,'秘银普通组',49.17,59.07,129.26],
[134,'辉银优胜组',49.17,59.07,129.26],
[135,'辉银普通组',49.17,59.07,129.26],
[136,'白金优胜组',49.17,59.07,129.26],
[137,'白金普通组',49.17,59.07,129.26],
[144,'大世界寻梦港',238.78,300,145.75],
[148,'联赛休息室',49.17,59.07,129.26],
[166,'万化城',216.85,302.27,176.42],
[213,'无妄海',65,300,70],
[235,'鬼狱幻境',91.84,103.63,161.4],
[298,'刺骨之地',337.19,300.22,102.35],
[346,'龙战之野',192.17,298.07,354.88],
[349,'疾风草原',222.61,300.56,95.72],
[351,'万流城',285.17,301.37,197.63],
[364,'枫色秋苑',89.76,57.9,42.35],
[389,'钻石优胜组',49.17,59.07,129.26],
[390,'钻石普通组',49.17,59.07,129.26],
[502,'争锋助战',49.17,59.07,129.26],
[503,'争锋休息室',49.17,59.07,129.26],
[517,'联赛休息室',49.17,59.07,129.26],
[1250,'跨服休息室',49.17,59.07,129.26],
[1508,'赤焰旧地休息室',49.17,59.07,129.26]
]


class change_scene_gm:
	def __init__(self, person):
		self.person = person

	def run(self):
		gevent.sleep(2)
		self.person['cmdstr'] = 'okcs'
		res = self.person.ActionCG_GMCMDSTR()
		if not res[0]:
			return res
		gevent.sleep(2)
		scene_choice = random.choice(scene_data)
		self.person['cmdstr'] = 'cs,' + str(scene_choice[0])
		pos_param = ''
		for i in range(2,5):
			pos_param += ',' + str(scene_choice[i])
		self.person['cmdstr'] += pos_param
		loadlog.debug("account "+ self.person['account'] + " rand scene "+ str(scene_choice) + " gen : " + self.person['cmdstr'])
		res = self.person.ActionCG_GMCMDSTR()
		if not res[0]:
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
		return res
