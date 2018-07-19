# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
import time
import importlib


def data_format_print(str):
    """
    字符串格式化
    :param str:
    :return:
    """
    print(get_current_time() + ":" + str)


def get_all_testcases(classpath, kw="test_"):
    """
    通过路径获取所有case
    :param classpath:
    :param keywords:
    :return: [{pyfile_name: class_name}]
    """
    testcases = []
    for _dir in os.listdir(classpath):
        if kw in _dir:
            py_name = _dir.split(".")[0]
            m1 = importlib.import_module("src.case." + py_name)
            testcases.append({py_name: dir(m1)[1]})

    return testcases


def get_current_time(type="d"):
    """
    获取当前时间
    :param type:
    :return:
    """
    if type == "d":
        format_str = "%Y-%m-%d"
    if type == "H":
        format_str = "%Y-%m-%d-%H"
    if type == "M":
        format_str = "%Y-%m-%d-%H-%M"
    if type == "S":
        format_str = "%Y-%m-%d-%H-%M-%S"

    return time.strftime(format_str, time.localtime(time.time()))


def exec_cmd(cmd):
    """
    执行cmd命令并返回实时输出结果
    :param cmd:
    :return:
    """
    try:
        r = os.popen(cmd)
        text = r.read()
        r.close()
    except:
        pass

    return text


if __name__ == "__main__":
    print(get_all_testcases(classpath="../case/", kw="test"))

