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
    except Exception as e:
        raise Exception("解析数据XML时发生异常，请检查XML格式")

    return tree.getroot()


def get_project_config(xml_path="./conf/project.xml", config_type="product", item="all"):
        """
        通过指定参数获取指定项目配置
        :param config_type: 配置文件类型 product local等
        :param item: 某个配置下的指定节点，如appiumServerHome， 默认为所有节点
        :return: {item1, item2}
        """
        result = {}
        root = get_xml_root(xml_path)

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


def get_phone_config(xml_path="./conf/phone.xml", config_type="product", name="all"):
    """
        通过指定参数获取指定手机配置
        :param config_type: 配置文件类型 product local等
        :param name: 某个配置下的指定节点，如vivo， 默认为所有节点
        :return: {server1, server2}
    """
    results = []
    root = get_xml_root(xml_path)

    # 遍历XML所有节点
    for child in root:
        # 某个节点下全部
        if child.get("type") == config_type and name.lower() == "all":
            for c in child:
                phone = {}
                phone["band"] = c.text
                phone["app_package"] = c.get("appPackage")
                phone["app_activity"] = c.get("appActivity")
                phone["device_name"] = c.get("deviceName")
                phone["platform_name"] = c.get("platformName")
                phone["platform_version"] = c.get("platformVersion")

                results.append(phone)

        # 某个节点的指定参数
        if child.get("type") == config_type and name.lower() != "all":
            for c in child:
                if c.text == name:
                    phone = {}
                    phone["band"] = c.text
                    phone["app_package"] = c.get("appPackage")
                    phone["app_activity"] = c.get("appActivity")
                    phone["device_name"] = c.get("deviceName")
                    phone["platform_name"] = c.get("platformName")
                    phone["platform_version"] = c.get("platformVersion")

                    results.append(phone)

    return results


if __name__ == "__main__":
    print(get_project_config(xml_path="../../conf/project.xml", config_type="local", item="all"))
    print(get_phone_config(xml_path="../../conf/phone.xml", config_type="product", name="all"))
    pass