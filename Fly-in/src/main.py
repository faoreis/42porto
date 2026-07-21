from parser import input_file
from visualization.visualRenderer import TerminalRenderer



def main() -> None:
    graph = input_file("data/maps/easy/01_linear_path.txt")
    renderer = TerminalRenderer(graph)
    renderer.render()

if __name__ == "__main__":
    main()
