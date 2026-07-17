from models.graph import Graph
from parser.validator import ft_validator_nb_drones
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


def ft_valid_input(inputlines: list[str], graph: Graph) -> None:
    nbdrones = None

    for line in inputlines:
        if line.startswith("nb_drones:") and nbdrones is None:
            nbdrones = ft_validator_nb_drones(line.split(":", 1)[-1])

        if nbdrones is None:
            raise InputError("Input file nb_drones")

    graph.nb_drones = nbdrones

    return graph


def input_file(namefile: str) -> Graph:
    graph = Graph()

    try:
        lines = open_file(namefile)

        if not lines:
            raise InputError("Empty file")

        ft_valid_input(lines, graph)
    except InputError as error:
        print(error)

    return graph
