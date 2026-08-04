from models import Graph, Simulation, Connection
from typing import TYPE_CHECKING
import data.input_config.input_structure as input_config
from .pathFinder import PathFinder
import math


class TerminalRenderer:
    def __init__(self, graph: Graph, scale_zone_x: int = 6, scale_connection: int = 8) -> None:
        self.graph = graph
        self.width = 0
        self.height = 0
        self.scale_zone_x = scale_zone_x
        self.scale_zone_y = scale_zone_x // 2
        self.scale_connection = scale_connection
        self.separator = 5
        self.grid = []

    def set_width(self) -> None:
        max_x = max(self.graph.zones, key=lambda z: z.x)
        self.width = ((max_x.x) * self.scale_zone_x) + (max_x.x * self.scale_connection) + len(max_x.name)

    def set_height(self) -> None:
        max_y = max(self.graph.zones, key=lambda z: z.y)
        if max_y.y == 0:
            self.height = self.scale_zone_y + self.separator
        else:
            self.height = (max_y.y * (self.scale_zone_y)) + (max_y.y  * self.scale_connection) + self.separator  + 1

    def clear_terminal(self) -> None:
        print("\x1b[2J\x1b[1;1H", end="")

    def zone_map_cord(self, x: int, y: int):
        min_x = min(zone.x for zone in self.graph.zones)
        min_y = min(zone.y for zone in self.graph.zones)
        offset_x = -min_x
        offset_y = -min_y
        
        draw_x = x + offset_x
        draw_y = y + offset_y
        
        start_x = draw_x  * (self.scale_zone_x + self.scale_connection)
        start_y = draw_y  * (self.scale_zone_y)

        if start_y > 0:
            start_y = start_y + (draw_y * self.separator)

        return (start_x, start_y)

    def connection_map_cord(self, x: int, y: int):
        connection_x, connection_y = self.zone_map_cord(x, y)
        connection_x = connection_x + self.scale_zone_x
        connection_y = connection_y + (self.scale_zone_y // 2)

        return(connection_x, connection_y)

    def connection_sorter(self, connections: list[Connection]) -> list[Connection]:
        print(connections)
        def get_dist(conn: Connection):
            z1 = self.graph.get_zone(conn.zone1)
            z2 = self.graph.get_zone(conn.zone2)
            return math.dist((z1.x, z1.y), (z2.x, z2.y))

        return sorted(connections, key=get_dist, reverse=True)


    def render(self, simulation: Simulation) -> None:
        self.clear_terminal()
        self.set_width()
        self.set_height()

        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]


        for zone in self.graph.zones:
            color_zone = input_config.ANSI_COLORS_NAMES.get(zone.color, 15)
            color = f"\033[48;5;{color_zone}m"
            reset = "\033[0m"

            start_x , start_y = self.zone_map_cord(zone.x, zone.y)

            for y in range(self.scale_zone_y):
                for x in range(self.scale_zone_x):
                    self.grid[start_y + y][start_x + x] = f"X"
            i = 0
            for i in range(len(zone.name)):
                self.grid[start_y + self.scale_zone_y][start_x + i] = "S"

        zones_by_name = {zone.name: zone for zone in self.graph.zones}

        connection_finder = PathFinder(self.grid, self.width, self.height)

        connections_sorted = self.connection_sorter(self.graph.connections)
        print(connections_sorted)

        for connection in connections_sorted:
            connection_finder.set_grid(self.grid)
            zone1 = zones_by_name[connection.zone1]
            zone2 = zones_by_name[connection.zone2]

            if zone2.x > zone1.x:
                start = zone1
                end = zone2
            else:
                start = zone2
                end = zone1

            start_x, start_y = self.connection_map_cord(start.x, start.y)
            end_x, end_y = self.connection_map_cord(end.x, end.y)
            if start.x != end.x:
                end_x -= self.scale_zone_x +1

            path_connection = connection_finder.find_path((start_x, start_y), (end_x, end_y))
            print(path_connection)

            for i in range(len(path_connection)):
                current = path_connection[i]
                if current is None:
                    continue

                if i < len(path_connection) - 1:
                    next_cell = path_connection[i + 1]
                else:
                    next_cell = None

                if i > 0:
                    previous = path_connection[i - 1]
                else:
                    previous = None

                if previous is None or next_cell is None:
                    self.grid[current[1]][current[0]] = "\u253C"
                    continue

                dx1 = current[0] - previous[0]
                dy1 = current[1] - previous[1]

                dx2 = next_cell[0] - current[0]
                dy2 = next_cell[1] - current[1]
                

                if dy1 == 0 and dy2 == 0:
                    self.grid[current[1]][current[0]] = "─"
                elif dx1 == 0 and dx2 == 0:
                    self.grid[current[1]][current[0]] = "│"
                elif (dx1, dy1, dx2, dy2) in [(-1,0,0,1), (0,-1,1,0)]:
                    self.grid[current[1]][current[0]] = "┌"
                elif (dx1, dy1, dx2, dy2) in [(-1,0,0,-1), (0,1,1,0)]:
                    self.grid[current[1]][current[0]] = "└"
                elif (dx1, dy1, dx2, dy2) in [(1,0,0,1), (0,-1,-1,0)]:
                    self.grid[current[1]][current[0]] = "┐"
                elif (dx1, dy1, dx2, dy2) in [(1,0,0,-1), (0,1,-1,0)]:
                    self.grid[current[1]][current[0]] = "┘"

        self.draw_visual_zones()
        self.draw_drones(simulation)
        
        for row in self.grid:
            print("".join(row))

    def draw_visual_zones(self) -> None:
        for zone in self.graph.zones:
            color_zone = input_config.ANSI_COLORS_NAMES.get(zone.color, 15)
            color = f"\033[48;5;{color_zone}m"
            reset = "\033[0m"

            start_x , start_y = self.zone_map_cord(zone.x, zone.y)

            for y in range(self.scale_zone_y):
                for x in range(self.scale_zone_x):
                    self.grid[start_y + y][start_x + x] = f"{color} {reset}"
            i = 0
            for i in range(len(zone.name)):
                self.grid[start_y + self.scale_zone_y][start_x + i] = zone.name[i]


    def draw_drones(self, simulation: Simulation) -> None:
        for drone in simulation.drones:
            zone = drone.zone
            nb_drones_zone = simulation.drones_in_zone(zone)

            start_x, start_y = self.zone_map_cord(zone.x, zone.y)

            drone_x = start_x + self.scale_zone_x // 2
            drone_y = start_y + self.scale_zone_y // 2

            self.grid[drone_y][drone_x - 1] = "D"

            nb_drone_str = str(len(nb_drones_zone))

            for i in range(len(nb_drone_str)):
                self.grid[drone_y][drone_x + i] = nb_drone_str[i]

