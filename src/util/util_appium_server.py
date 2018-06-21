# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
import threading
from src.util.util_xml import get_project_config


class AppiumServer:
    def __init__(self, url = "127.0.0.1", port=4723, bp=5723, sp=6723, type="usb"):
        self.bp = bp
        self.sp = sp
        self.url = url
        self.port = port
        self.type = type

        print("init appium server ...")
        
    def start_server(self):
        appium_server_path = get_project_config("local", "appiumServerHome")["appiumServerHome"]
        # usb连接
        if self.type == "usb":
            command = "node %s --address %s --port %s --no-reset " \
                      "--session-override" % (appium_server_path, self.url, self.port)
        # 无线连接
        if self.type == "wireless":
            command = "node %s --address %s --port %s --no-reset " \
                      "--session-override" % (appium_server_path, self.url, self.port)

        # 执行命令
        os.system(command)

    def kill_task(self, task_name): 
        command = "taskkill /f /im " + task_name
        print("kill %s task ..." %task_name)
        os.system(command)
        
    def stop_server(self):
        self.kill_task("node.exe")

    def restart_server(self):
        self.stop_server()
        self.start_server()


if __name__ == "__main__":
    appium = AppiumServer()
    appium.start_server()