import ex0


def test_factory(factory: ex0.creaturefactory.CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
        firefactory: ex0.creaturefactory.CreatureFactory,
        waterfactory: ex0.creaturefactory.CreatureFactory
        ) -> None:
    firebase = firefactory.create_base()
    waterbase = waterfactory.create_base()
    print(firebase.describe())
    print(" vs.")
    print(waterbase.describe())
    print(" figth!")
    print(firebase.attack())
    print(waterbase.attack())


def main() -> None:
    print("Testing factory")
    firefactory = ex0.creaturefactory.FlameFactory()
    test_factory(firefactory)
    print("\nTesting factory")
    waterfactory = ex0.creaturefactory.AquaFactory()
    test_factory(waterfactory)
    print("\nTesting battle")
    test_battle(firefactory, waterfactory)


if __name__ == "__main__":
    main()
