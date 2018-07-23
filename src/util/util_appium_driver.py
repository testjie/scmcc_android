# -*- coding: utf-8 -*-
__author__ = 'snake'

from appium import webdriver


class AppiumDriver:
    def __init__(self, device_name, platform_name, platform_version, app_package, app_activity, url):
        desired_caps = {}
        desired_caps['udid'] = device_name
        desired_caps['deviceName'] = device_name               # adb devices查到的设备名
        desired_caps['platformName'] = platform_name
        desired_caps['platformVersion'] = platform_version
        desired_caps['appPackage'] = app_package          # 被测App的包名
        desired_caps['appActivity'] = app_activity  # 启动时的Activity
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.android_driver = webdriver.Remote(url, desired_caps)

    def get_android_driver(self):
        return self.android_driver


if __name__ == "__main__":
    from src.util.util_xml import get_phone_config

    phone = get_phone_config(config_type="local", name="魅蓝")[0]
    appium_driver = AppiumDriver(phone["device_name"], phone["platform_name"],
                                 phone["platform_version"], phone["app_package"], phone["app_activity"], phone["url"])

