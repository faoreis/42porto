from abc import ABC, abstractmethod
from ex0.creature import Creature

class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        ...

class TransformCapability(ABC):
    def __init__(self):
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Sproutling(Creature,HealCapability):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"
    

class Bloomelle(Creature, HealCapability):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self):
        return "Bloomelle uses Petal Dance!"
    
    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."
    
    def transform(self) -> str:
        self.transformed = True
        return "Shiftling shifts into a sharper form!"
    
    def revert(self) -> str:
        self.transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self) -> str:
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."
    
    def transform(self) -> str:
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"
    
    def revert(self):
        self.transformed = False
        return "Morphagon stabilizes its form."
