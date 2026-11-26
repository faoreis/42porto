from .graph import Graph
from .zone import Zone
from .pathfinding import PathFinder
from .drone import Drone
from .connection import Connection
from collections import deque


class Simulation:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.drones = self.create_drones()
        self.turn: int = 0
        self.history: list[str] = []

    def create_drones(self) -> list[Drone]:
        drones = []

        start_zone = self.graph.found_start_zone()
        for i in range(self.graph.nb_drones):
            drones.append(Drone(i + 1, start_zone))

        return drones

    def finished(self):
        return all(drone.finished for drone in self.drones)

    def drones_in_zone(self, zone) -> list[Drone]:
        return [drone for drone in self.drones if drone.zone == zone]

    # def move_drone(self, drone: Drone, zone: Zone) -> None:
    #     drone.zone = zone


    def drones_on_connection(self, conn: Connection) -> list[Drone]:
        return [
            d for d in self.drones
            if d.in_transit
            and d.transit_connection is not None
            and d.transit_connection == conn
        ]


    # def neighbors(self, zone):
    #     neighbors = []

    #     for connection in self.graph.connections:
    #         if connection.zone1 == zone.name:
    #             neighbors.append(
    #                 next(z for z in self.graph.zones if z.name == connection.zone2)
    #             )

    #         elif connection.zone2 == zone.name:
    #             neighbors.append(
    #                 next(z for z in self.graph.zones if z.name == connection.zone1)
    #             )

    #     return neighbors


    def prepare(self) -> None:
        finder = PathFinder(self.graph)
        path = finder.find_path()

        if not path:
            raise RuntimeError("No path from start to end")

        for drone in self.drones:
            drone.path = path
            drone.index = 0
            drone.finished = False



    def step(self) -> list[str]:
        """
        Executa um turno.
        Devolve a lista de tokens deste turno (ex: ["D1-roof1", "D2-corridorA"]).
        Também acrescenta a linha em self.history.
        """
        tokens: list[str] = []

        # 1) Primeiro: quem já está em trânsito (obrigatório avançar)
        for drone in self.drones:
            if drone.finished or not drone.in_transit:
                continue
            tokens.append(drone.advance_transit())

        # 2) Depois: tentativas de novo movimento
        #    (ordem estável por id para ser determinístico)
        for drone in sorted(
            (d for d in self.drones if not d.finished and not d.in_transit),
            key=lambda d: d.id,
        ):
            next_z = drone.next_zone()
            if next_z is None:
                continue

            conn = self.graph.get_connection(drone.zone.name, next_z.name)
            if conn is None:
                continue

            # Capacidade da connection
            if len(self.drones_on_connection(conn)) >= conn.max_link_capacity:
                continue  # espera

            # Capacidade da zone destino
            # (drones que saem neste turno já não contam se usares occupies_zone
            #  só para quem não está in_transit; para ser mais preciso podes
            #  calcular "free slots" tendo em conta saídas)
            occupied = len(self.drones_in_zone(next_z))
            if not next_z.has_capacity_for(occupied) and not next_z.end:
                continue  # espera

            # Restricted = 2 turns
            if next_z.type_zone == "restricted":
                drone.begin_transit(conn, next_z, turns=2)
                tokens.append(drone.advance_transit())  # 1º turno do trânsito
            else:
                tokens.append(drone.move_to(next_z))

        self.turn += 1
        if tokens:
            line = " ".join(tokens)
            self.history.append(line)
        return tokens

    def run(self) -> list[str]:
        """Corre até todos terminarem; devolve o histórico completo."""
        self.prepare()
        while not self.finished():
            self.step()
        return self.history

    # def step(self):

    #     for drone in self.drones:

    #         if drone.finished:
    #             continue

    #         next_zone = drone.path[drone.index + 1]
    #         next_zone_drones = self.drones_in_zone(next_zone)
    #         if next_zone.end:
    #             self.move_drone(drone, next_zone)
    #             drone.index += 1
    #             drone.finished = True
    #         elif next_zone.get_max_drones() > len(self.drones_in_zone(next_zone)):
    #             self.move_drone(drone, next_zone)
    #             drone.index += 1


    # def bfs(self):
    #     # Track visited nodes to prevent cycles
    #     visited = set()
    #     start_zone =  self.graph.found_start_zone()
        
    #     # Initialize FIFO queue with the source node
    #     queue = deque([start_zone])
    #     visited.add(start_zone)
    #     path = []
    #     while queue:
    #         # Pop the oldest node added to the queue
    #         current_zone = queue.popleft()
    #         path.append(current_zone)
    #         if current_zone.end:
    #             return path
            
    #         # Check all direct neighbors
    #         for neighbor in self.neighbors(current_zone):
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 queue.append(neighbor)



