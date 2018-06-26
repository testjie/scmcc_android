# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
import threading
from src.util.util_xml import get_project_config


class AppiumServer:
    def __init__(self, url="127.0.0.1", ap=4723, bp=5723, sp=6723, conn_type="usb"):
        self.bp = bp
        self.sp = sp
        self.url = url
        self.ap = ap
        self.bp = bp
        self.sp = sp
        self.conn_type = conn_type

        print("init appium server ...")
        
    def start_server(self):
        appium_server_path = get_project_config("local", "appiumServerHome")["appiumServerHome"]
        # usb连接
        if self.conn_type == "usb":
            command = "node %s --address %s --port %s --bootstrap-port %s --selendroid-port %s --no-reset " \
                      "--session-override" % (appium_server_path, self.url, self.ap, self.bp, self.sp)
        # 无线连接
        if self.conn_type == "wireless":
            command = "node %s --address %s --port %s --bootstrap-port %s --selendroid-port %s --no-reset " \
                      "--session-override" % (appium_server_path, self.url, self.ap, self.bp, self.sp)

        # 执行命令
        os.system(command)

    def kill_task(self, task_name): 
        command = "taskkill /f /im  node.exe"
        print("kill %s task ..." % node.exe)
        os.system(command)
        
    def stop_server(self):
        self.kill_task("node.exe")



if __name__ == "__main__":
    appium = AppiumServer()
    appium.start_server()