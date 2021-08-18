import random

def coin_flip():
    """Randomly return 'head' or 'tails'."""
    if random.randint(0,1) == 0:
        return "head"
    else:
        return "tails"

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "head"

print("Fair Coin Flip Test")

heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if coin_flip() == "head":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

print(f"heads:{heads_tally},tails:{tails_tally}")