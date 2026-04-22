def secure_archive(file: str, order: int) -> tuple[bool, str]:
    try:
        if order == 1:
            with open(file, "r") as content:
                string = content.read()
                return (True, string)
        else:
            with open(file, "w") as content:
                wirtestring = "Content successfully written to file"
                content.write(wirtestring)
                return (True, wirtestring)
    except FileNotFoundError as error:
        return (False, str(error))
    except PermissionError as error:
        return (False, str(error))


def archive() -> None:
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 1))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("test.txt", 1))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", 1))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test2.txt", 2))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    archive()
