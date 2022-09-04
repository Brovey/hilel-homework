import math


def degrees2radians(degrees):  # returns float
    radians = degrees * (math.pi/180)
    return math.cos(radians)


print(degrees2radians(60), degrees2radians(45), degrees2radians(40))

