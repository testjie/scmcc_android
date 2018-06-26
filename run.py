# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
import time
import unittest
import threading
import xmlrunner

from src.util.util_xml import get_phone_config
from src.util.util_adb import restart_adb_server
from src.util.util_common import get_all_testcases
from src.util.util_appium_server import AppiumServer
from src.util.util_appium_driver import AppiumDriver
from src.util.util_param_testcase import ParametrizedTestCase


def kill_task():
    command = "taskkill /f /im node.exe"
    os.system(command)


def start_appium_servers(devices, ap=4721, bp=4722, sp=4723):
    """
    线程
    :param devices:
    :param ap:
    :param bp:
    :param sp:
    :return:
    """
    # 将每个设备的appium-server添加到线程池
    server_threads = []
    for _ in range(0, len(devices)):
        ap, bp, sp = ap + 3, bp + 3, sp + 3
        appium_server = AppiumServer(ap=ap, bp=bp, sp=sp)
        t = threading.Thread(target=appium_server.start_server)
        server_threads.append(t)

    # 多线程启动appium_server
    for t in server_threads:
        t.start()


def run_cases(devices=[], ap=4721):
    test_suite, threadings = [], []
    test_suites = unittest.TestSuite()

    for device in devices:
        # 获取设备信息并生成driver对象
        ap = ap + 3
        device_name = device["device_name"]
        app_package = device["app_package"]
        app_activity = device["app_activity"]
        platform_name = device["platform_name"]
        platform_version = device["platform_version"]
        url = "http://localhost:" + str(ap) + "/wd/hub"

        # 获取driver对象
        driver = AppiumDriver(device_name, platform_name, platform_version, app_package, app_activity, url)

        # 分别添加每一个设备的suite
        for case in get_all_testcases(classpath="./src/case/"):
            for k, v in case.items():
                exec("from src.case." + k + " import " + v)
                test_suite.append(ParametrizedTestCase.parametrize(eval(v), driver))

        # 将case添加进线程池
        print("add all case success!")
        test_suites.addTests(test_suite)
        runner = xmlrunner.XMLTestRunner()
        thread = threading.Thread(target=runner.run, args=(test_suites,))
        threadings.append(thread)
        test_suite.clear()

    # 多线程并发运行case
    for t in threadings:
        t.start()
        t.join()


def run():
    # 重启adb server 防止adb for windows抽风
    restart_adb_server()

    # 多线程运行appium-server
    ap, bp, sp = 4721, 4722, 4723   # appium-port, bootstrap-port, selendroid-port,
    devices = get_phone_config()
    start_appium_servers(devices, ap=ap, bp=bp, sp=sp)

    # 等待10s,防止初选server没有启动完再运行所有case
    time.sleep(10)
    run_cases(devices=devices, ap=ap)

    # 关闭appium-server
    print("关闭appium server...")
    kill_task()


def run_old():

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
    server_xpath = environment_path + "server.xml"
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
    device_xmlPath = environment_path + "phone.xml"
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



