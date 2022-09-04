import math


def degrees2radians(degrees):  # returns float
    """Receives degrees and returns radians"""
    radians = degrees * (math.pi/180)
    return radians


print(math.cos(degrees2radians(60)), (math.cos(degrees2radians(45)), (math.cos(degrees2radians(40)))))
