
from abc import ABC, abstractmethod

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
        if not isinstance(pokemon, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Pokemon '{pokemon.name}'"
                f" for this aggressive strategy"
            )
        print(pokemon.transform())
        print(pokemon.attack())
        print(pokemon.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, pokemon: Pokemon) -> bool:
        return isinstance(pokemon, HealCapability)

    def act(self, pokemon: Pokemon) -> None:
        if not isinstance(pokemon, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Pokemon '{pokemon.name}'"
                f" for this defensive strategy"
            )
        print(pokemon.attack())
        print(pokemon.heal())
