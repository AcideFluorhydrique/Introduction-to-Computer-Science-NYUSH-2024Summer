#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 00:52:11 2020

@author: xg7
"""

from point import Point
mat = True
try:
    import matplotlib.pyplot as plt
except Exception as err:
    mat = False
    print(err)


class Polygon:
    """
    A polygon class with a list of points
    """

    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def get_point(self, index):
        # check that the index is valid
        if 0 < index < len(self.points):
            return self.points[index-1]
        else:
            return

    def plot(self):
        x = []
        y = []
        for i in range(len(self.points)):
            x.append(self.points[i].x)
            y.append(self.points[i].y)
        x.append(self.points[0].x)
        y.append(self.points[0].y)
        if mat:
            plt.plot(x, y)
            plt.show()

    def insert_point_at(self, x, y, index):
        self.points.insert(index, Point(x, y))


"""
We have a Rectangle class that is a subclass of the Polygon class. 
However, the Rectangle is initialized by the left lower corner, 
the width, and height (see the following figure), 
which is different from that of the Polygon class. 
Please note that the left lower corner P is an object of the Point class. 
"""

"""
You need to write the __init__ method to initialize the Rectangle properly 
so that the methods that are inherited from the Polygon class can work 
without any modification. 
When you run the test code, the output should look like the following,
"""

class Rectangle(Polygon):
    """
    A rectangle class with a point as a left lower corner
    """
    # complete the Rectangle to pass the test


    def __init__(self, w, h, p):
        super().__init__()
        self.add_point(p.x, p.y)
        self.add_point(p.x + w, p.y)
        self.add_point(p.x + w, p.y + h)
        self.add_point(p.x, p.y + h)
        # pass


# test
if __name__ == "__main__":
    # from point import Point


    p1 = Polygon()
    # p1.add_point(0, 0)
    # p1.add_point(0, 3)
    # p1.add_point(4, 0)
    #p1.add_point(4, 3)
    # p1.plot()

    rect = Rectangle(5, 5, Point(0, 0))
    rect.plot()
