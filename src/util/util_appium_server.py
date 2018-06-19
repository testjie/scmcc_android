# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
from util_xml import get_server_config
from util_xml import get_project_config


class AppiumServer:
    def __init__(self, host_url="127.0.0.1", host_port=4723, conn_type="usb"):
        self.host_url = host_url
        self.host_port = host_port
        self.conn_type = conn_type
        print("init appium server ...") 
        
    def start_server(self):
        appium_server_path = get_project_config("local", "appiumServerHome")["appiumServerHome"]
        # usb连接
        if self.conn_type == "usb":
            command = "node %s --address %s --port %s --no-reset " \
                      "--session-override" % (appium_server_path, self.host_url, self.host_port)
        # 无线连接
        if self.conn_type == "wireless":
            command = "node %s --address %s --port %s --no-reset " \
                      "--session-override" % (appium_server_path, self.host_url, self.host_port)

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
    appium = AppiumServer(host_port=4123)
    appium.start_server()