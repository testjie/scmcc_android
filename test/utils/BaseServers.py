'''
Created on 2017年3月7日

@author: snake
'''

from com.mazda.utils.XmlUtils import XmlUtils


class BaseServers:
    
    def __init__(self, xml_path, server_name):
        self.servers_map = XmlUtils.readServersXMLDocument(xml_path, server_name)
        
        
    def get_serverMap(self):
        return self.servers_map
    


