"""
No, this fails the OCP principle. OCP forbids it. If we want to give a new percent
discount maybe, to a diff.
type of customers, you will see that a new logic will be added.
To make it follow the OCP principle, we will add a new class that will extend the
Abstract Class Discount.
In this new class, we would implement its new behavior:
"""

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def get_discount(self):
        pass

class FavDiscount(Discount):
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.4

# Test the classes
fav_discount = FavDiscount('fav', 100)
vip_discount = VIPDiscount('vip', 100)

print(f'The Fav discount is: {fav_discount.get_discount()}%')
print(f'The VIP discount is: {vip_discount.get_discount()}%')
