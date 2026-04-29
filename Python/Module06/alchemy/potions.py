from alchemy import elements as alchemy_elements
import elements


def strength_potion() -> str:
    return (
        f"Strength potion brewedbwith "
        f"'{elements.create_fire()}' and '{elements.create_water()}'"
    )


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{alchemy_elements.create_earth()}' "
        f"and '{alchemy_elements.create_air()}'"
    )
