import random

achievements = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Master Builder",
        "Hidden Path Finder",
        "Gladiator",
        "Navigator",
        "Sharpshooter",
        "Healer",
        "Assassin"
]


def gen_player_achievements() -> set[str]:
    p_achievements = []
    a_len = random.randint(1, len(achievements))
    p_achievements = random.sample(achievements, a_len)
    return set(p_achievements)


def player_achievements() -> None:
    alice_achievements = gen_player_achievements()
    print("Player Alice: ", alice_achievements)
    bob_achievements = gen_player_achievements()
    print("Player Bob: ", bob_achievements)
    charlie_achievements = gen_player_achievements()
    print("Player Charlie: ", charlie_achievements)
    dylan_achievements = gen_player_achievements()
    print("Player Dylan: ", dylan_achievements)
    union = (
        alice_achievements
        | bob_achievements
        | charlie_achievements
        | dylan_achievements
    )
    print("\nAll distinct achievements: ", union)
    inter = (
        alice_achievements
        & bob_achievements
        & charlie_achievements
        & dylan_achievements
    )
    print("\nCommon achievements: ", inter)
    diffa = (
        alice_achievements
        - bob_achievements
        - charlie_achievements
        - dylan_achievements
    )
    print("\nOnly Alice has: ", diffa)
    diffb = (
        bob_achievements
        - alice_achievements
        - charlie_achievements
        - dylan_achievements
    )
    print("\nOnly Bob has: ", diffb)
    diffc = (
        charlie_achievements
        - bob_achievements
        - alice_achievements
        - dylan_achievements
    )
    print("\nOnly Charlie has: ", diffc)
    diffd = (
        dylan_achievements
        - bob_achievements
        - charlie_achievements
        - alice_achievements
    )
    print("\nOnly Dylan has: ", diffd)
    missia = (
        set(achievements) - alice_achievements
    )
    print("\nAlice is missing: ", missia)
    missib = (
        set(achievements) - bob_achievements
    )
    print("Bob is missing: ", missib)
    missic = (
        set(achievements) - charlie_achievements
    )
    print("Charlie is missing: ", missic)
    missid = (
        set(achievements) - dylan_achievements
    )
    print("Dylan is missing: ", missid)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player_achievements()
