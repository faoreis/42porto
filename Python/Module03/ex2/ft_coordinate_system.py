import math


def get_player_pos() -> tuple[float, ...]:
    stop = True
    while (stop):
        valid = True
        listcoord = []
        coord = input("Enter new coordinates as floats in format 'x,y,z': ")
        listcoord = coord.split(",")
        if len(listcoord) == 3:
            temp = []
            for cord in listcoord:
                try:
                    value = float(cord)
                    temp.append(value)
                except ValueError as error:
                    print(f"Error on parameter '{cord}': {error}")
                    valid = False
            if valid:
                coord_tupple = tuple(temp)
                stop = False
        else:
            print("Invalid syntax")
    return coord_tupple


def ft_calculate() -> None:
    print("Get a first set of coordinates")
    tuple1 = get_player_pos()
    print("Got a first tuple:", tuple1)
    print(f'It includes: X= {tuple1[0]}, Y= {tuple1[1]}, Z= {tuple1[2]}')
    x1 = tuple1[0]
    y1 = tuple1[1]
    z1 = tuple1[2]
    d = round(math.sqrt((x1-0)**2 + (y1-0)**2 + (z1-0)**2), 4)
    print("Distance to center: ", d)
    print()
    print("Get a second set of coordinates")
    tuple2 = get_player_pos()
    x2 = tuple2[0]
    y2 = tuple2[1]
    z2 = tuple2[2]
    d2 = round(math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2), 4)
    print("Distance between the 2 sets of coordinates: ", d2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    ft_calculate()
