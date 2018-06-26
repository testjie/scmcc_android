# -*- coding: utf-8 -*-
__author__ = 'snake'

from src.util.util_param_testcase import ParametrizedTestCase


class TestCaseLogout(ParametrizedTestCase):
    def setUp(self):
        ParametrizedTestCase.setUp(self)
        assert self.driver is not None

    def test_case4(self):
        print("I'm test_case1")
        assert self.driver is None

    def test_case5(self):
        assert self.driver is not None

    def test_case6(self):
        assert self.driver is not None




