class GardenError(Exception):
    def __init__(self, message: str):
        super.__init__(message)
    
    def __str__(self):
        return f"{self.message}"


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
    try:#misschien dit ook nog iteratief maken?
        garden_condition(6, 16)
        garden_condition(16, 6)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_garden_condition()
