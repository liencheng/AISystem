#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
=======================================================================

=======================================================================
'''
import random
import gevent


class shizhuang_ranse():
    def __init__(self, person):
        self.person = person

    def run(self):
        self.person.ACGRequestBuyMarketItem(12004, 12004101, 1, 0, 12000, 0)
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGEquipItem(0, 8, 4)
        gevent.sleep(3)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGSetFashionColor()
        gevent.sleep(2)
        self.person.ACGIdle()

'''
        self.person['itemindex'] = []
        self.person.ACGRequestBuyMarketItem(12004, 12004101, 1, 0, 12000, 0)
        gevent.sleep(2)
        self.person.ACGIdle()

#        while len(self.person['itemindex']) <0:
#            gevent.sleep(2)
#            self.person.ACGIdle()
#        try:
#            self.person['dataIndex'] = self.person['itemdata'][0].dataIndex
#        except Exception,e:
#            print str(self.person['accounts']) + '-----------------' + str(len(self.person['itemdata']))

#        self.person.ACGEquipItem(self.person['itemindex'][0],8,4)
#        gevent.sleep(3)
#        self.person.ACGIdle()
        self.person.ACGEquipItem(0,8,4)
        gevent.sleep(3)
        self.person.ACGIdle()


        self.person.ACGRequestBuyMarketItem(12001, 1200211, 999, 0, 12000, 0)
        gevent.sleep(2)
        self.person.ACGIdle()

#        self.person.ACGFashionWeekCommitList(1)
        gevent.sleep(2)
        self.person.ACGIdle()
        self.person.ACGSetFashionColor()
        gevent.sleep(2)
        self.person.ACGIdle()

#        self.person.ACGFashionWeekCommitList(1)
        gevent.sleep(2)
        self.person.ACGIdle()

        self.person.ACGCommitProduct()
        gevent.sleep(2)
        self.person.ACGIdle()
'''