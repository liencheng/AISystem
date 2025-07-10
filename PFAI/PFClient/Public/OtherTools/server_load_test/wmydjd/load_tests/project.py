# -*- coding: utf-8 -*-

import os
import sys
import platform
import time
import logging

def load_file(path):
    directory, personfile = os.path.split(path)
    added_to_path = False
    index = None
    if directory not in sys.path:
        sys.path.insert(0, directory)
        added_to_path = True
    else:
        i = sys.path.index(directory)
        if i != 0:
            index = i
            sys.path.insert(0, directory)
            del sys.path[i + 1]
    imported = __import__(os.path.splitext(personfile)[0])
    if added_to_path:
        del sys.path[0]
    if index is not None:
        sys.path.insert(index + 1, directory)
        del sys.path[0]
    return imported


currentdir = os.path.split(os.path.realpath(__file__))[0]
sysstr = platform.system()
logname = 'locust.log' #+time.strftime('%Y%m%d')

if (sysstr == "Windows"):
    projectfile = currentdir[:currentdir.rfind('\\') + 1] + 'person.py'
    logname = currentdir[:currentdir.rfind('\\') + 1] + "logs\\"+ logname
else:
    projectfile = currentdir[:currentdir.rfind('/') + 1] + 'person.py'
    logname = currentdir[:currentdir.rfind('/') + 1] +"logs/" + logname

projectmodule = load_file(projectfile)  # load person.py from ../

