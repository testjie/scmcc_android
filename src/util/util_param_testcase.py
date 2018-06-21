# -*- coding: utf-8 -*-
__author__ = 'snake'

import unittest    


class ParametrizedTestCase(unittest.TestCase):    
 
    def __init__(self, methodName='runTest', driver=None):
        super(ParametrizedTestCase, self).__init__(methodName)    
        self.driver = driver    

    @staticmethod    
    def parametrize(testcase_klass, driver=None):
        """ Create a suite containing all tests taken from the given  
            subclass, passing them the parameter 'param'.  
        """   
        testloader = unittest.TestLoader()    
        testnames = testloader.getTestCaseNames(testcase_klass)    
        suite = unittest.TestSuite()    
        for name in testnames:    
            suite.addTest(testcase_klass(name, driver=driver))
        return suite