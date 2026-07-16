def ft_validator_nb_drones(nb_drones: str) -> int:
    ndrones = int(nb_drones)

    if ndrones <= 0:
        raise ValueError("The number of drones must be greater than 0")
    
    return ndrones
