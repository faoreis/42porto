from models import Graph

class TerminalRenderer:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.width = 0
        self.height = 0
        self.scale_zone = 3
        self.scale_connection = 4

    def set_width(self) -> None:
        max_x = max(self.graph.zones, key=lambda z: z.x)
        self.width = ((max_x.x + 1) * self.scale_zone) + (max_x.x * self.scale_connection)

    def set_height(self) -> None:
        max_y = max(self.graph.zones, key=lambda z: z.y)
        if max_y.y == 0:
            self.height = self.scale_zone
        else:
            self.height = (max_y.y * self.scale_zone) + (max_y.y  * self.scale_connection)

    def clear_terminal(self) -> None:
        print("\x1b[2J\x1b[1;1H", end="")

    def render(self) -> None:
        self.clear_terminal()
        self.set_width()
        self.set_height()

        grid = [["\033[48;5;197m  " for _ in range(self.width)] for _ in range(self.height)]

        for zone in self.graph.zones:
            start_x = zone.x * (self.scale_zone + self.scale_connection)
            start_y = zone.y * self.scale_zone

            for y in range(self.scale_zone):
                for x in range(self.scale_zone):
                    grid[start_y + y][start_x + x] = "\033[48;5;47m  "


        for row in grid:
            print("".join(row))


