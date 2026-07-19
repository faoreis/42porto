from exception.inputException import InputError
from models.graph import Zone


def ft_validator_nb_drones(nb_drones: str) -> int:
    try:
        nbrones = int(nb_drones)
    except ValueError as error:
        raise InputError(f"nb_drones - {error}")

    if nbrones <= 0:
        raise InputError("The number of drones must be greater than 0")

    return nbrones

def ft_validator_zone(zone: str, start: bool = False, end: bool = False) -> Zone:
    try:
        name, x, y, teste = zone.strip().split(" ", 3)
        if " " in name.strip() or "-" in name.strip() or name.strip() == "":
            raise InputError("Zone name cannot be empty or contain spaces or dashes")
        x = int(x)
        y = int(y)
        teste = teste.strip()
    except ValueError as error:
        raise InputError(f"Error in zone format - {error}")
    
    return Zone(name.strip(), x, y, start=start, end=end)

    
    