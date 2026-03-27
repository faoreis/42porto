class Plant:
    def __init__(self, name, _height, age):
        self.name = name
        self._height = height
        self._age = age

    def show(self):
        print(f'{self.name}: {self._height:.1f}cm, {self._age} days old')

    def grow(self):
        self._height += 0.8

    def age(self):__init__
        self._age += 1


def ft_plant_growth():
    plant = Plant("Rose", 25, 30)
    x = plant.height
    for i in range(5):
        print(f'=== Day {i + 1} ===')
        plant.show()
        plant.grow()
        plant.age()
    y = plant.height
    print(f'Growth this week: {(y - x):.1f}cm')


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth()
