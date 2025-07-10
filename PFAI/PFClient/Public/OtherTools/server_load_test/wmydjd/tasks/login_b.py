import gevent
from tasks import actions
from tasks.actions import accounts
import loadlog


class login_b:
    def __init__(self, person):
        self.log = None
        self.person = person

    def run(self, server_ip, server_port, account_prefix, account_startwith, log=loadlog):
        self.log = log
        self.person['account'] = str(accounts.account.getUserAccount(account_prefix, account_startwith))
        self.person['session'] = b''
        res = self.person.AConnectToServer(server_ip, server_port)
        if not res[0]:
            loadlog.error(f"{str(accounts.account.getUserAccount(account_prefix, account_startwith))}: Couldn't connect to {server_ip}:{server_port}")
            return res

        res = actions.Functions.wait_for_packet(self.person, "GC_SESSION")
        if not res[0]:
            error_str = str(self.person['account']) + " wait for GC_SESSION failed"
            self.log.error(error_str)
            return res

        if self.person['session'] != b'':
            self.person['rapidvalidatecode'] = -1
            self.person['autoselectroleguid'] = 0xFFFFFFFFFFFFFFFF
            res = self.person.ActionCG_LOGIN()
            if not res[0]:
                return res
            if not self.person.getloadflag():
                self.log.info(res)

            gevent.sleep(2)
            if len(self.person['roleguidlist']) == 0:
                res = self.person.ActionCG_CREATE_ROLE()
                if not res[0]:
                    return res
                if self.person['createresult'] != 0:
                    error_str = f"{str(self.person['account'])} : create role failed, createresult: {str(self.person['createresult'])}"
                    # print(error_str)
                    self.log.error(error_str)
            else:
                # use first role
                self.person['guid'] = self.person['roleguidlist'][0]
                res = self.person.ActionCG_SELECT_ROLE()
                if not res[0]:
                    return res
                if self.person['selectresult'] != 0:
                    self.log.error("select role failed, selectresult:" + str(self.person['selectresult']))
                    return res
            self.log.info(f"{str(self.person['account'])} : login ok")
            gevent.sleep(3)
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
            self.log.info(f"{str(self.person['account'])} : login enter scene ok")
            gevent.sleep(2)
            self.person['cmdstr'] = 'b'
            res = self.person.ActionCG_GMCMDSTR()
            if not res[0]:
                return res
        else:
            self.log.error("GC_SESSION recevie failed")
            return False,0,"session recevie failed"
        return res

