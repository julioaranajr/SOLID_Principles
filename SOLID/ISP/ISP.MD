# I: Interface Segregation Principle (ISP)

## Definition

The Interface Segregation Principle states that a client should not be forced to implement an interface that it does not use. This principle is about breaking up large interfaces into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them.

The Interface Segregation Principle is the fourth principle of the SOLID principles.

## Example

Let's consider a class that violates the Interface Segregation Principle:

```python
from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def fax(self):
        pass

class MultiFunctionPrinter(Machine):
    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")

    def fax(self):
        print("Faxing")

class OldFashionedPrinter(Machine):
    def print(self):
        print("Printing")

    def scan(self):
        raise NotImplementedError("This printer cannot scan")

    def fax(self):
        raise NotImplementedError("This printer cannot fax")
```

## How does this class violate the Interface Segregation Principle?

