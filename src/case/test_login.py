# -*- coding: utf-8 -*-
__author__ = 'snake'

from time import sleep
from src.util.util_param_testcase import ParametrizedTestCase


class TestCaseLogin(ParametrizedTestCase):
    def setUp(self):
        ParametrizedTestCase.setUp(self)
        assert self.driver is not None
        self.driver.press_keycode(26)

    def test_login_success(self):
        assert self.driver is not None

    def test_login_failed(self):
        assert self.driver is not None
