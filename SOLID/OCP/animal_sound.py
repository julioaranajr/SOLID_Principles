class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print(f'{animal.name} makes roar sound')
        elif animal.name == 'mouse':
            print(f'{animal.name} makes squeak sound')
        elif animal.name == 'snake':
            print(f'{animal.name} makes hiss sound')

animal_sound(animals)