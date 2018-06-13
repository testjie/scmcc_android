'''
Created on 2017年3月7日

@author: snake
'''
from com.mazda.utils.CommonUtils import CommonUtils
from com.mazda.utils.XmlUtils import XmlUtils


class BaseDevices:
    
    def __init__(self, xml_path, platform_name):
        self.devices_map = XmlUtils.readDevicesXMLDocument(xml_path, platform_name)
        
        
    def get_deviceMap(self):
        return self.devices_map
    

