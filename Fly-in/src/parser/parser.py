from models.graph import Graph
from parser.validator import ft_validator_nb_drones, ft_validator_zone, ft_validator_connection, ft_connection_exists
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
    connections = []

    for line in inputlines:
        if line.startswith("nb_drones:"):
            if nbdrones is not None:
                raise InputError("Input file have more than one nb_drones")
            nbdrones = ft_validator_nb_drones(line)
            continue
        
        if line.startswith("start_hub:"):
            if start_hub:
                raise InputError("Input file have more than one start_hub")
            startzone = ft_validator_zone(line, start=True)
            zones.append(startzone)
            start_hub = True
            continue
        
        if line.startswith("end_hub:"):
            if end_hub:
                raise InputError("Input file have more than one end_hub")
            endzone = ft_validator_zone(line, end=True)
            zones.append(endzone)
            end_hub = True
            continue

        if line.startswith("hub:"):
            hub = ft_validator_zone(line)
            zones.append(hub)
            continue
        
        if line.startswith("connection:"):
            connection = ft_validator_connection(line, zones)
            isValid = ft_connection_exists(connection, connections)
            if not isValid:
                raise InputError(f"Connection: {connection.zone1}-{connection.zone2} - Already exists")
            connections.append(connection)
            continue

        raise InputError(f"Invalid line in input file: {line}")

    graph = Graph(nbdrones, zones, connections)

    for zone in graph.zones:
        zone.print_zone()
    
    for connection in graph.connections:
        connection.print_connection()

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
