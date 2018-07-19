# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
import time
import unittest
import threading

from src.util.util_xml import get_phone_config
from src.util.util_adb import restart_adb_server
from src.util.util_adb import is_connect_devices
from src.util.util_common import get_current_time
from src.util.util_common import get_all_testcases
from src.util.util_appium_server import AppiumServer
from src.util.util_appium_driver import AppiumDriver
from src.util.util_htmltestrunner import HTMLTestRunner
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
        ad = AppiumDriver(device_name, platform_name, platform_version, app_package, app_activity, url)
        driver = ad.get_android_driver()

        # 分别添加每一个设备的suite
        for case in get_all_testcases(classpath="./src/case/"):
            for k, v in case.items():
                exec("from src.case." + k + " import " + v)
                test_suite.append(ParametrizedTestCase.parametrize(eval(v), driver))

        # 将case添加进线程池
        print("设备【{}】添加所有用例成功!".format(device["band"]))
        test_suites.addTests(test_suite)

        # 创建文件夹
        floder_path = "./report/{}/".format(get_current_time())
        if not os.path.exists(floder_path):
            os.makedirs(floder_path)

        # 使用htmltestrunner执行cases
        retry = 1
        report_desc = "【{}】for掌厅测试描述".format(device["band"])
        report_title = "【{}】for掌厅测试报告".format(device["band"])
        fb = open(floder_path + device["band"] + "-report.html", "wb+")
        runner = HTMLTestRunner(stream=fb, title=report_title, description=report_desc, retry=retry)

        thread = threading.Thread(target=runner.run, args=(test_suites,))
        threadings.append(thread)
        test_suite.clear()

    # 多线程并发运行case
    for t in threadings:
        t.start()
        t.join()


    print()


def run():
    # 重启adb server 防止adb for windows抽风
    restart_adb_server()
    print("【info】正在重启adb-server...")
    time.sleep(10)

    # 判断哪些设备已经连接
    devices = get_phone_config()
    devices = is_connect_devices(devices)
    if devices is None:
        print("【error】未发现已连接的设备，终止本次测试...")
        return

    # 多线程运行appium-server
    ap, bp, sp = 4721, 4722, 4723   # appium-port, bootstrap-port, selendroid-port,
    start_appium_servers(devices, ap=ap, bp=bp, sp=sp)

    # 等待10s,防止出现server没有启动完就运行case
    time.sleep(10)
    run_cases(devices=devices, ap=ap)

    # 关闭appium-server
    kill_task()


if __name__ =="__main__":  
    run()



