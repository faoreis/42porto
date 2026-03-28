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


def wilting(wilting: bool) -> None:
    if wilting:
        raise PlantError("The tomato plant is wilting!")


def water(water: int) -> None:
    if water > 1:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Error Demo ===")
    print("Testing PlantError...")
    try:
        wilting(True)
    except PlantError as e:
        print(f'Caught PlantError: {e}')
    print()
    print("Testing WaterError...")
    try:
        water(2)
    except WaterError as e:
        print(f'Caught WaterError: {e}')
    print()
    print("Testing catching all garden errors...")
    try:
        wilting(True)
    except GardenError as e:
        print(f'Caught GardenError: {e}')
    try:
        water(2)
    except GardenError as e:
        print(f'Caught GardenError: {e}')
    print()
    print("All custom error types work correctly!")
