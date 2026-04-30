from abc import ABC, abstractmethod
from . import creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> creature.Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> creature.Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        Flameling = creature.Flameling("Flameling", "Fire")
        return Flameling

    def create_evolved(self) -> creature.Creature:
        Pyrodon = creature.Pyrodon("Pyrodon", "Fire/Flying")
        return Pyrodon


class AquaFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        Aquabub = creature.Aquabub("Aquabub", "Water")
        return Aquabub

    def create_evolved(self) -> creature.Creature:
        Torragon = creature.Torragon("Torragon", "Water")
        return Torragon
