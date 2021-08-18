import random


def coin_flip():
    if random.randint(0,1) == 0:
        return "head"
    else:
        return "tails"

total_count = 0
for i in range(10_000):
    count = 1
    pre = coin_flip()
    while True:
        count = count + 1
        if pre != coin_flip():
            break
    total_count += count

print(f"average flips is {total_count/10_000}.")
