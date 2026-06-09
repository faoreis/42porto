from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    match operation:
        case "add":
            return reduce(lambda x, y: x + y, spells)
        case "multiply":
            return reduce(lambda x, y: x * y, spells)
        case "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        case "min":
            return reduce(lambda x, y: x if x < y else y, spells)
        case _:
            raise ValueError("Exist one or more operation invalid!")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanted {target} with {element} magic (Power: {power})"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    dict_enchanter: dict[str, Callable] = {}
    dict_enchanter['version1'] = partial(
        base_enchantment,
        power=50,
        element="Fire"
    )
    dict_enchanter['version2'] = partial(
        base_enchantment,
        power=50,
        element="Water"
    )
    dict_enchanter['version3'] = partial(
        base_enchantment,
        power=50,
        element="Earth"
    )

    return dict_enchanter


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def memoized_fibonacci2(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def display(spell: Any) -> str:
        return "Unknown spell type"

    @display.register
    def _(spell: int) -> str:
        return f"Damage {spell}: 42 damage"

    @display.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @display.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return display


def main() -> None:
    spell_powers = [38, 49, 14, 38, 44, 18]
    operations = ['add', 'multiply', 'max', 'min']
    print("\nTesting spell reducer...")
    try:
        for operation in operations:
            print(f"{operation}: {spell_reducer(spell_powers, operation)}")
    except ValueError as error:
        print(error)

    print("\nTesting enchanter partial...")
    enchanter = partial_enchanter(base_enchantment)
    print(enchanter['version1'](target="Sword"))
    print(enchanter['version2'](target="Shield"))
    print(enchanter['version3'](target="Arrow"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("Testing spell dispatcher...")
    test = spell_dispatcher()
    print(test(42))
    print(test("fireball"))
    print(test([1, 2, 3, 4, 5]))
    print(test(32.43))


if __name__ == "__main__":
    main()
