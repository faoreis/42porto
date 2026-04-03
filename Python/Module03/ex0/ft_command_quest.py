import sys


def ft_command_quest(argv: list[str]) -> None:
    print("Program name:", argv[0])
    lagr = len(argv)
    if lagr > 1:
        print("Arguments received:", lagr - 1)
        for i in range(lagr - 1):
            print(f'Arguments {i + 1}: {argv[i + 1]}')
    else:
        print("No arguments privided!")
    print("Total arguments:", lagr)


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest(sys.argv)
