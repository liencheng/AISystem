# -*- coding: utf-8 -*-
"""
=======================================================================

-----------------------------------------------------------------------
Created:
-----------------------------------------------------------------------
Description:    诸神之战  机器人基础脚本
关于加密：

-----------------------------------------------------------------------

=======================================================================
"""
import gevent
import loadlog
import time
import tasks
# from tasks.actions.net_packets import Xor32


class Person:
    def __init__(self,loadtestflag=False, locust_events=None):
        self.__data = {}
        self.__action = None
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0
        self.__loadflag = loadtestflag
        self.__locust_events = locust_events

        self.__data['inputbuffer'] = b''
        self.__data['socket'] = None
        self.__data['loginresult'] = -1
        self.__data['selectresult'] = -1

        self.__data['num_receive_packets'] = 0
        self.__data['seq'] = 0  # packet seq

        self.__data['is_packect_truncated'] = False
        self.__data['packet_rec_time'] = 0
        self.__data['heartbeatTime'] = 0
        self.__data['messageid'] = 0
        self.__data['messageid_dict'] = {}

        self.__data['realworldid'] = None
        self.__data['session'] = b''  # server send by GC_SESSION
        self.__data['ansi_time'] = 0
        self.__data['account'] = ""
        self.__data['lasttoken'] = ""
        self.__data['nickname'] = ""
        self.__data['headurl'] = ""
        self.__data['rapidvalidatecode'] = -1
        self.__data['autoselectroleguid'] = 0xFFFFFFFFFFFFFFFF

        self.__data['playerguid'] = -1
        self.__data['playername'] = ""
        self.__data['rolelist'] = []  # role list from login_ret
        self.__data['level'] = 0
        self.__data['profession'] = 0  # player profession
        self.__data['sceneclass'] = 0  # scene class(id)
        self.__data['sceneinst'] = 0  # scene instance (line)

        self.__data['posx'] = 0  # posX
        self.__data['posy'] = 0  # posY
        self.__data['posz'] = 0  # posz
        self.__data['speed'] = 500  # move speed

    def setdata(self, name, value):
        self.__data[name] = value
        return self.getdata(name)

    def getdata(self, name):
        if name in self.__data.keys() and self.__data[name] is not None:
            return self.__data[name]
        else:
            return None

    def getloadflag(self):
        return self.__loadflag

    def __getitem__(self, name):
        return self.getdata(name)

    def __setitem__(self, name, value):
        return self.setdata(name, value)

    def __getattr__(self, name):
        def errorinfo(*args, **kwargs):
            return (False, 0, "Action: %s not defined" % name)

        if name in tasks.__all__:
            if self.__action.__class__.__name__ != name:
                self.__action = eval('tasks.%s.%s(self)' % (name, name))
            func = self.__action.run
        elif name in tasks.actions.__all__:
            if self.__action.__class__.__name__ != name:
                self.__action = eval('tasks.actions.%s.%s(self)' % (name, name))
            func = self.__action.run
        else:
            return errorinfo

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            run_func = "run"+name
            if self.__locust_events:
                if result is not None:
                    if result[0] is True:
                        #request_type, name, response_time, response_length, exception, context, ** kwargs
                        #self.__locust_events.request.fire("GameRobot", name, result[1], 0, None, None)
                        self.__locust_events.request.fire(request_type="GameRobot", name=run_func, response_time=result[1], response_length=0, exception=None, context=None)
                        self.__data['num_receive_packets'] +=1
                    else:
                        #self.__locust_events.request.fire("GameRobot", name, result[1], 0, result[2], None)
                        self.__locust_events.request.fire(request_type="GameRobot", name=run_func, response_time=result[1], response_length=0, exception=result[2], context=None)
                        self.__data['num_receive_packets'] = 0
            return result
        return wrapper

    def __str__(self):
        return self.__data

    def __repr__(self):
        return self.__data

    def dump(self):
        return self.__data

    def getaction(self, name):
        return self.__getattr__(name)

    def taskqueue_append(self, taskname, duration_time=0, *args):
        self.__taskqueue.append((taskname, duration_time, args))

    def taskqueue_cleanup(self):
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0

    def taskqueue_execute(self):
        if len(self.__taskqueue) == 0:
            return (True, 0, "Task queue is empty")
        res = self.__getattr__(self.__taskqueue[self.__taskqueueindex][0])(*self.__taskqueue[self.__taskqueueindex][2])
        queuelen = len(self.__taskqueue)
        if self.__taskqueue[self.__taskqueueindex][1] > 0:  # execute for duration_time
            if self.__taskqueuetimestamp == 0:  # execute first time
                self.__taskqueuetimestamp = time.time()
            else:
                total_time = int((time.time() - self.__taskqueuetimestamp) * 1000)
                if total_time >= self.__taskqueue[self.__taskqueueindex][1] * 1000:  # queue index + 1
                    if self.__taskqueueindex >= (queuelen - 1):
                        self.__taskqueueindex = 0
                    else:
                        self.__taskqueueindex += 1
                    self.__taskqueuetimestamp = 0
        else:  # execute once
            if self.__taskqueueindex >= (queuelen - 1):
                self.__taskqueueindex = 0
            else:
                self.__taskqueueindex += 1
        return res


