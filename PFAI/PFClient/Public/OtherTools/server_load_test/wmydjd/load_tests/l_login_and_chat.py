# -*- coding: utf-8 -*-
"""

"""
from locust import User, task, constant, SequentialTaskSet
import project
import TestParam
import loadlog

llog = loadlog.set_logger("load_chat")

load_customized = __import__("load_customized")


class ChatTests(SequentialTaskSet):

    @task
    def chat2(self):
        try:
            self.client.chat2()
        except Exception as e:
            llog.error(e)
            raise

    @task
    def chat5(self):
        try:
            self.client.chat5()
        except Exception as e:
            llog.error(e)
            raise


class ChatUser(User):
    wait_time = constant(11)
    tasks = [ChatTests]

    def __init__(self, environment):
        super().__init__(environment)
        self.client = project.projectmodule.Person(True, environment.events)

    def on_start(self):
        res = self.client.login_b(TestParam.server_ip, TestParam.server_port,
                                  TestParam.account_prefix,
                                  TestParam.account_startwith,
                                  llog)

        if not res[0]:
            llog.error(f"login failed. account {str(self.client['account'])}: {str(res[2])}")
            self.stop()
        else:
            llog.debug(self.client['account'] + " l_login_chat start")

    def on_stop(self):
        if self.client['socket']:
            self.client['socket'].close()
        llog.debug(f"account {self.client['account']} l_login_chat stoped")
        pass


if __name__ == '__main__':
    import os
    os.system('locust -f ./l_login_and_chat.py --web-host=127.0.0.1 ')

