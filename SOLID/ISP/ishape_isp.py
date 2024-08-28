"""
The classes must implement the new method or error will be thrown.

We see that it is impossible to implement a shape that can draw a circle
but not a rectangle or a square or a triangle.
We can just implement the methods to throw an error that shows the operation
cannot be performed.

ISP frowns against the design of this IShape interface.
To make our IShape interface conform to the ISP principle, we segregate the
actions to different interfaces.
Classes (Circle, Rectangle, Square, Triangle, etc) can just inherit from the
IShape interface and implement their own draw behavior.
"""

class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

class Triangle(IShape):
    def draw(self):
        pass

# The IShape interface is now fine grained and clients can implement only the methods they need.

# Test the classes
circle = Circle()
circle.draw()

square = Square()
square.draw()

rectangle = Rectangle()
rectangle.draw()

triangle = Triangle()
triangle.draw()

# The classes must implement the new method or error will be thrown.
print(f'circle: {circle} has method draw: {hasattr(circle, "draw")}')# True
print(f'square: {square} has method draw: {hasattr(square, "draw")}')# True
print(f'rectangle: {rectangle} has method draw: {hasattr(rectangle, "draw")}')# True
print(f'triangle: {triangle} has method draw: {hasattr(triangle, "draw")}')# True

# We see that it is impossible to implement a shape that can draw a circle but
# not a rectangle or a square or a triangle.

print(f'circle: {circle} has method draw: {hasattr(circle, "draw_square")}')    # False
print(f'square: {square} has method draw: {hasattr(square, "draw_rectangle")}') # False
