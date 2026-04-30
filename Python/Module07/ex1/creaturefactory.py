from ex0.creaturefactory import CreatureFactory, creature
from . import capability


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        Sproutling = capability.Sproutling("Sproutling", "Grass")
        return Sproutling

    def create_evolved(self) -> creature.Creature:
        Bloomelle = capability.Bloomelle("Bloomelle", "Grass/Fairy")
        return Bloomelle


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        Shiftling = capability.Shiftling("Shiftling", "Normal")
        return Shiftling

    def create_evolved(self) -> creature.Creature:
        Morphagon = capability.Morphagon("Morphagon", "Normal/Dragon")
        return Morphagon
