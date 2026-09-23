
from ex0.pokemon import Pokemon
from .capabilities import TransformCapability


class Ditto(Pokemon, TransformCapability):
    def __init__(self):
        super().__init__("Ditto", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return (f"{self.name} performs a boosted strike!")
        return (f"{self.name} attacks normally.")

    def transform(self) -> str:
        self.is_transformed = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        self.is_transformed = False
        return (f"{self.name} returns to normal.")


class Mew(Pokemon, TransformCapability):
    def __init__(self):
        super().__init__("Mew", "Psychic")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return (f"{self.name} unleashes a devastating morph strike!")
        return (f"{self.name} attacks normally.")

    def transform(self) -> str:
        self.is_transformed = True
        return (f"{self.name} morphs into a terrifying battle form!")

    def revert(self) -> str:
        self.is_transformed = False
        return (f"{self.name} stabilizes its form.")
