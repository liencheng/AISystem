# -*- coding: utf-8 -*-
"""

"""
from locust import User, task, constant, SequentialTaskSet
import project
import TestParam
import gevent
import loadlog
import socket
llog = loadlog.set_logger("load_login")

load_customized = __import__("load_customized")


# visit http://127.0.0.1:8089/ for loadtest testing

class Tests(SequentialTaskSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account = ''

    @task
    def login(self):
        try:
            self.account = ''
            res = self.client.login(TestParam.server_ip, TestParam.server_port,
                                    TestParam.account_prefix,
                                    TestParam.account_startwith,
                                    llog)
            if not res[0]:
                errstr = f"account {str(self.client['account'])}: {str(res[2])}"
                llog.error(errstr)
                self.user.stop()
            else:
                self.account = self.client['account']
                llog.info(self.account + " login")
        except socket.error as e:
            llog.error(e)
            self.user.stop()
        except Exception as e:
            print(e)
            raise

    @task
    def chat(self):
        try:
            self.client.chat5()
        except socket.error as e:
            llog.error(e)
            self.user.stop()
        except Exception as e:
            llog.error(e)
            raise

    @task
    def logout(self):
        try:
            llog.info(self.account + " logout")
            if self.client['socket'] and self.client['loginresult'] == 0:
                self.client['quittype'] = 0
                res = self.client.ActionCG_QUIT_GAME()
                gevent.sleep(2)
                if self.client['socket']:
                    self.client['socket'].close()
                return res
        except Exception as e:
            print(e)
            raise

    # @task
    # def all_tasks_done(self):
    #     print(self.account + " login tasks done, stopping user.")
    #     self.user.stop()


class LoginUser(User):
    wait_time = constant(5)
    tasks = [Tests]

    def __init__(self, environment):
        super().__init__(environment)
        self.client = project.projectmodule.Person(True, environment.events)

    def on_start(self):
        pass

    def on_stop(self):
        account = self.client['account']
        print(account + " l_login stoped")
        pass


if __name__ == '__main__':
    import os

    os.system('locust -f ./l_login.py --web-host=127.0.0.1 ')
