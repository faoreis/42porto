import sys


def ft_write(content: str) -> None:
    new_content = ""
    print("Transform data:\n---\n")
    lines = content.split("\n")
    for line in lines:
        new_content = new_content + line + "#\n"
    print(f'{new_content}\n---')
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    file = sys.stdin.readline().strip()
    if file != "":
        try:
            file_open = open(file, "w")
            print(f"Saving data to '{file}'")
            file_open.write(new_content)
            file_open.close()
            print(f"Data saved in file '{file}'")
        except FileNotFoundError as error:
            sys.stderr.write(
                f"[STDERR] Error opening file '{file}': {error}\n"
            )
        except PermissionError as error:
            sys.stderr.write(
                f"[STDERR] Error opening file '{file}': {error}\n"
            )
            print("Not saving data.")
    else:
        print("Not saving data.")


def ft_open_file(file: str) -> None:
    try:
        print(f"Accessing file '{file}'")
        file_open = open(file, "r")
        print("---\n")
        lines = file_open.read()
        print(lines)
        file_open.close()
        print(f"\n---\nFile '{file}' closed.\n")
        ft_write(lines)
    except FileNotFoundError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {error}\n")
    except PermissionError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {error}\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]} <file>')
    else:
        print("=== Cyber Archives Recovery ===")
        ft_open_file(sys.argv[1])
