from exception.inputException import InputError


def ft_validator_nb_drones(nb_drones: str) -> int:
    try:
        nbrones = int(nb_drones)
    except ValueError as error:
        raise InputError(f"nb_drones - {error}")

    if nbrones <= 0:
        raise InputError("The number of drones must be greater than 0")

    return nbrones
