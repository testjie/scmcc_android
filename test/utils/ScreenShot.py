'''
Created on 2017年3月6日

@author: SNake
'''
from com.mazda.utils.AppiumDriver import AppiumDriver
from com.mazda.utils.CommonUtils import CommonUtils


class ScreenShot:
    
    def __init__(self, driver, path):
        self.driver = driver
        self.screenShot_path = path + CommonUtils().get_current_time()  + ".png"
    
    """
            获取截屏图片
    """
    def get_screenShot(self):
        self.driver.get_screenshot_as_file(self.screenShot_path)
        
        
        
# 测试该方法

if __name__ == "__main__":
    
    
    driver_ip = "192.168.2.101:5555"
    udid = "192.168.2.101:5555"
    driver_platform = "Android"
    platform_version = "5.1"
    app_package = "com.shanghaionstar"
    app_start_activity = "com.shanghaionstar.activity.LoadingActivity"
    url = 'http://localhost:4723/wd/hub'
    driver = AppiumDriver(driver_ip, udid, driver_platform, platform_version, app_package, app_start_activity, url).get_android_driver()
    
    ScreenShot(driver, 'C:\\workspace_copy_20161123\\Mazda\\com\\mazda\\reports\\').get_screenShot()