from models.graph import Graph

def open_file(file: str) -> list[str]:
    try:
        with open(file, "r") as content:
            listlines = content.readlines()
            lines = [item.strip() for item in listlines if item.strip() and not item.startswith('#')]
            
    except FileNotFoundError as error:
        print(f"Error opening file '{file}': {error}\n")
    except PermissionError as error:
        print(f"Error opening file '{file}': {error}\n")
    
    return lines
    
def valid_input(inputlines: list[str], graph: Graph) -> None:
    ndrones = None

    if inputlines[0].startswith("nb_drones:"):
        try:
            ndrones = int(inputlines[0].split(":", 1)[-1])
            if ndrones <= 0:
                raise ValueError("The number of drones must be greater than 0")
                
        except ValueError as error:
            print(f"Error input nb_drones: {error}\n")
    else:
        print("Warning: 'nb_drones' key not found at the start of the file.\n")

    for line in inputlines[1:]:
        pass
        
    graph.nb_drones = ndrones

def input_file(namefile: str) -> Graph:
    graph = Graph()
    
    lines = open_file(namefile)
    for line in lines:
        print(line)
    valid_input(lines, graph)
    return graph