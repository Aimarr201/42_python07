
from ex0.factory import PokemonFactory
from .healing import Bulbasaur, Venusaur
from .transforming import Ditto, Mew
from ex0.pokemon import Pokemon


class HealingPokemonFactory(PokemonFactory):
    def create_base(self) -> Pokemon:
        return Bulbasaur()

    def create_evolved(self) -> Pokemon:
        return Venusaur()


class TransformPokemonFactory(PokemonFactory):
    def create_base(self) -> Pokemon:
        return Ditto()

    def create_evolved(self) -> Pokemon:
        return Mew()
