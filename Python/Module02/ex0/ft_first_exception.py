def test_temperature(temp_str: str) -> None:
    try:
        int(temp_str)
        print(f'Temperature is now {temp_str}°C')
    except ValueError as e:
        print(f'Caught input_temperature error: {e}')


def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    test_temperature(temp_str)


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    input_temperature("25")
    print()
    input_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")
