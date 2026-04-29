from alchemy.grimoire import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    for ingredient in ingredients.split(" "):
        if ingredient in light_spellbook.light_spell_allowed_ingredients():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
