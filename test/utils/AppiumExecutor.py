'''
Created on 2017年3月6日

@author: snake
'''

from selenium.webdriver.support.select import Select


class AppiumExecutor:

    def __init__(self, driver):
        self.driver = driver
    
    """
        通过id/name/xpath/classname查找元素
        若不是以上四种方法，函数将会抛出异常
        
        driver-appium初始化driver对象
        element_property-元素属性（id/name/classname/xpath）
        property_value-元素属性对应的值（id=”login“，name=”username“）
        
        appium 1.5.2以上版本不支持find_by_name
    """
    def find_element(self, locator):
        try:
            if locator.get_type() == "id":
                return self.driver.find_element_by_id(locator.get_value())
            if locator.get_type() == "name":
                return self.driver.find_element_by_name(locator.get_value())
            if locator.get_type() == "xpath":
                return self.driver.find_element_by_xpath(locator.get_value())
            if locator.get_type() == "class":
                return self.driver.find_element_by_class_name(locator.get_value())
        except :
            return None
        
        raise Exception("Element Not Found!")
    
    

    
    def switch_to_alert(self):
        self.driver.switch_to_alert()

    def switch_to_default_content(self):
        self.driver.switch_to_default_content()
    
        
    """
        在元素中输入文本
        
        driver-appium初始化driver对象
        elmement-元素对象
        values-输入文本
    """
    def type(self, locator, values):
        e = self.find_element(locator)
        e.send_keys(values)

    
    def click(self, locator):
        e = self.find_element(locator)
        e.click()

    
    
    def is_exist(self, locator):
        try:
            if self.find_element(locator) is not None:
                return True
            else:
                return False
        except:
            return False

    
    def clear(self, locator):
        e = self.find_element(locator)
        e.clear()
    

    """
        获取元素文本
        
        driver-appium初始化driver对象
        elmement-元素对象
    """
    def get_text(self, locator):
        e = self.find_element(locator)
        return e.get_attribute("text")




    """
        判断对象是否存在
        
        elmement-元素对象
    """
    def is_displayed(self, locator):
        try:
            self.find_element(locator).is_displayed()
            return True
        except Exception:
            return False



    """
        通过js设置input输入框的值
        
        driver-appium初始化driver对象
        element_property-元素属性（id/name/classname/xpath）
        property_value-元素属性对应的值（id=”login“，name=”username“）
        value-需要设置的值
    """
    def input_set(self, driver, element_property, property_value, values):
        js = "$('input[%s=%s]').attr('value','%s');" %(element_property, property_value, values)
        driver.execute_script(js)
    
    
    
    """
        设置select的值，常用于地区设置
        
        driver-appium初始化driver对象
        element-select对象
        value-需要设置的值
    """
    def select_set(self, locator, values):
        Select(locator).select_by_visible_text(values)
