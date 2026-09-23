
from ex1 import HealingPokemonFactory, TransformPokemonFactory


def test_healing():
    print("Testing Pokemon with healing capability")
    healing_factory = HealingPokemonFactory()

    print(" base:")
    base_heal = healing_factory.create_base()
    print(base_heal.describe())
    print(base_heal.attack())
    print(base_heal.heal())

    print(" evolved:")
    evolved_heal = healing_factory.create_evolved()
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(evolved_heal.heal())


def test_transform():
    print("Testing Pokemon with transform capability")
    transform_factory = TransformPokemonFactory()

    print(" base:")
    base_transform = transform_factory.create_base()
    print(base_transform.describe())
    print(base_transform.attack())
    print(base_transform.transform())
    print(base_transform.attack())
    print(base_transform.revert())

    print(" evolved:")
    evolved_transform = transform_factory.create_evolved()
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(evolved_transform.transform())
    print(evolved_transform.attack())
    print(evolved_transform.revert())


if __name__ == "__main__":
    test_healing()
    print("")
    test_transform()
