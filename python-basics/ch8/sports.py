BASKETBALL = "basketball"
GOLF = "golf"
sport = input("Enter a sport:")
p1_score = int(input("Enter player1 score:"))
p2_score = int(input("Enter player2 score:"))

if sport.lower() == BASKETBALL:
    if p1_score == p2_score:
        print("Draw")
    elif p1_score > p2_score:
        print("P1 wins")
    else:
        print("P2 wins")
elif sport.lower() == GOLF:
    if p1_score == p2_score:
        print("Draw")
    elif p1_score > p2_score:
        print("P2 wins")
    else:
        print("P1 wins")
else:
    print("Unknown sports")

# Simplify the if branchs
sport = sport.lower()
if p1_score == p2_score: # No matter which sport, equal score means `draw`
    print("Draw")
elif sport == GOLF or sport == BASKETBALL:
    p1_wins_ball = (sport == BASKETBALL) and (p1_score > p2_score)
    p1_wins_golf = (sport == GOLF) and (p1_score < p2_score)
    p1_wins = p1_wins_golf or p1_wins_ball
    if p1_wins:
        print("P1 wins")
    else:
        print("P2 wins")
else:
    print("Unknown sports")
