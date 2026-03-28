class Plant:
    class Status:
        def __init__(self) -> None:
            self.__grow = 0
            self.__age = 0
            self.__show = 0
            self.__shade = 0

        def display(self) -> None:
            print(
                f'Stats: {self.__grow} grow, {self.__age} age, '
                f'{self.__show} show'
            )

        def display_tree(self) -> None:
            print(
                f'Stats: {self.__grow} grow, {self.__age} age, '
                f'{self.__show} show'
            )
            print(f'{self.__shade} shade')

        def inc_grow(self) -> None:
            self.__grow += 1

        def inc_shade(self) -> None:
            self.__shade += 1

        def inc_age(self) -> None:
            self.__age += 1

        def inc_show(self) -> None:
            self.__show += 1

    def __init__(self, name: str, height: float, ages: int) -> None:
        self.name = name
        self._height = height
        self._age = ages
        self._status = self.Status()

    @classmethod
    def default(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def show(self) -> None:
        print(f'{self.name}: {self._height:.1f}cm, {self._age} days old')
        self._status.inc_show()

    def grow(self, valor: float) -> None:
        self._height += valor
        self._status.inc_grow()

    def age(self, valor: int) -> None:
        self._age += valor
        self._status.inc_age()

    @staticmethod
    def checksages(days: int) -> bool:
        return days > 365


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        color: str
    ) -> None:
        super().__init__(name, height, ages)
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
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f'Tree {self.name} now produces a shade of {self._height:.1f}cm '
            f'long and {self.trunk_diameter:.1f}cm wide.'
        )
        self._status.inc_shade()

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self.trunk_diameter:.1f}cm')


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f'Harvest season: {self.harvest_season:}')
        print(f'Nutritional value: {self.nutritional_value:}')

    def grow(self, valor: float) -> None:
        super().grow(valor)
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seed = 0

    def show(self) -> None:
        super().show()
        print(f'Seeds: {self.seed}')

    def bloom(self) -> None:
        super().bloom()

    def seeds(self, valor: int) -> None:
        self.seed += valor


def display_status(plant: Plant) -> None:
    plant._status.display()


def ft_plant_types() -> None:
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
    sunflower.bloom()
    sunflower.seeds(42)
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
