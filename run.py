'''
Created on 2017年3月8日

@author: SNake
'''
import datetime
import threading
from time import sleep
import time
import unittest

from com.mazda.environment.BaseDevices import BaseDevices
from com.mazda.environment.BaseServers import BaseServers
from com.mazda.testcase.ParametrizedTestCase import ParametrizedTestCase
from com.mazda.utils import HTMLTestRunnerPlus
from com.mazda.utils.AdbUtils import AdbUtils
from com.mazda.utils.AppiumDriver import AppiumDriver
from com.mazda.utils.AppiumServer import AppiumServer
from com.mazda.utils.CommonUtils import CommonUtils


def run(self):

    utils = CommonUtils()
    appium_server = AppiumServer()

    environment_path = utils.get_windows_environment_path()
    testcast_path = utils.get_windows_testcases_path()
    logs_path = utils.get_windows_logs_path()
    result_path = utils.get_windows_result_path()
    po_path = utils.get_windows_po_path()

    appium_server.stop_server()
    """ 获取并启动服务端
    """

    server_name = "src"
    appium_server_threads = [] # server线程池
    server_xpath = environment_path + "servers.xml"
    server_info = BaseServers(server_xpath, server_name).get_serverMap()

    # 载入appiumServer线程池
    for server in server_info.get("src"):
        logs = logs_path + server.get_address() + "-" + server.get_port() + "-" + CommonUtils.get_current_time() + ".txt"
        server_thread = threading.Thread(target=appium_server.start_server, args=((server.get_address(), server.get_port(), logs,)))
        appium_server_threads.append(server_thread)

    # 启动appiumServer线程池
    for thread in appium_server_threads:
        thread.start()

    CommonUtils.data_format_print("启动appium服务器中，等待10秒...")
    sleep(10)

    "重启adb"
    AdbUtils.start_server()

    """ 获取并启动服务端
    """
    platform_name = "Android"
    appium_start_threads = []
    device_xmlPath = environment_path + "devices.xml"
    device_info = BaseDevices(device_xmlPath, platform_name).get_deviceMap()

    # 获取并启动多个设备
    for device in device_info.get("Android"):
        "重新连接adb"

        AdbUtils.reconncet_adb(device.get_deviceName())
        driver = AppiumDriver(device.get_deviceName(), device.get_udid(), device.get_platformName(),
                              device.get_platformVersion(), device.get_appPackage(), device.get_appActivity(),
                              device.get_url()).get_android_driver()

        # 导入测试集/执行测试套件/整合测试报告
        runner = None
        test_suite = []
        test_suites = unittest.TestSuite()
        for case in CommonUtils().get＿all_testcase_by_classpath(CommonUtils().get_windows_testcases_path() , "TestCase_"):
            exec("from com.mazda.case."+ case +" import " + case)
            test_suite.append(ParametrizedTestCase.parametrize(eval(case), driver, po_path + "po.xml"))
            print("add all case success!")


        test_suites.addTests(test_suite)
        screenShot_path = result_path
        device_name = device.get_cellPhoneName()
        screenShot_path = screenShot_path + device_name +"-" + utils.get_current_time()

        fb = open(result_path + device.get_cellPhoneName() + "-" + CommonUtils.get_current_time() +"-testReport.html","wb")
        runner = HTMLTestRunnerPlus.HTMLTestRunner(fb, 1, "测试报告", "测试描述", device.get_deviceName(), screenShot_path)
        thread = threading.Thread(target=runner.run, args=(test_suites,))

        appium_start_threads.append(thread)
        test_suite.clear()

    # 启动设备线程池
    for thread in appium_start_threads:
        thread.start()
        thread.join()


    appium_server.stop_server()
    return


if __name__ =="__main__":  
    run()



