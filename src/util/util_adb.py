# -*- coding: utf-8 -*-
__author__ = 'snake'

import os

class AdbUtils:

    @staticmethod
    def connector(device):
        AdbUtils.start_server()
        os.system("adb connect " + device)
        
    @staticmethod
    def disconnector(device):
        os.system("adb disconnect " + device)
        
    @staticmethod
    def start_server():
        os.system("adb start-server")
        
    @staticmethod
    def stop_server():
        os.system("adb kill-server")

    @staticmethod
    def restart_server():
        AdbUtils.stop_server()
        AdbUtils.start_server()
        
    @staticmethod
    def reconncet_adb(device):
        AdbUtils.disconnector(device)
        AdbUtils.connector(device)
