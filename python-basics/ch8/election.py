import random

def region_elect(probability):
    if random.random() < probability:
        return 1
    else:
        return 0

def elect_A():
    n = region_elect(.87) + region_elect(.65) + region_elect(.17)
    if n >= 2:
        return True
    else:
        return False

count = 0
for i in range(10_000):
    if elect_A():
        count += 1

print(f"percentage {count/10_000}")
