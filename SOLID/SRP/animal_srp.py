"""
This is a simple example of the Single Responsibility Principle.

The Single Responsibility Principle states that a class should have only one
reason to change, meaning that a class should have only one job.

- The Animal class has only one job, which is to represent an animal.
- The AnimalDB class has only one job, which is to save and retrieve animals.
- The Animal class is responsible for representing an animal, while the AnimalDB
  class is responsible for saving and retrieving animals.
"""

class Animal:
    """
    Represents an animal.

    Args:
        name (str): The name of the animal.

    Methods:
        get_name(): Returns the name of the animal.
    """
    def __init__(self, name: str):  # Initializes the Animal class.
        self.name = name        # Initializes the name of the animal.

    def get_name(self) -> str:      # Returns the name of the animal.
        pass

    def __str__(self):              # Returns the name of the animal.
        return f"{self.name}"

class AnimalDB:
    def get_animal(self) -> Animal: # Returns the animal.
        pass

    def save(self, animal: Animal): # Saves the animal.
        pass
