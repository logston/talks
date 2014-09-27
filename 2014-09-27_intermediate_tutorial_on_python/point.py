import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x0=0, y0=0):
        x_diff = self.x - x0
        y_diff = self.y - y0
        return math.sqrt(float(x_diff**2 + y_diff**2))

    def __str__(self):
        return '<Point (%d, %d)>' % (self.x, self.y)
