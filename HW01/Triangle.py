# -*- coding: utf-8 -*-

#############################################################################################################
# Requirement:                                                                                              #
# “Write a function classify_triangle() that takes three  parameters: a, b, and c.                          #
# The three parameters represent the lengths of the sides of a triangle.                                    #
# The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral,  #
# and whether it is a right triangle as well.”                                                              #
#############################################################################################################

def classify_triangle(a, b, c):

    x = int(a)
    y = int(b)
    z = int(c)

    # Return "Equilateral" if all the sides are equal to each other.
    if x == y == z:
        return "Equilateral"
    # Return "Isosceles" if any 2 sides are equal to each other.
    elif x == y or y == z or z == x:
        return "Isosceles"
    # Return "Right" if sum of any 2 side's square is equal to square of third side.
    elif x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        return "Right"
    # Return "Scalene" if length of all sides is different.
    elif x != y and y != z and x != y:
        return "Scalene"
    else:
        return "None"

# End of file
