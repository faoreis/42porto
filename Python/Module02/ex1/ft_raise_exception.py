def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
        input_temperature(temp)
    except ValueError as e:
        print(f'Caught input_temperature error: {e}')


def input_temperature(temp: int) -> None:
    if temp < 0:
        raise ValueError
        (f'Caught input_temperature error: \
{temp}°C is too cold for plants (min 0°C)')
    elif temp > 40:
        raise ValueError(f'Caught input_temperature error: \
{temp}°C is too hot for plants (max 40°C)')
    print(f'Temperature is now {temp}°C')


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
