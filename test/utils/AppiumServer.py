'''
Created on 2017年3月6日

@author: snake
'''
import os


class AppiumServer:
    
    def __init__(self):
        print("init appium server ...") 
        
    def start_server(self, host_ip, host_port, logs_path):
#         command = "appium -a %s -p %s --no-reset --session-override > %s" %(host_ip, host_port, logs_path)
        command = "appium -a %s -p %s --no-reset --session-override" %(host_ip, host_port)
        os.system(command)   
        
    def kill_task(self, task_name): 
        command = "taskkill /f /im " + task_name
        print("kill %s task ..." %task_name)
        os.system(command)
        
    def stop_server(self):
        self.kill_task("node.exe")
