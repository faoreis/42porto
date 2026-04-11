import sys


def ft_command_quest(argv: list[str]) -> None:
    print("Program name:", argv[0])
    lagr = len(argv[1:])
    if lagr > 0:
        print("Arguments received:", lagr)
        for i in range(lagr):
            print(f'Arguments {i + 1}: {argv[i + 1]}')
    else:
        print("No arguments privided!")
    print("Total arguments:", lagr + 1)


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest(sys.argv)