class PersonSet:
    """task queue"""
    def __init__(self):
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0

    def taskqueue_append(self, personobj, taskname, duration_time=0, *args):
        self.__taskqueue.append((personobj, taskname, duration_time, args))

    def taskqueue_execute(self):
        res = ((self.__taskqueue[self.__taskqueueindex][0]).getaction(self.__taskqueue[self.__taskqueueindex][1]))(
            *self.__taskqueue[self.__taskqueueindex][3])
        queuelen = len(self.__taskqueue)
        if self.__taskqueue[self.__taskqueueindex][2] > 0:  # execute for duration_time
            if self.__taskqueuetimestamp == 0:  # execute first time
                self.__taskqueuetimestamp = time.time()
            else:
                total_time = int((time.time() - self.__taskqueuetimestamp) * 1000)
                if total_time >= self.__taskqueue[self.__taskqueueindex][2] * 1000:  # queue index + 1
                    if self.__taskqueueindex >= (queuelen - 1):
                        self.__taskqueueindex = 0
                    else:
                        self.__taskqueueindex += 1
                    self.__taskqueuetimestamp = 0
        else:  # execute once
            if self.__taskqueueindex >= (queuelen - 1):
                self.__taskqueueindex = 0
            else:
                self.__taskqueueindex += 1
        return res

    def taskqueue_cleanup(self):
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0


class NPC:
    def __init__(self, attrs):
        (serverid, hp, isdie, posx, posy, name, curforce) = attrs
        self.__data = {}
        self.__data['serverid'] = serverid
        self.__data['hp'] = hp  # blood
        self.__data['isdie'] = isdie  # is die or not
        self.__data['posx'] = posx
        self.__data['posy'] = posy
        self.__data['name'] = name
        self.__data['curforce'] = curforce  # 1-StandNPC,2-YellowMonster,3-RedMonster,5-Fellow

    def setdata(self, name, value):
        self.__data[name] = value
        return self.getdata(name)

    def getdata(self, name):
        if name in self.__data.keys() and self.__data[name] != None:
            return self.__data[name]
        else:
            return None

    def __getitem__(self, name):
        return self.getdata(name)

    def __setitem__(self, name, value):
        return self.setdata(name, value)


if __name__ == "__main__":
    from load_tests import TestParam
    loadlog.info("Starting")
    #print("Starting")
    a1 = Person(False)
    loadlog.info("created Person")
    a1["profession"] = 6
    res = a1.login_b(TestParam.server_ip, 3341, 't_','41930')
    if res and res[0]:
        # res = a1.create_team()
        # if res and res[0]:
        #     print("create team ok")
        # else:
        #     print("create team failed")
        res = a1.change_scene()
        if res and res[0]:
            res = a1.change_scene_gm()
            if res and res[0]:
                res = a1.change_scene_gm()
    else:
        print("login failed")
    gevent.sleep(4)
    #res = a1.req_rank()
    #res = a1.createguild()

    # a2 = Person(True)
    # #a2["profession"] = 6
    # res = a1.login_b(TestParam.server_ip, 3341, 't_','41931')
    # if res and res[0]:
    #     res = a1.create_team()
    #     if res and res[0]:
    #         print("join team ok")
    # else:
    #     print("join failed")
    #res = a2.createguild()
    # if not res[0] :
    #     print("last action error info")
    #     print(res)
    # else :
    #     # 退出
    #     a1['quittype'] = 0
    #     res = a1.ActionCG_QUIT_GAME()
    #     a1['socket'].detach()
    # # a1.ACGIdle()
    #     print("finished")

    gevent.sleep(5)
    # a1.ACGGmCommand('ac', ['3', '99999999'])
    # a1.ACGGmCommand('ac', ['2', '99999999'])
    # a1.ACGGmCommand('ac', ['1', '99999999'])

