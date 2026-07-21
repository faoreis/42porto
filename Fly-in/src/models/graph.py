class Graph:
    def __init__(self, nb_drones: int, zones: list[Zone], connections: list[Connection]):
        self.nb_drones = nb_drones
        self.zones = zones
        self.connections = connections

    def add_zone(self, zone: Zone):
        self.zones.append(zone)

class Zone:
    def __init__(self, name: str, x: int, y: int, start: bool = False, end: bool = False, color: str = None, max_drones: int = 1, type_zone: str = "normal"):
        self.name = name
        self.x = x
        self.y = y
        self.start = start
        self.end = end
        self.color = color
        self.max_drones = max_drones
        self.type_zone = type_zone

    def set_start(self, start: bool):
        self.start = start
    
    def set_end(self, end: bool):
        self.end = end
    
    def print_zone(self):
        print(f"Zone: {self.name}, Coordinates: ({self.x}, {self.y}), Start: {self.start}, End: {self.end}, Color: {self.color}, Max Drones: {self.max_drones}, Type: {self.type_zone}")

class Connection:
    def __init__(self, zone1: str, zone2: str, max_connections: int):
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_connections = max_connections

    def __eq__(self, other):
        return (self.zone1 == other.zone1 and self.zone2 == other.zone2)

    def print_connection(self):
        print(f"Connection: {self.zone1} -> {self.zone2}, Max Connections: {self.max_connections}")

