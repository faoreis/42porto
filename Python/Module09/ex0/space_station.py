import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=0, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxigen_level: float = Field(ge=0.0, le=100.0)
    # https://pydantic.dev/docs/validation/latest/api/pydantic/standard_library_types
    last_maintenance: datetime.datetime = Field(le=datetime.datetime.now())
    is_operational: bool = Field(default=True, validate_default=True)
    notes: str = Field(default="", max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name=" International Space Station",
            crew_size=6,
            power_level=85.5,
            oxigen_level=92.3,
            last_maintenance=datetime.datetime(2024, 1, 15),
            is_operational=True,
            notes="All systems nominal."
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxigen_level}%")
        if station.is_operational:
            print("Expected validation error:")
            print("Status: Operational")
        else:
            print("Status: Not operational")
    except ValidationError as error:
        print("Expected validation error:")
        for err in error.errors():
            print(err['msg'])

    print("\n========================================")
    try:
        station2 = SpaceStation(
            station_id="ISS001",
            name=" International Space Station",
            crew_size=25,
            power_level=85.5,
            oxigen_level=92.3,
            last_maintenance=datetime.datetime(2024, 1, 15),
            is_operational=True,
            notes="All systems nominal."
        )
        print("Valid station created:")
        print(f"ID: {station2.station_id}")
        print(f"Name: {station2.name}")
        print(f"Crew: {station2.crew_size} people")
        print(f"Power: {station2.power_level}%")
        print(f"Oxygen: {station2.oxigen_level}%")
        print(f"Status: {station2.is_operational}")
    except ValidationError as error:
        print("Expected validation error:")
        for err in error.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
