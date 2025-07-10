# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# Copyright
# 游戏中用到的常量
# ----------------------------------------------------------------



class LOGINTYPE:
    TEST = 0
    WX = 1
    QQ = 2


class BIOSTYPE:
    ANDROID = 2
    IOS = 3
    PC = 4


class NETWORKSTATE:
    CLOSE = 0
    CELLULAR = 1
    WIFI = 2
    UNKNOWN = 3


# CG_LOGIN
LoginType = int(LOGINTYPE.TEST)  # TEST
PlatformId = LoginType
GameVersion = 0  # formal
ProgramVersion = 19  # 11
ForceEnter = True  #
Bios = int(BIOSTYPE.PC)
RealBios = int(BIOSTYPE.ANDROID)
BiMac = "000000"  # device udid
DeviceToken = ""  # device
OnePushId = DeviceToken
ChannelName = "Test"  #
ChannelId = "0"
SubChannelId = "0" # device
PhoneModel = "Windows"
SystemSoftware = "Windows"
TelecomOper = "MSDK:TelecomOper"
Network = str(NETWORKSTATE.WIFI)
ScreenWidth = 222
ScreenHeight = 333
PixelDensity = 0
Channel = 0
RegiserChannel = 0
Cpu = "test-locust--"
Memory = 128
GlRender = "GlRender"
GlVersion = "GlVersion"
DeviceId = "locust-tester"
OpenKey = ""
PF = ""
PFKey = ""
WakeupPlatform = -1
RegisterChannel = 0
DeviceType = -1
ClientLanguage = "CN"
AccountActivation = ""
AccountToken = "" # TEST account access token is '', otherwise use last access token

#GC_LOGIN_RET
LOGIN_RESULT = {
    0: "SUCCESS",
    1: "FAIL_VALIDATEPROCESS",
    2: "FAIL_READROLELIST",
    3: "FAIL_ALREADYLOGIN",
    4: "FAIL_QUEUEFULL",
    5: "FAIL_NEEDFORCEENTER",
    6: "FAIL_PACKETNOTMATCH",
    7: "FAIL_VERSIONNOTMATCH",
    8: "FAIL_ONLYALLOWGM",
    9: "FAIL_IPWHITELISTLIMIT",
    10: "FAIL_PLATFORMRESTRICT",
    11: "FAIL_ACCOUNTREGISTERFULL",
    12: "FAIL_ACCOUNTSDKERR",
    13: "FAIL_FREEZEACCOUNT",
    14: "FAIL_GUARDACCOUNT",
    15: "FAIL_PAFORCEACCOUNT",
    16: "FAIL_TP"
}
