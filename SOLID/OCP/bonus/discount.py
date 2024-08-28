"""
Another example:
Let’s imagine you have a store, and you give a discount of 20% to your favorite
customers using this class:
When you decide to offer double the 20% discount to VIP customers.
You may modify the class like this:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4

# Test the classes
fav_discount = Discount('fav', 100)
vip_discount = Discount('vip', 100)

print(f'The Fav discount is: {fav_discount.give_discount()}%')
print(f'The VIP discount is: {vip_discount.give_discount()}%')
