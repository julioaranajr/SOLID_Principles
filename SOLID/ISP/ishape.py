"""
Interface Segregation Principle

Make fine grained interfaces that are client specific.
Clients should not be forced to depend upon interfaces that they do not use.

This principle deals with the disadvantages of implementing big interfaces.
Let’s look at the below IShape interface:
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError

"""
This interface draws squares, circles, rectangles.
Class Circle, Square or Rectangle implementing the IShape interface must define the methods draw_square(), draw_rectangle(), draw_circle().
"""

class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

"""
It’s quite funny looking at the code above. Class Rectangle implements methods (draw_circle and draw_square) it has no use of, likewise Square implementing draw_circle, and draw_rectangle, and class Circle (draw_square, raw_rectangle).
If we add another method to the IShape interface, like draw_triangle(),
"""
