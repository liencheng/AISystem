# -*- coding: utf-8 -*-
"""

"""
from locust import User, task, constant, TaskSet
import project
import TestParam
import loadlog

llog = loadlog.set_logger("load_change_scene")

load_customized = __import__("load_customized")

# visit http://127.0.0.1:8089/ for loadtest testing

class ChangeSceneTests(TaskSet):

    @task(3)
    def change(self):
        try:
            self.client.change_scene_gm()
        except Exception as e:
            llog.error(e)
            raise

    @task(1)
    def change3(self):
        try:
            self.client.change_scene()
        except Exception as e:
            llog.error(e)
            raise


class ChangeSceneUser(User):
    wait_time = constant(11)
    tasks = [ChangeSceneTests]

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
            llog.debug(self.client['account'] + " l_login_change_scene start")

    def on_stop(self):
        if self.client['socket']:
            self.client['socket'].close()
        llog.debug(f"account {self.client['account']} l_login_change_scene stoped")
        pass


if __name__ == '__main__':
    import os
    os.system('locust -f ./l_login_and_change_scene.py --web-host=127.0.0.1 ')

