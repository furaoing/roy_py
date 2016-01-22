# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:23:52 2015

@author: Taikor
"""
import os
import time
import codecs
import json
import sys
import logging


def listdir_powered(folder):
    files = os.listdir(folder)
    myfiles = list()

    for file in files:
        myfiles.append(os.path.join(folder, file))
    myfiles = sorted(myfiles)
    return myfiles


def f_read(_file, mode="read", strip_option=True):
    s = None
    mode_enum = ("read", "readlines", "iter")
    strip_option_enum = (True, False)

    if mode not in mode_enum:
        logging.warning("Wrong Argument Given: mode")
        raise Exception
    if strip_option not in strip_option_enum:
        logging.warning("Wrong Argument Given: strip_option")
        raise Exception
    # check if a illegal argument was given

    if mode == "read":
        with codecs.open(_file, "r", encoding="utf8") as f:
            s = f.read()
    elif mode == "readlines":
        with codecs.open(_file, "r", encoding="utf8") as f:
            s = f.readlines()

            if strip_option:
                for i in range(len(s)):
                    s[i] = s[i].strip("\n")
                    s[i] = s[i].strip("\r")
                    s[i] = s[i].strip(" ")
                    s[i] = s[i].strip("\t")
    else:
        # Already checked value of mode, no chance to handle exceptions here
        pass

    return s


def f_read_generator(_file, strip_option=True):
    strip_option_enum = (True, False)
    if strip_option not in strip_option_enum:
        logging.warning("Wrong Argument Given: strip_option")
        raise Exception
    f = codecs.open(_file, "r", encoding="utf8")
    while True:
        yield f.readline()


def f_write(_file, content, mode="w"):
    with codecs.open(_file, mode, encoding="utf8") as f:
        f.write(content)
    return 0


def json_read(_file):
    json_str = f_read(_file)
    json_obj = json.loads(json_str)
    return json_obj


def json_write(_file, json_obj):
    json_str = json.dumps(json_obj, ensure_ascii=False)
    f_write(_file, json_str)
    return 0


class Timer(object):
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def t_elapsed(self):
        return self.end_time - self.start_time


def get_entry_pth():
    tmp = sys.path[0]
    if sys.path[0] == "":
        return os.getcwd()
    else:
        return tmp


def create_abs_path(relative_pth):
    base_path = get_entry_pth()
    abs_path = os.path.join(base_path, relative_pth)
    return abs_path


if __name__ == "__main__":
    print(create_abs_path("afd"))
