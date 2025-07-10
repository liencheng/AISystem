import gevent
from tasks import actions
from tasks.actions import accounts
import random


class rand_rank:
    def __init__(self, person):
        self.person = person

    def run(self):

        rank_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 19, 20, 22, 47, 50, 52, 59]

        random.shuffle(rank_types)
        for rank_type in rank_types:
            self.person['nType'] = rank_type
            self.person['nPage'] = random.randint(0, 2)
            res = self.person.ActionCG_ASK_RANK()
            if not res[0]:
                return res
            gevent.sleep(2)

        return res
