from models import Graph

class TerminalRenderer:
    def __init__(self, graph: Graph, scale_zone_x: int = 6, scale_connection: int = 8) -> None:
        self.graph = graph
        self.width = 0
        self.height = 0
        self.scale_zone_x = scale_zone_x
        self.scale_zone_y = scale_zone_x // 2
        self.scale_connection = scale_connection

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

    def render(self) -> None:
        self.clear_terminal()
        self.set_width()
        self.set_height()
        

        GREEN = "\033[48;5;47m"
        RESET = "\033[0m"

        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        for zone in self.graph.zones:
            min_x = min(zone.x for zone in self.graph.zones)
            min_y = min(zone.y for zone in self.graph.zones)
            
            offset_x = -min_x
            offset_y = -min_y
            
            draw_x = zone.x + offset_x
            draw_y = zone.y + offset_y
            
            start_x = draw_x  * (self.scale_zone_x + self.scale_connection)
            start_y = draw_y  * (self.scale_zone_y)

            for y in range(self.scale_zone_y):
                for x in range(self.scale_zone_x):
                    grid[start_y + y][start_x + x] = f"{GREEN} {RESET}"

                if y == 1 and not zone.end:
                    for i in range(self.scale_connection):
                        grid[start_y + 1][start_x + self.scale_zone_x + i] = "-"

        for row in grid:
            print("".join(row))

        print("\033[0m")


