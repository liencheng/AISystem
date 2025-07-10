#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
=======================================================================


=======================================================================
'''
import random
import gevent
import actions

class moveToPos():
    def __init__(self, person):
        self.client = person

    def run(self, posls=[]):       
        for item in posls:
            item = {'x': item['x'] + random.randint(-10000, 10000),  'y': item['y'],'z': item['z'] + random.randint(-10000, 10000)}
            #print "moveToPos:%s-> %s, %s, %s" %(self.client['accounts'], str(item['x']), str(item['y']), str(item['z']))
            self.client.ActionCG_(item)
            self.client.ACGIdle()
            gevent.sleep(3)




