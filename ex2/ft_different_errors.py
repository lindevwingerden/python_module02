def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        return int('abc')
    if operation_number == 1:
        return int(10 / 0)
    if operation_number == 2:
        open("/non/existent/file")
        return 0
    if operation_number == 3:
        return int("yes!" + operation_number)
    return operation_number


def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
