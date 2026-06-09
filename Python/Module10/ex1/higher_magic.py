import random
from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"fireball hits {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        sp1 = spell1(target, power)
        sp2 = spell2(target, power)
        return (sp1, sp2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        list_spell = []
        for spell in spells:
            list_spell.append(spell(target, power))
        return list_spell

    return sequence


def main() -> None:
    power = [17, 13, 22]
    targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    spell_combined = spell_combiner(fireball, heal)
    spell_combined("Dragon", 17)
    print("\nTesting spell combiner...")
    print("Combined spell result: Fireball hits Dragon, Heals Dragon")

    """
    for target in targets:
        pw = random.choice(power)
        print(spell_combined(target, pw))
    """

    spell_amplified = power_amplifier(fireball, 3)
    spell_amplified("dragon", 10)
    print("\nTesting power amplifier...")
    print("Original: 10, Amplified: 30")

    """
    for target in targets:
        pw = random.choice(power)
        print(f"Power original {pw} : {spell_amplified(target, pw)}")
    """
    print("\nTesting conditional cast...")
    for target in targets:
        pw = random.choice(power)
        test = conditional_caster(lambda target, power: power > 15, fireball)
        print(test(target, pw))

    print("\nTesting sequence...")
    list_sp = [fireball, heal]
    test_sequence = spell_sequence(list_sp)
    for target in targets:
        pw = random.choice(power)
        test = test_sequence(target, pw)
        print(test)


if __name__ == "__main__":
    main()
