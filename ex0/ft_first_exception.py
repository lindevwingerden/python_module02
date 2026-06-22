def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    valid_input = "25"
    invalid_input = "abc"
    for test_input in valid_input, invalid_input:
        print(f"\nInput data is '{test_input}'")
        try:
            result = input_temperature(test_input)
            print(f"Temperature is now {result}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
