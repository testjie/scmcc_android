'''
Created on 2017年3月7日

@author: SNake
'''
import os
import sys
import time


class CommonUtils:

    """ 
              格式化输出字符串 
            
       str-输出字符串 
    """
    @staticmethod
    def data_format_print(str):
        print (CommonUtils.get_current_time() +" : "+ str)


    """
        获取项目绝对路径
    """
    def get_project_path(self):
        return sys.path[0] 
    
    
    """
        获取项目根路径
    """
    def get_windows_base_path(self):
        return sys.path[0] + "\\" 
       
    """
        获取日志文件路径
    """  
    def get_windows_logs_path(self):
        return sys.path[0] + "\\com\\mazda\\logs\\"  
    """
        获取页面对象路径
    """
    def get_windows_po_path(self): 
        return sys.path[0] + "\\com\\mazda\\po\\"
    """
        获取用例脚本路径
    """
    def get_windows_testcases_path(self):
        return sys.path[0] + "\\com\\mazda\\case\\"

    """
        获取测试报告路径
        -包含测试报告路径
        -包含截图路径
    """
    def get_windows_result_path(self):
        return sys.path[0] + "\\com\\mazda\\reports\\"
    """
        获取Environment路径
    """
    def get_windows_environment_path(self):
        return sys.path[0] + "\\com\\mazda\\environment\\"
  
    def get_windows_bll_path(self):
        return sys.path[0] + "\\com\\mazda\\bll\\"
  
    def get_windows_apk_path(self):
        return sys.path[0] + "\\com\\mazda\\apk\\"
  
  
    """  获取项目根路径
    """
    def get_liunx_base_path(self):
        return sys.path[0] + "/" 
       
    """
        获取日志文件路径
    """
    def get_liunx_logs_path(self):
        return sys.path[0] + "/com/mazda/logs/"  
    """
        获取页面对象路径
    """
    def get_liunx_po_path(self): 
        return sys.path[0] + "/com/mazda/po/"
    """
        获取用例脚本路径
    """
    def get_liunx_testcases_path(self):
        return sys.path[0] + "/com/mazda/case/"

    """
        获取测试报告路径
        -包含测试报告路径
        -包含截图路径
    """
    def get_liunx_result_path(self):
        return sys.path[0] + "/com/mazda/reports/"
    """
        获取Environment路径
    """
    def get_liunx_environment_path(self):
        return sys.path[0] + "/com/mazda/environment/"
  
    def get_liunx__bll_path(self):
        return sys.path[0] + "/com/mazda/bll/"
  
    def get_liunx_apk_path(self):
        return sys.path[0] + "/com/mazda/apk/"
  
    def get＿all_testcase_by_classpath(self, classpath, keywords):
        testcase_name = []
        for dir in os.listdir(classpath):
            if keywords in dir:
                testcase_name.append(dir.split(".")[0])
        
        return testcase_name  
    
    """
        获取当前时间
    """
    @staticmethod
    def get_current_time():
        return time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    
    










    