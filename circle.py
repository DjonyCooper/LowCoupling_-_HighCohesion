import math, shapes

class Circle(shapes.Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius
