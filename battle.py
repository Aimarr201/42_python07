
from ex0 import FireFactory, WaterFactory, PokemonFactory


def test_factory(factory: PokemonFactory):
    print("Testing factory")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print()


def test_battle(factory1: PokemonFactory, factory2: PokemonFactory):
    print("Testing battle")

    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()

    print(fighter1.describe())
    print(" vs.")
    print(fighter2.describe())
    print(" fight!")

    print(fighter1.attack())
    print(fighter2.attack())


if __name__ == "__main__":
    fire_fac = FireFactory()
    water_fac = WaterFactory()

    test_factory(fire_fac)
    test_factory(water_fac)
    test_battle(fire_fac, water_fac)
