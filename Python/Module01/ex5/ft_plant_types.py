class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f'{self.name}: {self._height:.1f}cm, {self._age} days old')

    def grow(self) -> None:
        self._height += 2.1

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f'Color: {self.color}')
        if self.bloomed:
            print(f'{self.name} is blooming beautifully!')
        else:
            print(f'{self.name} has not bloomed yet')


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f'Tree {self.name} now produces a shade of {self._height:.1f}cm '
            f'long and {self.trunk_diameter:.1f}cm wide.'
        )

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self.trunk_diameter:.1f}cm')


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f'Harvest season: {self.harvest_season:}')
        print(f'Nutritional value: {self.nutritional_value:}')

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


def ft_plant_types() -> None:
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
