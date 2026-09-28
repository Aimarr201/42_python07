
from typing import List, Tuple

from ex0 import PokemonFactory, FireFactory, WaterFactory
from ex1 import HealingPokemonFactory, TransformPokemonFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy
from ex2 import DefensiveStrategy, InvalidStrategyError


def battle(opponents: List[Tuple[PokemonFactory, BattleStrategy]]):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    pokemons = []
    for factory, strategy in opponents:
        pokemons.append((factory.create_base(), strategy))
    for i in range(len(pokemons)):
        for j in range(i + 1, len(pokemons)):
            pokemon1, strategy1 = pokemons[i]
            pokemon2, strategy2 = pokemons[j]
            print("* Battle *")
            print(pokemon1.describe())
            print(" vs.")
            print(pokemon2.describe())
            print(" now fight!")
            try:
                strategy1.act(pokemon1)
                strategy2.act(pokemon2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def test_basic():
    print("Tournament 0 (basic)")
    print("[ (Charmander+Normal), (Healing+Defensive) ]")
    battle([
        (FireFactory(), NormalStrategy()),
        (HealingPokemonFactory(), DefensiveStrategy()),
    ])


def test_error():
    print("Tournament 1 (error)")
    print("[ (Charmander+Aggressive), (Healing+Defensive) ]")
    battle([
        (FireFactory(), AggressiveStrategy()),
        (HealingPokemonFactory(), DefensiveStrategy()),
    ])


def test_multiple():
    print("Tournament 2 (multiple)")
    print("[ (Squirtle+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (WaterFactory(), NormalStrategy()),
        (HealingPokemonFactory(), DefensiveStrategy()),
        (TransformPokemonFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    test_basic()
    print("")
    test_error()
    print("")
    test_multiple()
