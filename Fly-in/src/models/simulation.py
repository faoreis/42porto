from .graph import Graph, Zone
from .drone import Drone
from collections import deque

class Simulation:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.drones = self.create_drones() 

    def create_drones(self) -> list[Drone]:
        drones = []

        start_zone = self.graph.found_start_zone()
        for i in range(self.graph.nb_drones):
            drones.append(Drone(i + 1, start_zone))

        return drones

    def drones_in_zone(self, zone) -> list[Drone]:
        return [drone for drone in self.drones if drone.zone == zone]

    def move_drone(self, drone: Drone, zone: Zone) -> None:
        drone.zone = zone

    def neighbors(self, zone):
        neighbors = []

        for connection in self.graph.connections:
            if connection.zone1 == zone.name:
                neighbors.append(
                    next(z for z in self.graph.zones if z.name == connection.zone2)
                )

            elif connection.zone2 == zone.name:
                neighbors.append(
                    next(z for z in self.graph.zones if z.name == connection.zone1)
                )

        return neighbors


    def bfs(self):
        # Track visited nodes to prevent cycles
        visited = set()
        start_zone =  self.graph.found_start_zone()
        # Initialize FIFO queue with the source node
        queue = deque([start_zone])
        visited.add(start_zone)
        path = []
        while queue:
            # Pop the oldest node added to the queue
            current_zone = queue.popleft()
            path.append(current_zone)
            if current_zone.end:
                print("Goal encontrado!")
                return path
            
            # Check all direct neighbors
            for neighbor in self.neighbors(current_zone):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
