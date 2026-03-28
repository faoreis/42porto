class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.ages = age

    def show(self) -> None:
        return f'{self.name}: {self.height:.1f}cm, {self.ages} days old'

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.ages += 1


def ft_plant_factory()  -> None:
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
