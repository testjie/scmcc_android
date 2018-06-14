# -*- coding: utf-8 -*-
__author__ = 'snake'

from com.mazda.environment.Servers import Servers
from com.mazda.environment.Devices import Devices
from com.mazda.po.Locator import Locator
import xml.etree.ElementTree as ET


class XmlUtils:
    
    @staticmethod
    def get_po_by_xml(xml_path, page_name):
        tree = None
        root = None
        page_hashMap = {}

        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
        except :
            raise Exception("解析数据XML时发生异常，请检查XML格式")
        
        
        # 遍历XML所有节点，并获取指定名称的所有Locator
        for child in root:
            locators = []
            
            if child.get("pageName") == page_name:
                for c in child:
                    locator = Locator(c.get("type"), c.text, c.get("value"), c.get("time_Out"))
                    locators.append(locator)
    
    
                # 不考虑locators为空
                if (len(locators) != 0):
                    page_hashMap[child.get("pageName")] = locators
                    
        return page_hashMap


    @staticmethod
    def get_devices_by_xml(xml_path, platform_name):
        tree = None
        root = None
        devices_hashMap = {}
        
        
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
        except:
            raise Exception("解析数据XML时发生异常，请检查XML格式")
        
        # 遍历XML所有节点，并获取指定名称的所有Device
        for child in root:
            devices = []
     
            if child.get("platformName") == platform_name:
                for c in child:
                    device = Devices(c.get("deviceName"), c.get("udid"), c.get("platformName"),
                                     c.get("platformVersion"), c.get("appPackage"), c.get("appActivity"), c.text, c.get("url"))
                    devices.append(device)
                
                
                # 不考虑devices为空
                if (len(devices) != 0):
                    devices_hashMap[child.get("platformName")] = devices

        return devices_hashMap
    
    
    @staticmethod
    def get_server_by_xml(xml_path, server_name):
        tree = None
        root = None
        servers_hashMap = {}
        
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
        except :
            raise Exception("解析数据XML时发生异常，请检查XML格式")

        # 遍历XML所有节点，并获取指定名称的所有Device
        for child in root:
            servers = []
            if child.get("serverName") == server_name:
                for c in child:
                    server = Servers(c.get("port"), c.get("address"), c.text)
                    servers.append(server)

                # 不考虑devices为空
                if (len(servers) != 0):
                    servers_hashMap[child.get("serverName")] = servers

        return servers_hashMap
    

    """解析XML，实现PO层"""
    if __name__ == "__main__":
        print(XmlUtils.readPOXMLDocument('../po/po.xml', "settingPage"))
        print(XmlUtils.readDevicesXMLDocument('../environment/devices.xml', "Android"))
        print(XmlUtils.readServersXMLDocument('../environment/servers.xml', "src"))
