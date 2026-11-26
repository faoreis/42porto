from asyncio import graph
from typing import Optional
from .graph import Graph
from .zone import Zone
from heapq import heappop, heappush

class PathFinder:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.adjacency_list = self.graph.build_adjacency()

    def find_path(self) -> list[Zone]:
        start_zone = self.graph.found_start_zone()
        end_zone = self.graph.found_end_zone()

        if start_zone is None or end_zone is None:
            return []

        pq: list[tuple[float, int, str]] = []
        counter = 0
        heappush(pq, (0.0, counter, start_zone.name))

        best_cost: dict[str, float] = {start_zone.name: 0.0}
        parent: dict[str, Optional[str]] = {start_zone.name: None}

        while pq:
            cost, _, name = heappop(pq)
            if cost > best_cost.get(name, float("inf")):
                continue
            if name == end_zone.name:
                return self._reconstruct(parent, end_zone.name)

            for neighbor, _conn in self.adjacency_list.get(name, []):
                step = self.graph.movement_cost(neighbor)
                if step is None:
                    continue  # blocked

                new_cost = cost + step
                nname = neighbor.name
                if new_cost < best_cost.get(nname, float("inf")):
                    best_cost[nname] = new_cost
                    parent[nname] = name
                    counter += 1
                    heappush(pq, (new_cost, counter, nname))

    def _reconstruct(self, parent: dict[str, Optional[str]], goal_name: str) -> list[Zone]:
        names: list[str] = []
        cur: Optional[str] = goal_name
        while cur is not None:
            names.append(cur)
            cur = parent[cur]
        names.reverse()
        index = {z.name: z for z in self.graph.zones}
        return [index[n] for n in names]

    def find_shortest_path(graph: Graph) -> list[Zone]:
        return PathFinder(graph).find_path()

        

