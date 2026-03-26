class Plant:
    class Status:
        def __init__(self):
            self.__grow = 0
            self.__age = 0
            self.__show = 0
            self.__shade = 0

        def display(self):
            print(f'Stats: {self.__grow} grow, {self.__age} age, {self.__show} show')

        def display_tree(self):
            print(f'Stats: {self.__grow} grow, {self.__age} age, {self.__show} show')
            print(f'{self.__shade} shade')

        def inc_grow(self):
            self.__grow += 1

        def inc_shade(self):
            self.__shade += 1

        def inc_age(self):
            self.__age += 1

        def inc_show(self):
            self.__show += 1

    def __init__(self, name, height, ages):
        self.name = name
        self.height = height
        self.ages = ages
        self._status = self.Status()

    @classmethod
    def default(cls):
        return cls("Unknown plant", 0, 0)

    def show(self):
        print(f'{self.name}: {self.height:.1f}cm, {self.ages} days old')
        self._status.inc_show()

    def grow(self, valor):
        self.height += valor
        self._status.inc_grow()

    def age(self, valor):
        self.ages += valor
        self._status.inc_age()

    @staticmethod
    def checksages(days):
        return days > 365


class Flower(Plant):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages)
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
    def __init__(self, name, height, ages, trunk_diameter):
        super().__init__(name, height, ages)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f'Tree {self.name} now produces a shade of {self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.')
        self._status.inc_shade()

    def show(self):
        super().show()
        print(f'Trunk diameter: {self.trunk_diameter:.1f}cm')


class Vegetable(Plant):
    def __init__(self, name, height, ages, harvest_season, nutritional_value):
        super().__init__(name, height, ages)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f'Harvest season: {self.harvest_season:}')
        print(f'Nutritional value: {self.nutritional_value:}')

    def grow(self, valor):
        super().grow(valor)
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages, color)
        self.seeds = 0

    def show(self):
        super().show()
        print(f'Seeds: {self.seeds}')

    def bloom(self, valor):
        super().bloom()
        self.seeds += valor


def display_status(plant):
    plant._status.display()


def ft_plant_types():
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    anonymous = Plant.default()

    print("=== Check year-old")
    print(f'Is 30 days more than a year? -> {Plant.checksages(30)}')
    print(f'Is 400 days more than a year? -> {Plant.checksages(400)}')
    print()
    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    rose._status.display()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(8)
    rose.show()
    rose._status.display()
    print()
    print("=== Tree")
    oak.show()
    print("[statistics for Oak]")
    oak._status.display_tree()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak._status.display_tree()
    print()
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower._status.display()
    print()
    print("=== Anonymous")
    anonymous.show()
    print("[statistics for Unknown plant]")
    anonymous._status.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_plant_types()
