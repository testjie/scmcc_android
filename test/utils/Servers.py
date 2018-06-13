'''
Created on 2017年3月7日

@author: snake
'''



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