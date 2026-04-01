import random


def gen_player_achievements() -> set:
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
    p_achievements = []
    a_len = random.randint(1, len(achievements))
    p_achievements = random.sample(achievements, a_len)
    return set(p_achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    alice_achievements = gen_player_achievements()
    print("Player Alice: ", alice_achievements)
    bob_achievements = gen_player_achievements()
    print("Player Bob: ", bob_achievements)
    charlie_achievements = gen_player_achievements()
    print("Player Charlie: ", charlie_achievements)
    dylan_achievements = gen_player_achievements()
    print("Player Dylan: ", dylan_achievements)
    print()
    union = (
        alice_achievements
        | bob_achievements
        | charlie_achievements
        | dylan_achievements
    )
    print("All distinct achievements: ", union)
    inter = (
        alice_achievements
        & bob_achievements
        & charlie_achievements
        & dylan_achievements
    )
    print("Common achievements: ", inter)
    diffa = (
        alice_achievements
        - bob_achievements
        - charlie_achievements
        - dylan_achievements       
    )


