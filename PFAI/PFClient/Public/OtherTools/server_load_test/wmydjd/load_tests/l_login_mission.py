# -*- coding: utf-8 -*-
"""

"""
import os
from locust import User, between, task, SequentialTaskSet
import project
import TestParam


# visit http://127.0.0.1:8089/ for loadtest testing


class MissionUser(User):
    wait_time = between(1, 2)
    def __init__(self, environment):
        super().__init__(environment)
        self.client = project.projectmodule.Person(True, environment.events.request)

    def on_start(self):
        try:
            self.client.login(TestParam.server_ip, TestParam.server_port,
                              TestParam.account_prefix,
                              TestParam.account_start(os.path.basename(__file__).split(".")[0]))
        except Exception as e:
            print(e)
            raise Exception

    @task
    def mission(self):
        try:
            res = self.client.mission_displayed()
            print (f"finished mission {self.client['account']}")
            # if not res[0]:
            #     raise Exception(f"{str(self.client['account'])} {str(res[2])}")
        except Exception as e:
            print(e)



# if __name__ == '__main__':
#
#     test  = MissionUser()
#     test.on_start()
#     test.mission()
#
