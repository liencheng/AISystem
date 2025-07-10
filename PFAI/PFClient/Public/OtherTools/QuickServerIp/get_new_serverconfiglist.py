#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
import os
import shutil
import traceback


latest_version = "20211123_1031"  # =auto_get_latest_version

# svn settings
svn_absolute_path = "svn://10.17.5.110/export/svnroot/PS/ProjectS/Branches/Main/Server/Config/"
ServerConfigList_Operation_config_name = "ServerConfigList_Operation.txt"
ServerConfigList_config_name = "ServerConfigList.txt"
svn_ServerConfigList_Operation_path = svn_absolute_path + ServerConfigList_Operation_config_name
svn_ServerConfigList_path = svn_absolute_path + ServerConfigList_config_name

# local gm folders
local_tool_root = os.path.abspath(os.curdir) # ".\\Public\\OtherTools\\QuickServerIp"
tmp_folder_local = local_tool_root + os.sep + "tmp"
tmp_ServerConfigList_Operation_path = tmp_folder_local + os.sep + ServerConfigList_Operation_config_name
tmp_ServerConfigList_path = tmp_folder_local + os.sep + ServerConfigList_config_name


def make_clean_tmp():
    # clean up tmp folder
    if os.path.exists(tmp_folder_local):
        shutil.rmtree(tmp_folder_local)
        os.mkdir(tmp_folder_local)
        return True
    else:
        os.mkdir(tmp_folder_local)
        return True


def svn_export():
    global latest_version
    svn_auth_string = "--username chiwenyang --password cZg2NJ --no-auth-cache --non-interactive --force"
    try:
        svn_export_str = "svn export %s %s %s" % (svn_ServerConfigList_Operation_path, tmp_ServerConfigList_Operation_path, svn_auth_string)
        os.system(svn_export_str)
        latest_version = str(datetime.now())
    except Exception as e:
        #traceback.print_tb()
        print"Error: svn checkout path {%s} failed" % svn_ServerConfigList_Operation_path
        return False
    try:
        svn_export_str = "svn export %s %s %s" % (svn_ServerConfigList_path, tmp_ServerConfigList_path, svn_auth_string)
        os.system(svn_export_str)
        return True
    except Exception as e:
        #traceback.print_tb()
        print"Error: svn checkout path {%s} failed" % svn_ServerConfigList_path
        return False

def do_update():
    if make_clean_tmp():
        return svn_export()
    return False

def read_server_ip():
    server_ips = {}
    with open(tmp_ServerConfigList_Operation_path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            line_list = line.split("\t")
            if len(line_list) < 13:
                continue
            if line_list[12] != '-1' and line_list[0].isdigit():
                server_ips[int(line_list[0])] = line_list[12]
    return server_ips


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if do_update():
        print "last update " + latest_version
        print read_server_ip()


