import sys


def valid_input(args: list[str]) -> dict[str, int]:
    dic = {}
    for arg in args:
        if ':' in arg:
            key , value = arg.split(":", 1)
            try:
                value = int(value)
                if key in dic.keys():
                    print(f"Redundant item '{key}' - discarding")
                else:
                    dic[key] = value
            except ValueError as error:
                print(f"Quantity error for '{key}': {error}")
        else:
            print(f"Error - invalid parameter '{arg}'")
    return(dic)


def display_info(dic: dict[str, int]) -> None:
    print("Got inventory:", dic)
    print("Item list:", list(dic.keys()))
    total = sum(dic.values())
    print(f'Total quantity of the {len(dic.values())} items: {total}')
    for key in dic.keys():
        


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    dic = valid_input(sys.argv)
    display_info(dic)