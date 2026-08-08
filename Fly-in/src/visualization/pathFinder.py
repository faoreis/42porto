from models import Graph
from collections import deque
import data.input_config.input_structure as input_structure

class PathFinder:
    def __init__(self, grid: list[list[str]], width: int, height: int):
        self.grid = grid
        self.width = width
        self.height = height
        self.occupied_edges: set[frozenset[tuple[int, int]]] = set()
        self.occupied_zone_connection = []

    def set_grid(self, grid: list[list[str]]):
        self.grid = grid


    def neighbours(
        self,
        x: int,
        y: int,
        ends: set[tuple[int, int]],
        blocked_points: set[tuple[int, int]]
    ):
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if not (0 <= nx < self.width and 0 <= ny < self.height):
                continue

            if (nx, ny) in blocked_points:
                continue

            edge = frozenset({
                (x, y),
                (nx, ny)
            })

            if edge in self.occupied_edges:
                continue

            cell = self.grid[ny][nx]
            if cell == " ":
                yield (nx, ny)
            elif cell in input_structure.PATH_CHARS:
                yield (nx, ny)
            elif (nx, ny) == ends:
                yield (nx, ny)

    
    def find_path(
        self,
        starts: list[tuple[int, int]],
        ends: list[tuple[int, int]],
        blocked_points: set[tuple[int, int]]
    ):
        blocked_points.update(self.occupied_zone_connection)
        queue = deque()
        visited = set()
        parent = {}
        ends_set = set(ends)

        for start in starts:
            if start not in self.occupied_zone_connection:
                queue.append(start)
                visited.add(start)
                parent[start] = None

        while queue:
            current = queue.popleft()

            if current in ends_set:
                self.occupied_zone_connection.append(current)
                path = []

                while current is not None:
                    path.append(current)
                    current = parent[current]

                path.reverse()
                
                self.occupied_zone_connection.append(path[0])
                return path

            for neighbour in self.neighbours(*current, ends_set, blocked_points):
                if neighbour in visited:
                    continue

                visited.add(neighbour)
                parent[neighbour] = current
                queue.append(neighbour)
   
        return []

    def register_path(self, path):

        for i in range(len(path) - 1):

            edge = frozenset({
                path[i],
                path[i + 1]
            })

            self.occupied_edges.add(edge)