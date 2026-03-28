class GardenError(Exception):
    def __init__(self, message: str) -> None:
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown garden error")


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown plant error")


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown water error")


def water_plant(name: str) -> None:
    if name == name.capitalize():
        print(f'Watering {name}: [OK]')
    else:
        raise PlantError(f"Invalid plant name to water: '{name}'")


def test_watering_sistem() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrot")
    except PlantError as error:
        print(f'Caught PlantError: {error}')
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrot")
    except PlantError as error:
        print(f'Caught PlantError: {error}')
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_sistem()
    print()
    print("Cleanup always happens, even with errors!")
