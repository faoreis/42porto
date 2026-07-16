from models.graph import Graph
from parser.validator import ft_validator_nb_drones

def open_file(file: str) -> list[str]:
    lines = []
    try:
        with open(file, "r") as content:
            listlines = content.readlines()
            lines = [item.strip() for item in listlines if item.strip() and not item.startswith('#')]
            
    except FileNotFoundError as error:
        print(f"Error opening file '{file}': {error}\n")
    except PermissionError as error:
        print(f"Error opening file '{file}': {error}\n")
    
    return lines
    
def ft_valid_input(inputlines: list[str], graph: Graph) -> None:
    nbdrones = None

    for line in inputlines:

        if line.startswith("nb_drones:") and nbdrones is None:
            try:
                nbdrones = ft_validator_nb_drones(line.split(":", 1)[-1])
            except ValueError as error:
                print(f"Error input nb_drones: {error}\n")
        else:
            raise ValueError("Warning: 'nb_drones' key not found at the start of the file.\n")
            continue
        
    graph.nb_drones = nbdrones

    return graph

def input_file(namefile: str) -> Graph:
    graph = Graph()
    
    lines = open_file(namefile)
    for line in lines:
        print(line)
    ft_valid_input(lines, graph)
    return graph