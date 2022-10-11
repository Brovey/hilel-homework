from math import sqrt


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def check(self, inc_dot):
        segment_len = sqrt(((self.x - dot.x) ** 2) + ((self.y - dot.y) ** 2))
        if segment_len <= self.radius:
            return True
        else:
            return False


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


circle = Circle(10, 15, 5)
dot = Dot(15, 10)
print(circle.check(dot))
