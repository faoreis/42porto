def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])
    min_power = min(mages, key=lambda x: x['power'])
    avg_power = sum(mage['power'] for mage in mages) / len(mages)
    return {
        'max_power': max_power['power'],
        'min_power': min_power['power'],
        'avg_power': round(avg_power, 2)
    }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 77, 'type': 'armor'},
        {'name': 'Crystal Orb', 'power': 76, 'type': 'weapon'},
        {'name': 'Light Prism', 'power': 78, 'type': 'focus'},
        {'name': 'Ice Wand', 'power': 120, 'type': 'focus'}
    ]

    mages = [
        {'name': 'River', 'power': 88, 'element': 'shadow'},
        {'name': 'Alex', 'power': 78, 'element': 'wind'},
        {'name': 'Storm', 'power': 72, 'element': 'light'},
        {'name': 'Zara', 'power': 62, 'element': 'lightning'},
        {'name': 'Phoenix', 'power': 84, 'element': 'lightning'}
    ]

    spells = ['fireball', 'earthquake', 'tsunami', 'freeze']

    artifacts_sorted = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(
        f"{artifacts_sorted[0]['name']} "
        f"({artifacts_sorted[0]['power']} power) "
        f"comes before {artifacts_sorted[1]['name']} "
        f"({artifacts_sorted[0]['power']} power)"
    )

    mages_filter = power_filter(mages, 80)
    print("\nTesting power filter (80 power)...")
    for mage in mages_filter:
        print(f"{mage['name']} - {mage['power']} power")

    spells_transformed = spell_transformer(spells)
    print("\nTesting spell transformer...")
    print(" ".join(spells_transformed))

    mages_statistics = mage_stats(mages)
    print("\nTesting mage stats...")
    print(
        f"Max: {mages_statistics['max_power']}, "
        f"Min: {mages_statistics['min_power']}, "
        f"Avg: {mages_statistics['avg_power']}"
    )


if __name__ == "__main__":
    main()
