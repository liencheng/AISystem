# -*- coding: utf-8 -*-
"""

"""
import os
from locust import User, constant, task, TaskSet
import project
import TestParam
import loadlog

llog = loadlog.set_logger("load_rank")

load_customized = __import__("load_customized")


class RankTests(TaskSet):
    @task
    def req_rank(self):
        try:
            llog.info(f"{self.client['account']}: req_rank task started")
            self.client.req_rank()
        except Exception as e:
            print(e)
            raise

    @task
    def rank_rank(self):
        try:
            llog.info(f"{self.client['account']}: rank_rank task started")
            self.client.rank_rank()
        except Exception as e:
            print(e)
            raise


class RankUser(User):
    wait_time = constant(2)
    tasks = [RankTests]

    def __init__(self, environment):
        super().__init__(environment)
        self.client = project.projectmodule.Person(True, environment.events)
        print("login")
        res = self.client.login_b(TestParam.server_ip, TestParam.server_port,
                                  TestParam.account_prefix,
                                  TestParam.account_startwith,
                                  llog)
        if not res[0]:
            errstr = f"account {str(self.client['account'])}: {str(res[2])}"
            llog.error(errstr)
            self.stop("login failed" + errstr)

    def on_start(self):
        print(f"account {self.client['account']} l_login_req_rank start")

    def on_stop(self):
        if self.client['socket']:
            self.client['socket'].close()
        print(f"account {self.client['account']} l_login_req_rank stoped")
        pass


if __name__ == '__main__':
    import os

    os.system('locust -f ./l_login_req_rank.py --web-host=127.0.0.1 ')
