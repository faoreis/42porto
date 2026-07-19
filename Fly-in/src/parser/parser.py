from models.graph import Graph
from parser.validator import ft_validator_nb_drones, ft_validator_zone
from exception.inputException import InputError


def open_file(file: str) -> list[str]:
    lines = []
    try:
        with open(file, "r") as content:
            listlines = content.readlines()
            lines = [
                item.strip() for item in listlines if item.strip() and
                not item.startswith('#')
            ]
    except FileNotFoundError as error:
        raise InputError(error)
    except PermissionError as error:
        raise InputError(error)

    return lines


def ft_valid_input(inputlines: list[str]) -> None:
    nbdrones = None
    start_hub = end_hub = False
    zones = []

    for line in inputlines:
        if line.startswith("nb_drones:"):
            if nbdrones is not None:
                raise InputError("Input file have more than one nb_drones")
            nbdrones = ft_validator_nb_drones(line.split(":", 1)[-1])
        
        if line.startswith("start_hub:"):
            if start_hub:
                raise InputError("Input file have more than one start_hub")
            startzone = ft_validator_zone(line.split(":", 1)[-1], start=True)
            zones.append(startzone)
            start_hub = True
        
        if line.startswith("end_hub:"):
            if end_hub:
                raise InputError("Input file have more than one end_hub")
            endzone = ft_validator_zone(line.split(":", 1)[-1], end=True)
            zones.append(endzone)
            end_hub = True

        if line.startswith("hub:"):
            hub = ft_validator_zone(line.split(":", 1)[-1], end=True)
            zones.append(hub)

    graph = Graph(nbdrones, zones)

    for zone in graph.zones:
        zone.print_zone()
    

    return None


def input_file(namefile: str) -> Graph:
    graph = None
    try:
        lines = open_file(namefile)

        if not lines:
            raise InputError("Empty file")

        graph = ft_valid_input(lines)
    except InputError as error:
        print(error)
    return graph
