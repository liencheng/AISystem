#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
=======================================================================

-----------------------------------------------------------------------
Description:    Locust控制器，使用该窗体设置testparam属性值并启动master、slave进行测试
-----------------------------------------------------------------------
History:   

=======================================================================
'''

from tkinter import *
import tkinter.ttk as ttk
import threading
import datetime
import subprocess
import os
import tkinter.messagebox as tkMessageBox
import time
from time import ctime, sleep
import webbrowser
from load_tests import TestParam


class LocustMgr:
    def __init__(self):
        self.root = Tk()
        self.root.title("完美世界S压测工具v1.0")
        self.root.resizable(0, 0)
        self.root.geometry('600x700')

        self.frame_head_title = Frame(width=500, height=50)
        self.frame_head_top = Frame(width=500, height=150)
        self.frame_center_top = Frame(width=500, height=150)
        self.frame_center_body = Frame(width=500, height=200)
        self.frame_bottom = Frame(width=500, height=50)

        # 定义标题
        self.head_title_frame = Frame(self.frame_head_title)
        self.head_title_text = Label(self.frame_head_title, text="完美世界S压测配置",
                                     font=('', 20), bg="blue", fg="white")
        self.head_title_text.grid(row=0, column=0)

        self.scriptMgr = ScriptMgr()
        server_ip, server_port, client_version, account_prefix, account_start_with, account_step = self.scriptMgr.getTestParamInfo()
        # 定义游戏服务器设置区域
        self.var_server_ip = StringVar()  # 声明游戏服务器IP
        self.var_server_ip.set(TestParam.server_ip)
        self.var_server_port = StringVar()  # 声明游戏服务器端口号
        self.var_server_port.set(TestParam.server_port)
        self.var_client_version = StringVar()  # 声明游戏服务器版本号
        self.var_client_version.set(TestParam.client_version)  # 设置为默认-1，后面保存testparam会用到

        self.head_top_frame = Frame(self.frame_head_top)
                # server ip
        self.head_top_frame_server_ip_text = Label(self.frame_head_top, text="游戏服务器IP：", font=('', 18))
        self.head_top_frame_server_ip_value = Entry(self.frame_head_top, textvariable=self.var_server_ip, width=16,
                                                    font=('', 16))
        self.var_server_ip.set(server_ip)
        # server port
        self.head_top_frame_server_port_text = Label(self.frame_head_top, text="游戏服务器端口：", font=('', 18))
        self.head_top_frame_server_port_value = Entry(self.frame_head_top, textvariable=self.var_server_port, width=16,
                                                      font=('', 16))
        self.var_server_port.set(server_port)
        #client version
        self.head_top_frame_client_version_text = Label(self.frame_head_top, text="游戏服务器版本：",
                                                            font=('', 18))
        self.head_top_frame_client_version_value = Entry(self.frame_head_top, textvariable=self.var_client_version,
                                                             width=16, font=('', 16))
        self.var_client_version.set(client_version)
                # ip, port, version布局
        self.head_top_frame_server_ip_text.grid(row=1, column=0, sticky=W)
        self.head_top_frame_server_ip_value.grid(row=1, column=1, sticky=W)

        self.head_top_frame_server_port_text.grid(row=2, column=0, sticky=W)
        self.head_top_frame_server_port_value.grid(row=2, column=1, sticky=W)

        self.head_top_frame_client_version_text.grid(row=3, column=0, sticky=W)
        self.head_top_frame_client_version_value.grid(row=3, column=1, sticky=W)

        # 定义脚本设置区域 frame_center_top
        self.var_scriptId = IntVar()  # 声明脚本编号
        self.var_scriptName = StringVar()  # 声明运行脚本
        self.var_startNum = StringVar()  # 声明起始账号

        self.account_prefix = str(account_prefix)
        self.account_step = int(account_step)
        self.account_start = int(account_start_with)

        self.center_top_frame = Frame(self.frame_center_top)
        file_dir = os.getcwd() + os.sep + "load_tests"
        scriptList = self.get_script(file_dir)
        self.center_top_frame_script_text = Label(self.frame_center_top, text="压测脚本", font=('', 18))
        self.center_top_frame_script_value = ttk.Combobox(self.frame_center_top, values=scriptList, width=20,
                                                          font=('', 16))
        # self.center_top_frame_script_value.current(0)
        self.center_top_frame_startNum_text = Label(self.frame_center_top, text="起始账号", font=('', 18))
        self.center_top_frame_startNum_value = Entry(self.frame_center_top, textvariable=self.var_startNum, width=20,
                                                     font=('', 16))
        self.var_startNum.set(f"{str(account_prefix)}{str(account_start_with)}")

        # 定义脚本添加、删除区域
        self.center_top_frame_add = Button(self.frame_center_top, text="增加worker", command=self.button_add,
                                           font=('', 16))
        self.center_top_frame_del = Button(self.frame_center_top, text="删除worker", command=self.button_del,
                                           font=('', 16))

        self.center_top_frame_script_text.grid(row=1, column=0, sticky=W)
        self.center_top_frame_script_value.grid(row=1, column=1, columnspan=2,sticky=W)
        self.center_top_frame_startNum_text.grid(row=2, column=0, sticky=W)
        self.center_top_frame_startNum_value.grid(row=2, column=1, sticky=W)
        self.center_top_frame_add.grid(row=3, column=0, sticky=W)
        self.center_top_frame_del.grid(row=3, column=3, sticky=W)

        # 定义中心列表显示区域
        self.tree = ttk.Treeview(self.frame_center_body, show="headings", height=18,
                                 columns=("slaveId", "scriptName", "startNum"))
        self.vbar = ttk.Scrollbar(self.frame_center_body, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格标题
        self.tree.column("slaveId", width=50, anchor='center')
        self.tree.column("scriptName", width=250, anchor='center')
        self.tree.column("startNum", width=200, anchor='center')
        self.tree.heading("slaveId", text="编号")
        self.tree.heading("scriptName", text="脚本")
        self.tree.heading("startNum", text="起始账号")
        # 调用方法获取表格内容插入
        # self.get_tree()
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义底部运行、停止区域

        self.buttom_frame = Frame(self.frame_bottom)
        self.buttom_frame_button_start = Button(self.frame_bottom, text=" 运 行 ", command=self.button_start,
                                                font=('', 20))

        self.buttom_frame_button_stop = Button(self.frame_bottom, text=" 停 止 ", command=self.button_stop,
                                               font=('', 20))
        self.buttom_frame_button_start.grid(row=0, column=0)
        self.buttom_frame_button_stop.grid(row=0, column=3)

        # 整体区域定位
        self.frame_head_title.grid(row=0, column=0,columnspan=3)
        self.frame_head_top.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.frame_center_top.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.frame_center_body.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky=W)
        self.frame_bottom.grid(row=4, column=0, sticky=W)

        self.frame_head_title.grid_propagate(0)
        self.frame_head_top.grid_propagate(0)
        self.frame_center_top.grid_propagate(0)
        self.frame_center_body.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.root.mainloop()

    # 添加slave
    def button_add(self):
        increate_step = self.account_step
        scriptName, scriptStartNum = self.getAddedSlaveInfo()
        # 如果该脚本已经存在，则不作操作
        if (self.exist_tree_checkbyAccount(scriptStartNum) == FALSE):
            self.set_tree(scriptName, scriptStartNum)
            old_num_start = int(scriptStartNum[len(self.account_prefix):])
            old_num_start+= increate_step
            new_acount_start = self.account_prefix + str(old_num_start)
            self.var_startNum.set(new_acount_start)
        self.scriptMgr.update_account_map(scriptName.split('.')[0], scriptStartNum, scriptStartNum + increate_step)
    # 删除选中slave
    def button_del(self):
        if (len(self.tree.selection()) > 0):
            selected_item = self.tree.selection()[0]
            self.del_tree(selected_item)

    # 启动locust
    def button_start(self):
        # 运行按钮更改状态
        self.setRunningState()

        #scriptMgr = ScriptMgr()
        osMgr = OSMgr()
        # 脚本池
        loucst_cmds = []
        # 线程池
        threads = []

        # 需要执行的命令列表
        tasksList = ['locust.exe']
        # clear locust and python task before run script
        osMgr.killTask(tasksList)
        sleep(3)

        self.gameserver_ip = self.var_server_ip.get()
        self.gameserver_port = self.var_server_port.get()
        self.gameserver_version = self.var_client_version.get()

        self.scripts = self.get_tree()
        if (len(self.scripts) == 0):
            return

        # loucst_master_cmd = r'locust -f %s --master --master-host=127.0.0.1 --web-host=127.0.0.1' %(scriptMgr.getScriptFullPath(self.scripts[0].scriptName))
        loucst_master_cmd = r'locust -f load_tests\%s --master --master-host=127.0.0.1 --web-host=127.0.0.1' % (
            self.scripts[0].scriptName)
        master_th = threading.Thread(target=osMgr.execCmdBysubprocess, args=(loucst_master_cmd,))
        master_th.start()
        threads.append(master_th)
        print("%s: %s--->started\n" % (
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), loucst_master_cmd))
        sleep(3)

        for s in self.scripts:
            # 设置TestParam
            self.scriptMgr.setTestParamInfo(self.gameserver_ip, self.gameserver_port, self.gameserver_version, self.account_prefix, s.startNum, self.account_step)
            # 生成locust.slave脚本
            locust_slave_cmd = r'locust -f load_tests\%s --worker --master-host=127.0.0.1' % (s.scriptName)
            # 生成slave线程
            slave_th = threading.Thread(target=osMgr.execCmdBysubprocess, args=(locust_slave_cmd,))
            # 启动slave线程
            slave_th.start()
            # 将线程添加到线程池中
            threads.append(slave_th)
            print("%s: %s--->started\n" % (datetime.datetime.now(), locust_slave_cmd))
            # 间隔一定时间再启动下一个slave线程
            sleep(1)

        # 等待线程运行完毕
        # for th in threads:
        # th.join()

        # os.system('"C:/Program Files/Internet Explorer/iexplore.exe" http://127.0.0.1:8089/')
        webbrowser.open('http://127.0.0.1:8089/')

    # 停止
    def button_stop(self):
        isQuit = tkMessageBox.askquestion(title="关闭窗口", message="请确认已经下载完locust性能数据")
        if (isQuit == 'no'):
            return

        # 需要执行的命令列表
        tasksList = ['locust.exe', 'python.exe']
        osMgr = OSMgr()
        # clear locust and python task before run script
        osMgr.killTask(tasksList)
        sleep(3)

    # 获取指定目录下所有压测脚本
    def get_script(self, file_dir):
        scripts = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if (os.path.splitext(file)[1] == '.py') and ('l_' in os.path.splitext(file)[0]):
                    scripts.append(file)

        return scripts

        # 获取待增加脚本信息用于插入到Treeview中

    def getAddedSlaveInfo(self):
        selectedScriptName = self.center_top_frame_script_value.get()
        selectedScriptStartNum = self.center_top_frame_startNum_value.get()

        return (selectedScriptName, selectedScriptStartNum)

    # 获取treeview所有脚本信息
    def get_tree(self):
        tv_nodes = []
        childen = self.tree.get_children()
        for item in childen:
            s = scriptNode(self.tree.item(item, 'values')[1], self.tree.item(item, 'values')[2])
            tv_nodes.append(s)
        return tv_nodes

    # 添加节点
    def set_tree(self, name, startNum):

        curIndex = len(self.tree.get_children())
        self.tree.insert("", "end", values=(curIndex + 1, name, startNum))

    # 依据脚本名称检验指定名称的节点是否存在
    def exist_tree_checkbyname(self, name):
        tv_items = self.tree.get_children()
        for item in tv_items:
            item_name = self.tree.item(item, 'values')[1]
            if name in item_name:
                return True
        return False

    # 依据脚本名称检验指定名称的节点是否存在
    def exist_tree_checkbyAccount(self, account):
        tv_items = self.tree.get_children()
        for item in tv_items:
            item_account = self.tree.item(item, 'values')[2]
            if account in item_account:
                return True
        return False
        # 依据脚本名称以及开始账号检验指定名称的节点是否存在

    def exist_tree2(self, name, startNum):
        tv_items = self.tree.get_children()
        for item in tv_items:
            item_name = self.tree.item(item, 'values')[1]
            item_startNum = self.tree.item(item, 'values')[2]
            if (name in item_name) or (startNum in item_startNum):
                return True
        return False

        # 删除节点

    def del_tree(self, selected_item):
        self.tree.delete(selected_item)
        self.refresh_tree()

    # 刷新treeview（特别是在删除之后执行刷新）
    def refresh_tree(self):
        tv_nodes = []
        tv_items = self.tree.get_children()
        for item in tv_items:
            tv_nodes.append(self.tree.item(item, 'values'))

        for _ in map(self.tree.delete, self.tree.get_children("")):
            pass
        for index in range(len(tv_nodes)):
            self.tree.insert("", "end", values=(index + 1, tv_nodes[index][1], tv_nodes[index][2]))

            # 设置运行状态下的各个控件信息

    # 【运行】【添加】【删除】按钮置灰
    def setRunningState(self):
        self.buttom_frame_button_start['text'] = '运行中'
        self.buttom_frame_button_start['state'] = 'disabled'
        self.center_top_frame_add['state'] = 'disabled'
        self.center_top_frame_del['state'] = 'disabled'
        # self.buttom_frame_button_stop.focus_set()


'''
记录待运行脚本节点信息
scriptName: 脚本名称
startNum: 脚本开始运行账号
'''


class scriptNode():
    def __init__(self, name='TestParam.py', start=100000):
        self.scriptName = name
        self.startNum = start

    def set(self, name, start):
        self.scriptName = name
        self.startNum = start

    def get(self):
        return (self.scriptName, self.startNum)


'''
脚本操作工具
'''


class ScriptMgr:
    def __init__(self):
        self.load_tests_fullPath = os.getcwd() + os.sep + "load_tests"
        self.testParam_fullPath = self.load_tests_fullPath + os.sep + "TestParam.py"
        self.account_start_map={}
    # 获取Locust工程下TestParam.py绝对路径

    def update_account_map(self, load_test_name, start_with, end_at):
        self.account_start_map[load_test_name] = [start_with, end_at]

    def getTestParamPath(self):
        return self.testParam_fullPath + os.sep + "TestParam.py"

    # 获取LoadTests绝对路径
    def getLoadTestsDirFullPath(self):
        return self.load_tests_fullPath

    # 获取给定脚本的绝对路径
    def getScriptFullPath(self, name):
        return self.load_tests_fullPath + os.sep + name

    # 解析原始TestParam.py获取游戏服务器配置信息
    # 返回server_ip,server_port,client_version
    def getTestParamInfo(self):
        server_ip = '127.0.0.1'
        server_port = 3341
        client_version = "1.21.105"
        account_prefix = 't'
        account_startwith = 100000
        startNum = 0
        endNum = 0
        account_step = 1000

        with open(self.testParam_fullPath, 'r') as f:
            for line in f.readlines():
                if str(line).find('#') == 0:
                    continue
                if 'server_ip' in line:
                    server_ip = str(line.split('=')[1].strip().strip('"').strip('\''))
                elif 'server_port' in line:
                    server_port = int(line.split('=')[1].strip().strip('"').strip('\''))
                elif 'client_version' in line:
                    client_version = str(line.split('=')[1].strip().strip('"').strip('\''))
                elif 'account_prefix' in line:
                    account_prefix = str(line.split('=')[1].strip().strip('"').strip('\''))
                elif 'account_startwith' in line:
                    account_startwith = int(line.split('=')[1].strip())
                elif 'account_step' in line:
                    account_step = int(line.split('=')[1].strip())

        return server_ip, server_port, client_version, account_prefix, account_startwith, account_step

    # 根据窗体属性值更新TestParam.py文件
    def setTestParamInfo(self, server_ip, server_port, client_version, accountprefix, accountstart, accountstep):
        testparam_import_str = u"#import project\n"
        testparam_server_ip_str = u"server_ip = '%s'\n" % (server_ip)
        testparam_server_port_str = u"server_port = %d\n" % (int(server_port))
        testparam_client_version_str = u"client_version = '%s'\n" % (str(client_version))
        testparam_account_prefix_str = u"account_prefix = '%s'\n" % (str(accountprefix))
        testparam_account_step_str = u"account_step = %s\n" % (str(accountstep))
        testparam_account_startwith_str = u"account_startwith = %s\n" % (str(accountstart[len(accountprefix):]))

        with open(self.testParam_fullPath, 'w') as f:
            f.write("# generated by tools\n")
            f.write(testparam_import_str)
            f.write(testparam_server_ip_str)
            f.write(testparam_server_port_str)
            # 某些项目没有版本号属性，因此当client_version==-1时，表示该项目没有client_version属性，不需要添加该属性
            if (str(client_version) != ''):
                f.write(testparam_client_version_str)
            f.write(testparam_account_prefix_str)
            f.write(testparam_account_step_str)
            f.write(testparam_account_startwith_str)
            f.close()


'''
系统管理工具
'''


class OSMgr():
    # 杀死列表中指定进程
    def killTask(self, tasknames):
        for task in tasknames:
            cmdstr = "taskkill /F /IM %s" % (task)
            self.execCmd(cmdstr)

    # 执行Cmd命令
    def execCmd(self, cmd):
        try:
            # os.system(cmd)
            p = os.popen(cmd)
            print(p.read())
            print("%s: command [%s] started\n" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), cmd))
        except Exception as e:
            print('[%s]\t failed, detail:\n%s\n' % (cmd, e))

    # 执行Cmd命令
    def execCmdBysubprocess(self, cmd):
        try:
            subprocess.call(cmd, shell=True, stdout=subprocess.PIPE)
            print("%s: command [%s] started\n" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), cmd))
        except Exception as e:
            print('[%s]\t failed, detail:\n%s\n' % (cmd, e))


if __name__ == '__main__':
    LocustMgr()
