class PlantError(GardenError):
    pass


def water_plant(plant_name) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants) -> None:
    print("Opening watering system")
    for plant_name in plants:
        try:
            water_plant(plant_name)
        except PlantError as e:
            print(f"Caught PlantError: {e}\n.. ending tests and returning to main")
        finally:
            print("Closing watering system")#dit klopt nog niet