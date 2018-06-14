# -*- coding: utf-8 -*-
__author__ = 'snake'


class BaseServers:

    def __init__(self, xml_path, server_name):
        self.servers_map = XmlUtils.readServersXMLDocument(xml_path, server_name)

    def get_serverMap(self):
        return self.servers_map


class Servers:

    def __init__(self, port, address, server_name):
        self.port = port
        self.address = address
        self.server_name = server_name
        
    def get_port(self):
        return self.port
    
    def get_address(self):
        return self.address
    
    def get_serverName(self):
        return self.server_name