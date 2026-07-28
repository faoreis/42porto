from parser import input_file
from visualization import TerminalRenderer
from models import Simulation

def main() -> None:
    #graph = input_file("data/maps/easy/02_simple_fork.txt")
    graph = input_file("data/maps/hard/01_maze_nightmare.txt")
    simulation = Simulation(graph)
    renderer = TerminalRenderer(graph, 6, 8)

    simulation.run(renderer)

    #Teste mover automatico
    # drone = simulation.drones[0]

    # while not drone.zone.end:
    #     next_zone = simulation.neighbors(drone.zone)[0]
    #     simulation.move_drone(drone, next_zone)

    #     renderer.render()
    #     input()

    # Teste para ver os vizinhos
    # for zone in simulation.graph.zones:
    #     print(f"{zone.name}: ", end="")

    #     for neighbor in simulation.neighbors(zone):
    #         print(neighbor.name, end=" ")

    #     print()

    #Teste manual para mover um drone até ao fim (mapa linear)
    # renderer.render()

    # input("Enter...")

    # simulation.move_drone(simulation.drones[0], "waypoint1")
    # renderer.render()

    # input("Enter...")

    # simulation.move_drone(simulation.drones[0], "waypoint2")
    # renderer.render()

    # input("Enter...")

    # simulation.move_drone(simulation.drones[0], "goal")
    # renderer.render()


if __name__ == "__main__":
    main()
