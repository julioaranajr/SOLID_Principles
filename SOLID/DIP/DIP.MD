# D: Dependency Inversion Principle (DIP)

## Definition

The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules. Both should depend on abstractions. In addition, abstractions should not depend on details. Details should depend on abstractions.

The Dependency Inversion Principle is the fifth principle of the SOLID principles.

## Example

Let's consider a class that violates the Dependency Inversion Principle:

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on")

    def turn_off(self):
        print("LightBulb: turned off")

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def turn_on(self):
        self.bulb.turn_on()

    def turn_off(self):
        self.bulb.turn_off()

bulb = LightBulb()
switch = Switch(bulb)
switch.turn_on()
switch.turn_off()
```

## How does this class violate the Dependency Inversion Principle?

The `Switch` class violates the Dependency Inversion Principle because it depends directly on the `LightBulb` class, a low-level module.

## Why is this a problem?

The problem with this design is that the `Switch` class is tightly coupled to the `LightBulb` class, making it difficult to change or extend the behavior of the `Switch` class without modifying the `LightBulb` class. This violates the open/closed principle and makes the code less flexible and maintainable.

Also, the `Switch` class is tightly coupled to the `LightBulb` class, making it difficult to test the `Switch` class in isolation. This violates the single responsibility principle and makes the code harder to test.

## How can we fix this?

To fix this violation of the Dependency Inversion Principle, we can introduce an abstraction (interface) between the `Switch` and `LightBulb` classes. This way, the `Switch` class will depend on an abstraction (interface) instead of a concrete implementation, and the `LightBulb` class will depend on the same abstraction (interface) instead of details.

Here's an updated version of the code that follows the Dependency Inversion Principle:

```python
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on")

    def turn_off(self):
        print("LightBulb: turned off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

bulb = LightBulb()
switch = Switch(bulb)
switch.turn_on()
switch.turn_off()
```

Now, the `Switch` class depends on the `Switchable` interface, and the `LightBulb` class implements the `Switchable` interface. This way, the `Switch` class is decoupled from the `LightBulb` class, and the code is more flexible, maintainable, and testable.

## Conclusion

The Dependency Inversion Principle is an important principle of the SOLID principles that helps to decouple high-level modules from low-level modules, making the code more flexible, maintainable, and testable. By following this principle, you can write better object-oriented code that is easier to extend, modify, and test.
