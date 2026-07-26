from .graph import Zone

class Drone:
    def __init__(self, id: int, zone: Zone):
        self.id = id
        self.zone = zone