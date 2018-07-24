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


def adb_slide_unlock(uuid="", slide_dire="UP"):
    """
    使用adb命令模拟滑动解锁，vivo需要在开发者选项中中开启USB模拟点击
    :param slide_dire: UP:上滑 / DOWN: 下滑 / RIGHT: 右滑 / LEFG: 左滑; uuid: 设备序列号
    :return:
    """
    cmds = []
    if "state=OFF" in exec_cmd("adb shell dumpsys power"):  # 判断屏幕是否亮
        cmds.append("adb shell input keyevent 26")  # 模拟电源键
    if uuid == "":
        slide_cmd = "adb shell input touchscreen swipe"
    else:
        slide_cmd = "adb {} shell input touchscreen swipe".format("-s " + uuid)

    if slide_dire.upper() == "UP":
        cmds.append(slide_cmd + " 600 1000 600 300")
    if slide_dire.upper() == "DOWN":
        cmds.append(slide_cmd + " 600 300 600 1000")
    if slide_dire.upper() == "RIGHT":
        cmds.append(slide_cmd + " 100 300 600 300")
    if slide_dire.upper() == "LEFT":
        cmds.append(slide_cmd + "600 300 100 300")

    for cmd in cmds:
        exec_cmd(cmd)


if __name__ == "__main__":
    # from src.util.util_xml import get_phone_config
    # devices = get_phone_config(xml_path="../../conf/phone.xml")
    # print(is_connect_devices(devices))

    adb_slide_unlock(slide_dire="up")