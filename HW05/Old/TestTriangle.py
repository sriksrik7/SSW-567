# -*- coding: utf-8 -*-
"""
Updated Sep 16, 2020
Added additionl test cases to test triangle program.
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Srikanth Uppada
"""

import unittest
import HtmlTestRunner

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Test Case7
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(15, 17, 8), 'Right', '15,17,8 should be Right triangle')

    # Test Case8
    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(2, 5, 6), 'Scalene', '2,5,6 should be Scalene')

    # Test Case9
    def testInvalidInputTrianglesA(self):
        self.assertEqual(classifyTriangle(201, 15, 24), 'InvalidInput', '201,15,24 should be InvalidInput')

    # Test Case10
    def testInvalidInputTrianglesB(self):
        self.assertEqual(classifyTriangle(50, 201, 40), 'InvalidInput', '50,201,40 should be InvalidInput')

    # Test Case11
    def testInvalidInputTrianglesC(self):
        self.assertEqual(classifyTriangle(70, 120, 201), 'InvalidInput', '70,120,201 should be InvalidInput')

    # Test Case12
    def testInvalidInputTrianglesD(self):
        self.assertEqual(classifyTriangle(-1, 5, 6), 'InvalidInput', '-1,5,6 should be InvalidInput')

    # Test Case13
    def testInvalidInputTrianglesE(self):
        self.assertEqual(classifyTriangle(8, -6, 3), 'InvalidInput', '8,-6,3 should be InvalidInput')

    # Test Case14
    def testInvalidInputTrianglesF(self):
        self.assertEqual(classifyTriangle(16, 13, -4), 'InvalidInput', '16,13,-4 should be InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
