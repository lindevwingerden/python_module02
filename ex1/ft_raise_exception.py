class TooCold(Exception):
    pass


class TooHot(Exception):
    pass


def input_temperature(temp_str: str) -> int:
    result = int(temp_str)
    if result < 0:
        raise TooCold
    if result > 40:
        raise TooHot
    return int(temp_str)


def test_temperature() -> None:
    valid_input = "25"
    invalid_input = "abc"
    too_hot = "100"
    too_cold = "-50"
    for input in valid_input, invalid_input, too_hot, too_cold:
        print(f"\nInput data is '{input}'")
        try:
            result = input_temperature(input)
            print(f"Temperature is now {result}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        except TooCold:
            print(f"Caught input_temperature error: {input}°C is too cold",
                  "for plants (min 0°C)")
        except TooHot:
            print(f"Caught input_temperature error: {input}°C is too hot",
                  "for plants (max 40°C)")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
