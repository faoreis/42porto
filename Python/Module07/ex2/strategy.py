from abc import ABC, abstractmethod
from ex1.capability import HealCapability, TransformCapability
from typing import Any


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, factory: Any) -> None:
        ...

    @abstractmethod
    def is_valid(self, factory) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        print(creature.attack())

    def is_valid(self, creature: Any) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise Exception(
                f"Invalid Creature '{creature.__class__.__name__}' "
                f"for this aggressive strategy"
            )

    def is_valid(self, factory: Any) -> bool:
        if isinstance(factory, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(
                f"Invalid Creature '{creature.__class__.__name__}' "
                f"for this defensive strategy"
            )

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
