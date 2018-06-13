'''
Created on 2017年3月6日

@author: snake
'''
from appium import webdriver


class AppiumDriver:
    
    def __init__(self, device, udid, device_platform, device_version, app_package, app_start_activity, url):
        desired_caps = {}
        desired_caps['deviceName'] = device    #adb devices查到的设备名
        desired_caps['udid'] = udid
        desired_caps['platformName'] = device_platform
        desired_caps['platformVersion'] = device_version        
        desired_caps['appPackage'] = app_package    #被测App的包名
        desired_caps['appActivity'] = app_start_activity  #启动时的Activity
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = False
        
        self.android_driver = webdriver.Remote(url, desired_caps)


    def get_android_driver(self):
        return self.android_driver

    