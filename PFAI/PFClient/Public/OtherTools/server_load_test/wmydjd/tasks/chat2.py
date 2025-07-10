import gevent
from tasks import actions
from tasks.actions import accounts


class chat2:
	def __init__(self, person):
		self.person = person

	def run(self):
		print("chat2")

		self.person['Content'] = 'chatchatchat'
		self.person['Channel'] = 1
		self.person['Link'] = []
		self.person['LinkData'] = []
		self.person['VoiceFile'] = ''
		self.person['VoiceDuration'] = 0
		self.person['LinkItemGuid'] = []
		self.person['LinkFairyGuid'] = []
		self.person['LinkTitleId'] = []
		self.person['LinkFashionId'] = []
		self.person['ReceiverGuid'] = 0
		self.person['ReceiverName'] = ''
		self.person['ChannelParam'] = 0
		self.person['EmotionUnlock'] = 0
		self.person['LinkPetId'] = []
		self.person['LinkGodWeapon'] = []
		self.person['VoiceLanguage'] = ''
		res = self.person.ActionCG_CHAT()
		if not res[0]:
			return res

		gevent.sleep(11)
		self.person['Content'] = 'gogogo'
		self.person['Channel'] = 1
		self.person['Link'] = []
		self.person['LinkData'] = []
		self.person['VoiceFile'] = ''
		self.person['VoiceDuration'] = 0
		self.person['LinkItemGuid'] = []
		self.person['LinkFairyGuid'] = []
		self.person['LinkTitleId'] = []
		self.person['LinkFashionId'] = []
		self.person['ReceiverGuid'] = 0
		self.person['ReceiverName'] = ''
		self.person['ChannelParam'] = 0
		self.person['EmotionUnlock'] = 0
		self.person['LinkPetId'] = []
		self.person['LinkGodWeapon'] = []
		self.person['VoiceLanguage'] = ''
		return self.person.ActionCG_CHAT()
