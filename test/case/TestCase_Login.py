'''
Created on 2017年3月8日

@author: SNake
'''
from time import sleep

from com.mazda.bll.Login import Login
from com.mazda.po.BasePage import BasePage
from com.mazda.testcase.ParametrizedTestCase import ParametrizedTestCase
from com.mazda.utils.AppiumExecutor import AppiumExecutor


class TestCase_Login(ParametrizedTestCase):
    def setUp(self):
        ParametrizedTestCase.setUp(self)
        assert Login(self.driver, self.po_path).is_logined() == False

    
    def test_login_success(self):
        appium_exc = AppiumExecutor(self.driver)        
        appium_exc.switch_to_alert()


        if appium_exc.is_exist(BasePage("homeAlert", "现在就去", self.po_path).get_locator()) == True:
            appium_exc.click(BasePage("homeAlert", "现在就去", self.po_path).get_locator())
            assert appium_exc.is_exist(BasePage("settingPage", "登陆", self.po_path).get_locator()) == True
        
        appium_exc.type(BasePage("loginPage", "用户名", self.po_path).get_locator(), "")
        appium_exc.type(BasePage("loginPage", "密码", self.po_path).get_locator(), "")
        appium_exc.type(BasePage("loginPage", "用户名", self.po_path).get_locator(), "18408223928")
        appium_exc.type(BasePage("loginPage", "密码", self.po_path).get_locator(), "123456")
        appium_exc.click(BasePage("loginPage", "登陆", self.po_path).get_locator())
             
        
        sleep(5)
        assert appium_exc.find_element(BasePage("homePage", "设置", self.po_path).get_locator())
        
        
        # 恢复初始环境
        appium_exc.click(BasePage("homePage", "设置", self.po_path).get_locator())
        appium_exc.click(BasePage("settingPage", "退出", self.po_path).get_locator())
        appium_exc.switch_to_alert()
        appium_exc.click(BasePage("settingAlert", "确认", self.po_path).get_locator())
        
        return

    def test_login_failed(self):
        print("I'm test_case3")


if __name__ == "__main__":
    print(ParametrizedTestCase.parametrize(TestCase_Login, None))