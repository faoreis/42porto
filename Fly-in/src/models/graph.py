class Graph:
    def __init__(self, nb_drones: int, zones: list[Zone]):
        self.nb_drones = nb_drones
        self.zones = zones

    def add_zone(self, zone: Zone):
        self.zones.append(zone)

class Zone:
    def __init__(self, name: str, x: float, y: float, start: bool = False, end: bool = False):
        self.name = name
        self.x = x
        self.y = y
        self.start = start
        self.end = end

    def set_start(self, start: bool):
        self.start = start
    
    def set_end(self, end: bool):
        self.end = end
    
    def print_zone(self):
        print(f"Zone: {self.name}, Coordinates: ({self.x}, {self.y}), Start: {self.start}, End: {self.end}")
