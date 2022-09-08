from math import sqrt


def circles_intersect(x1, y1, r1, x2, y2, r2):  # returns boolean value
    """Function get coordinates and radius of two circles and returns True if they are not intersected"""
    segment_length = sqrt(((x2 - x1)**2)+((y2-y1)**2))
    if segment_length == 0 and r1 == r2:  # check are circles are the same
        return True
    elif segment_length > r1 + r2:  # check  for non intersection
        return True
    elif segment_length < abs(r1 - r2):  # check is one circle  in another
        return True

    else:
        return False


def main():
    if circles_intersect(50, 70, 100, 100, 50, 150) is True:
        print("Кола не перетиняються")
    else:
        print("Кола перетиняються")


main()
