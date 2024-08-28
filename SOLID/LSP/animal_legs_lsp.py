"""
To make this function follow the LSP principle
we will follow the LSP requirements:
If the super-class (Animal) has a method that accepts a
super-class type (Animal) parameter.
Its sub-class(Pigeon) should accept as argument a super-class
type (Animal type) or sub-class type(Pigeon type).
If the super-class returns a super-class type (Animal).
Its sub-class should return a super-class type (Animal type)
or sub-class type(Pigeon).
Now, we can re-implement animal_leg_count function:
"""

animals = []

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())

animal_leg_count(animals)

"""
The animal_leg_count function cares less the type of Animal passed,
it just calls the leg_count method.
All it knows is that the parameter must be of an Animal type, either
the Animal class or its sub-class.
The Animal class now have to implement/define a leg_count method.
And its sub-classes have to implement the leg_count method:
"""

class Animal:
    def leg_count(self):
        pass

class Lion(Animal):
    def leg_count(self):
        return 4

class Mouse(Animal):
    def leg_count(self):
        return 4

class Pigeon(Animal):
    def leg_count(self):
        return 2

"""
When it’s passed to the animal_leg_count function,
it returns the number of legs a lion has.
You see, the animal_leg_count doesn’t need to know
the type of Animal to return its leg count,
it just calls the leg_count method of the Animal type
because by contract a sub-class of Animal class must implement
the leg_count function.
"""

animals = [
    Lion(),
    Mouse(),
    Pigeon()
    ]

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
