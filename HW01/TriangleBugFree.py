# -*- coding: utf-8 -*-

#############################################################################################################
# Requirement:                                                                                              #
# “Write a function classify_triangle() that takes three  parameters: a, b, and c.                          #
# The three parameters represent the lengths of the sides of a triangle.                                    #
# The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral,  #
# and whether it is a right triangle as well.”
#
# Additional Requirement:
# return a string "InvalidInput" if all the lengths of the sides are integer values.
# return a string "InvalidInput" if all the lengths of the sides are none zero and negative values.
# return a string "NotTriangle" if the sum of any 2 sides is less than the third side.
#############################################################################################################

def classify_triangle(a, b, c):

    # Check if the inputs are valid.
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "InvalidInput"

    x = int(a)
    y = int(b)
    z = int(c)

    # Check if the inputs are none zero and negative values.
    if x <= 0 or y <= 0 or z <= 0:
        return "InvalidInput"

    # Check if the sum of any given 2 inputs is less than the third input to form a triangle.
    # Else return NotTriangle
    if x + y <= z or y + x <= z or x + z <= y:
        return "NotTriangle"

    # Return "Equilateral" if all the sides are equal to each other.
    if x == y == z:
        return "Equilateral"
    # Return "Isosceles" if any 2 sides are equal to each other.
    elif x == y or y == z or z == x:
        return "Isosceles"
    # Return "Right" if sum of any 2 side's square is equal to square of third side.
    elif x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        return "Right"
    # Return "Scalene" if length of all sides are different.
    elif x != y and y != z and x != y:
        return "Scalene"

# End of file
