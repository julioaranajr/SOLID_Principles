# L: Liskov Substitution Principle (LSP)

## Definition

The Liskov Substitution Principle (LSP) states that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application or affecting the correctness of the program.

That requires the objects of your subclasses to behave in the same way as the objects of your superclass. This means if you have a base class and a derived class, you should be able to use instances of the derived class wherever instances of the base class are expected, without breaking the application.

The Liskov Substitution Principle is the third principle of the SOLID principles.

## Example

Let's consider a class that violates the Liskov Substitution Principle:

```python
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def area(self) -> int:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, size: int):
        super().__init__(size, size)

    def set_width(self, width: int):
        self.width = width
        self.height = width

    def set_height(self, height: int):
        self.width = height
        self.height = height

rectangle = Rectangle(2, 3)
square = Square(2)

rectangle.set_width(4)
rectangle.set_height(5)

square.set_width(4)
square.set_height(5)

print(rectangle.area())  # Output: 20
print(square.area())  # Output: 25
```

## How does this class violate the Liskov Substitution Principle?

The `Square` class violates the Liskov Substitution Principle because it does not behave in the same way as the `Rectangle` class. The `Square` class overrides the `set_width` and `set_height` methods to ensure that the width and height are always the same, which is not the case for the `Rectangle` class.

Also, the `Square` class does not have a `set_size` method, which is expected for a square.

## Why is this a problem?

If you have a method that expects a `Rectangle` object and you pass a `Square` object to it, the method may not behave as expected because the `Square` object does not behave in the same way as the `Rectangle` object.

## How will this design cause issues in the future?

If you have to test the `Rectangle` and `Square` classes, you have to test both the `set_width`, `set_height`, and `area` methods for the `Rectangle` class and the `set_width`, `set_height`, and `area` methods for the `Square` class. This can make testing more complex and time-consuming.

## How can we fix this violation?

To fix this violation, we can use the following design:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

class Square(Shape):
    def __init__(self, size: int):
        self.size = size

    def area(self) -> int:
        return self.size * self.size
```

Now, the `Rectangle` and `Square` classes behave in the same way, and you can use instances of the `Square` class wherever instances of the `Rectangle` class are expected, without breaking the application.

This design follows the Liskov Substitution Principle because objects of the `Rectangle` and `Square` classes can be used interchangeably without affecting the correctness of the program.

## Conclusion

The Liskov Substitution Principle states that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application or affecting the correctness of the program. This principle helps you design classes that are easy to use and maintain, and that can be extended without breaking the existing code.

By following the Liskov Substitution Principle, you can make your code more flexible, maintainable, and testable, and avoid unexpected behavior when using objects of different classes.
