'''
Created on 2017年3月7日

@author: snake
'''


class Devices:
    def __init__(self, device_name, udid, platform_name, platform_version, app_package, app_activity, cellphone_name, url):
        self.url = url
        self.udid = udid
        self.device_name = device_name
        self.app_package = app_package
        self.app_activity = app_activity
        self.platform_name = platform_name
        self.cellPhone_name = cellphone_name
        self.platform_version = platform_version

    def get_url(self):
        return self.url

    def get_device_name(self):
        return self.device_name

    def get_udid(self):
        return self.udid

    def get_platform_name(self):
        return self.platform_name
    
    def get_platform_version(self):
        return self.platform_version
    
    def get_app_package(self):
        return self.app_package
    
    def get_app_activity(self):
        return self.app_activity
    
    def get_cell_phone_name(self):
        return self.cellPhone_name
