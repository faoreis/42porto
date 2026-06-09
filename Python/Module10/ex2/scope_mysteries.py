from typing import Callable


def mage_counter() -> Callable:
    counter = 0

    def counter_call() -> int:
        nonlocal counter
        counter += 1
        return counter
    return counter_call


def spell_accumulator(initial_power: int) -> Callable:
    initial = initial_power

    def accumulator(power: int) -> int:
        nonlocal initial
        initial += power
        return initial
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    fact_enchantment = enchantment_type

    def enchantment(item: str) -> str:
        result = fact_enchantment + " " + item
        return result
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        if key in memory:
            return str(memory[key])
        else:
            return "Memory not found"

    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1 -", counter_a())
    print("counter_a call 2 -", counter_a())
    print("counter_b call 1 -", counter_b())

    print("\nTesting spell accumulator...")
    accbase = spell_accumulator(100)
    accbase1 = spell_accumulator(100)
    print(f"Base 100, add 20: {accbase(20)}")
    print(f"Base 100, add more 20: {accbase(20)}")
    print(f"Base1 100, add 30: {accbase1(30)}")

    print("\nTesting enchantment factory...")
    enchantment1 = enchantment_factory("Dark")
    enchantment2 = enchantment_factory("Windy")
    enchantment3 = enchantment_factory("Radiant")
    print(enchantment1("Ring"))
    print(enchantment2("Wand"))
    print(enchantment3("Amulet"))
    print(enchantment1("Armor"))

    print("\nTesting memory vault...")
    memory = memory_vault()
    print("Store 'secret' = 42")
    memory['store']("secret", 42)
    print("Recall 'secret':", memory['recall']("secret"))
    print("Recall 'unknown':", memory['recall']("unknown"))


if __name__ == "__main__":
    main()
