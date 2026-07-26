from models import Simulation

class TerminalRenderer:
    def __init__(self, simulation: Simulation, scale_zone_x: int = 6, scale_connection: int = 8) -> None:
        self.simulation = simulation
        self.width = 0
        self.height = 0
        self.scale_zone_x = scale_zone_x
        self.scale_zone_y = scale_zone_x // 2
        self.scale_connection = scale_connection
        self.grid = []

    def set_width(self) -> None:
        max_x = max(self.simulation.graph.zones, key=lambda z: z.x)
        self.width = ((max_x.x + 1) * self.scale_zone_x) + (max_x.x * self.scale_connection)

    def set_height(self) -> None:
        max_y = max(self.simulation.graph.zones, key=lambda z: z.y)
        if max_y.y == 0:
            self.height = self.scale_zone_y + 1
        else:
            self.height = (max_y.y * (self.scale_zone_y)) + (max_y.y  * self.scale_connection) + 1

    def clear_terminal(self) -> None:
        print("\x1b[2J\x1b[1;1H", end="")

    def zone_map_cord(self, x: int, y: int):
        min_x = min(zone.x for zone in self.simulation.graph.zones)
        min_y = min(zone.y for zone in self.simulation.graph.zones)
        offset_x = -min_x
        offset_y = -min_y
        
        draw_x = x + offset_x
        draw_y = y + offset_y
        
        start_x = draw_x  * (self.scale_zone_x + self.scale_connection)
        start_y = draw_y  * (self.scale_zone_y)

        return (start_x, start_y)

    def connection_map_cord(self, x: int, y: int):
        connection_x, connection_y = self.zone_map_cord(x, y)
        connection_x = connection_x + self.scale_zone_x
        connection_y = connection_y + (self.scale_zone_y // 2)

        return(connection_x, connection_y)


    def render(self) -> None:
        self.clear_terminal()
        self.set_width()
        self.set_height()
        

        GREEN = "\033[48;5;47m"
        RESET = "\033[0m"

        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]


        for zone in self.simulation.graph.zones:
            start_x , start_y = self.zone_map_cord(zone.x, zone.y)

            for y in range(self.scale_zone_y):
                for x in range(self.scale_zone_x):
                    self.grid[start_y + y][start_x + x] = f"{GREEN} {RESET}"
            i = 0
            for i in range(len(zone.name)):
                self.grid[start_y + self.scale_zone_y][start_x + i] = zone.name[i]


        zones_by_name = {zone.name: zone for zone in self.simulation.graph.zones}

        for connection in self.simulation.graph.connections:
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

            end_x -= self.scale_zone_x 

            if start_y == end_y:
                    for i in range(end_x - start_x):
                        self.grid[start_y][start_x + i] = "\u2594"

            elif start_y < end_y:
                self.grid[start_y][start_x] = "\u2594"
                i = 0
                while i < end_y - start_y:
                    self.grid[start_y + i][start_x + i + 1] = "\\"
                    i += 1

                x = start_x + i + 1
                while x < end_x:
                    self.grid[start_y + i][x] = "\u2594"
                    x += 1
                    
            elif end_y < start_y:
                self.grid[start_y][start_x] = "\u2594"
                i = 1
                while i <= start_y - end_y:
                    self.grid[start_y - i][start_x + i] = "/"
                    i += 1

                x = start_x + i
                while x < end_x:
                    self.grid[end_y][x] = "\u2594"
                    x += 1

        self.draw_drones()

        for row in self.grid:
            print("".join(row))

    def draw_drones(self):
        for drone in self.simulation.drones:
            zone = drone.zone
            nb_drones_zone = self.simulation.drones_in_zone(zone)

            start_x, start_y = self.zone_map_cord(zone.x, zone.y)

            drone_x = start_x + self.scale_zone_x // 2
            drone_y = start_y + self.scale_zone_y // 2

            self.grid[drone_y][drone_x - 1] = "D"
            self.grid[drone_y][drone_x] = str(len(nb_drones_zone))

