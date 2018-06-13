'''
Created on 2017年3月12日

@author: SNake
'''
from com.mazda.utils.AppiumExecutor import AppiumExecutor
from com.mazda.utils.AppiumDriver import AppiumDriver
from time import sleep
from com.mazda.po.BasePage import BasePage


class Login():
    def __init__(self, driver, po_path):
        self.driver = driver
        self.po_path = po_path
        self.appium_exe = AppiumExecutor(self.driver)

        
    def is_logined(self):
        sleep(3)
        self.appium_exe.switch_to_alert()
        if False == self.appium_exe.is_exist(BasePage("homeAlert", "首页提示语", self.po_path).get_locator()):
            return True

        message = self.appium_exe.get_text(BasePage("homeAlert", "首页提示语", self.po_path).get_locator())
        if message == "尊敬的用户，您可以加入壹马会，享受更多的服务。":
            return False
        else:
            return True
        
if __name__ == "__main__":
    driver = AppiumDriver("192.168.1.205:5555", "192.168.1.205:5555", "Android", 
                          "5.1", "com.vcyber.MazdaClubForUser", "com.rzqc.mazda.activity.StartActivity", 
                          "http://localhost:4723/wd/hub").get_android_driver()
    print(Login(driver).is_logined())