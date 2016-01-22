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


def listdir_enchanced(folder):
    files = os.listdir(folder)
    myfiles = list()

    for file in files:
        myfiles.append(os.path.join(folder, file))
    myfiles = sorted(myfiles)
    return myfiles


def get_content(file, mode="read"):
    """
    Return a iterable object when "iterable" is given as the argument for "mode"
    :param file:
    :param mode:
    :return:
    """
    if mode == "read":
        with codecs.open(file, "r", encoding="utf8") as f:
            s = f.read()
        return s

    if mode == "readlines":
        with codecs.open(file, "r", encoding="utf8") as f:
            s = f.readlines()
            for i in range(len(s)):
                s[i] = s[i].strip("\n")
                s[i] = s[i].strip("\r")
                s[i] = s[i].strip(" ")
                s[i] = s[i].strip("\t")
        return s

    if mode == "iterable":
        my_f = open(file, "r")
        while True:
            s = my_f.readline()
            if not s:
                my_f.close()
                break
            yield s


def get_content_list(file):
    with codecs.open(file, "r", encoding="utf8") as f:
        s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].strip("\n")
            s[i] = s[i].strip("\r")
            s[i] = s[i].strip(" ")
            s[i] = s[i].strip("\t")
    return s


def to_string(_list, _sep):
    my_str = _sep.join(_list)
    return my_str


def write_content(file, content):
    with codecs.open(file, "w", encoding="utf8") as f:
        f.write(content)
    return 0


def json_loads(file):
    json_str = get_content(file)
    json_obj = json.loads(json_str)
    return json_obj


def json_dumps(file, json_obj):
    json_str = json.dumps(json_obj, ensure_ascii=False)
    write_content(file, json_str)
    return 0


class running_timer:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = 0

    def end(self):
        self.end_time = time.time()
        running_time = self.end_time - self.start_time
        return running_time


class RunningTimer:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = 0

    def end(self):
        self.end_time = time.time()
        running_time = self.end_time - self.start_time
        return running_time


class Timer(object):
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def time(self):
        return self.end_time - self.start_time


def get_dir_of_main_script():
    tmp = sys.path[0]
    if sys.path[0] == "":
        return os.getcwd()
    else:
        return tmp


def create_abs_path(relative_pth):
    base_path = get_dir_of_main_script()
    abs_path = os.path.join(base_path, relative_pth)
    return abs_path


def get_formated_time(mode="text"):
    struct_time = time.localtime()
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day = struct_time.tm_mday
    hour = struct_time.tm_hour
    min = struct_time.tm_min
    sec = struct_time.tm_sec
    if mode == "text":
        formated_time = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(min) + ":" + str(sec)
    elif mode == "log":
        formated_time = str(year) + "-" + str(month) + "-" + str(day) + "-" + str(hour) + "-" + str(min) + "-" + str(sec)
    else:
        print("Error: Incorrect argument given, please check your value of mode")
        raise Exception
    return formated_time


if __name__ == "__main__":
    file_path = r"C:\Users\Taikor\Desktop\test.txt"
    result = get_content_list(file_path)
    print(type(result[0]))
    print(result)