# -*- coding: utf-8 -*-
__author__ = 'snake'

from time import sleep
from src.util.util_param_testcase import ParametrizedTestCase


class TestCase_Login(ParametrizedTestCase):
    def setUp(self):
        ParametrizedTestCase.setUp(self)
        assert False

    def test_login_success(self):
        assert False

    def test_login_failed(self):
        print("I'm test_case3")


if __name__ == "__main__":
    print(ParametrizedTestCase.parametrize(TestCase_Login, None))