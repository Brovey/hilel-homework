import cmath
from math import sqrt
from cmath import sqrt as complex_sqrt  # used for negative sqrt

a = float(input("Введить коефіцієнти a: "))
b = float(input("Введить коефіцієнти a: "))
c = float(input("Введить коефіцієнти c: "))


def solve_quadratic_equation(a, b, c):
    # always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
    discriminant = b**2 - (4*a*c)
    if discriminant > 0:
        x1 = (-b - sqrt(discriminant)) / (2 * a)  # if D > 0
        x2 = (-b + sqrt(discriminant)) / (2 * a)  # if D > 0
        return x1, x2
    elif discriminant == 0:
        x1 = -b / (2 * a)  # if D = 0b
        x2 = None
        return x1, x2
    else:
        i_discriminant = complex_sqrt(discriminant)
        x1 = (b + i_discriminant)/2
        x2 = (b - i_discriminant)/2
        return x1, x2


def main():
    if solve_quadratic_equation(a, b, c)[0] is not None and solve_quadratic_equation(a, b, c)[1] is None:
        print("x =", solve_quadratic_equation(a, b, c)[0])
    else:
        print("x1 =", solve_quadratic_equation(a, b, c)[0])
        print("x2 =", solve_quadratic_equation(a, b, c)[1])


main()
