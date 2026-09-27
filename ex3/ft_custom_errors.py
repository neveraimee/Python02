class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)

def plant_check() -> None:
    raise PlantError("The tomato plant is wilting!")

def water_check() -> None:
    raise WaterError("Not enough water in the tank!")


def testing_customserrors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as p:
        print(f"Caught PlantError: {p}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except  WaterError as w:
        print(f"Caught WaterError: {w}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as g:
        print(f"Caught GardenError: {g}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as g:
        print(f"Caught GardenError: {g}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    testing_customserrors()
