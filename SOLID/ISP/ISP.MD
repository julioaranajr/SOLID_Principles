# I: Interface Segregation Principle (ISP)

## Definition

The Interface Segregation Principle states that a client should not be forced to implement an interface that it does not use.

This principle is about breaking up large interfaces into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them.

The main idea behind ISP is to prevent the creation of “fat” or “bloated” interfaces that include methods that are not required by all clients.

By segregating interfaces into smaller, more specific ones, clients only depend on the methods they actually need, promoting loose coupling and better code organization.

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

The `OldFashionedPrinter` class violates the Interface Segregation Principle because it is forced to implement the `scan` and `fax` methods, even though it does not use them.

## Why is this a problem?

If a client wants to use the `OldFashionedPrinter` class, it will have to implement the `scan` and `fax` methods, even though they are not needed. This can lead to unnecessary code and potential bugs.

## How will this design cause issues in the future?

If a client wants to use the `OldFashionedPrinter` class, it will have to implement the `scan` and `fax` methods, even though they are not needed. This can lead to unnecessary code and potential bugs.

## How can we fix this?

To fix this issue, we can segregate the `Machine` interface into smaller, more specific interfaces:

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")

    def fax(self):
        print("Faxing")

class OldFashionedPrinter(Printer):
    def print(self):
        print("Printing")

class Photocopier(Printer, Scanner):
    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")

class MultiFunctionDevice(Printer, Scanner, Fax):
    def __init__(self, printer, scanner, fax):
        self.printer = printer
        self.scanner = scanner
        self.fax = fax

    def print(self):
        self.printer.print()

    def scan(self):
        self.scanner.scan()

    def fax(self):
        self.fax.fax()

printer = OldFashionedPrinter()
printer.print()

printer = MultiFunctionPrinter()
printer.print()
printer.scan()
printer.fax()

photocopier = Photocopier()
photocopier.print()
photocopier.scan()

mfd = MultiFunctionDevice(MultiFunctionPrinter(), MultiFunctionPrinter(), MultiFunctionPrinter())
mfd.print()
mfd.scan()
mfd.fax()
```

By segregating the `Machine` interface into smaller, more specific interfaces, we can now create classes that only implement the methods they need, promoting loose coupling and better code organization.

## Conclusion

The Interface Segregation Principle is an important principle that helps to promote loose coupling and better code organization by breaking up large interfaces into smaller and more specific ones.

Also, by segregating interfaces into smaller, more specific ones, clients only depend on the methods they actually need, which can help to prevent the creation of “fat” or “bloated” interfaces that include methods that are not required by all clients.

By following the Interface Segregation Principle, we can create more maintainable and flexible code that is easier to understand and modify.
