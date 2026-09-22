
from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name: str, Pokemon_type: str):
        self.name = name
        self.type = Pokemon_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Pokemon"


class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fire")

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Charizard(Pokemon):
    def __init__(self):
        super().__init__("Charizard", "Fire/Flying")

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Water")

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Blastoise(Pokemon):
    def __init__(self):
        super().__init__("Blastoise", "Water")

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")
