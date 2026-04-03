import sys


def ft_score_analytics(argv: list[str]) -> None:
    if len(argv) == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        newlist = []
        for arg in argv[1:]:
            try:
                newlist.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(newlist) == 0:
            print(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )
        else:
            print("Scores processed:", newlist)
            print("Total players:", len(newlist))
            print("Total score:", sum(newlist))
            print("Average score:", sum(newlist) / len(newlist))
            print("High score:", max(newlist))
            print("Low score:", min(newlist))
            print("Score range:", max(newlist) - min(newlist))


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics(sys.argv)
