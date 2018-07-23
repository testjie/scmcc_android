# -*- coding: utf-8 -*-
__author__ = 'snake'

from uiautomator import Device


def wake_up(uuid=""):
    d = Device(uuid)
    print(d.info)
    d.screen.on()

if __name__ == "__main__":
    wake_up(uuid="1f09cafe")