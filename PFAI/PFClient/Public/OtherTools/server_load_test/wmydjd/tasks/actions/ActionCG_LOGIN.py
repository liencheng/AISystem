# -*- coding: utf-8 -*-
from Config import Configuration
from tasks.actions import net_packets
from tasks.actions import Functions
import loadlog

class ActionCG_LOGIN:
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = net_packets.PACKETS.CG_LOGIN(self.person)
        # params begin ( don't move this line )

        packet['logintype'] = Configuration.LoginType
        packet['gameversion'] = Configuration.GameVersion
        packet['programversion'] = Configuration.ProgramVersion
        packet['forceenter'] = Configuration.ForceEnter
        packet['maxpacketid'] = net_packets.Defines.MAX_ID()
        packet['accountname'] = self.person['account']
        packet['token'] = Configuration.AccountToken
        packet['bios'] = Configuration.Bios
        packet['bimac'] = Configuration.BiMac
        packet['rapidvalidatecode'] = self.person['rapidvalidatecode']
        packet['autoselectroleguid'] = self.person['autoselectroleguid']
        packet['onepushid'] = Configuration.OnePushId
        packet['accountactivation'] = Configuration.AccountActivation
        # packet['mediaid'] = self.person['mediaid']
        packet['phonemodel'] = Configuration.PhoneModel
        packet['platformid'] = Configuration.PlatformId
        packet['systemsoftware'] = Configuration.SystemSoftware
        packet['telecomoper'] = Configuration.TelecomOper
        packet['network'] = Configuration.Network
        packet['screenwidth'] = Configuration.ScreenWidth
        packet['screenheight'] = Configuration.ScreenHeight
        packet['pixeldensity'] = Configuration.PixelDensity
        packet['channel'] = Configuration.Channel
        packet['cpu'] = Configuration.Cpu
        packet['memory'] = Configuration.Memory
        packet['glrender'] = Configuration.GlRender
        packet['glversion'] = Configuration.GlVersion
        packet['deviceid'] = Configuration.DeviceId
        packet['openkey'] = Configuration.OpenKey
        packet['pf'] = Configuration.PF
        packet['pfkey'] = Configuration.PFKey
        packet['wakeupplatform'] = Configuration.WakeupPlatform
        packet['registerchannel'] = Configuration.RegisterChannel
        packet['realbios'] = Configuration.RealBios
        packet['nickname'] = self.person['nickname']
        packet['headurl'] = self.person['headurl']
        packet['devicetype'] = Configuration.DeviceType
        packet['channelname_onesdk'] = Configuration.ChannelName
        packet['channelid_onesdk'] = Configuration.ChannelId
        packet['subchangeid_onesdk'] = Configuration.SubChannelId
        packet['client_language'] = Configuration.ClientLanguage
        # params end ( don't move this line)
        res = Functions.send_packet(packet)
        if res[0]:
            res = Functions.wait_for_packet(self.person, "GC_LOGIN_RET")
            if res[0]:
                if self.person['loginresult'] != 0:
                    loadlog.info(f"login result {self.person['loginresult']} {Configuration.LOGIN_RESULT[self.person['loginresult']]}"
                                 f"validateprocessfailcode:{self.person['validateprocessfailcode']},"
                                 f"validatefailcode:{self.person['validatefailcode']},"
                                 f"validatefailmsg:{self.person['validatefailmsg']}")
                    return False, res[1], f"account {self.person['account']} Login Failed, result ={self.person['loginresult']} "
        return res
