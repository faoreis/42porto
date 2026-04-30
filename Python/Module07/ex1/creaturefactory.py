from ex0.creaturefactory import CreatureFactory
from . import capability

class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        Sproutling = capability.Sproutling("Sproutling", "Grass")
        return Sproutling
    
    def create_evolved(self):
        Bloomelle = capability.Bloomelle("Bloomelle", "Grass/Fairy")
        return Bloomelle
    

class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        Shiftling = capability.Shiftling("Shiftling", "Normal")
        return Shiftling
    
    def create_evolved(self):
        Morphagon = capability.Morphagon("Morphagon", "Normal/Dragon")
        return Morphagon