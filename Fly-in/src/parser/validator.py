from exception.inputException import InputError
from models.graph import Zone, Connection
import data.input_config as input_config


def ft_validator_nb_drones(line: str) -> int:
    nb_drones = line.split(":", 1)[-1].strip()
    try:
        nbrones = int(nb_drones)
    except ValueError as error:
        raise InputError(f"nb_drones - {error}")

    if nbrones <= 0:
        raise InputError("nb_drones - The number of drones must be greater than 0")

    return nbrones


def ft_valid_name(name: str) -> str:
    if "-" in name.strip() or name.strip() == "":
        raise InputError("Zone name cannot be empty or contain spaces or dashes")
    return name.strip()


def ft_validator_metadata_zone(metadata: str) -> tuple[str, int, str]:
    metadata_params = metadata.split(" ")
    color = None
    max_drones = 1
    type_zone = "normal"

    for param in metadata_params:
        if param.startswith("color="):
            color = param.split("=")[-1]
        elif param.startswith("max_drones="):
            try:
                max_drones = int(param.split("=")[-1])
            except ValueError as error:
                raise InputError(f"max_drones - {error}")
        elif param.startswith("zone="):
            type_zone = param.split("=")[-1]
            if type_zone not in input_config.zone_types:
                raise InputError(f"zone - Invalid zone type: {type_zone}.")
            
    return (color, max_drones, type_zone)


def ft_validator_zone(zone: str, start: bool = False, end: bool = False) -> Zone:
    color = None
    max_drones = 1
    type_zone = "normal"

    try:
        zone_params = zone.strip().split(" ")

        if len(zone_params) > 4:
            if not(zone_params[4].startswith("[") and zone_params[4].endswith("]")):
                raise InputError(f'"{zone_params[0]} {zone_params[1]}" format is invalid - Extra parameters found"')
            
            color, max_drones, type_zone = ft_validator_metadata_zone(zone_params[4][1:-1])

        name = ft_valid_name(zone_params[1])
        x = zone_params[2]
        y = zone_params[3]
    except ValueError as error:
        raise InputError(f'"{zone_params[0]} {zone_params[1]}" format is invalid - {error}')
    
    return Zone(name.strip(), x, y, start, end, color, max_drones, type_zone)


def ft_valid_connection_zones(connection: str, zones: list[Zone]) -> tuple[str, str]:
    zone1, zone2 = connection.strip().split("-")
    zone1_exists = any(zone.name == zone1 for zone in zones)
    zone2_exists = any(zone.name == zone2 for zone in zones)

    if not zone1_exists or not zone2_exists:
        return None, None
    
    return zone1, zone2


def ft_validator_metadata_connection(metadata: str) -> int:
    max_connections = 1
    if metadata.startswith("max_connections="):
        try:
            max_connections = int(metadata.split("=")[-1])
        except ValueError as error:
            raise InputError(f"max_connections - {error}")
        
        if max_connections <= 0:
            raise InputError("max_connections - The number of connections must be greater than 0")
        
        return max_connections


def ft_validator_connection(connection: str, zones: list[Zone]) -> Connection:
    max_connections = 1
    connecton_params = connection.strip().split(" ")

    if len(connecton_params) > 2:
        if not(connecton_params[2].startswith("[") and connecton_params[2].endswith("]")):
            raise InputError(f'"{connecton_params[0]} {connecton_params[1]}" format is invalid - Extra parameters found"')
        
        max_connections = ft_validator_metadata_connection(connecton_params[2][1:-1])

    zone1, zone2 = ft_valid_connection_zones(connecton_params[1], zones)
    if zone1 is None or zone2 is None:
        raise InputError(f"Connection - One or both zones do not exist: {connecton_params[1]}, {connecton_params[2]}")
    
    return Connection(zone1, zone2, max_connections)


def ft_connection_exists(connection: Connection, connections: list[Connection]) -> bool:
    if connection in connections:
        return False
    
    if (connection.zone2, connection.zone1) in [(conn.zone1, conn.zone2) for conn in connections]:
        return False
    
    return True