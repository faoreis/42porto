import ex0
import ex1
import ex2
from typing import Any


def battle(opponents: list[tuple[Any, ex2.strategy.BattleStrategy]]) -> None:
    creatures = []
    for creature, strategy in opponents:
        creatures.append((creature.create_base(), strategy))
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature1 = creatures[i][0]
            strategy1 = creatures[i][1]
            creature2 = creatures[j][0]
            strategy2 = creatures[j][1]
            print("\n* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as error:
                print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    firefactory = ex0.creaturefactory.FlameFactory()
    waterfactory = ex0.creaturefactory.AquaFactory()
    healfactory = ex1.creaturefactory.HealingCreatureFactory()
    trasformfactory = ex1.creaturefactory.TransformCreatureFactory()
    normal = ex2.strategy.NormalStrategy()
    defensive = ex2.strategy.DefensiveStrategy()
    aggressive = ex2.strategy.AggressiveStrategy()
    opponents = [(firefactory, normal), (healfactory, defensive)]
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    battle(opponents)
    opponents = [(firefactory, aggressive), (healfactory, defensive)]
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    battle(opponents)
    opponents = [
        (waterfactory, normal),
        (healfactory, defensive),
        (trasformfactory, aggressive)
    ]
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    battle(opponents)


if __name__ == "__main__":
    main()
