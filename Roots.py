"""
author: Sam Dzialo
Email: sad8333@rit.edu
language: python3.7
"""
import math


def quadratic_roots(a, b, c):
    """takes in the three coefficients and then use them to identify
    how many roots there are, and what they are. """
    print("Equation: ", a, "x^2 + ", b, "x +", c, sep="")  # sets up equation
    i = (b*b)-(4*a*c)
    if a == 0:
        print("One Root")
        print("x = ", -c)
    else:
        if i < 0:
            print("No Roots.")
        elif i == 0:
            print("One Root.")
            print("x = ", (-b+math.sqrt(i))/(2*a))
        elif i > 0:
            print("Two Roots.")
            print("x1 = ", (-b+math.sqrt(i))/(2*a))  # positive quadratic formula
            print("x2 = ", (-b-math.sqrt(i))/(2*a))  # negative quadratic formula


def test_files():
    """Test multiple different possible inputs to test if
    the code works as it is intended to"""
    quadratic_roots(1, 0, 0)
    quadratic_roots(-1, 2, 3)
    quadratic_roots(2, 3, 0)
    quadratic_roots(2, -11, -21)
    quadratic_roots(4, 1, 4)
    quadratic_roots(-8, 0, 4)
    quadratic_roots(142, 1, 2)
    quadratic_roots(-13, 0, 5)
    quadratic_roots(2, 4, 8)
    quadratic_roots(1, 2, 1)


def main():
    """Ask the user for the three coefficients to create an equation and then
    calls the quadratic_roots function to find the roots of the equation"""
    s = "n"
    while s == "n":
        a = int(input("Enter the first coefficient: "))  # a coefficient
        b = int(input("Enter the Second coefficient: "))  # b coefficient
        c = int(input("Enter the Third coefficient: "))  # c coefficient
        quadratic_roots(a, b, c)
        s = input("Would you like to use test files? (press n to input coefficients yourself) (y/n): ")
    test_files()


main()
