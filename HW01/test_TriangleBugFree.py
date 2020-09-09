# -*- coding: utf-8 -*-
import pytest
from TriangleBugFree import classify_triangle


# Test Class for testing the function triangle.
class TestClass:

    def test_case1(self):
        print("Test for Equilateral triangle\n")
        assert classify_triangle(1, 1, 1) == "Equilateral"

    def test_case2(self):
        print("Test for Equilateral triangle\n")
        assert classify_triangle(9, 9, 9) == "Equilateral"

    def test_case3(self):
        print("Test for Isosceles triangle\n")
        assert classify_triangle(2, 2, 1) == "Isosceles"

    def test_case4(self):
        print("Test for Isosceles triangle\n")
        assert classify_triangle(5, 7, 7) == "Isosceles"

    def test_case5(self):
        print("Test for Isosceles triangle\n")
        assert classify_triangle(9, 3, 9) == "Isosceles"

    def test_case6(self):
        print("Test for Right triangle\n")
        assert classify_triangle(5, 12, 13) == "Right"

    def test_case7(self):
        print("Test for Right triangle\n")
        assert classify_triangle(17, 15, 8) == "Right"

    def test_case8(self):
        print("Test for Right triangle\n")
        assert classify_triangle(7, 24, 25) == "Right"

    def test_case9(self):
        print("Test for Scalene triangle\n")
        assert classify_triangle(2, 5, 6) == "Scalene"

    def test_case10(self):
        print("Test for Scalene triangle\n")
        assert classify_triangle(10, 15, 24) == "Scalene"

    def test_case11(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(2, 3, 6) == "NotTriangle"

    def test_case12(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(10, 12, 24) == "NotTriangle"

    def test_case13(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(1, 2, 3) == "NotTriangle"

    def test_case14(self):
        print("Test for Negative sides\n")
        assert classify_triangle(-1, -1, -1) == "InvalidInput"

    def test_case15(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(0, 0, 0) == "InvalidInput"

    def test_case16(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(0.5, 1.0, 2.35) == "InvalidInput"


# Main function.
if __name__ == '__main__':
    print('Running test cases')
    pytest.main()

# End of file
