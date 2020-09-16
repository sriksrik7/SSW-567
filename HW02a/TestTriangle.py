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

    # Test Case1
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    # Test Case2
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    # Test Case3
    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')

    # Test Case4
    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isoceles', '2,2,1 should be Isoceles')

    # Test Case5
    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 7, 7), 'Isoceles', '5,7,7 should be Isoceles')

    # Test Case6
    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(9, 3, 9), 'Isoceles', '9,3,9 should be Isoceles')

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

    # Test Case15
    def testInvalidInputTrianglesG(self):
        self.assertEqual(classifyTriangle(0.5, 1.0, 2.35), 'InvalidInput', '0.5,1.0,2.35 should be InvalidInput')

    # Test Case16
    def testInvalidInputTrianglesH(self):
        self.assertEqual(classifyTriangle(0, 199, 199), 'InvalidInput', '0,199,199 should be InvalidInput')

    # Test Case17
    def testInvalidInputTrianglesI(self):
        self.assertEqual(classifyTriangle(199, 0, 199), 'InvalidInput', '199,0,199 should be InvalidInput')

    # Test Case18
    def testInvalidInputTrianglesK(self):
        self.assertEqual(classifyTriangle(199, 199, 0), 'InvalidInput', '199,199,0 should be InvalidInput')

    # Test Case19
    def testNotATriangleTrianglesA(self):
        self.assertEqual(classifyTriangle(10, 12, 24), 'NotATriangle', '10,12,24 should be NotATriangle')

    # Test Case20
    def testNotATriangleTrianglesB(self):
        self.assertEqual(classifyTriangle(6, 2, 3), 'NotATriangle', '6,2,3 should be NotATriangle')

    # Test Case21
    def testNotATriangleTrianglesC(self):
        self.assertEqual(classifyTriangle(1, 3, 2), 'NotATriangle', '1,3,2 should be NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
