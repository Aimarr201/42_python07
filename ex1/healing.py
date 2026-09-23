
from ex0.pokemon import Pokemon
from .capabilities import HealCapability


class Bulbasaur(Pokemon, HealCapability):
    def __init__(self):
        super().__init__("Bulbasaur", "Grass/Poison")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")


class Venusaur(Pokemon, HealCapability):
    def __init__(self):
        super().__init__("Venusaur", "Grass/Poison")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")
