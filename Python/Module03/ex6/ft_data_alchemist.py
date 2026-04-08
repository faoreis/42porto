import random


def ft_data_alchemist() -> None:
    lista = [
        'Alice', 'bob', 'Charlie',
        'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]
    print("\nInitial list of players:", lista)
    lista_ac = [e.capitalize() for e in lista]
    print("New list with all names capitalized:", lista_ac)
    lista_c = [e for e in lista if e == e.capitalize()]
    print("New list of capitalized names only:", lista_c)
    dict_p = {e: random.randrange(5000) for e in lista_ac}
    print("\nScore dict:", dict_p)
    x = round(sum(dict_p.values()) / len(dict_p))
    print("Score average is:", x)
    dict_pa = {p: s for p, s in dict_p.items() if s > x}
    print("High scores:", dict_pa)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    ft_data_alchemist()
