
from abc import ABC, abstractmethod

from .pokemon import Pokemon, Charmander, Charizard, Squirtle, Blastoise


class PokemonFactory(ABC):
    @abstractmethod
    def create_base(self) -> Pokemon:
        pass

    @abstractmethod
    def create_evolved(self) -> Pokemon:
        pass


class FireFactory(PokemonFactory):
    def create_base(self) -> Pokemon:
        return Charmander()

    def create_evolved(self) -> Pokemon:
        return Charizard()


class WaterFactory(PokemonFactory):
    def create_base(self) -> Pokemon:
        return Squirtle()

    def create_evolved(self) -> Pokemon:
        return Blastoise()
