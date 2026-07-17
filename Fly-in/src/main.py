from parser.parser import input_file
from models.graph import Graph

def main() -> None:
    grap1 = input_file("../data/maps/easy/01_linear_path.txt")
    print(grap1.nb_drones)

if __name__ == "__main__":
    main()