class Plant:
    def __init__(self, name, height, _age):
        self.name = name
        self.height = height
        self._age = _age

    def show(self):
        print(f'{self.name}: {self.height:.1f}cm, {self._age} days old')

    def grow(self):
        self.height += 2.1

    def age(self):
        self._age += 1


class Flower(Plant):
    def __init__(self, name, height, _age, color):
        super().__init__(name, height, _age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f'Color: {self.color}')
        if self.bloomed:
            print(f'{self.name} is blooming beautifully!')
        else:
            print(f'{self.name} has not bloomed yet')


class Tree(Plant):
    def __init__(self, name, height, _age, trunk_diameter):
        super().__init__(name, height, _age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f'Tree {self.name} now produces a shade of {self.height:.1f}cm '
            f'long and {self.trunk_diameter:.1f}cm wide.'
        )

    def show(self):
        super().show()
        print(f'Trunk diameter: {self.trunk_diameter:.1f}cm')


class Vegetable(Plant):
    def __init__(self, name, height, _age, harvest_season, nutritional_value):
        super().__init__(name, height, _age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f'Harvest season: {self.harvest_season:}')
        print(f'Nutritional value: {self.nutritional_value:}')

    def grow(self):
        super().grow()
        self.nutritional_value += 1


def ft_plant_types():
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
