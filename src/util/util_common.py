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
    print (get_current_time() +" : "+ str)


def get_all_testcase_by_classpath(self, classpath, keywords):
    """
    通过路径获取所有case
    :param self:
    :param classpath:
    :param keywords:
    :return:
    """
    testcase_name = []
    for _dir in os.listdir(classpath):
        if keywords in _dir:
            testcase_name.append(_dir.split(".")[0])

    return testcase_name


def get_current_time():
    """
    获取当前时间
    :return:
    """
    return time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    
    










    