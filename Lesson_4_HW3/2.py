from math import sqrt


def triangle_square_and_perimeter(a, b):  # returns 2 values
    gipot = sqrt(a**2 + b**2)
    perimetr = a + b + gipot
    square = (a*b)/2
    return square, perimetr

