class Plant:
    def __init__(self, name, height, _age):
        self.name = name
        self.height = height
        self._age = _age

    def show(self):
        return f'{self.name}: {self.height:.1f}cm, {self._age} days old'

    def grow(self):
        self.height += 0.8

    def age(self):
        self._age += 1


def ft_plant_factory():
    plant = Plant("Rose", 25, 30)
    plant1 = Plant("Oak", 200, 365)
    plant2 = Plant("Cactus", 5, 90)
    plant3 = Plant("Sunflower", 80, 45)
    plant4 = Plant("Fern", 15, 120)

    print(f'created: {plant.show()}')
    print(f'created: {plant1.show()}')
    print(f'created: {plant2.show()}')
    print(f'created: {plant3.show()}')
    print(f'created: {plant4.show()}')


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
