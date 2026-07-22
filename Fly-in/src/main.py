from parser import input_file
from visualization import TerminalRenderer

def main() -> None:
    graph = input_file("data/maps/easy/02_simple_fork.txt")
    renderer = TerminalRenderer(graph, 6, 8)
    renderer.render()

if __name__ == "__main__":
    main()
