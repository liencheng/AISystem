# -*- coding: utf-8 -*-
"""

"""
from locust import User, constant, task, TaskSet

import project
import TestParam
import loadlog

load_customized = __import__("load_customized")

llog = loadlog.set_logger("load_mixed")

# visit http://127.0.0.1:8089/ for loadtest testing
class MixTests(TaskSet):
    @task
    def rand_rank(self):
        try:
            llog.info(f"{self.client['account']}: rand_rank task started")
            self.client.rand_rank()
        except Exception as e:
            print(e)
            raise
    @task
    def chat5(self):
        try:
            llog.info(f"{self.client['account']}: chat5 task started")
            self.client.chat5()
        except Exception as e:
            print(e)
            raise
    @task
    def change_scene_gm(self):
        try:
            llog.info(f"{self.client['account']}: change_scene_gm task started")
            self.client.change_scene_gm()
        except Exception as e:
            print(e)
            raise


class LoadUser(User):
    wait_time = constant(5)
    tasks = [MixTests]

    def __init__(self, environment):
        super().__init__(environment)
        self.client = project.projectmodule.Person(True, environment.events)
        print("login")
        print("TestParams : ", TestParam.account_prefix)
        print("TestParams : ", TestParam.account_startwith)

        res = self.client.login_b(TestParam.server_ip, TestParam.server_port,
                                  TestParam.account_prefix,
                                  TestParam.account_startwith,
                                  llog)
        if not res or not res[0]:
            errstr = f"account {str(self.client['account'])}: {str(res[2])}"
            llog.error(errstr)
            self.stop("login failed" + errstr)

    def on_start(self):
        print(f"account {self.client['account']} l_login_and_mix_all start")
        llog.debug(f"account_start={TestParam.account_prefix}{TestParam.account_startwith}")

    def on_stop(self):
        if self.client['socket']:
            self.client['socket'].close()
        print(f"account {self.client['account']} l_login_and_mix_all stoped")
        pass


if __name__ == '__main__':
    import os
    os.system('locust -f ./l_login_and_mix_all.py --web-host=127.0.0.1 ')
    #os.system('locust -f ./l_login_and_mix_all.py --worker --account_prefix=t_ --account_start=90000')