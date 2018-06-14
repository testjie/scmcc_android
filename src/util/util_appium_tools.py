# -*- coding: utf-8 -*-
__author__ = 'snake'

from selenium.webdriver.support.select import Select


def find_element(driver, by="xpath", value=""):
    """
    find_element id name xpath classname
    :param self:
    :param locator:
    :return:
    """
    try:
        if by == "id":
            return driver.find_element_by_id(value)
        if by == "name":
            return driver.find_element_by_name(value)
        if by == "xpath":
            return driver.find_element_by_xpath(value)
        if by == "classname" or by == "class":
            return driver.find_element_by_class_name(value)
    except:
        return None

    raise Exception("Element Not Found!")


def switch_to_alert(driver):
    """
    切换到弹窗
    :param driver:
    :return:
    """
    driver.switch_to_alert()


def switch_to_default_content(driver):
    """
    切换到默认窗口,常用语从弹窗切换回页面
    :param self:
    :return:
    """
    driver.switch_to_default_content()

def is_exist(self, element):
    """
    检查元素是否存在
    :param self:
    :param locator:
    :return:
    """
    try:
        if element is not None:
            return True
        else:
            return False
    except:
        return False


def is_displayed(element):
    """
    检查元素是否显示
    :param element:
    :return:
    """
    try:
        element.is_displayed()
        return True
    except :
        return False


def input_set(driver, element_property, property_value, values):
    """
    通过js设置input输入框的值

    :param driver: 初始化driver对象
    :param element_property: 元素属性（id/name/classname/xpath）
    :param property_value: 元素属性对应的值（id=”login“，name=”username“）
    :param values:  需要设置的值
    :return:
    """
    js = "$('input[%s=%s]').attr('value','%s');" % (element_property, property_value, values)
    driver.execute_script(js)


def select_set(self, locator, values):
    """
    设置select的值，常用语地区设置
    :param locator:
    :param values:
    :return:
    """
    Select(locator).select_by_visible_text(values)


def get_screen_shot(driver, path):
    """
    截图
    :return:
    """
    driver.get_screenshot_as_file(path)

#
# class AppiumExecutor:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     """
#         通过id/name/xpath/classname查找元素
#         若不是以上四种方法，函数将会抛出异常
#
#         driver-appium初始化driver对象
#         element_property-元素属性（id/name/classname/xpath）
#         property_value-元素属性对应的值（id=”login“，name=”username“）
#
#         appium 1.5.2以上版本不支持find_by_name
#     """
#     def find_element(self, locator):
#         try:
#             if locator.get_type() == "id":
#                 return self.driver.find_element_by_id(locator.get_value())
#             if locator.get_type() == "name":
#                 return self.driver.find_element_by_name(locator.get_value())
#             if locator.get_type() == "xpath":
#                 return self.driver.find_element_by_xpath(locator.get_value())
#             if locator.get_type() == "class":
#                 return self.driver.find_element_by_class_name(locator.get_value())
#         except :
#             return None
#
#         raise Exception("Element Not Found!")
#
#
#
#
#     def switch_to_alert(self):
#         self.driver.switch_to_alert()
#
#     def switch_to_default_content(self):
#         self.driver.switch_to_default_content()
#
#
#     """
#         在元素中输入文本
#
#         driver-appium初始化driver对象
#         elmement-元素对象
#         values-输入文本
#     """
#     def type(self, locator, values):
#         e = self.find_element(locator)
#         e.send_keys(values)
#
#
#     def click(self, locator):
#         e = self.find_element(locator)
#         e.click()
#
#
#
#     def is_exist(self, locator):
#         try:
#             if self.find_element(locator) is not None:
#                 return True
#             else:
#                 return False
#         except:
#             return False
#
#
#     def clear(self, locator):
#         e = self.find_element(locator)
#         e.clear()
#
#
#     """
#         获取元素文本
#
#         driver-appium初始化driver对象
#         elmement-元素对象
#     """
#     def get_text(self, locator):
#         e = self.find_element(locator)
#         return e.get_attribute("text")
#
#
#
#
#     """
#         判断对象是否存在
#
#         elmement-元素对象
#     """
#     def is_displayed(self, locator):
#         try:
#             self.find_element(locator).is_displayed()
#             return True
#         except Exception:
#             return False
#
#
#
#     """
#         通过js设置input输入框的值
#
#         driver-appium初始化driver对象
#         element_property-元素属性（id/name/classname/xpath）
#         property_value-元素属性对应的值（id=”login“，name=”username“）
#         value-需要设置的值
#     """
#     def input_set(self, driver, element_property, property_value, values):
#         js = "$('input[%s=%s]').attr('value','%s');" %(element_property, property_value, values)
#         driver.execute_script(js)
#
#     def select_set(self, locator, values):
#         """
#         设置select的值，常用语地区设置
#         :param locator:
#         :param values:
#         :return:
#         """
#         Select(locator).select_by_visible_text(values)
#
#     def get_screen_shot(self):
#         """
#         截图
#         :return:
#         """
#         self.driver.get_screenshot_as_file(self.screenShot_path)