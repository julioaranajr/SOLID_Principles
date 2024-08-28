# S: Single Responsibility Principle (SRP)

## Definition

The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning that a class should have only one job. In other words, a class should have only one responsibility.

How does this principle help us to build better software?

- Testing — A class with one responsibility will have far fewer test cases.
- Lower coupling — Less functionality in a single class will have fewer dependencies.
- Organization — Smaller, well-organized classes are easier to search than monolithic ones.

The Single Responsibility Principle is the first principle of the SOLID principles.

## Example

Let's consider a class that violates the Single Responsibility Principle:

```python
class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def save(self, user: User):
        # Save the user to the database
        pass
```

## How does this class violate the Single Responsibility Principle?

The `User` class has two responsibilities:

1. It get user data.
2. It saves user data to the database.

## Why is this a problem?

If we need to change the way we save user data to the database, we have to modify the `User` class. This violates the Single Responsibility Principle because the `User` class has more than one reason to change.

## How will this design cause issues in the future?

If we need to change the way we save user data to the database, we have to modify the `User` class. This can lead to bugs and other issues because we are changing the class for a reason that is not related to storing user data.

Also, if we need to test the `User` class, we have to test both the `get_name` and `save` methods. This can make testing more complex and time-consuming.

## How can we fix this violation?

To fix this violation, we can separate the responsibilities into two classes:

```python
class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

class UserDB:
    def save(self, user: User):
        # Save the user to the database
        pass
```

Now, the `User` class has only one responsibility: to get user data. The `UserDB` class has the responsibility of saving user data to the database.

By separating the responsibilities into two classes, we have made the code easier to maintain, test, and understand. We have also made the code more flexible because we can change the way we save user data without modifying the `User` class.

## Conclusion

The Single Responsibility Principle helps us to build better software by making our code more maintainable, testable, and flexible. By following this principle, we can create classes that are easier to understand and work with, leading to a more robust and scalable codebase.
