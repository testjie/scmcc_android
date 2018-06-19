# -*- coding: utf-8 -*-
__author__ = 'snake'

import os


class AppiumServer:
    def __init__(self, host_name, host_port=4723, conn_type="usb"):
        self.host_name = host_name
        self.host_port = host_port
        self.conn_type = conn_type
        print("init appium server ...") 
        
    def start_server(self):
        # command = "appium -a %s -p %s --no-reset --session-override > %s" %(host_ip, host_port, logs_path)
        # command = "appium -a %s -p %s --no-reset --session-override" % (host_ip, host_port)
        # C:\Program Files (x86)\Appium\resources\app\node_modules\appium\build\lib\main.js
        if self.conn_type == "usb":
            command = "appium -a %s -p %s --no-reset --session-override" % (self.host_name, self.host_port)
        if self.conn_type == "wireless":
            command = "appium -a %s -p %s --no-reset --session-override" % (self.host_name, self.host_port)
        print(command)
        os.system(command)
        
    def kill_task(self, task_name): 
        command = "taskkill /f /im " + task_name
        print("kill %s task ..." %task_name)
        os.system(command)
        
    def stop_server(self):
        self.kill_task("node.exe")



if __name__ == "__main__":
    appium = AppiumServer(host_name="1f09cafe", host_port=4723)
    appium.start_server()