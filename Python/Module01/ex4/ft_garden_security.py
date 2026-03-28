class Plant:
    def __init__(self, name: str , height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> str:
        return f'{self.name}: {self._height:.1f}cm, {self._age} days old'

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self)  -> int:
        return self._age

    def set_height(self, sheight: float) -> bool:
        if sheight > 0:
            self._height += sheight
            return True
        else:
            print(f"{self.name}: Error, height can't be negative")
            return False

    def set_age(self, ages: int) -> bool:
        if ages > 0:
            self._age += ages
            return True
        else:
            print(f"{self.name}: Error, age can't be negative")
            return False


def ft_garden_security() -> None:
    rose = Plant("Rose", 15, 10)
    print(f'Plant created: {rose.show()}')
    print()
    if rose.set_height(10):
        print(f'heigth updated: {rose.get_height()} days')
    else:
        print("heigth update rejected")
    if rose.set_age(20):
        print(f'Age updated: {rose.get_age()} days')
    else:
        print("Age update rejected")
    print()
    if rose.set_height(-20):
        print(f'heigth updated: {rose.get_height()} days')
    else:
        print("heigth update rejected")
    if rose.set_age(-20):
        print(f'Age updated: {rose.get_age()} days')
    else:
        print("Age update rejected")
    print()
    print(f'Current state: {rose.show()}')


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_garden_security()
