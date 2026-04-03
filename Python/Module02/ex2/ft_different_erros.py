def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            10 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            print("abc" + 1)
        case _:
            print("Operation completed successfully")


def test_error_types(number: int) -> None:
    try:
        print(f'Testing operations {number}...')
        garden_operations(number)
    except ValueError as error:
        print(f'Caught ValueError: {error}')
    except ZeroDivisionError as error:
        print(f'Caught ZeroDivisionError: {error}')
    except FileNotFoundError as error:
        print(f'Caught FileNotFoundError: {error}')
    except TypeError as error:
        print(f'Caught TypeError: {error}')


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print()
    print("All error types tested successfully!")
