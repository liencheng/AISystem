import logging
import os
import sys
import platform

currentdir = os.path.split(os.path.realpath(__file__))[0]
sysstr = platform.system()

default = 'locust' #+time.strftime('%Y%m%d')

_loggers = {}

def set_logger(logname=default):
    logger = logging.getLogger(logname)
    _loggers[logname] = logger
    if (sysstr == "Windows"):
        filename = currentdir + "\\logs\\" + logname + '.log'
    else:
        filename = currentdir + "/logs/" + logname + '.log'

    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)s: %(message)s', datefmt='%H:%M:%S')

    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if (sysstr == "Windows"):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    else:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    return logger


llog = set_logger()


def info(msg, *args, **kw):
    llog.info(msg, *args, **kw)


def warning(msg, *args, **kw):
    llog.warning(msg, *args, **kw)


def error(msg, *args, **kw):
    llog.error(msg, *args, **kw)


def debug(msg, *args, **kw):
    llog.debug(msg, *args, **kw)


def getLogger(name):
    if name in _loggers.keys():
        return _loggers[name]
    else:
        return set_logger(name)


