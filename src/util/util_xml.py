# -*- coding: utf-8 -*-
__author__ = 'snake'


import xml.etree.ElementTree as ET


def get_xml_root(path):
    """
    通过path获取xml的root解析
    :param path:
    :return:
    """
    try:
        tree = ET.parse(path)
        return tree.getroot()
    except:
        raise Exception("解析数据XML时发生异常，请检查XML格式")


def get_project_config(config_type="product", item="all"):
        """
        通过指定参数获取指定项目配置
        :param config_type: 配置文件类型 product local等
        :param item: 某个配置下的指定节点，如appiumServerHome， 默认为所有节点
        :return: {item1, item2}
        """
        result = {}
        root = get_xml_root("../../conf/project.xml")

        # 遍历XML所有节点
        for child in root:
            # 某个节点下全部
            if child.get("type") == config_type and item.lower() == "all":
                for c in child:
                    result[c.get("name")] = c.text

            # 某个节点的指定参数
            if child.get("type") == config_type and item.lower() != "all":
                for c in child:
                    if c.get("name") == item:
                        result[c.get("name")] = c.text

            return result


def get_server_config(config_type="product", name="all"):
    """
        通过指定参数获取指定server配置
        :param config_type: 配置文件类型 product local等
        :param name: 某个配置下的指定节点，如vivo， 默认为所有节点
        :return: {server1, server2}
    """
    results = []
    root = get_xml_root("../../conf/server.xml")

    # 遍历XML所有节点
    for child in root:
        # 某个节点下全部
        if child.get("type") == config_type and name.lower() == "all":
            for c in child:
                server = {"name": c.text, "address": c.get("address"), "port": c.get("port")}
                results.append(server)

        # 某个节点的指定参数
        if child.get("type") == config_type and name.lower() != "all":
            for c in child:
                if c.text == name:
                    server = {"name": c.text, "address": c.get("address"), "port": c.get("port")}
                    results.append(server)

        return results


def get_phone_config(config_type="product", name="all"):
    """
        通过指定参数获取指定手机配置
        :param config_type: 配置文件类型 product local等
        :param name: 某个配置下的指定节点，如vivo， 默认为所有节点
        :return: {server1, server2}
    """
    results = []
    root = get_xml_root("../../conf/phone.xml")

    # 遍历XML所有节点
    for child in root:
        # 某个节点下全部
        if child.get("type") == config_type and name.lower() == "all":
            for c in child:
                server = {}
                server["name"] = c.text
                server["url"] = c.get("url")
                server["app_package"] = c.get("appPackage")
                server["app_activity"] = c.get("appActivity")
                server["device_name"] = c.get("deviceName")
                server["platform_name"] = c.get("platformName")
                server["platform_version"] = c.get("platformVersion")

                results.append(server)

        # 某个节点的指定参数
        if child.get("type") == config_type and name.lower() != "all":
            for c in child:
                if c.text == name:
                    server = {}
                    server["name"] = c.text
                    server["url"] = c.get("url")
                    server["app_package"] = c.get("appPackage")
                    server["app_activity"] = c.get("appActivity")
                    server["device_name"] = c.get("deviceName")
                    server["platform_name"] = c.get("platformName")
                    server["platform_version"] = c.get("platformVersion")

                    results.append(server)

        return results



if __name__ == "__main__":
    #print(get_project_config(config_type="local", item="all"))
    #print(get_server_config(config_type="local", name="魅蓝"))
    print(get_phone_config(config_type="local", name="vivo"))
