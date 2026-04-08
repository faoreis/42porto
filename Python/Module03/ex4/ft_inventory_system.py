import sys


def valid_input(args: list[str]) -> dict[str, int]:
    dic = {}
    for arg in args[1:]:
        if ':' in arg:
            key, value = arg.split(":", 1)
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
    return (dic)


def display_info(dic: dict[str, int]) -> None:
    print("Got inventory:", dic)
    print("Item list:", list(dic.keys()))
    total = sum(dic.values())
    print(f'Total quantity of the {len(dic.values())} items: {total}')
    max = 0
    min = 0
    itemi = ""
    itema = ""
    for key in dic.keys():
        print(f"Item {key} represents {((dic[key] / total) * 100):.1f}%")
        if min == 0:
            min = dic[key]
            itemi = key
        if dic[key] > max:
            max = dic[key]
            itema = key
        elif dic[key] < min:
            min = dic[key]
            itemi = key
    print(f'Item most abundant: {itema} with quantity {max}')
    print(f'Item least abundant: {itemi} with quantity {min}')
    dic.update({'magic_item': 1})
    print("Updated inventory:", dic)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    dic = valid_input(sys.argv)
    display_info(dic)
