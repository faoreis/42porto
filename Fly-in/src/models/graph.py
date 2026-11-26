from .connection import Connection
from .zone import Zone

class Graph:
    def __init__(self, nb_drones: int, zones: list[Zone], connections: list[Connection]):
        self.nb_drones = nb_drones
        self.zones = zones
        self.connections = connections


    def add_zone(self, zone: Zone):
        self.zones.append(zone)


    def found_start_zone(self):
        return next(zone for zone in self.zones if zone.start)


    def found_end_zone(self):
        return next(zone for zone in self.zones if zone.end)


    def get_zone(self, name: str) -> Zone:
        return next((zone for zone in self.zones if zone.name == name), None)
    

    def get_connection(self, name_a: str, name_b: str) -> Connection:
        for conn in self.connections:
            if (conn.zone1 == name_a and conn.zone2 == name_b) or (
                conn.zone1 == name_b and conn.zone2 == name_a
            ):
                return conn
        return None


    def movement_cost(self, destination: Zone) -> float | None:
        if destination.type_zone == "blocked":
            return None
        if destination.type_zone == "restricted":
            return 2.0
        if destination.type_zone == "priority":
            return 0.999
        return 1.0

    def build_adjacency(self) -> dict[str, list[tuple[Zone, Connection]]]:
        zone_name = {z.name: z for z in self.zones}

        adj: dict[str, list[tuple[Zone, Connection]]] = {z.name: [] for z in self.zones}

        for conn in self.connections:
            z1 = zone_name.get(conn.zone1)
            z2 = zone_name.get(conn.zone2)
            if z1 is None or z2 is None:
                continue
            adj[z1.name].append((z2, conn))
            adj[z2.name].append((z1, conn))
        return adj



