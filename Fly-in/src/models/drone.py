from .graph import Zone

class Drone:
    def __init__(self, id: int, start_zone: Zone):
        self.id = id
        self.zone = start_zone
        self.path = []
        self.index = 0
        self.finished = False

        