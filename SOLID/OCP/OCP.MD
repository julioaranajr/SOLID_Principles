# O: Open/Closed Principle (OCP)

## Definition

The Open/Closed Principle states that software entities should be open for extension but closed for modification.

This means that you should be able to add new functionality to a class without changing the existing code.

The design of a software entity should be such that you can introduce new functionality or behavior without modifying the existing code since changing the existing code might introduce bugs.

For Example: the classes, modules, function should be open for extension but closed for modification. In doing so, we stop ourselves from modifying existing code and causing potential new bugs in an otherwise happy application.

The Open/Closed Principle is the second principle of the SOLID principles.

## Example

Let's consider a class that violates the Open/Closed Principle:

```python
class Shape:
    def __init__(self, shape_type: str):
        self.shape_type = shape_type

    def draw(self):
        if self.shape_type == "circle":
            self.draw_circle()
        elif self.shape_type == "rectangle":
            self.draw_rectangle()

    def draw_circle(self):
        print("Drawing a circle")

    def draw_rectangle(self):
        print("Drawing a rectangle")
```

## How does this class violate the Open/Closed Principle?

The `Shape` class violates the Open/Closed Principle because if we want to add a new shape, such as a triangle, we have to modify the `Shape` class.

## Why is this a problem?

If we have to modify the `Shape` class every time we want to add a new shape, we are violating the Open/Closed Principle. This can lead to bugs and other issues because we are changing the class for a reason that is not related to drawing shapes.

## How will this design cause issues in the future?

If we have to modify the `Shape` class every time we want to add a new shape, we are violating the Open/Closed Principle. This can lead to bugs and other issues because we are changing the class for a reason that is not related to drawing shapes.

Also, if we need to test the `Shape` class, we have to test both the `draw` and `draw_circle` and `draw_rectangle` methods. This can make testing more complex and time-consuming.

## How can we fix this violation?

To fix this violation, we can use the Strategy Pattern:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")
```

Now, the `Shape` class is open for extension but closed for modification. We can add new shapes by creating new classes that inherit from the `Shape` class.

By using the Strategy Pattern, we have made the code easier to maintain, test, and understand. We have also made the code more flexible because we can add new shapes without modifying the `Shape` class.

## Conclusion

The Open/Closed Principle states that software entities should be open for extension but closed for modification. By following this principle, we can make our code more flexible, maintainable, and testable.
