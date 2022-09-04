import math
from math import sqrt


def cone_square_and_volume(radius, height):  # returns 2 floats
    cone_gen = sqrt(height ** 2 + radius ** 2)
    s_base = math.pi * (radius ** 2)
    s_side = math.pi * radius * cone_gen
    square = s_side + s_base
    volume = 1 / 3 * math.pi * (radius ** 2) * height
    return square, volume


