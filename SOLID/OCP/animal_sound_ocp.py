"""
This is a simple example of the Open/Closed Principle.

The Open/Closed Principle states that a class should be open
for extension but closed for modification.

- The Animal class is closed for modification because it is not being modified.
- The Animal class is open for extension because it can be extended to create new animal classes.
- The Lion, Mouse, and Snake classes extend the Animal class to create new animal classes.
- The animal_sound function is closed for modification because it is not being modified.
- The animal_sound function is open for extension because it can be extended
  to include new animal classes.
- The animal_sound function can be extended to include new animal classes
  by adding new animal classes to the animals list.
- The animal_sound function can be extended to include new animal classes
  by creating new animal classes that extend the Animal class.
- The animal_sound function can be extended to include new animal classes
  by creating new animal classes that implement the make_sound method.
- The animal_sound function can be extended to include new animal classes
  by creating new animal classes that implement the make_sound method with a new sound.
"""

class Animal:# This is the base class
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

# This is the derived class
class Lion(Animal):
    def make_sound(self):
        return 'roar'

# This is the derived class
class Mouse(Animal):
    def make_sound(self):
        return 'squeak'

# This is the derived class
class Snake(Animal):
    def make_sound(self):
        return 'hiss'

# This is the function that uses the classes
# This is the loop that iterates through the list of animals
def animal_sound(animal_list: list):
    for animal in animals:
        print(f'{animal.name} makes {animal.make_sound()} sound')

animals = [
    Lion('lion'),
    Mouse('mouse'),
    Snake('snake')]

animal_sound(animals)
