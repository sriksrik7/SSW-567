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

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
# pylint: disable=R0904
# pylint: disable=C0116
# pylint: disable=C0301
# pylint: disable=C0115
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Test Case1
    def test_right_triangle_a(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    # Test Case2
    def test_right_triangle_b(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    # Test Case3
    def test_equilateral_triangles_a(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')

    # Test Case4
    def test_isosceles_triangles_a(self):
        self.assertEqual(classify_triangle(2, 2, 1), 'Isoceles', '2,2,1 should be Isoceles')

    # Test Case5
    def test_isosceles_triangles_b(self):
        self.assertEqual(classify_triangle(5, 7, 7), 'Isoceles', '5,7,7 should be Isoceles')

    # Test Case6
    def test_isosceles_triangles_c(self):
        self.assertEqual(classify_triangle(9, 3, 9), 'Isoceles', '9,3,9 should be Isoceles')

    # Test Case7
    def test_right_triangle_c(self):
        self.assertEqual(classify_triangle(15, 17, 8), 'Right', '15,17,8 should be Right triangle')

    # Test Case8
    def test_scalene_triangles_a(self):
        self.assertEqual(classify_triangle(2, 5, 6), 'Scalene', '2,5,6 should be Scalene')

    # Test Case9
    def test_invalid_input_triangles_a(self):
        self.assertEqual(classify_triangle(201, 15, 24), 'InvalidInput', '201,15,24 should be InvalidInput')

    # Test Case10
    def test_invalid_input_triangles_b(self):
        self.assertEqual(classify_triangle(50, 201, 40), 'InvalidInput', '50,201,40 should be InvalidInput')

    # Test Case11
    def test_invalid_input_triangles_c(self):
        self.assertEqual(classify_triangle(70, 120, 201), 'InvalidInput', '70,120,201 should be InvalidInput')

    # Test Case12
    def test_invalid_input_triangles_d(self):
        self.assertEqual(classify_triangle(-1, 5, 6), 'InvalidInput', '-1,5,6 should be InvalidInput')

    # Test Case13
    def test_invalid_input_triangles_e(self):
        self.assertEqual(classify_triangle(8, -6, 3), 'InvalidInput', '8,-6,3 should be InvalidInput')

    # Test Case14
    def test_invalid_input_triangles_f(self):
        self.assertEqual(classify_triangle(16, 13, -4), 'InvalidInput', '16,13,-4 should be InvalidInput')

    # Test Case15
    def test_invalid_input_triangles_g(self):
        self.assertEqual(classify_triangle(0.5, 1.0, 2.35), 'InvalidInput', '0.5,1.0,2.35 should be InvalidInput')

    # Test Case16
    def test_invalid_input_triangles_h(self):
        self.assertEqual(classify_triangle(0, 199, 199), 'InvalidInput', '0,199,199 should be InvalidInput')

    # Test Case17
    def test_invalid_input_triangles_i(self):
        self.assertEqual(classify_triangle(199, 0, 199), 'InvalidInput', '199,0,199 should be InvalidInput')

    # Test Case18
    def test_invalid_input_triangles_k(self):
        self.assertEqual(classify_triangle(199, 199, 0), 'InvalidInput', '199,199,0 should be InvalidInput')

    # Test Case19
    def test_not_triangle_triangles_a(self):
        self.assertEqual(classify_triangle(10, 12, 24), 'NotATriangle', '10,12,24 should be NotATriangle')

    # Test Case20
    def test_not_triangle_triangles_b(self):
        self.assertEqual(classify_triangle(6, 2, 3), 'NotATriangle', '6,2,3 should be NotATriangle')

    # Test Case21
    def test_not_triangle_triangles_c(self):
        self.assertEqual(classify_triangle(1, 3, 2), 'NotATriangle', '1,3,2 should be NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
