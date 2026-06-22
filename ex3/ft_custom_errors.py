class GardenError(Exception):
    # def __init__(self, message: str):
    #     super().__init__(message)
    #     self._message = message

    # def __str__(self):
    #     return f"{self._message}"
    pass #gecommente stuk weghalen?


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def garden_condition(plant_rigidity: int, water_amount: int) -> bool:
    if plant_rigidity < 10:
        raise PlantError("The tomato plant is wilting!")
    elif water_amount < 10:
        raise WaterError("Not enough water in the tank!")
    else:
        return True


def test_garden_condition() -> None:
    test_array = [6, 16, 5]
    error_array = ["PlantError", "WaterError"]
    for i in range(2):
        print(f"\nTesting {error_array[i]}...")
        try:
            if garden_condition(test_array[i], test_array[i + 1]):
                print("No errors!")
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    for i in range(2):
        try:
            if garden_condition(test_array[i], test_array[i + 1]):
                print("No errors!")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_garden_condition()
