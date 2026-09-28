
from abc import ABC, abstractmethod
from typing import cast

from ex0.pokemon import Pokemon
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, pokemon: Pokemon) -> bool:
        pass

    @abstractmethod
    def act(self, pokemon: Pokemon) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, pokemon: Pokemon) -> bool:
        return True

    def act(self, pokemon: Pokemon) -> None:
        print(pokemon.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, pokemon: Pokemon) -> bool:
        return isinstance(pokemon, TransformCapability)

    def act(self, pokemon: Pokemon) -> None:
        if not self.is_valid(pokemon):
            raise InvalidStrategyError(
               f"Invalid Pokemon '{pokemon.name}' for this aggressive strategy"
            )

        poke = cast(TransformCapability, pokemon)

        print(poke.transform())
        print(pokemon.attack())
        print(poke.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, pokemon: Pokemon) -> bool:
        return isinstance(pokemon, HealCapability)

    def act(self, pokemon: Pokemon) -> None:
        if not self.is_valid(pokemon):
            raise InvalidStrategyError(
                f"Invalid Pokemon '{pokemon.name}' for this defensive strategy"
            )

        poke = cast(HealCapability, pokemon)

        print(pokemon.attack())
        print(poke.heal())
