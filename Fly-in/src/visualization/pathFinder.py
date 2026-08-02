from models import Graph
from collections import deque

class PathFinder:
    def __init__(self, grid: list[list[str]], width: int, height: int):
        self.grid = grid
        self.width = width
        self.height = height

    def set_grid(self, grid: list[list[str]]):
        self.grid = grid


    def neighbours(self, x: int, y: int, endx: int, endy: int):
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < self.width and 0 <= ny < self.height:
                if self.grid[ny][nx] == " " or (nx, ny) == (endx, endy):
                    yield (nx, ny)

    
    def find_path(self, start: tuple[int, int], end: tuple[int, int]):
        queue = deque([start])
        visited = {start}
        parent = {}

        while queue:
            current = queue.popleft()

            if current == end:
                break

            for neighbour in self.neighbours(*current, *end):
                if neighbour not in visited:
                    visited.add(neighbour)
                    parent[neighbour] = current
                    queue.append(neighbour)

        if end not in visited:
            return []

        path = []
        current = end

        while current != start:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()
   
        return path