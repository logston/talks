from __future__ import print_function


class Map(object):
    def __init__(self, point_list=None, width=4, height=4):
        self.width = width
        self.height = height
        self.points = {}
        if point_list:
            self.add_points(point_list)
 
    def add_point(self, point):
        self.points[(point.x, point.y)] = None
    
    def add_points(self, points):
        for point in points:
            self.add_point(point)
    
    def draw(self):
        for x in range(self.width):
            print('\t')
            for y in range(self.height):
                if (x, y) in self.points:
                    print('X', end='')
                else:
                    print('_', end='')
            print('')


