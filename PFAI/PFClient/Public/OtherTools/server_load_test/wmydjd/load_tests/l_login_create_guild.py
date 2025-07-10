# -*- coding: utf-8 -*-
"""

"""
import time

from locust import User, constant, task, SequentialTaskSet
import project
import TestParam
import loadlog

llog = loadlog.set_logger("load_create_guild")

load_customized = __import__("load_customized")


class GuildTests(SequentialTaskSet):
    @task
    def create(self):
        try:
            self.client.createguild()
        except Exception as e:
            llog.error(e)
            raise
    @task
    def all_tasks_done(self):
        llog.info("All tasks done! Stopping Locust.")
        self.user.stop()


class GuildUser(User):
    wait_time = constant(2)
    tasks = [GuildTests]

    def __init__(self, environment):
        super().__init__(environment)
        self.client = project.projectmodule.Person(True,environment.events)
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
        print(f"account {self.client['account']} l_login_create_guild start")

    def on_stop(self):
        if self.client['socket']:
            self.client['socket'].close()
        print(f"account {self.client['account']} l_login_create_guild stoped")
        pass


if __name__ == '__main__':
    import os
    os.system('locust -f ./l_login_create_guild.py --web-host=127.0.0.1 ')
