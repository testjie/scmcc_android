# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
from src.util.util_common import exec_cmd

def connect(device):
    """
    连接adb和设备
    :param device:
    :return:
    """
    os.system("adb connect " + device)


def disconnect(device):
    """
    断开adb设备连接
    :param device:
    :return:
    """
    os.system("adb disconnect " + device)


def start_adb_server():
    """
    启动adb服务
    :return:
    """
    os.system("adb start-server")


def stop_adb_server():
    """
    停止adb服务
    :return:
    """
    os.system("adb kill-server")


def restart_adb_server():
    """
    重启adb-server
    :return:
    """
    stop_adb_server()
    start_adb_server()


def reconncet_adb(device):
    """
    重连adb设备
    :param device:
    :return:
    """
    disconnect(device)
    connect(device)


def init_adb(device):
    """
    初始化adb环境,包括重启adb 重新连接adb
    :param device:
    :return:
    """
    restart_adb_server()
    reconncet_adb(device)


def is_connect_devices(devices):
    """
    判断哪些手机是否连接
    :return:
    """
    cmd = "adb devices"
    list_dev = []
    for device in devices:
        str = "{}\tdevice".format(device["device_name"])
        if str in exec_cmd(cmd):
            list_dev.append(device)

    return list_dev


if __name__ == "__main__":
    from src.util.util_xml import get_phone_config
    devices = get_phone_config(xml_path="../../conf/phone.xml")
    print(is_connect_devices(devices))