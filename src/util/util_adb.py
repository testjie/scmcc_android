# -*- coding: utf-8 -*-
__author__ = 'snake'

import os


def connect(device):
    start_server()
    os.system("adb connect " + device)


def disconnect(device):
    os.system("adb disconnect " + device)


def start_server():
    os.system("adb start-server")


def stop_server():
    os.system("adb kill-server")


def restart_server():
    stop_server()
    start_server()


def reconncet_adb(device):
    disconnect(device)
    connect(device)
