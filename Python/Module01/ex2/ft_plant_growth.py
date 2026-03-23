class Plant:
    def __init__(self, name, height, _age):
        self.name = name
        self.height = height
        self._age = _age

    def get_info(self):
        print(f'{self.name}: {self.height:.1f}cm, {self._age} days old')
    
    def grow(self):
        self.height += 0.8

    def age(self):
        self._age += 1



def ft_plant_growth():
    plant = Plant("Rose", 25, 30)
    plant.get_info()
    for i in range(6):
        print(f'=== Day {i + 1} ===')
        plant.grow()
        plant.age()
        plant.get_info()
    print("=== Growth this week: 6cm ===")


if  __name__ == "__main__":
    ft_plant_growth()