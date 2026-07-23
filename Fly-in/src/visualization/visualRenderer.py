from models import Graph

class TerminalRenderer:
    def __init__(self, graph: Graph, scale_zone_x: int = 6, scale_connection: int = 8) -> None:
        self.graph = graph
        self.width = 0
        self.height = 0
        self.scale_zone_x = scale_zone_x
        self.scale_zone_y = scale_zone_x // 2
        self.scale_connection = scale_connection
        self.grid = []

    def set_width(self) -> None:
        max_x = max(self.graph.zones, key=lambda z: z.x)
        self.width = ((max_x.x + 1) * self.scale_zone_x) + (max_x.x * self.scale_connection)

    def set_height(self) -> None:
        max_y = max(self.graph.zones, key=lambda z: z.y)
        if max_y.y == 0:
            self.height = self.scale_zone_y
        else:
            self.height = (max_y.y * (self.scale_zone_y)) + (max_y.y  * self.scale_connection)

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


        for zone in self.graph.zones:
            start_x , start_y = self.zone_map_cord(zone.x, zone.y)

            for y in range(self.scale_zone_y):
                for x in range(self.scale_zone_x):
                    self.grid[start_y + y][start_x + x] = f"{GREEN} {RESET}"


        zones_by_name = {zone.name: zone for zone in self.graph.zones}

        for connection in self.graph.connections:
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
                        self.grid[start_y][start_x + i] = "-"
            elif start_y < end_y:
                self.grid[start_y][start_x] = "-"
                i = 0
                while i <= end_y - start_y:
                    self.grid[start_y + i][start_x + i + 1] = "\\"
                    i += 1
                y = start_x + i
                while y < end_x:
                    self.grid[start_y + (i - 1)][y] = "-"
                    y += 1

        for row in self.grid:
            print("".join(row))

        print("\033[0m")


