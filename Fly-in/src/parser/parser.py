from models import Graph
from exception import InputError
from .validator import ft_validator_nb_drones, ft_validator_zone, ft_validator_connection, ft_connection_exists


def open_file(file: str) -> list[tuple[str, int]]:
    lines = []
    try:
        with open(file, "r") as content:
            for idx, raw_line in enumerate(content, start=1):
                if "#" in raw_line:
                    raw_line = raw_line[: raw_line.index("#")]
                cleaned = raw_line.strip()
                if cleaned:
                    lines.append((idx, cleaned))
    except FileNotFoundError as error:
        raise InputError(error)
    except PermissionError as error:
        raise InputError(error)
    except OSError as error:
        raise InputError(error)

    return lines


def ft_valid_input(inputlines: list[str]) -> None:
    nbdrones = None
    start_hub = end_hub = False
    zones = []
    connections = []

    for line_number, line in inputlines:
        if line.startswith("nb_drones:"):
            if nbdrones is not None:
                raise InputError("More than one nb_drones", line_number)
            nbdrones = ft_validator_nb_drones(line, line_number)
            continue
        
        if line.startswith("start_hub:"):
            if start_hub:
                raise InputError("More than one start_hub")
            startzone = ft_validator_zone(line, line_number ,start=True)
            zones.append(startzone)
            start_hub = True
            continue
        
        if line.startswith("end_hub:"):
            if end_hub:
                raise InputError("More than one end_hub")
            endzone = ft_validator_zone(line, line_number, end=True)
            zones.append(endzone)
            end_hub = True
            continue

        if line.startswith("hub:"):
            hub = ft_validator_zone(line, line_number)
            if hub.name in zones:
                raise InputError(f"Zone {hub.name} already exists", line_number)
            zones.append(hub)
            continue
        
        if line.startswith("connection:"):
            connection = ft_validator_connection(line, zones)
            isValid = ft_connection_exists(connection, connections)
            if not isValid:
                raise InputError(f"Connection: {connection.zone1}-{connection.zone2} - Already exists", line_number)
            connections.append(connection)
            continue

        raise InputError(f"Invalid line in input file: {line}", line_number)

    if nbdrones is None:
        raise InputError("Missing required 'nb_drones:' definition")
    if not start_hub:
        raise InputError("Missing required 'start_hub:' definition")
    if not end_hub:
        raise InputError("Missing required 'end_hub:' definition")

    graph = Graph(nbdrones, zones, connections)

    return graph


def input_file(namefile: str) -> Graph:
    graph = None

    lines = open_file(namefile)

    if not lines:
        raise InputError(
            "Empty file or file contains only comments/blank lines"
        )

    graph = ft_valid_input(lines)

    return graph
