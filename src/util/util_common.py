# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
import time


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
    :return:
    """
    testcases = []
    for _dir in os.listdir(classpath):
        if kw in _dir:
            testcases.append(_dir.split(".")[0])
    return testcases


def get_current_time():
    """
    获取当前时间
    :return:
    """
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    
    
if __name__ == "__main__":
    print(get_all_testcases(classpath="../case/", kw="test"))

