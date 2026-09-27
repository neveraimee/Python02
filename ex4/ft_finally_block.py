class PlantError(Exception): #what is exception
    def __init__(self, message: str = "Unknown plant error") -> None: #how can we declare the str while type hinting
        super().__init__(message) # what is super and init doing and why do we give message as a param


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")

def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    finally: #do we need finally here to end try?
        print("Closing water system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as p:
        print(f"Caught PlantError: {p}")
        print(".. ending tests and returning to main")
        return #why return here
    finally:
        print("Closing watering system")
        print()
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()