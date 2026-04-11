import sys


def ft_open_file(file: str) -> None:
    try:
        print(f"Accessing file '{file}'")
        file_open = open(file, "r")
        print("---\n")
        print(file_open.read())
        file_open.close()
        print(f"\n---\nFile '{file}' closed.")
    except FileNotFoundError as error:
        print(f"Error opening file '{file}': {error}\n")
    except PermissionError as error:
        print(f"Error opening file '{file}': {error}\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]} <file>')
    else:
        print("=== Cyber Archives Recovery ===")
        ft_open_file(sys.argv[1])
