import ex1


def test_factoryheal(factory: ex1.creaturefactory.CreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_factorytransform(factory: ex1.creaturefactory.CreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())
    

def main() -> None:
    print("Testing Creature with healing capability")
    healfactory = ex1.creaturefactory.HealingCreatureFactory()
    test_factoryheal(healfactory)
    print("\nTesting Creature with transform capability")
    trasformfactory = ex1.creaturefactory.TransformCreatureFactory()
    test_factorytransform(trasformfactory)


if __name__ == "__main__":
    main()
