import sys

print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    newlist = []
    for arg in sys.argv[1:]:
        try:
            newlist.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(newlist) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("Scores processed:", newlist)
        print("Total players:", len(newlist))
        total = 0
        for score in newlist:
            total += score
        print("Total score:", total)
        print("Average score:", total / len(newlist))
        print("High score:", max(newlist))
        print("Low score:", min(newlist))
        print("Score range:", max(newlist) - min(newlist))
