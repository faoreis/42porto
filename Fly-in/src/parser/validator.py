from exception import InputError
from models import Zone, Connection
import data.input_config.input_structure as input_config


def ft_validator_nb_drones(line: str, line_number: int) -> int:
    parts = line.split(":", 1)

    if len(parts) != 2:
        raise InputError("nb_drones - Invalid format. Expected 'nb_drones: <number>'", line_number)
    
    number_part = parts[1].strip()
    
    try:
        nbrones = int(number_part)
    except ValueError as error:
        raise InputError(f"nb_drones '{number_part}' is not a valid number, {error}", line_number)

    if nbrones <= 0:
        raise InputError("nb_drones - The number of drones must be greater than 0", line_number)

    return nbrones


def ft_valid_name(name: str, line_number: int) -> str:
    name_clean = name.strip()

    if not name_clean:
        raise InputError(f"Zone name '{name_clean}' cannot be empty", line_number)

    if "-" in name_clean:
        raise InputError(f"Zone name '{name_clean}' cannot contain dashes", line_number)

    if " " in name_clean:
        raise InputError(f"Zone name '{name_clean}' cannot contain spaces", line_number)

    return name_clean


def ft_validator_metadata_zone(metadata: str, line_number: int) -> tuple[str, int, str]:
    color = None
    max_drones = 1
    type_zone = "normal"

    for param in metadata.split(" "):

        if not param or "=" not in param:
            raise InputError(f"Invalid metadata format: '{param}'. Expected 'key=value'", line_number)

        key, _, value = param.partition("=")
        key = key.strip().lower()
        value = value.strip()

        if key == "color":
            if not value or " " in value:
                raise InputError("color value cannot be empty or contain spaces", line_number)

            color = value.lower()

        elif key == "max_drones":
            try:
                max_drones = int(value)
            except ValueError as error:
                raise InputError(f"Invalid metadata max_drones - {error}", line_number)

            if max_drones <= 0:
                raise InputError("Invalid metadata max_drones- The number of drones must be greater than 0", line_number)

        elif key == "zone":
            if value not in input_config.zone_types:
                raise InputError(f"Invalid metadata zone - Invalid zone type: {value}.")

            type_zone = value

        else:
            raise InputError(f"Invalid metadata '{param}'. Expected 'color', 'max_drones', or 'zone'", line_number)

    return (color, max_drones, type_zone)


def ft_validator_zone(line_zone: str, line_number: int, start: bool = False, end: bool = False) -> Zone:
    color = None
    max_drones = 1
    type_zone = "normal"

    try:
        prefix, data_zone = line_zone.split(":", 1)
    except ValueError:
        raise InputError(f"format is invalid - Zone line missing ':'", line_number)

    data_zone = data_zone.strip()

    if not data_zone:
        raise InputError(f"{prefix.strip()} - missing name and coordinates", line_number)

    metadata = None
    if data_zone.endswith("]"):
        metadata_start = data_zone.rfind("[")
        if metadata_start == -1:
            raise InputError(f"{prefix.strip()} - Invalid metadata format. Expected '[key=value ...]'", line_number)

        metadata = data_zone[metadata_start + 1 :-1]
        data_zone = data_zone[:metadata_start].strip()

    params_zone = data_zone.split(" ")
    
    if len(params_zone) != 3:
        raise InputError(
            f"Expected '<name> <x> <y>' after '{prefix.strip()}:', "
            f"got {len(params_zone)} tokens",
            line_number
        )
    
    name = ft_valid_name(params_zone[0], line_number)

    try:
        x = int(params_zone[1])
        y = int(params_zone[2])
    except ValueError as error:
        raise InputError(f"Invalid coordinates: {error}", line_number)

    if metadata is not None:
        color, max_drones, type_zone = ft_validator_metadata_zone(metadata, line_number)
    
    return Zone(name.strip(), x, y, start, end, color, max_drones, type_zone)



def ft_validator_metadata_connection(metadata: str, line_number: int) -> int:
    max_link_capacity = 1

    for param in metadata.split(" "):
        if not param or "=" not in param:
            raise InputError(
                f"Invalid connection metadata format: '{param}'. Expected 'key=value'",
                line_number
            )

        key, _, value = param.partition("=")
        key = key.strip().lower()
        value = value.strip()

        if key == "max_link_capacity":
            try:
                max_link_capacity = int(value)
            except ValueError as error:
                raise InputError(f"max_link_capacity - '{value}' is not a valid integer", line_number)

            if max_link_capacity <= 0:
                raise InputError("max_link_capacity - The number of connections must be greater than 0", line_number)

        else:
            raise InputError(
                f"Unknown connection metadata key '{key}'. "
                "Only 'max_link_capacity' is allowed",
                line_number,
            )
        
    return max_link_capacity


def ft_validator_connection(connection: str, zones: list[Zone], line_number: int) -> Connection:
    try:
        _, connection_params = connection.split(":", 1)
    except ValueError:
        raise InputError(f"Connection line missing ':'", line_number)

    connection_params = connection_params.strip()

    if not connection_params:
        raise InputError(f"Connection - missing zone names", line_number)

    metadata_str = None

    if connection_params.endswith("]"):
        start = connection_params.rfind("[")
        if start == -1:
            raise InputError(f"metadata missing opening '['", line_number)

        metadata_str = connection_params[start + 1 :-1]
        connection_params = connection_params[:start].strip()

    if "-" not in connection_params:
        raise InputError(f"Connection - Invalid format. Expected 'zone1-zone2'", line_number)

    connection_zones = connection_params.split("-")
    if len(connection_zones) != 2:
        raise InputError(f"Connection - Invalid format. Expected 'zone1-zone2'", line_number)

    zone1 = connection_zones[0].strip()
    zone2 = connection_zones[1].strip()

    if zone1 is None or zone2 is None:
        raise InputError(f"Connection - Zone names cannot be empty", line_number)

    zones_names = [zone.name for zone in zones]

    if zone1 not in zones_names:
        raise InputError(f"Connection - Zone '{zone1}' does not exist", line_number)

    if zone2 not in zones_names:
        raise InputError(f"Connection - Zone '{zone2}' does not exist", line_number)

    if zone1 == zone2:
        raise InputError(f"Connection - Zone names cannot be the same", line_number)

    max_link_capacity = 1

    if metadata_str is not None:
        max_link_capacity = ft_validator_metadata_connection(metadata_str, line_number)

    return Connection(zone1, zone2, max_link_capacity)


def ft_connection_exists(connection: Connection, connections: list[Connection]) -> bool:
    if connection in connections:
        return False
    
    if (connection.zone2, connection.zone1) in [(conn.zone1, conn.zone2) for conn in connections]:
        return False
    
    return True